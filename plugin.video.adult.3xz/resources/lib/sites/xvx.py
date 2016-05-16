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
title = 'XVX'
image = ''
art = ''
order = 7


class Site:

    def __init__(self, __params_):
        import re
        from addon import Addon
        from addondict import AddonDict as XBMCDict
        from BeautifulSoup import BeautifulSoup, SoupStrainer, Comment

        a = Addon()
        __site_ = self.__module__
        __mode_ = __params_['mode']

        __base_url_ = 'http://yespornplease.com'
        __home_url_ = __base_url_ + '/index.php'
        __popular_url_ = __base_url_ + '/index.php?p=1&m=today'
        __search_url_ = __base_url_ + '/search.php?q='
        __false_positives_ = ['']

        if __mode_ == 'main':
            __item_list_ = [{'site': __site_, 'mode': 'list', 'title': a.language(30006), 'content': 'movies',
                             'url': __home_url_, 'cover_url': a.image('all.png', image), 'backdrop_url': a.art(), 'type': 3},
                            {'site': __site_, 'mode': 'list', 'title': a.language(30016), 'content': 'movies',
                             'url': __popular_url_, 'cover_url': a.image('popular.png', image), 'backdrop_url': a.art(), 'type': 3},
                            {'site': __site_, 'mode': 'categories', 'title': a.language(30005), 'content': 'movies',
                             'url': __home_url_, 'cover_url': a.image('categories.png', image), 'backdrop_url': a.art(), 'type': 3},
                            {'site': __site_, 'mode': 'list', 'title': a.language(30004), 'content': 'search',
                             'url': __search_url_, 'cover_url': a.image('search.png', image), 'backdrop_url': a.art(), 'type': 3}]
            __item_list_.extend(a.favs_hist_menu(__site_))
            __item_list_.extend(a.extended_menu())
            a.add_items(__item_list_)
            a.end_of_directory()

        elif __mode_ == 'categories':
            __html_ = a.get_page(__params_['url'])
            __soup_ = BeautifulSoup(__html_, parseOnlyThese=SoupStrainer('div', {'id': 'categories'}))
            __item_list_ = []
            if __soup_:
                for __item_ in __soup_.findAll('a'):
                    if __item_: __item_list_.extend([{'site': __site_, 'mode': 'list', 'url': __item_.get('href').replace(' ', '+'),
                                                      'content': __params_['content'], 'title': __item_.string.encode('UTF-8'),
                                                      'cover_url': a.image(image, image), 'backdrop_url': a.art(), 'type': 3}])
            a.add_items(__item_list_)
            a.end_of_directory()

        elif __mode_ == 'list':
            if __params_['content'] == 'search':
                __item_ = a.search_input()
                if __item_: __params_['url'] = __search_url_ + __item_.replace(' ', '+')
                else: exit(1)
            elif __params_['content'] == 'goto':
                __last_item_ = re.search('p=([0-9]+)', __params_['url'])
                if __last_item_: __last_item_ = int(__last_item_.group(1))
                else: __last_item_ = 10000
                __item_ = a.page_input(__last_item_)
                if __item_: __params_['url'] = re.sub('p=[0-9]+', 'p=' + str(__item_), __params_['url']).replace(' ', '+')
                else: exit(1)
            __html_ = a.get_page(__params_['url'])
            __soup_ = BeautifulSoup(__html_, parseOnlyThese=SoupStrainer('div', {'id': 'videos'}))
            __item_list_ = []
            __params_['mode'] = 'play'
            __params_['content'] = 'movies'
            __params_['type'] = 0
            __params_['context'] = 0
            __params_['duration'] = '7200'
            if __soup_:
                __xbmcdict_ = XBMCDict(0).update(__params_)
                for __item_ in __soup_.findAll('div', {'class': 'video-preview'}):
                    if __item_:
                        __dict_ = __xbmcdict_.copy()
                        __temp_ = __item_.find('div', {'class': 'jcarousel'}).a
                        if __temp_:
                            __temp_ = __temp_.get('href')
                            if not __temp_.startswith('http://'): __temp_ = __base_url_ + __temp_
                            __dict_['url'] = __temp_
                            __dict_['title'] = __item_.find('div', {'class': 'preview-title'}).get('title').encode('UTF-8')
                            __dict_['tvshowtitle'] = __dict_['title']
                            __dict_['originaltitle'] = __dict_['title']
                            __temp_ = __item_.find('div', {'class': 'jcarousel'}).img.get('src')
                            if __temp_.startswith('//'): __temp_ = 'http:' + __temp_
                            __dict_['cover_url'] = a.image(__temp_)
                            __dict_['thumb_url'] = __dict_['cover_url']
                            __dict_['poster'] = __dict_['cover_url']
                            __temp_ = __item_.find('div', {'class': 'preview-info-box length'}).b.string
                            if __temp_:
                                __temp_ = re.search('([0-9]+):([0-9]+):([0-9]+)', __temp_)
                                __dict_['duration'] = str((int(__temp_.group(1)) * 60 * 60) + (int(__temp_.group(2)) * 60) + int(__temp_.group(3)))
                            __dict_['sub_site'] = __site_

                            __item_list_.extend([__dict_])

                __soup_ = BeautifulSoup(__html_, parseOnlyThese=SoupStrainer('body'))
                if __soup_.find('a', {'id': 'prev-page'}):
                    __item_ = __soup_.find('a', {'id': 'prev-page'}).get('href').replace(' ', '+')
                    if not __item_.startswith('http://'): __item_ = __base_url_ + __item_
                    if 'index.php' in __params_['url']: __item_ = __item_.replace('search.php', 'index.php')
                    __item_list_.extend([{'site': __site_, 'mode': 'list', 'url': __item_, 'content': __params_['content'],
                                          'title': a.language(30017, True), 'cover_url': a.image('previous.png', image),
                                          'backdrop_url': a.art(), 'type': 3}])
                if __soup_.find('a', {'id': 'next-page'}):
                    __item_ = __soup_.find('a', {'id': 'next-page'}).get('href').replace(' ', '+')
                    if 'index.php' in __params_['url']: __item_ = __item_.replace('search.php', 'index.php')
                    if not __item_.startswith('http://'): __item_ = __base_url_ + __item_
                    __item_list_.extend([{'site': __site_, 'mode': 'list', 'url': __item_, 'content': __params_['content'],
                                          'title': a.language(30018, True), 'cover_url': a.image('next.png', image),
                                          'backdrop_url': a.art(), 'type': 3}])

                __soup_ = BeautifulSoup(__html_, parseOnlyThese=SoupStrainer('div', {'id': 'pagination'}))
                __last_item_ = False
                if __soup_:
                    for __item_ in reversed(__soup_.findAll('a')):
                        __last_item_ = __item_.get('href')
                        if not __last_item_.startswith('http://'): __last_item_ = __base_url_ + __last_item_
                        break
                if __last_item_:
                    __item_list_.extend([{'site': __site_, 'mode': 'list', 'url': __last_item_, 'content': 'goto',
                                          'title': a.language(30019, True), 'cover_url': a.image('goto.png', image),
                                          'backdrop_url': a.art(), 'type': 3}])

            a.add_items(__item_list_)
            a.end_of_directory()

        elif __mode_ == 'play':
            __html_ = a.get_page(__params_['url'])
            __soup_ = BeautifulSoup(__html_, parseOnlyThese=SoupStrainer('object', {'id': 'videoContainer'}))
            __item_list_ = []
            if __soup_:
                __item_ = __soup_.find('param', {'name': 'flashvars'})
                __item_ = re.search('.*?video_url=(.+?)&.*?', str(__item_))
                if __item_: __item_ = __item_.group(1)
                __xbmcdict_ = XBMCDict(0).update(__params_)
                if __item_:
                    __dict_ = __xbmcdict_.copy()
                    __dict_['url'] = __item_
                    __item_list_.extend([__dict_])
                else: a.alert(a.language(30904, True), sound=False)
            if __item_list_:
                from playback import Playback
                Playback().choose_sources(__item_list_)
            else: a.alert(a.language(30904, True), sound=False)
