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
title = 'StreamGloud'
image = ''
art = ''
order = 5


class Site():

    def __init__(self, __params_):
        import re
        from addon import Addon
        from addondict import AddonDict as XBMCDict
        from BeautifulSoup import BeautifulSoup, SoupStrainer, Comment

        a = Addon()
        __site_ = self.__module__
        __mode_ = __params_['mode']

        __home_url_ = 'http://qwertty.net'
        __search_url_ = __home_url_ + '/index.php?do=search&subaction=search&full_search=0&search_start=0&result_from=1&story='
        __false_positives_ = ['']

        if __mode_ == 'main':
            __item_list_ = [{'site': __site_, 'mode': 'list', 'title': a.language(30006), 'content': 'movies',
                             'url': __home_url_, 'cover_url': a.image('all.png', image), 'backdrop_url': a.art(), 'type': 3},
                            {'site': __site_, 'mode': 'categories', 'title': a.language(30005), 'content': 'movies',
                             'url': __home_url_, 'cover_url': a.image('categories.png', image), 'backdrop_url': a.art(), 'type': 3},
                            {'site': __site_, 'mode': 'list', 'title': a.language(30004), 'content': 'search',
                             'url': __search_url_, 'cover_url': a.image('search.png', image), 'backdrop_url': a.art(), 'type': 3}]
            __item_list_.extend(a.favs_hist_menu(__site_))
            a.add_items(__item_list_)
            a.end_of_directory()

        elif __mode_ == 'categories':
            __html_ = a.get_page(__params_['url'])
            __soup_ = BeautifulSoup(__html_, parseOnlyThese=SoupStrainer('div', {'class': 'navi-wrap'}))
            __item_list_ = []
            if __soup_:
                for __item_ in __soup_.findAll('a'):
                    if __item_: __item_list_.extend([{'site': __site_, 'mode': 'list', 'url': __home_url_ + __item_.get('href'),
                                                      'content': __params_['content'], 'title': __item_.string.encode('UTF-8'),
                                                      'cover_url': a.image(image, image), 'backdrop_url': a.art(), 'type': 3}])
            a.add_items(__item_list_)
            a.end_of_directory()

        elif __mode_ == 'list':
            if __params_['content'] == 'search':
                __item_ = a.search_input()
                if __item_: __params_['url'] = __search_url_ + __item_
                else: exit(1)
            elif __params_['content'] == 'goto':
                if 'do=search' in __params_['url']: __last_item_ = re.search('search_start=([0-9]+)', __params_['url'])
                else: __last_item_ = re.search('/page/([0-9]+)/', __params_['url'])
                if __last_item_: __last_item_ = int(__last_item_.group(1))
                else: __last_item_ = 10000
                __item_ = a.page_input(__last_item_)
                if __item_:
                        if 'do=search' in __params_['url']:
                            __page_ = re.sub(r'(search_start=)([0-9]+)', '\g<01>' + str(__item_), __params_['url'])
                            __params_['url'] = re.sub(r'(result_from=)([0-9]+)', '\g<01>' + str(int(str(__item_)) * 10 + 1), __page_)
                        else:
                            __params_['url'] = re.sub('/page/[0-9]+/', '/page/' + str(__item_) + '/', __params_['url'])
                else: exit(1)
            __html_ = a.get_page(__params_['url'])
            __soup_ = BeautifulSoup(__html_, parseOnlyThese=SoupStrainer('div', {'id': 'dle-content'}))
            __item_list_ = []
            __params_['mode'] = 'play'
            __params_['content'] = 'movies'
            __params_['type'] = 0
            __params_['context'] = 0
            __params_['duration'] = '7200'
            if __soup_:
                __xbmcdict_ = XBMCDict(0).update(__params_)
                for __item_ in __soup_.findAll('div', {'class': 'short-item'}):
                    if __item_:
                        __dict_ = __xbmcdict_.copy()
                        __dict_['url'] = __item_.a.get('href')
                        __dict_['title'] = __item_.a.img.get('alt').encode('UTF-8')
                        __dict_['tvshowtitle'] = __dict_['title']
                        __dict_['originaltitle'] = __dict_['title']
                        __item_ = __home_url_ + __item_.a.img.get('src').replace('/thumbs', '')
                        __dict_['cover_url'] = a.image(__item_)
                        __dict_['thumb_url'] = __dict_['cover_url']
                        __dict_['poster'] = __dict_['cover_url']
                        __dict_['sub_site'] = __site_

                        __item_list_.extend([__dict_])
            __soup_ = BeautifulSoup(__html_, parseOnlyThese=SoupStrainer('div', {'class': 'bottom-nav'}))
            if __soup_:
                __last_item_ = len(__soup_.findAll('a', href=True)) - 1
                for __index_, __item_ in enumerate(__soup_.findAll('a', href=True)):
                    __page_ = ''
                    if __item_:
                        if __index_ == 0 and __item_.string.encode('UTF-8') != 'Back': __last_item_ -= 1
                        if __item_.string.encode('UTF-8') == 'Back':
                            if __item_.get('href') == '#':
                                __temp_ = re.search('.*list_submit\(([0-9]+)\).*',__item_.get('onclick'))
                                if __temp_:
                                    __page_ = re.sub(r'(search_start=)([0-9]+)', '\g<01>' + __temp_.group(1), __params_['url'])
                                    __page_ = re.sub(r'(result_from=)([0-9]+)', '\g<01>' + str(int(__temp_.group(1)) * 10 + 1), __page_)
                            else:
                                __page_ = __item_.get('href')
                            if __page_:
                                __item_list_.extend([{'site': __site_, 'mode': 'list', 'url': __page_, 'content': __params_['content'],
                                                      'title': a.language(30017, True), 'cover_url': a.image('previous.png', image),
                                                      'backdrop_url': a.art(), 'type': 3}])
                        if __item_.string.encode('UTF-8') == 'Next':
                            if __item_.get('href') == '#':
                                __temp_ = re.search('.*list_submit\(([0-9]+)\).*',__item_.get('onclick'))
                                if __temp_:
                                    __page_ = re.sub(r'(search_start=)([0-9]+)', '\g<01>' + __temp_.group(1), __params_['url'])
                                    __page_ = re.sub(r'(result_from=)([0-9]+)', '\g<01>' + str(int(__temp_.group(1)) * 10 + 1), __page_)
                            else:
                                __page_ = __item_.get('href')
                            if __page_:
                                __item_list_.extend([{'site': __site_, 'mode': 'list', 'url': __page_, 'content': __params_['content'],
                                                      'title': a.language(30018, True), 'cover_url': a.image('next.png', image),
                                                      'backdrop_url': a.art(), 'type': 3}])
                        if __index_ == __last_item_:
                            if __item_.get('href') == '#':
                                __temp_ = re.search('.*list_submit\(([0-9]+)\).*',__item_.get('onclick'))
                                if __temp_:
                                    __page_ = re.sub(r'(search_start=)([0-9]+)', '\g<01>' + __temp_.group(1), __params_['url'])
                                    __page_ = re.sub(r'(result_from=)([0-9]+)', '\g<01>' + str(int(__temp_.group(1)) * 10 + 1), __page_)
                            else:
                                __page_ = __item_.get('href')
                            if __page_:
                                __item_list_.extend([{'site': __site_, 'mode': 'list', 'url': __page_, 'content': 'goto',
                                                      'title': a.language(30019, True), 'cover_url': a.image('goto.png', image),
                                                      'backdrop_url': a.art(), 'type': 3}])
            a.add_items(__item_list_)
            a.end_of_directory()

        elif __mode_ == 'play':
            __html_ = a.get_page(__params_['url'])
            __soup_ = BeautifulSoup(__html_, parseOnlyThese=SoupStrainer('div', {'class': 'full-text clearfix desc-text'}))
            __item_ = __soup_.find('a')
            __item_list_ = []
            __xbmcdict_ = XBMCDict(0).update(__params_)
            if __item_:
                __dict_ = __xbmcdict_.copy()
                __dict_['url'] = __item_.get('href')
                __item_list_.extend([__dict_])
            else: a.alert(a.language(30904, True), sound=False)
            if __item_list_:
                from playback import Playback
                Playback().choose_sources(__item_list_)
            else: a.alert(a.language(30904, True), sound=False)
