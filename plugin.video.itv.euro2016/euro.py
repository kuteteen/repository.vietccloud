# -*- coding: utf-8 -*-

'''
Copyright (C) 2014                                                     

This program is free software: you can redistribute it and/or modify   
it under the terms of the GNU General Public License as published by   
the Free Software Foundation, either version 3 of the License, or      
(at your option) any later version.                                    

This program is distributed in the hope that it will be useful,        
but WITHOUT ANY WARRANTY; without even the implied warranty of         
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the          
GNU General Public License for more details.                           

You should have received a copy of the GNU General Public License      
along with this program. If not, see <http://www.gnu.org/licenses/>  
'''                                                                           

import urllib,urllib2,re,os,json,base64
import xbmcplugin,xbmcgui,xbmcaddon

addon = xbmcaddon.Addon(id='plugin.video.itv.euro2016')
profile = addon.getAddonInfo('profile')
home = addon.getAddonInfo('path')
dataPatch = xbmc.translatePath(os.path.join(home, 'resources'))
logos = xbmc.translatePath(os.path.join(dataPatch, 'logos\\'))
infos = xbmc.translatePath(os.path.join(dataPatch, 'infos\\'))
optimals = xbmc.translatePath(os.path.join(dataPatch, 'optimals\\'))
fanart = xbmc.translatePath(os.path.join(home, 'fanart.jpg'))
icon = xbmc.translatePath(os.path.join(home, 'icon.png'))
sys.path.append(os.path.join(home,'resources','lib'));from BeautifulSoup import BeautifulSoup;import urlfetch

dict = {'Goalkeeper':'[COLOR gold]GK[/COLOR]', 'Defender':'[COLOR lime]DF[/COLOR]', 'Midfield':'[COLOR blue]MF[/COLOR]', 'Forward':'[COLOR red]FW[/COLOR]', ' ':'', '\n':''}

def replace_all(text, dict):
	try:
		for a, b in dict.iteritems():
			text = text.replace(a, b)
		return text
	except:
		pass		

def alert(message,title="Thông báo!"):
    xbmcgui.Dialog().ok(title,"",message)

def notification(message, timeout=10000):
    xbmc.executebuiltin((u'XBMC.Notification("%s", "%s", %s, %s)' % ('EURO 2016', message, timeout, icon)).encode("utf-8"))

def home():
    alert(u'Truy cập addon ITVPLUS để xem được nội dung này!');sys.exit()
	
def notify():
    alert(u'Nội dung đang được chúng tôi cập nhật!');sys.exit()

def categories(url,name):
    if 'Lịch Thi Đấu' in name:
	    content = makeRequest(d ( "zero" , url ))
	    items = re.compile('<channel>\s*date:(.+?)\s*time:(.+?)\s*group:(.+?)\s*match:(.+?)\s*img:(.+?)\s*</channel>').findall(content)
	    for date, time, group, match, img in items:
		    addDir( date + '       ' + time + '             '  + group + '            '  + match, match, 5, img, isFolder=False)	

    if 'Bảng Xếp Hạng' in name:
	    content = makeRequest(d ( "zero" , url ))
	    items = re.compile('<table>\s*<name>(.+?)</name>').findall(content)
	    for group in items:
		    addDir( '[COLOR green]' + group + '[/COLOR]', group, 5, '', isFolder=False)
		    match = re.compile('<table>\s*<name>' + group + '</name>((?s).+?)</table>').findall(content)
		    for items in match:
		        item = re.compile('<td class="st"></td>\s*<td class="idx">(.+?)</td>\s*<td class="team"><a href=".+?"><b>(.+?)</b></a></td>\s*.+?\s*<td class="sub">(.+?)</td>\s*<td class="sub">(.+?)</td>\s*<td class="pnt">(.+?)</td>').findall(items)
		        for rank, name, tran, hs, diem in item:
		            name = '[COLOR gold]' + name + '[/COLOR]'
		            tran = 'Số Trận: ' + '[COLOR blue]' + tran + '[/COLOR]'
		            hs = 'Hiệu Số: ' + '[COLOR lime]' + hs + '[/COLOR]'
		            diem = 'Điểm: ' + '[COLOR red]' + diem + '[/COLOR]'
		            addDir( rank + '    ' + name + '             '  + tran + '            '  + hs + '            '  + diem, rank, 5, 'http', isFolder=False)
    if 'High Light' in name:
	    content = makeRequest(d ( "zero" , url ))
	    items = re.compile("<title>([^<]*)<\/title>\s*<link>([^<]+)<\/link>\s*<thumbnail>(.+?)</thumbnail>").findall(content)
	    for title,url,thumbnail in items:
		    addDir( title ,url , 100, thumbnail, isFolder=False)
    if 'Kênh Phát Sóng' in name:
	    content = makeRequest(d ( "zero" , url ))
	    match = re.compile('<channel>\s*<name>(.+?)</name>\s*<thumbnail>(.*?)</thumbnail>').findall(content)
	    for channel_name, thumb in match:
		    addDir( '[COLOR red]%s[/COLOR]' % channel_name.split(':')[0] + ': ' + '[COLOR blue]%s[/COLOR]' % channel_name.split(':')[1], channel_name, 5, thumb, isFolder=False)
		    channel = re.compile('<channel>\s*<name>' + channel_name + '</name>((?s).+?)</channel>').findall(content)
		    for items in channel:
		        item = re.compile('#EXTINF.+,(.+)\s(.+?)\s').findall(items)
		        for name, link in item:
		            addDir( name, link, 100, thumb, isFolder=False )
    xbmc.executebuiltin('Container.SetViewMode(502)')

