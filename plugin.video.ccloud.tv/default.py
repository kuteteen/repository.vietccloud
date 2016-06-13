# -*- coding: utf-8 -*-

import urllib, urllib2, sys, re, os, base64
import xbmc, xbmcgui, xbmcplugin, xbmcaddon

plugin_handle = int(sys.argv[1])
mysettings = xbmcaddon.Addon(id = 'plugin.video.ccloud.tv')
profile = mysettings.getAddonInfo('profile')
home = mysettings.getAddonInfo('path')
fanart = icon = xbmc.translatePath(os.path.join(home, 'icon.png'))
iconpath = xbmc.translatePath(os.path.join(home, 'resources/icons'))
local_path = mysettings.getSetting('local_path')
online_path = mysettings.getSetting('online_path')
enable_adult_section = mysettings.getSetting('enable_adult_section')

xml_regex = '<title>(.*?)</title>\s*<link>(.*?)</link>\s*<thumbnail>(.*?)</thumbnail>'
m3u_thumb_regex = 'tvg-logo=[\'"](.*?)[\'"]'
group_title_regex = 'group-title=[\'"](.*?)[\'"]'
m3u_regex = '#(.+?),(.+)\s*(.+)\s*'
media_regex = '<medialink>(.*?)</medialink>'

myk = 'ZG1sbGRHTmpiRzkxWkE9PQ=='.decode('base64').decode('base64')
mydict = {';':'', '&amp;':'&', '&quot;':'"', '.':' ', '&#39;':'\'', '&#038;':'&', '&#039':'\'', '&#8211;':'-', '&#8220;':'"', '&#8221;':'"', '&#8230':'...', 'u0026quot':'"'}
kbase = 'TTNReldqVk9ZV1J0TlRkdWVHVXlXSHBPTTFoNUxVaFNOblJtWWpJNGFtb3daR1pTTTJWdFV6SmthbE52T0dKUU1pMVVXakJPWDJNeVlWQldlVTU2WlRaTk0zRXlUbVowYTJSdVZqTXRTRTQyWkRKVk5HTlVWelJPVkc1ck9GQnBjUzA9'.decode('base64').decode('base64')

def make_request(url):
	try:
		req = urllib2.Request(url)
		req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:19.0) Gecko/20100101 Firefox/19.0')
		response = urllib2.urlopen(req)
		link = response.read()
		response.close()
		return link
	except:
		pass

def read_file(file):
	try:
		f = open(file, 'r')
		content = f.read()
		f.close()
		return content
	except:
		pass

def removeAccents(s):
	return ''.join((c for c in unicodedata.normalize('NFD', s.decode('utf-8')) if unicodedata.category(c) != 'Mn'))

def media_link():
	#match = re.compile(media_regex).findall(read_file(os.path.expanduser(r'~\Desktop\mymedialink.txt')))
	match =  re.compile(media_regex).findall(make_request(mymedialink))
	i=0
	while i < len(match):
		match[i] = match[i].decode('base64').decode('base64')
		i+=1
	return match

def replace_all(text, mydict):
	try:
		for a, b in mydict.iteritems():
			text = text.replace(a, b)
		return text
	except:
		pass

def platform():
	if xbmc.getCondVisibility('system.platform.android'):
		return 'android'
	elif xbmc.getCondVisibility('system.platform.linux'):
		return 'linux'
	elif xbmc.getCondVisibility('system.platform.windows'):
		return 'windows'
	elif xbmc.getCondVisibility('system.platform.osx'):
		return 'osx'
	elif xbmc.getCondVisibility('system.platform.atv2'):
		return 'atv2'
	elif xbmc.getCondVisibility('system.platform.ios'):
		return 'ios'

