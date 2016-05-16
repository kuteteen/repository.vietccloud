# -*- coding: UTF-8 -*-
"""
    Copyright (C) 2014  smokdpi

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


""" Site information used for main menu if more than 1 site """
title = 'Xtheatre'
image = ''
art = ''
order = 3


class Site:

    def __init__(self, __params_):
        import re
        from addon import Addon
        from addondict import AddonDict as XBMCDict
        from BeautifulSoup import BeautifulSoup, SoupStrainer, Comment

        a = Addon()
        __site_ = self.__module__
        __mode_ = __params_['mode']

        __home_url_ = 'http://xtheatre.net/'
        __search_url_ = __home_url_ + '?s='
        __false_positives_ = ['http://watchxxxhd.net/watch-full-movies-hd/', 'http://watchxxxhd.net',
                              'http://watchxxxhd.net/category/movies/', 'http://watchxxxhd.net/category/ategorized222/',
                              'http://watchxxxhd.net/watch-full-movies-hd/']

        if __mode_ == 'main':
            __item_list_ = [{'site': __site_, 'mode': 'list', 'title': a.language(30006), 'content': 'movies',
                             'url': __home_url_ + '?filtre=date&cat=0', 'cover_url': a.image('all.png', image), 'backdrop_url': a.art(), 'type': 3},
                            {'site': __site_, 'mode': 'categories', 'title': a.language(30005), 'content': 'movies',
                             'url': __home_url_ + 'categories/', 'cover_url': a.image('categories.png', image), 'backdrop_url': a.art(), 'type': 3},
                            {'site': __site_, 'mode': 'list', 'title': a.language(30004), 'content': 'search',
                             'url': __search_url_, 'cover_url': a.image('search.png', image), 'backdrop_url': a.art(), 'type': 3}]
            __item_list_.extend(a.favs_hist_menu(__site_))
            __item_list_.extend(a.extended_menu())
            a.add_items(__item_list_)
            a.end_of_directory()

        elif __mode_ == 'categories':
            __html_ = a.get_page(__params_['url'])
            __soup_ = BeautifulSoup(__html_, parseOnlyThese=SoupStrainer('ul', {'class': 'listing-cat'}))
            __item_list_ = []
            if __soup_:
                for __item_ in __soup_.findAll('li'):
                    if __item_:
                        if __item_.a.get('href') not in __false_positives_:
                            try:
                                __vidcount_ = __item_.findAll('span', {'class': 'nb_cat border-radius-5'})[0].string.encode('UTF-8')
                                __vidcount_ = re.sub('\svideo[s]*', '', __vidcount_)
                            except: __vidcount_ = '0'
                            if __vidcount_ and __vidcount_ != '0':
                                __title_ = __item_.a.get('title').encode('UTF-8') + ' (%s)' % __vidcount_
                                __item_list_.extend([{'site': __site_, 'mode': 'list', 'url': __item_.a.get('href'),
                                                      'content': __params_['content'], 'title': __title_,
                                                      'cover_url': a.image(__item_.img.get('src'), image), 'backdrop_url': a.art(), 'type': 3}])

            a.add_items(__item_list_)
            a.end_of_directory()

        elif __mode_ == 'list':
            if __params_['content'] == 'search':
                __item_ = a.search_input()
                if __item_: __params_['url'] = __search_url_ + __item_
                else: exit(1)
            elif __params_['content'] == 'goto':
                __last_item_ = re.search('/page/([0-9]+)/', __params_['url'])
                if __last_item_: __last_item_ = int(__last_item_.group(1))
                else: __last_item_ = 10000
                __item_ = a.page_input(__last_item_)
                if __item_: __params_['url'] = re.sub('/page/[0-9]+/', '/page/' + str(__item_) + '/', __params_['url'])
                else: exit(1)
            __html_ = a.get_page(__params_['url'])
            __soup_ = BeautifulSoup(__html_, parseOnlyThese=SoupStrainer('ul', {'class': 'listing-videos listing-extract'}))
            __item_list_ = []
            __params_['mode'] = 'play'
            __params_['content'] = 'movies'
            __params_['type'] = 0
            __params_['context'] = 0
            __params_['duration'] = '7200'
            if __soup_:
                __xbmcdict_ = XBMCDict(0).update(__params_)
                for __item_ in __soup_.findAll('li', {'class': 'border-radius-5 box-shadow'}):
                    if __item_:
                        if __item_.a.get('href') not in __false_positives_:
                            __dict_ = __xbmcdict_.copy()
                            if 'full movie' not in __dict_['title'].lower() and 'xtheatre' not in __dict_['title'].lower():
                                __dict_['duration'] = '1500'
                                __dict_['content'] = 'episodes'
                            __dict_['url'] = __item_.a.get('href')
                            __dict_['title'] = __item_.a.get('title').encode('UTF-8')
                            __dict_['tvshowtitle'] = __dict_['title']
                            __dict_['originaltitle'] = __dict_['title']
                            __dict_['cover_url'] = a.image(__item_.img.get('data-lazy-src'))
                            __dict_['thumb_url'] = __dict_['cover_url']
                            __dict_['poster'] = __dict_['cover_url']
                            __dict_['sub_site'] = __site_

                            __item_list_.extend([__dict_])
            __soup_ = BeautifulSoup(__html_, parseOnlyThese=SoupStrainer('div', {'class': 'pagination'}))
            __last_item_ = False
            if __soup_:
                for __item_ in __soup_.findAll('a'):
                    if (__item_.string.encode('UTF-8') == 'Last »') or (__item_.get('class') == 'last'):
                        __last_item_ = __item_.get('href')
                        break
                if __last_item_ is False:
                    for __last_item_ in __soup_.findAll('a', {'class': 'inactive'}): pass
                    if __last_item_: __last_item_ = __last_item_.get('href')
                __item_ = __soup_.find('span', {'class': 'current'})
                if __item_:
                    if __item_.parent:
                        __item_ = __item_.parent
                        if __item_.previousSibling:
                            if __item_.previousSibling.find('a'):
                                __item_list_.extend([{'site': __site_, 'mode': 'list', 'url': __item_.previousSibling.a.get('href'), 'content': __params_['content'],
                                                      'title': a.language(30017, True), 'cover_url': a.image('previous.png', image),
                                                      'backdrop_url': a.art(), 'type': 3}])
                        if __item_.nextSibling:
                            if __item_.nextSibling.find('a'):
                                __item_list_.extend([{'site': __site_, 'mode': 'list', 'url': __item_.nextSibling.a.get('href'), 'content': __params_['content'],
                                                      'title': a.language(30018, True), 'cover_url': a.image('next.png', image),
                                                      'backdrop_url': a.art(), 'type': 3}])
            if __last_item_:
                __item_list_.extend([{'site': __site_, 'mode': 'list', 'url': __last_item_, 'content': 'goto',
                                      'title': a.language(30019, True), 'cover_url': a.image('goto.png', image),
                                      'backdrop_url': a.art(), 'type': 3}])

            a.add_items(__item_list_)
            a.end_of_directory()

        elif __mode_ == 'play':
            __html_ = a.get_page(__params_['url'])
            __soup_ = BeautifulSoup(__html_, parseOnlyThese=SoupStrainer('div', {'class': 'video-embed'}))
            __item_list_ = []
            if __soup_:
                for __script_ in __soup_.findAll('script'):
                    __item_ = ''
                    if __script_.get('src'):
                        if 'http://videomega.tv/validatehash.php' in __script_['src']: __item_ = __script_['src']
                        elif 'ref=' in __script_.get('src'):
                            __temp_ = re.search('.*ref=[\'"](.+?)[\'"]', __script_.get('src'))
                            if __temp_: __item_ = 'http://videomega.tv/iframe.php?ref=' + __temp_.group(1)
                        __xbmcdict_ = XBMCDict(0).update(__params_)
                        if __item_:
                            __dict_ = __xbmcdict_.copy()
                            __dict_['url'] = __item_
                            __item_list_.extend([__dict_])
                if __soup_.find('iframe', src=True):
                    __item_ = ''
                    for __iframe_ in __soup_.findAll('iframe', src=True):
                        if __iframe_.get('data-lazy-src'):
                            __item_ = __iframe_.get('data-lazy-src')
                        else:
                            __item_ = __iframe_.get('src').replace('\\', '')
                        __xbmcdict_ = XBMCDict(0).update(__params_)
                        if __item_:
                            __dict_ = __xbmcdict_.copy()
                            __dict_['url'] = __item_
                            __item_list_.extend([__dict_])
            __soup_ = BeautifulSoup(__html_, parseOnlyThese=SoupStrainer('div', {'id': 'video-infos'}))
            if __soup_:
                __item_ = ''
                for __p_ in __soup_.findAll('p'):
                    if __p_.iframe:
                        __item_ = __p_.iframe.get('src')
                        __xbmcdict_ = XBMCDict(0).update(__params_)
                        if __item_:
                            __dict_ = __xbmcdict_.copy()
                            __dict_['url'] = __item_
                            __item_list_.extend([__dict_])
            if __item_list_:
                from playback import Playback
                Playback().choose_sources(__item_list_)
            else: a.alert(a.language(30904, True), sound=False)