def info(url,name):
	content = makeRequest(url)
	items = re.compile('<a href="/uefaeuro/(.+?)" class="table_team-name_block" title="(.+?)">').findall(content)[:24]
	for href, title in items:
		addDir( title, url + href, 4, infos + title + '.png', isFolder=True)
	xbmc.executebuiltin('Container.SetViewMode(500)')

def info_result(url):
    content = makeRequest(url)	
    soup = BeautifulSoup(str(content), convertEntities=BeautifulSoup.HTML_ENTITIES)
    items = soup.findAll('li',{'class' : 'squad--team-player'})
    for item in items:
        href = item.find('a').get('href')
        title = item.find('a').get('title')
        thumb = item.find('img').get('src')
        player_role = item.find('span',{'class':'squad--player-role'}).string
        pr = replace_all(player_role.encode('utf-8'), dict)		
        player_num = item.find('span',{'class':'squad--player-num'}).string.replace(' ','')
        pn = replace_all(player_num.encode('utf-8'), dict)
        addDir( pr + '   ' + title.encode('utf-8') + '   (' + pn + ')', href, 5, thumb, isFolder=False)
    xbmc.executebuiltin('Container.SetViewMode(502)')

def d ( k , e ) :
    data = [ ]
    e = base64.urlsafe_b64decode ( e )
    for i in range ( len ( e ) ) :
        ch1 = k [ i % len ( k ) ]
        ch2 = chr ( ( 256 + ord ( e [ i ] ) - ord ( ch1 ) ) % 256 )
        data.append ( ch2 )
    return "".join ( data )	
	
def resolveUrl(url):
    if d('euro','yNng0NXeoNrG4ebk19ag0tTi') in url:
        content = makeRequest(url)
        mediaUrl = re.compile('"url":"(.+?index.m3u8)",').findall(content)[0].replace('\\','')
    else:
        mediaUrl = url
    OOoO = Advertisement()
    item = xbmcgui.ListItem(path = mediaUrl)
    xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, item)
    if len(OOoO) > 0:
        try: xbmc.sleep(3000);xbmc.Player().setSubtitles(OOoO);print OOoO
        except: pass	
    return

def Advertisement():
    content = makeRequest(decry('aHR0cDovL3hibWMuaXR2cGx1cy5uZXQvTE9HTy9GQVEvJXMudHh0') % addon.getSetting('temp_patch'))
    OOoO = re.search('sub:"(.+?)",',content)
    if OOoO:OOoO = OOoO.group(1)
    else:OOoO = ''
    return OOoO	
	
def makeRequest(url, headers=None):
    if headers is None:
        headers = {'User-agent' : 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
                 'Referer' : 'http://www.google.com'}
    try:
        req = urllib2.Request(url,headers=headers)
        f = urllib2.urlopen(req)
        body=f.read()
        return body
    except:
        pass 
  
def addLink(name,url,mode,iconimage):
    u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&iconimage="+urllib.quote_plus(iconimage)  
    liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
    liz.setInfo( type="Video", infoLabels={ "Title": name } )
    liz.setProperty('IsPlayable', 'true')  
    ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz)  

def addDir(name,url,mode,iconimage,isFolder=False):
    u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)
    ok=True
    liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
    liz.setInfo( type="Video", infoLabels={ "Title": name } )
    if not isFolder:
        liz.setProperty('IsPlayable', 'true')
    ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=isFolder)
    return ok
	  	
def get_params():
    param=[]
    paramstring=sys.argv[2]
    if len(paramstring)>=2:
        params=sys.argv[2]
        cleanedparams=params.replace('?','')
        if (params[len(params)-1]=='/'):
            params=params[0:len(params)-2]
        pairsofparams=cleanedparams.split('&')
        param={}
        for i in range(len(pairsofparams)):
            splitparams={}
            splitparams=pairsofparams[i].split('=')
            if (len(splitparams))==2:
                param[splitparams[0]]=splitparams[1]
    return param

decry = base64.b64decode
params=get_params()
url=None
name=None
mode=None
iconimage=None

try:url=urllib.unquote_plus(params["url"])
except:pass
try:name=urllib.unquote_plus(params["name"])
except:pass
try:mode=int(params["mode"])
except:pass
try:iconimage=urllib.unquote_plus(params["iconimage"])
except:pass

if mode==None or url==None or len(url)<1:home()
elif mode==1:home()
elif mode==2:categories(url,name)
elif mode==3:info(url,name)
elif mode==4:info_result(url)
elif mode==100:
    dialogWait = xbmcgui.DialogProgress()
    dialogWait.create('***ITVPLUS***', 'Đang tải. Vui lòng chờ trong giây lát...')
    resolveUrl(url)
    dialogWait.close()
    del dialogWait
elif mode==500:notify()
	
xbmcplugin.setContent(int(sys.argv[1]), 'movies')
xbmcplugin.endOfDirectory(int(sys.argv[1]))