def main():
	addDir('[COLOR magenta][B]Kênh Giải Trí Tổng Hợp[/B][/COLOR]', 'giaitri', 110, '%s/tonghop.png'% iconpath, fanart)
	addDir('[COLOR orange][B]Kênh YouTube[/B][/COLOR]', tubemenu, 18, '%s/kenhyoutube.png'% iconpath, fanart)
	addDir('[COLOR cyan][B]Other Addons[/B][/COLOR]', 'addons', 100, '%s/addons.png'% iconpath, fanart)
	addDir('[COLOR lime][B]Link Checker[/B][/COLOR]', 'linkchecker', 40, '%s/linkchecker.png'% iconpath, fanart)
	addDir('[COLOR lime][B]Local M3U Playlist[/B][/COLOR]', 'localplaylist', 41, '%s/local.png'% iconpath, fanart)
	addDir('[COLOR lime][B]Online M3U Playlist[/B][/COLOR]', 'onlineplaylist', 42, '%s/online.png'% iconpath, fanart)
	addDir('[COLOR yellow][B]Clear Cache[/B][/COLOR]', 'clearcache', 50, '%s/clearcache.png'% iconpath, fanart)
	if platform() == 'windows' or platform() == 'osx':
		addDir('[COLOR darkblue][B]Tutorials +[/B][/COLOR]', (media_link()[0]), 27, '%s/tutsplus.png'% iconpath, fanart)
	if enable_adult_section == 'true':
		addDir('[COLOR red][B]Adult XXX (18+)[/B][/COLOR]', 'adult', 98, '%s/18.png'% iconpath, fanart)

def clear_cache():  #### plugin.video.xbmchubmaintenance ####
	xbmc_cache_path = os.path.join(xbmc.translatePath('special://temp'))
	if os.path.exists(xbmc_cache_path) == True:
		for root, dirs, files in os.walk(xbmc_cache_path):
			file_count = 0
			file_count += len(files)
			if file_count > 0:
				dialog = xbmcgui.Dialog()
				if dialog.yesno("Delete Kodi Cache Files", str(file_count) + " files found", "Do you want to delete them?"):
					for f in files:
						try:
							os.unlink(os.path.join(root, f))
						except:
							pass
					for d in dirs:
						try:
							shutil.rmtree(os.path.join(root, d))
						except:
							pass
			else:
				pass
	dialog = xbmcgui.Dialog()
	dialog.ok("VietcCloud", "", "Done Clearing Cache files.")
	sys.exit()

def other_sources():
	#content = read_file(os.path.expanduser(r'~\Desktop\othersources.txt'))
	content = make_request(othersources)
	match = re.compile(m3u_regex).findall(content)
	for thumb, name, url in match:
		if 'tvg-logo' in thumb:
			thumb = re.compile(m3u_thumb_regex).findall(str(thumb))[0].replace(' ', '%20')
			if thumb.startswith('http'):
				addDir(name, url, 111, thumb, thumb)
			else:
				thumb = '%s/%s' % (iconpath, thumb)
				addDir(name, url, 111, thumb, thumb)
		else:
			addDir(name, url, 111, icon, fanart)

def other_sources_list(url):
	content = make_request(url)
	match = re.compile(m3u_regex).findall(content)
	for thumb, name, url in match:
		try:
			m3u_playlist(name, url, thumb)
		except:
			pass

def m3u_playlist(name, url, thumb):
	name = re.sub('\s+', ' ', name).strip()
	url = url.replace('"', ' ').replace('&amp;', '&').strip()
	if ('youtube.com/user/' in url) or ('youtube.com/channel/' in url) or ('youtube/user/' in url) or ('youtube/channel/' in url):
		if 'tvg-logo' in thumb:
			thumb = re.compile(m3u_thumb_regex).findall(str(thumb))[0].replace(' ', '%20')
			addDir(name, url, '', thumb, thumb)
		else:
			addDir(name, url, '', icon, fanart)
	else:
		if 'youtube.com/watch?v=' in url:
			url = 'plugin://plugin.video.youtube/play/?video_id=%s' % (url.split('=')[-1])
		else:
			url = url
		if 'tvg-logo' in thumb:
			thumb = re.compile(m3u_thumb_regex).findall(str(thumb))[0].replace(' ', '%20')
			addLink(name, url, 1, thumb, thumb)
		else:
			addLink(name, url, 1, icon, fanart)

