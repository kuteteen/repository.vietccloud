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
title = 'PlayPorn'
image = ''
art = ''
order = 6


class Site:

    def __init__(self, __params_):
        import re
        from addon import Addon
        from addondict import AddonDict as XBMCDict
        from BeautifulSoup import BeautifulSoup, SoupStrainer, Comment

        a = Addon()
        __site_ = self.__module__
        __mode_ = __params_['mode']

        __home_url_ = 'http://playporn.to/'
        __search_url_ = __home_url_ + '?submit=Search&s='
        __movies_url_ = __home_url_ + 'category/xxx-movie-stream/'
        __scenes_url_ = __home_url_ + 'category/xxx-scenes-stream/'
        __false_positives_ = ['http://playporn.to/deutsche-milfs-anonym-sex/']

        if __mode_ == 'main':
            __item_list_ = [{'site': __site_, 'mode': 'list', 'title': a.language(30003), 'content': 'movies',
                             'url': __home_url_, 'cover_url': a.image('recent.png', image), 'backdrop_url': a.art(), 'type': 3},
                            {'site': __site_, 'mode': 'sub', 'title': a.language(30001), 'content': 'movies',
                             'url': __movies_url_, 'cover_url': a.image('movies.png', image), 'backdrop_url': a.art(), 'type': 3},
                            {'site': __site_, 'mode': 'sub', 'title': a.language(30002), 'content': 'movies',
                             'url': __scenes_url_, 'cover_url': a.image('scenes.png', image), 'backdrop_url': a.art(), 'type': 3},
                            {'site': __site_, 'mode': 'list', 'title': a.language(30004), 'content': 'search',
                             'url': __search_url_, 'cover_url': a.image('search.png', image), 'backdrop_url': a.art(), 'type': 3}]
            __item_list_.extend(a.favs_hist_menu(__site_))
            __item_list_.extend(a.extended_menu())
            a.add_items(__item_list_)
            a.end_of_directory()

        elif __mode_ == 'sub':
            __item_list_ = [{'site': __site_, 'mode': 'list', 'title': a.language(30006), 'content': __params_['content'],
                             'url': __params_['url'], 'cover_url': a.image('all.png', image), 'backdrop_url': a.art(), 'type': 3},
                            {'site': __site_, 'mode': 'category', 'title': a.language(30005), 'content': __params_['content'],
                             'url': __home_url_, 'cover_url': a.image('categories.png', image), 'backdrop_url': a.art(), 'type': 3}]
            a.add_items(__item_list_)
            a.end_of_directory()

        elif __mode_ == 'category':
            __item_ = 1
            if 'scenes' in __params_['url'].lower(): __item_ = 2
            __html_ = a.get_page(__home_url_)
            __soup_ = BeautifulSoup(__html_, parseOnlyThese=SoupStrainer('ul', 'nav fl'))
            __item_list_ = []
            for __item_ in __soup_.findAll('ul')[__item_].findAll({'a': True}):
                __item_list_.extend([{'site': 'playporn', 'mode': 'list', 'url': __item_.get('href'), 'content': __params_['content'],
                                      'title': __item_.contents[0].encode('UTF-8'), 'cover_url': a.image(image, image),
                                      'backdrop_url': a.art(), 'type': 3}])
            if __item_list_:
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
            __soup_ = BeautifulSoup(__html_, parseOnlyThese=SoupStrainer('body'))
            __item_list_ = []
            __params_['mode'] = 'play'
            __params_['content'] = 'movies'
            __params_['type'] = 0
            __params_['context'] = 0
            __params_['duration'] = '7200'
            __xbmcdict_ = XBMCDict(0).update(__params_)
            for __item_ in __soup_.findAll('div', 'photo-thumb-image'):
                if not __item_.a.get('href') in __false_positives_:
                    __dict_ = __xbmcdict_.copy()
                    if 'scenes' in __params_['url']:
                        __dict_['duration'] = '2700'
                        __dict_['content'] = 'episodes'
                    __dict_['url'] = __item_.a.get('href')
                    __dict_['title'] = __item_.a.get('title').encode('UTF-8')
                    __dict_['tvshowtitle'] = __dict_['title']
                    __dict_['originaltitle'] = __dict_['title']
                    __dict_['cover_url'] = a.image(__item_.img.get('src'))
                    __dict_['thumb_url'] = __dict_['cover_url']
                    __dict_['poster'] = __dict_['cover_url']
                    __dict_['sub_site'] = __site_

                    __item_list_.extend([__dict_])
            __soup_ = BeautifulSoup(__html_, parseOnlyThese=SoupStrainer('div', 'more_entries'))
            if __soup_:
                __item_ = __soup_.find('a', 'previouspostslink')
                if __item_: __item_list_.extend([{'site': __site_, 'mode': 'list', 'url': __item_.get('href'), 'content': __params_['content'],
                                                  'title': a.language(30017, True), 'cover_url': a.image('previous.png', image),
                                                  'backdrop_url': a.art(), 'type': 3}])
                __item_ = __soup_.find('a', 'nextpostslink')
                if __item_: __item_list_.extend([{'site': __site_, 'mode': 'list', 'url': __item_.get('href'), 'content': __params_['content'],
                                                  'title': a.language(30018, True), 'cover_url': a.image('next.png', image),
                                                  'backdrop_url': a.art(), 'type': 3}])
                __item_ = __soup_.find('a', 'last')
                if __item_: __item_list_.extend([{'site': __site_, 'mode': 'list', 'url': __item_.get('href'), 'content': 'goto',
                                                  'title': a.language(30019, True), 'cover_url': a.image('goto.png', image),
                                                  'backdrop_url': a.art(), 'type': 3}])
            if __item_list_:
                a.add_items(__item_list_)
                a.end_of_directory()

        elif __mode_ == 'play':
            __html_ = a.get_page(__params_['url'])
            __soup_ = BeautifulSoup(__html_, parseOnlyThese=SoupStrainer('div', {'id': 'loopedSlider'}))
            __soup_ = __soup_.find(text=lambda text: isinstance(text, Comment))
            if __soup_:
                __soup_ = re.sub('&lt;', '<', __soup_.encode('utf-8'))
                __soup_ = re.sub('&gt;', '>', __soup_)
                __soup_ = BeautifulSoup(__soup_, parseOnlyThese=SoupStrainer('div', 'video'))
                if __soup_:
                    __item_list_ = []
                    __xbmcdict_ = XBMCDict(0).update(__params_)
                    for __item_ in __soup_.findAll('iframe'):
                        __dict_ = __xbmcdict_.copy()
                        __dict_['url'] = __item_.get('src').replace('http://playporn.to/stream/all/?file=', '').encode('UTF-8')
                        if 'flashx.tv' in __dict_['url'].lower():
                            __item_ = re.search('hash=(.+?)&', __dict_['url'])
                            if __item_: __dict_['url'] = 'http://flashx.tv/video/' + __item_.group(1) + '/'
                        elif 'played.to' in __dict_['url'].lower():
                            __item_ = re.search('embed-([a-zA-Z0-9]+?)-.+?html', __dict_['url'])
                            if __item_: __dict_['url'] = 'http://played.to/' + __item_.group(1)
                        __item_list_.extend([__dict_])
                    if __item_list_:
                        from playback import Playback
                        Playback().choose_sources(__item_list_)
                    else: a.alert(a.language(30904, True), sound=False)
                else: a.alert(a.language(30904, True), sound=False)
            else: a.alert(a.language(30904, True), sound=False)