"""
    SALTS XBMC Addon
    Copyright (C) 2014 tknorris

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
import re
import urllib
import urlparse

from salts_lib import dom_parser
from salts_lib import kodi
from salts_lib import scraper_utils
from salts_lib import log_utils
from salts_lib.constants import FORCE_NO_MATCH
from salts_lib.constants import VIDEO_TYPES
import scraper


XHR = {'X-Requested-With': 'XMLHttpRequest'}
BASE_URL = 'http://xmovies8.tv'

class XMovies8V2_Scraper(scraper.Scraper):
    base_url = BASE_URL
    
    def __init__(self, timeout=scraper.DEFAULT_TIMEOUT):
        self.timeout = timeout
        self.base_url = kodi.get_setting('%s-base_url' % (self.get_name()))

    @classmethod
    def provides(cls):
        return frozenset([VIDEO_TYPES.MOVIE, VIDEO_TYPES.SEASON, VIDEO_TYPES.EPISODE])

    @classmethod
    def get_name(cls):
        return 'xmovies8.v2'

    def resolve_link(self, link):
        return link

    def format_source_label(self, item):
        return '[%s] %s' % (item['quality'], item['host'])

    def get_sources(self, video):
        source_url = self.get_url(video)
        hosters = []
        if source_url and source_url != FORCE_NO_MATCH:
            html = self.__get_embedded_page(source_url)
            fragment = dom_parser.parse_dom(html, 'div', {'class': '[^"]*download[^"]*'})
            if fragment:
                page_url = urlparse.urljoin(self.base_url, source_url)
                for match in re.finditer('href="([^"]+)[^>]+>([^<]+)', fragment[0]):
                    stream_url, label = match.groups()
                    quality = scraper_utils.height_get_quality(label)
                    stream_url += '|User-Agent=%s&Referer=%s' % (scraper_utils.get_ua(), urllib.quote(page_url))
                    hoster = {'multi-part': False, 'host': self._get_direct_hostname(stream_url), 'class': self, 'quality': quality, 'views': None, 'rating': None, 'url': stream_url, 'direct': True}
                    hosters.append(hoster)
            
        return hosters

    def get_url(self, video):
        return self._default_get_url(video)
    
    def _get_episode_url(self, season_url, video):
        html = self.__get_embedded_page(season_url)
        fragment = dom_parser.parse_dom(html, 'ul', {'class': 'movie-parts'})
        if fragment:
            match = re.search('href="([^"]+)[^>]*>\s*%s\s*<' % (video.episode), fragment[0])
            if match:
                return match.group(1)

    def __get_embedded_page(self, page_url):
        url = urlparse.urljoin(self.base_url, page_url)
        html = self._http_get(url, cache_limit=.5)
        match = re.search('''ajax\({\s*url\s*:\s*['"]([^'"]+).*?data\s*:\s*['"]([^'"]+)''', html, re.DOTALL)
        if match:
            url, data = match.groups()
            html = self._http_get(url, data=data, headers=XHR, cache_limit=.5)
            return html
        else:
            return ''
    
    def search(self, video_type, title, year, season=''):
        search_url = urlparse.urljoin(self.base_url, '/?s=%s' % urllib.quote_plus(title))
        html = self._http_get(search_url, allow_redirect=False, cache_limit=.25)
        results = []
        matches = []
        season_pattern = '(.*?)\s*-?\s*Season\s+(\d+)'
        if html.startswith('http://') and '/movie/' in html:
            url = html
            html = self._http_get(html, allow_redirect=False, cache_limit=.25)
            title = dom_parser.parse_dom(html, 'h1')
            if title:
                match_title_year = title[0]
                is_season = re.search(season_pattern, match_title_year, re.I)
                matches.append((url, match_title_year, is_season))
        else:
            for result in dom_parser.parse_dom(html, 'div', {'class': 'info'}):
                match = re.search('href="([^"]+)"[^>]*>([^<]+)', result, re.DOTALL)
                if match:
                    url, match_title_year = match.groups()
                    match_title_year = match_title_year.strip()
                    is_season = re.search(season_pattern, match_title_year, re.I)
                    if not is_season and video_type == VIDEO_TYPES.MOVIE or is_season and VIDEO_TYPES.SEASON:
                        matches.append((url, match_title_year, is_season))
        
        for url, match_title_year, is_season in matches:
            match_year = ''
            if video_type == VIDEO_TYPES.MOVIE:
                match = re.search('(.*?)\s+\((\d{4})\)', match_title_year)
                if match:
                    match_title, match_year = match.groups()
                else:
                    match_title = match_title_year
            else:
                if is_season:
                    match_title = '%s - Season %s' % (is_season.groups())
                    if season and int(is_season.group(2)) != int(season):
                        continue
                else:
                    match_title = match_title_year
    
            if not year or not match_year or year == match_year:
                result = {'url': scraper_utils.pathify_url(url), 'title': scraper_utils.cleanse_title(match_title), 'year': match_year}
                results.append(result)
        return results