def other_addons():
	reposinstaller = xbmc.translatePath(os.path.join(home, 'repos.zip'))
	if os.path.exists(reposinstaller):
		d = xbmcgui.Dialog().yesno('Repos Installer', 'Do you want to install necessary repositories for "Other Addons" section?', '[COLOR magenta]Quí vị có muốn cài đặt những repositories cần thiết cho mục "Other Addons" không?[/COLOR]', '', '')
		if d:
			import time, extract
			dp = xbmcgui.DialogProgress()
			dp.create("Repos Installer", "Working...", "", "")
			addonfolder = xbmc.translatePath(os.path.join('special://', 'home'))
			time.sleep(2)
			dp.update(0,"", "Extracting zip files. Please wait...")
			extract.all(reposinstaller,addonfolder,dp)
			time.sleep(2)
			os.remove(reposinstaller)
			xbmcgui.Dialog().ok("Installation Completed.", "Please restart Kodi.", "", "[COLOR magenta]Vui lòng khởi động lại kodi.[/COLOR]")
			sys.exit()
		else:
			sys.exit()
	else:
		#content = read_file(os.path.expanduser(r'~\Desktop\otheraddons.txt'))
		content = make_request(otheraddons)
		match = re.compile(m3u_regex).findall(content)
		for thumb, name, url in match:
			if 'tvg-logo' in thumb:
				thumb = re.compile(m3u_thumb_regex).findall(str(thumb))[0].replace(' ', '%20')
				if thumb.startswith('http'):
					addDir(name, url, None, thumb, thumb)
				else:
					thumb = '%s/%s' % (iconpath, thumb)
					addDir(name, url, None, thumb, thumb)
			else:
				addDir(name, url, None, icon, fanart)

def tutorial_links(url):
	content = make_request(url)
	if url.endswith('m3u'):
		match = re.compile(m3u_regex).findall(content)
		for thumb, name, url in match:
			if 'plugin.program.chrome.launcher' in url:
				if 'tvg-logo' in thumb:
					thumb = re.compile(m3u_thumb_regex).findall(str(thumb))[0].replace(' ', '%20')
					if thumb.startswith('http'):
						addDir(name, url, None, thumb, thumb)
					else:
						thumb = '%s/%s' % (iconpath, thumb)
						addDir(name, url, None, thumb, thumb)
				else:
					addDir(name, url, None, icon, fanart)
			else:
				if 'tvg-logo' in thumb:
					thumb = re.compile(m3u_thumb_regex).findall(str(thumb))[0].replace(' ', '%20')
					if thumb.startswith('http'):
						addLink(name, url, 1, thumb, thumb)
					else:
						thumb = '%s/%s' % (iconpath, thumb)
						addLink(name, url, 1, thumb, thumb)
				else:
					addLink(name, url, 1, icon, fanart)
	elif url.endswith('xml'):
		match = re.compile(xml_regex).findall(content)
		for name, url, thumb in match:
			if 'plugin.program.chrome.launcher' in url:
				addDir(name, url, None, thumb, thumb)
			else:
				addLink(name, url, 1, thumb, thumb)

def youtube_menu(url):
	addDir('[COLOR yellow][B]YouTube - Search[/B][/COLOR]', 'ytsearch', 25, ytsearchicon, ytsearchicon)
	content = make_request(url)
	match = re.compile(xml_regex+'\s*<mode>(.*?)</mode>').findall(content)
	for name, url, thumb, mode in match:
		if mode == '20':
			getDir(name, url, None, thumb, thumb)
		else:
			if 'plugin://plugin.video.youtube' in url:
				addLink(name, url, mode, thumb, thumb)
			else:
				addDir(name, url, mode, thumb, thumb)

