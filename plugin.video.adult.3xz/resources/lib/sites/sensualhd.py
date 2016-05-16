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
title = 'PornHardX'
image = ''
art = ''
order = 1


class Site:

    def __init__(self, __params_):
        import re
        from addon import Addon
        from addondict import AddonDict as XBMCDict
        from BeautifulSoup import BeautifulSoup, SoupStrainer, Comment

        a = Addon()
        __site_ = self.__module__
        __mode_ = __params_['mode']

        __home_url_ = 'http://pornhardx.com/'
        __movies_url_ = __home_url_ + 'category/full-movie/'
        __scenes_url_ = __home_url_ + 'video/'
        __search_url_ = __home_url_ + '?s='
        __false_positives_ = ['http://pornhardx.com/video', 'http://pornhardx.com/video/?order=viewed',
                              'http://pornhardx.com/video/?order=liked', 'http://pornhardx.com/']

        if __mode_ == 'main':
            __item_list_ =[]
            __item_list_.extend([{'site': __site_, 'mode': 'list', 'title': a.language(30006), 'content': 'movies',
                                  'url': __scenes_url_, 'cover_url': a.image('all.png', image), 'backdrop_url': a.art(), 'type': 3}])
            __item_list_.extend([{'site': __site_, 'mode': 'list', 'title': a.language(30003), 'content': 'movies',
                                  'url': __home_url_, 'cover_url': a.image('recent.png', image), 'backdrop_url': a.art(), 'type': 3}])
            __item_list_.extend([{'site': __site_, 'mode': 'categories', 'title': a.language(30005), 'content': 'movies',
                                  'url': __scenes_url_, 'cover_url': a.image('categories.png', image), 'backdrop_url': a.art(), 'type': 3}])
            __item_list_.extend([{'site': __site_, 'mode': 'list', 'title': a.language(30004), 'content': 'search',
                                  'url': __search_url_, 'cover_url': a.image('search.png', image), 'backdrop_url': a.art(), 'type': 3}])
            __item_list_.extend(a.favs_hist_menu(__site_))
            __item_list_.extend(a.extended_menu())
            a.add_items(__item_list_)
            a.end_of_directory()

        elif __mode_ == 'categories':
            __html_ = a.get_page(__params_['url'])
            __soup_ = BeautifulSoup(__html_, parseOnlyThese=SoupStrainer('div', {'id': 'navigation-wrapper'}))
            __item_list_ = []
            if __soup_:
                for __item_ in __soup_.findAll('a', {'href': True}):
                    if __item_:
                        if __item_.get('href') not in __false_positives_:
                            if 'full-movie' in __params_['url']:
                                if __movies_url_ != __item_.get('href') and 'full-movie' in __item_.get('href'):
                                    __item_list_.extend([{'site': __site_, 'mode': 'list', 'url': __item_.get('href'),
                                                          'content': __params_['content'], 'title':__item_.contents[0].encode('UTF-8'),
                                                          'cover_url': a.image(image, image), 'backdrop_url': a.art(), 'type': 3}])
                            elif 'full-movie' not in __item_.get('href'):
                                __item_list_.extend([{'site': __site_, 'mode': 'list', 'url': __item_.get('href'),
                                                      'content': __params_['content'], 'title':__item_.contents[0].encode('UTF-8'),
                                                      'cover_url': a.image(image, image), 'backdrop_url': a.art(), 'type': 3}])
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
            __soup_ = BeautifulSoup(__html_, parseOnlyThese=SoupStrainer('div', {'class': re.compile('col-sm-8(?:\s*main-content)*')}))
            __item_list_ = []
            __params_['mode'] = 'play'
            __params_['content'] = 'movies'
            __params_['type'] = 0
            __params_['context'] = 0
            __params_['duration'] = '7200'
            if __soup_:
                __xbmcdict_ = XBMCDict(0).update(__params_)
                for __item_ in __soup_.findAll('div', {'class': re.compile('.*(?:col-xs-6 item|post type-post status-publish).*')}):
                    if __item_:
                        if __item_.a.get('href') not in __false_positives_:
                            __dict_ = __xbmcdict_.copy()
                            if 'full-movie' not in __params_['url']:
                                __dict_['duration'] = '1500'
                                __dict_['content'] = 'episodes'
                            if __item_.h3:
                                __dict_['url'] = __item_.h3.a.get('href')
                                if __item_.h3.a.contents: __dict_['title'] = __item_.h3.a.contents[0].encode('UTF-8')
                                else: __dict_['title'] = 'Untitled'
                            elif __item_.h2:
                                __dict_['url'] = __item_.h2.a.get('href')
                                if __item_.h2.a.contents: __dict_['title'] = __item_.h2.a.contents[0].encode('UTF-8')
                                else: __dict_['title'] = 'Untitled'
                            __dict_['tvshowtitle'] = __dict_['title']
                            __dict_['originaltitle'] = __dict_['title']
                            __dict_['cover_url'] = a.image(__item_.img.get('src'))
                            __dict_['thumb_url'] = __dict_['cover_url']
                            __dict_['poster'] = __dict_['cover_url']
                            __dict_['sub_site'] = __site_

                            __item_list_.extend([__dict_])
            __soup_ = BeautifulSoup(__html_, parseOnlyThese=SoupStrainer('ul', {'class': 'pagination'}))
            if __soup_.li:
                __item_ = __soup_.find('a', {'class': 'prev page-numbers'})
                if __item_:
                    __item_list_.extend([{'site': __site_, 'mode': 'list', 'url': __item_.get('href'), 'content': __params_['content'],
                                          'title': a.language(30017, True), 'cover_url': a.image(image, image),
                                          'backdrop_url': a.art(), 'type': 3}])
                __item_ = __soup_.find('a', {'class': 'next page-numbers'})
                if __item_:
                    __item_list_.extend([{'site': __site_, 'mode': 'list', 'url': __item_.get('href'), 'content': __params_['content'],
                                          'title': a.language(30018, True), 'cover_url': a.image(image, image),
                                          'backdrop_url': a.art(), 'type': 3}])
                    if len(__soup_.findAll('a')) > 2:
                        __last_item_= __soup_.find('a', {'class': 'next page-numbers'}).parent.previousSibling.a.get('href')
                        __item_list_.extend([{'site': __site_, 'mode': 'list', 'url': __last_item_, 'content': 'goto',
                                              'title': a.language(30019, True), 'cover_url': a.image(image, image),
                                              'backdrop_url': a.art(), 'type': 3}])
                else:
                    __item_ = __soup_.find('span', {'class': 'page-numbers current'})
                    if __item_:
                        if len(__soup_.findAll('a')) > 2:
                            __last_item_ = __soup_.find('span', {'class': 'page-numbers current'}).parent.previousSibling.a.get('href')
                            __item_list_.extend([{'site': __site_, 'mode': 'list', 'url': __last_item_, 'content': 'goto',
                                                  'title': a.language(30019, True), 'cover_url': a.image('goto.png', image),
                                                  'backdrop_url': a.art(), 'type': 3}])
            else:
                __soup_ = BeautifulSoup(__html_, parseOnlyThese=SoupStrainer('ul', {'class': 'pager'}))
                __item_ = __soup_.find('li', {'class': 'previous'})
                if __item_:
                    __item_list_.extend([{'site': __site_, 'mode': 'list', 'url': __item_.previousSibling.get('href'), 'content': __params_['content'],
                                          'title': a.language(30017, True), 'cover_url': a.image('previous.png', image),
                                          'backdrop_url': a.art(), 'type': 3}])
                __item_ = __soup_.find('li', {'class': 'next'})
                if __item_:
                    __item_list_.extend([{'site': __site_, 'mode': 'list', 'url': __item_.previousSibling.get('href'), 'content': __params_['content'],
                                          'title': a.language(30018, True), 'cover_url': a.image('next.png', image),
                                          'backdrop_url': a.art(), 'type': 3}])
            a.add_items(__item_list_)
            a.end_of_directory()

        elif __mode_ == 'play':
            __html_ = a.get_page(__params_['url'])
            __soup_ = BeautifulSoup(__html_, parseOnlyThese=SoupStrainer('object', {'id': re.compile('flashplayer.+')}))
            __item_ = ''
            __item_list_ = []
            if __soup_:
                for __item_ in __soup_.findAll('param', {'name': 'FlashVars'}):
                    __item_ = __item_.get('value')
                    __item_ = re.search('.*?proxy\.link=(.+?)&(?:proxy|skin).*?', __item_)
                    if __item_:
                        if __item_ not in __item_list_: __item_ = __item_.group(1)
                        else: __item_ = ''
                    else: __item_ = ''
                    __xbmcdict_ = XBMCDict(0).update(__params_)
                    if __item_:
                        __dict_ = __xbmcdict_.copy()
                        __dict_['url'] = __item_
                        __item_list_.extend([__dict_])
            __soup_ = BeautifulSoup(__html_, parseOnlyThese=SoupStrainer('video'))
            __item_ = ''
            if __soup_:
                for __item_ in __soup_.findAll('source'):
                    __src_ = __item_.get('src')
                    if __src_:
                        __xbmcdict_ = XBMCDict(0).update(__params_)
                        if __item_ and ('..' not in __src_):
                            __dict_ = __xbmcdict_.copy()
                            try: __dict_['src_title'] = __item_.get('data-res') + 'p'
                            except: pass
                            __dict_['url'] = __src_
                            __item_list_.extend([__dict_])
            __soup_ = BeautifulSoup(__html_, parseOnlyThese=SoupStrainer('div', {'class': 'videoWrapper player'}))
            __item_ = ''
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
                for __iframe_ in __soup_.findAll('iframe'):
                    __item_ = ''
                    if __iframe_.get('src'):
                        if 'http://videomega.tv/validatehash.php' in __iframe_['src']: __item_ = __iframe_['src']
                        elif 'ref=' in __iframe_.get('src'):
                            __temp_ = re.search('.*ref=[\'"](.+?)[\'"]', __iframe_.get('src'))
                            if __temp_: __item_ = 'http://videomega.tv/iframe.php?ref=' + __temp_.group(1)
                        else: __item_ = __iframe_.get('src')
                        __xbmcdict_ = XBMCDict(0).update(__params_)
                        if __item_:
                            __dict_ = __xbmcdict_.copy()
                            __dict_['url'] = __item_
                            __item_list_.extend([__dict_])
            __soup_ = BeautifulSoup(__html_, parseOnlyThese=SoupStrainer('div', {'class': re.compile('player player-small.*')}))
            __item_ = ''
            if __soup_:
                for __iframe_ in __soup_.findAll('iframe'):
                    __item_ = ''
                    if __iframe_.get('src'):
                        if 'http://videomega.tv/validatehash.php' in __iframe_['src']: __item_ = __iframe_['src']
                        elif 'ref=' in __iframe_.get('src'):
                            __temp_ = re.search('.*ref=[\'"](.+?)[\'"]', __iframe_.get('src'))
                            if __temp_: __item_ = 'http://videomega.tv/iframe.php?ref=' + __temp_.group(1)
                        else: __item_ = __iframe_.get('src')
                        __xbmcdict_ = XBMCDict(0).update(__params_)
                        if __item_:
                            __dict_ = __xbmcdict_.copy()
                            __dict_['url'] = __item_
                            __item_list_.extend([__dict_])
            if __item_list_:
                from playback import Playback
                Playback().choose_sources(__item_list_)
            else: a.alert(a.language(30904, True), sound=False)