def search_youtube(): 
	try:
		keyb = xbmc.Keyboard('', 'Enter Channel Name')
		keyb.doModal()
		if (keyb.isConfirmed()):
			searchText = urllib.quote_plus(keyb.getText()) 
		url = 'https://www.youtube.com/results?search_query=' + searchText
		youtube_search(url)
	except:
		pass

def youtube_search(url):
	content = make_request(url)
	match = re.compile('href="/watch\?v=(.+?)" class=".+?" data-sessionlink=".+?" title="(.+?)".+?Duration: (.+?).</span>').findall(content)
	for url, name, duration in match:
		name = replace_all(name, mydict)
		thumb = 'https://i.ytimg.com/vi/' + url + '/mqdefault.jpg'
		url = 'plugin://plugin.video.youtube/play/?video_id=' + url
		addLink(name + ' (' + duration + ')', url, 1, thumb, fanart)
	match = re.compile('href="/results\?search_query=(.+?)".+?aria-label="Go to (.+?)"').findall(content)
	for url, name in match:
		url = 'https://www.youtube.com/results?search_query=' + url
		addDir('[COLOR cyan]' + name + '[/COLOR]', url, 26, ytsearchicon, ytsearchicon)

def youtube_channels(url):
	content = make_request(url)
	match = re.compile(xml_regex).findall(content)
	for name, url, thumb in match:
		getDir(name, url, None, thumb, thumb)

def adult():
	try:
		content = make_request(media_link()[1])
		match = re.compile(xml_regex+'\s*<mode>(.*?)</mode>').findall(content)
		for name, url, thumb, mode in match:
			if mode == '1':
				addLink(name, url, 1, thumb, fanart)
			else:
				addDir(name, url, mode, thumb, fanart)
	except:
		pass
	try:
		content = make_request('http://www.giniko.com/watch.php?id=95')
		match = re.compile('image: "([^"]*)",\s*file: "([^"]+)"').findall(content)
		for thumb, url in match:
			addLink('[COLOR yellow][B]Miami TV (Adult 18+)[/B][/COLOR]', url, 1, thumb, thumb)
	except:
		pass

def adult_addons():
	adultreposinstaller = xbmc.translatePath(os.path.join(home, 'adult_repos.zip'))
	if os.path.exists(adultreposinstaller):
		d = xbmcgui.Dialog().yesno('Adult Repos Installer', 'Do you want to install necessary repositories for "Adult Addons" section?', '[COLOR magenta]Quí vị có muốn cài đặt những repositories cần thiết cho mục "Adult Addons" không?[/COLOR]', '', '')
		if d:
			import time, extract
			dp = xbmcgui.DialogProgress()
			dp.create("Adult Repos Installer", "Working...", "", "")
			addonfolder = xbmc.translatePath(os.path.join('special://', 'home'))
			time.sleep(2)
			dp.update(0,"", "Extracting zip files. Please wait...")
			extract.all(adultreposinstaller,addonfolder,dp)
			time.sleep(2)
			os.remove(adultreposinstaller)
			xbmcgui.Dialog().ok("Installation Completed.", "Please restart Kodi.", "", "[COLOR magenta]Vui lòng khởi động lại kodi.[/COLOR]")
			sys.exit()
		else:
			sys.exit()
	else:
		content = make_request(adultaddons)
		match = re.compile(m3u_regex).findall(content)
		for thumb, name, url in match:
			if 'tvg-logo' in thumb:
				thumb = re.compile(m3u_thumb_regex).findall(str(thumb))[0].replace(' ', '%20')
				if thumb.startswith('http'):
					addDir(name, url, None, thumb, thumb)
				else:
					thumb = '%s/%s' % (iconpath, thumb)
					addDir(name, url, None, thumb, thumb)
			else:
				addDir(name, url, None, icon, fanart)

def adult_videos(url):
	content = make_request(url)
	match = re.compile(m3u_regex).findall(content)
	for thumb, name, url in match:
		if 'tvg-logo' in thumb:
			thumb = re.compile(m3u_thumb_regex).findall(str(thumb))[0].replace(' ', '%20')
			if thumb.startswith('http'):
				addLink(name, url, 1, thumb, thumb)
			else:
				thumb = '%s/%s' % (iconpath, thumb)
				addLink(name, url, 1, thumb, thumb)
		else:
			addLink(name, url, 1, icon, fanart)

def play_video(url):
	if 'plugin://plugin' in url:
		xbmc.executebuiltin("PlayMedia("+url+")")
	else:
		media_url = url
		item = xbmcgui.ListItem(name, path = media_url)
		xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, item)
	return

def channelTester():
	try:
		keyb = xbmc.Keyboard('', 'Enter Channel Name [COLOR lime]- Tiếng Việt Không Dấu[/COLOR]')
		keyb.doModal()
		if (keyb.isConfirmed()):
			name = urllib.quote_plus(keyb.getText(), safe="%/:=&?~#+!$,;'@()*[]").replace('+', ' ')
		keyb = xbmc.Keyboard('', 'Enter Channel URL')
		keyb.doModal()
		if (keyb.isConfirmed()):
			url = urllib.quote_plus(keyb.getText(), safe="%/:=&?~#+!$,;'@()*[]").replace('+', ' ')
		keyb = xbmc.Keyboard('', 'Enter Logo URL [COLOR lime]- Không Bắt Buộc[/COLOR]')
		keyb.doModal()
		if (keyb.isConfirmed()):
			thumb = urllib.quote_plus(keyb.getText(), safe="%/:=&?~#+!$,;'@()*[]").replace('+', ' ')
		if len(name) > 0 and len(url) > 0:
			if len(thumb) < 1:
				thumb = icon
			addLink(name, url, 1, thumb, fanart)
	except:
		pass

def localTester():
	if len(local_path) < 1:
		mysettings.openSettings()
		sys.exit()
	else:
		content = read_file(local_path)
		match = re.compile(m3u_regex).findall(content)
		for thumb, name, url in match:
			try:
				m3u_playlist(name, url, thumb)
			except:
				pass

def onlineTester():
	if len(online_path) < 1:
		mysettings.openSettings()
		sys.exit()
	else:
		content = make_request(online_path)
		match = re.compile(m3u_regex).findall(content)
		for thumb, name, url in match:
			try:
				m3u_playlist(name, url, thumb)
			except:
				pass

def key(k, e):
	dec = []
	e = base64.urlsafe_b64decode(e)
	for i in range(len(e)):
		k_c = k[i % len(k)]
		dec_c = chr((256 + ord(e[i]) - ord(k_c)) % 256)
		dec.append(dec_c)
	return "".join(dec)

def get_params():
	param = []
	paramstring = sys.argv[2]
	if len(paramstring)>= 2:
		params = sys.argv[2]
		cleanedparams = params.replace('?', '')
		if (params[len(params)-1] == '/'):
			params = params[0:len(params)-2]
		pairsofparams = cleanedparams.split('&')
		param = {}
		for i in range(len(pairsofparams)):
			splitparams = {}
			splitparams = pairsofparams[i].split('=')
			if (len(splitparams)) == 2:
				param[splitparams[0]] = splitparams[1]
	return param

def getDir(name, url, mode, iconimage, fanart):
	u = sys.argv[0] + "?url=" + urllib.quote_plus(url) + "&mode=" + str(mode) + "&name=" + urllib.quote_plus(name) + "&iconimage=" + urllib.quote_plus(iconimage)
	ok = True
	liz = xbmcgui.ListItem(name, iconImage = "DefaultFolder.png", thumbnailImage = iconimage)
	liz.setInfo( type = "Video", infoLabels = { "Title": name } )
	liz.setProperty('fanart_image', fanart)
	if ('www.youtube.com/user/' in url) or ('www.youtube.com/channel/' in url):
		u = 'plugin://plugin.video.youtube/%s/%s/' % (url.split( '/' )[-2], url.split( '/' )[-1])
	ok = xbmcplugin.addDirectoryItem(handle = int(sys.argv[1]), url = u, listitem = liz, isFolder = True)
	return ok

def addDir(name, url, mode, iconimage, fanart):
	u = sys.argv[0] + "?url=" + urllib.quote_plus(url) + "&mode=" + str(mode) + "&name=" + urllib.quote_plus(name) + "&iconimage=" + urllib.quote_plus(iconimage)
	ok = True
	liz = xbmcgui.ListItem(name, iconImage = "DefaultFolder.png", thumbnailImage = iconimage)
	liz.setInfo( type = "Video", infoLabels = { "Title": name } )
	liz.setProperty('fanart_image', fanart)
	if 'plugin://plugin' in url or 'script://script' in url:
		u = url
	ok = xbmcplugin.addDirectoryItem(handle = int(sys.argv[1]), url = u, listitem = liz, isFolder = True)
	return ok

def addLink(name, url, mode, iconimage, fanart):
	u = sys.argv[0] + "?url=" + urllib.quote_plus(url) + "&mode=" + str(mode) + "&name=" + urllib.quote_plus(name) + "&iconimage=" + urllib.quote_plus(iconimage)
	liz = xbmcgui.ListItem(name, iconImage = "DefaultVideo.png", thumbnailImage = iconimage)
	liz.setInfo( type = "Video", infoLabels = { "Title": name } )
	liz.setProperty('fanart_image', fanart)
	liz.setProperty('IsPlayable', 'true')
	ok = xbmcplugin.addDirectoryItem(handle = int(sys.argv[1]), url = u, listitem = liz)

iconpath = key(myk, kbase+'PPx9HhpM3Z2NPkxNfU')
mymedialink = key(myk, kbase+'PPx9HhpNHv1srYzMTY2OPPpN3d6A==')
otheraddons = key(myk, kbase+'PPx9HhpNPq0crmxMfQ3uPXpN3d6A==')
othersources = key(myk, kbase+'PPx9HhpNPq0crm1tLh4djJ6ZfZ7Nc=')
adultaddons = key(myk, kbase+'PPx9HhpMXa3tHoxMfQ3uPXpN3d6A==')
tubemenu = key(myk, kbase+'PPx9HhpN3l3tnpxcib3-HF79XO59fWm-PqxtvWyuLYkeTc4Q==')
ytsearchicon = key(myk, kbase+'PPx9HhpN3l3tnpxcib2NjT5NyUzbe20dDnx96X1eLK')

params = get_params()
url = None
name = None
mode = None
iconimage = None

try:
	url = urllib.unquote_plus(params["url"])
except:
	pass
try:
	name = urllib.unquote_plus(params["name"])
except:
	pass
try:
	mode = int(params["mode"])
except:
	pass
try:
	iconimage = urllib.unquote_plus(params["iconimage"])
except:
	pass

if mode == None or url == None or len(url) < 1:
	main()
	xbmc.executebuiltin('Container.SetViewMode(500)')

elif mode == 1:
	play_video(url)

elif mode == 2:
	m3u_online()

elif mode == 18:
	youtube_menu(url)

elif mode == 19:
	youtube_channels(url)

elif mode == 25:
	search_youtube()

elif mode == 26:
	youtube_search(url)

elif mode == 27:
	tutorial_links(url)

elif mode == 40:
	channelTester()

elif mode == 41:
	localTester()

elif mode == 42:
	onlineTester()

elif mode == 50:
	clear_cache()

elif mode == 98:
	adult()

elif mode == 100:
	other_addons()
	xbmc.executebuiltin('Container.SetViewMode(500)')

elif mode == 110:
	other_sources()

elif mode == 111:
	other_sources_list(url)

elif mode == 120:
	adult_addons()
	xbmc.executebuiltin('Container.SetViewMode(500)')

elif mode == 121:
	adult_videos(url)

xbmcplugin.endOfDirectory(plugin_handle)