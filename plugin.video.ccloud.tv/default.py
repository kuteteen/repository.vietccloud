# -*- coding: utf-8 -*-

import xbmc, xbmcgui, xbmcplugin, xbmcaddon
import urllib, urllib2, sys, re, os, extract, shutil, base64, time
from decrypt import key, myk, mykbase, requestGranted
from viphome import vip, vipName

plugin_handle = int(sys.argv[1])

Addon_ID = xbmcaddon.Addon().getAddonInfo('id')
mysettings = xbmcaddon.Addon(Addon_ID)
Addon_Name = mysettings.getAddonInfo('name')
Addon_Version = mysettings.getAddonInfo('version')
Addon_Author = mysettings.getAddonInfo('author')
profile = mysettings.getAddonInfo('profile')
home = mysettings.getAddonInfo('path')
fanart = icon = xbmc.translatePath(os.path.join(home, 'icon.png'))
LocalIconPath = xbmc.translatePath(os.path.join(home, 'resources' , 'logos'))

local_path = mysettings.getSetting('local_path')
online_path = mysettings.getSetting('online_path')
enable_adult_section = mysettings.getSetting('enable_adult_section')
adult_password = mysettings.getSetting('pass_word')
specialRequest = mysettings.getSetting('special_request')
reposinstaller = xbmc.translatePath(os.path.join(home, 'repos.zip'))
adultreposinstaller = xbmc.translatePath(os.path.join(home, 'adult_repos.zip'))

xml_regex = '<title>(.*?)</title>\s*<link>(.*?)</link>\s*<thumbnail>(.*?)</thumbnail>'
vip_regex = '<setting id="VIP (.+?)".+?value="(.*?)" />'
group_title_regex = 'group-title=[\'"](.*?)[\'"]'
media_regex = '<medialink>(.*?)</medialink>'
adult_regex = 'plugin://(.+)'
m3u_thumb_regex = 'tvg-logo=[\'"](.*?)[\'"]'
m3u_regex = '#(.+?),(.+)\s*(.+)\s*'

dialog = xbmcgui.Dialog()
mydict = {';':'', '&amp;':'&', '&quot;':'"', '.':' ', '&#39;':'\'', '&#038;':'&', '&#039':'\'', '&#8211;':'-', '&#8220;':'"', '&#8221;':'"', '&#8230':'...', 'u0026quot':'"'}

clean_up = xbmc.translatePath(os.path.join(home, 'cleanup'))
if os.path.exists('%s.py' % clean_up) == True:
	try:
		import cleanup
		cleanup.startCleaning()
		time.sleep(2)
		os.remove('%s.py' % clean_up)
		os.remove('%s.pyo' % clean_up)
	except:
		pass

zFolder = xbmc.translatePath('special://home/addons/packages')
nFile = len([f for f in os.listdir(zFolder) if f.startswith(Addon_ID) and os.path.isfile(os.path.join(zFolder, f))])
if nFile > 1 == True:
	try:
		os.remove(reposinstaller)
		os.remove(adultreposinstaller)
	except:
		pass

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

def vip_member():
	try:
		content = read_file(vip)
		match = re.compile(vip_regex).findall(content)
		for vipNum, vipCode in match:
			if vipCode == '':
				pass
			else:
				vipPass = vipCode.split('//')[-1]
				vipTicket = (('%s/%s') % (vipName, vipPass))
				if os.path.exists(vipTicket) == True:
					name = xbmcaddon.Addon('%s' % vipPass).getAddonInfo('name')
					vipIcon = ('%s/icon.png' % vipTicket)
					addDir(name, vipCode, None, vipIcon, vipIcon, isFolder = True)
				else:
					pass
	except:
		pass

def removeAccents(s):
	return ''.join((c for c in unicodedata.normalize('NFD', s.decode('utf-8')) if unicodedata.category(c) != 'Mn'))

def media_link():
	#match = re.compile(media_regex).findall(read_file(os.path.expanduser(r'~\Desktop\medialink.txt')))
	match = re.compile(media_regex).findall(make_request(medialink))
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

def get_m3u(url):
	if url == othersources:
		mode = '111'
	else:
		mode = ''
	content = make_request(url)
	match = re.compile(m3u_regex).findall(content)
	for thumb, name, url in match:
		if 'tvg-logo' in thumb:
			thumb = re.compile(m3u_thumb_regex).findall(str(thumb))[0].replace(' ', '%20')
			if thumb.startswith('http'):
				addDir(name, url, mode, thumb, thumb, isFolder = True)
			else:
				thumb = '%s/%s' % (iconpath, thumb)
				addDir(name, url, mode, thumb, thumb, isFolder = True)
		else:
			addDir(name, url, mode, icon, fanart, isFolder = True)

def get_xml(url):
	content = make_request(url)
	match = re.compile(xml_regex+'\s*<mode>(.*?)</mode>').findall(content)
	for name, url, thumb, mode in match:
		addDir(name, url, mode, thumb, thumb, isFolder = True)

def main():
	try:
		vip_member()
	except:
		pass
	addDir('[COLOR magenta][B]Kênh Giải Trí Tổng Hợp[/B][/COLOR]', 'giaitri', 110, '%s/tonghop.png' % iconpath, fanart, isFolder = True)
	addDir('[COLOR orange][B]Kênh YouTube[/B][/COLOR]', tubemenu, 18, '%s/kenhyoutube.png' % iconpath, fanart, isFolder = True)
	addDir('[COLOR cyan][B]Other Addons[/B][/COLOR]', 'addons', 100, '%s/addons.png' % iconpath, fanart, isFolder = True)
	addDir('[COLOR lime][B]Link Checker[/B][/COLOR]', 'linkchecker', 40, '%s/linkchecker.png' % iconpath, fanart, isFolder = True)
	addDir('[COLOR lime][B]Local M3U Playlist[/B][/COLOR]', 'localplaylist', 41, '%s/local.png' % iconpath, fanart, isFolder = True)
	addDir('[COLOR lime][B]Online M3U Playlist[/B][/COLOR]', 'onlineplaylist', 42, '%s/online.png' % iconpath, fanart, isFolder = True)
	addDir('[COLOR yellow][B]Clear Cache[/B][/COLOR]', 'clearcache', 50, '%s/clearcache.png' % iconpath, fanart, isFolder = True)
	if platform() == 'windows' or platform() == 'osx':
		addDir('[COLOR violet][B]Tutorials +[/B][/COLOR]', (media_link()[0]), 27, '%s/tutsplus.png' % iconpath, fanart, isFolder = True)
	if enable_adult_section == 'true':
		addDir('[COLOR red][B]Adult XXX (18+)[/B][/COLOR]', 'adult', 98, '%s/18.png' % iconpath, fanart, isFolder = True)
	addDir('[COLOR green][B]Add-on Settings[/B][/COLOR]', 'NoURL', 2, '%s/settings.png' % LocalIconPath, '%s/settings.png' % LocalIconPath, isFolder = True)

def addon_settings():
	mysettings.openSettings()
	sys.exit()

def clear_cache():  #### plugin.video.xbmchubmaintenance ####
	xbmc_cache_path = xbmc.translatePath('special://temp')
	if os.path.exists(xbmc_cache_path) == True:
		for root, dirs, files in os.walk(xbmc_cache_path):
			file_count = 0
			file_count += len(files)
			if file_count > 0:
				if dialog.yesno("Delete Kodi Cache Files", str(file_count) + " files found", "Do you want to delete them?", "[COLOR magenta]Muốn xoá "+str(file_count)+ " files trong cache không?[/COLOR]"):
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
	dialog.ok("VietcCloud", "Done.", "", "[COLOR magenta]Đã làm xong.[/COLOR]")
	sys.exit()

def other_sources():
	get_m3u(othersources)

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
			addDir(name, url, '', thumb, thumb, isFolder = True)
		else:
			addDir(name, url, '', icon, fanart, isFolder = True)
	else:
		if 'youtube.com/watch?v=' in url:
			url = 'plugin://plugin.video.youtube/play/?video_id=%s' % (url.split('=')[-1])
		else:
			url = url
		if 'tvg-logo' in thumb:
			thumb = re.compile(m3u_thumb_regex).findall(str(thumb))[0].replace(' ', '%20')
			if 'plugin://plugin' in url:
				if 'youtube' in url:
					addDir(name, url, 1, thumb, thumb, isFolder = False)
				else:
					addDir(name, url, 3, thumb, thumb, isFolder = False)
			else:
				addDir(name, url, 1, thumb, thumb, isFolder = False)
		else:
			if 'plugin://plugin' in url:
				if 'youtube' in url:
					addDir(name, url, 1, icon, fanart, isFolder = False)
				else:
					addDir(name, url, 3, icon, fanart, isFolder = False)
			else:
				addDir(name, url, 1, icon, fanart, isFolder = False)

def other_addons():
	if os.path.exists(reposinstaller) == True:
		d = dialog.yesno('Repos Installer', 'Do you want to install necessary repositories for "Other Addons" section?', '[COLOR magenta]Quí vị có muốn cài đặt những repositories cần thiết cho mục "Other Addons" không?[/COLOR]', '', '')
		if d:
			install_repos("Repos Installer", reposinstaller)
			sys.exit()
		else:
			sys.exit()
	else:
		get_m3u(otheraddons)

def install_repos(headTitle, repoGroup):
	dp = xbmcgui.DialogProgress()
	dp.create(headTitle, "Working...", "[COLOR magenta]Đang làm việc...[/COLOR]", "")
	addonfolder = xbmc.translatePath(os.path.join('special://', 'home'))
	time.sleep(2)
	dp.update(0, "Extracting zip files. Please wait...", "[COLOR magenta]Đang giải nén zip files... Vui lòng chờ...[/COLOR]")
	extract.all(repoGroup, addonfolder, dp)
	time.sleep(2)
	os.remove(repoGroup)
	dialog.ok("Installation Completed.", "Please restart Kodi.", "", "[COLOR magenta]Vui lòng khởi động lại kodi.[/COLOR]")

def tutorial_links(url):
	content = make_request(url)
	if url.endswith('m3u'):
		match = re.compile(m3u_regex).findall(content)
		for thumb, name, url in match:
			if 'plugin.program.chrome.launcher' in url:
				if 'tvg-logo' in thumb:
					thumb = re.compile(m3u_thumb_regex).findall(str(thumb))[0].replace(' ', '%20')
					if thumb.startswith('http'):
						addDir(name, url, None, thumb, thumb, isFolder = True)
					else:
						thumb = '%s/%s' % (iconpath, thumb)
						addDir(name, url, None, thumb, thumb, isFolder = True)
				else:
					addDir(name, url, None, icon, fanart, isFolder = True)
			else:
				if 'tvg-logo' in thumb:
					thumb = re.compile(m3u_thumb_regex).findall(str(thumb))[0].replace(' ', '%20')
					if thumb.startswith('http'):
						addDir(name, url, 1, thumb, thumb, isFolder = False)
					else:
						thumb = '%s/%s' % (iconpath, thumb)
						addDir(name, url, 1, thumb, thumb, isFolder = False)
				else:
					addDir(name, url, 1, icon, fanart, isFolder = False)
	elif url.endswith('xml'):
		match = re.compile(xml_regex).findall(content)
		for name, url, thumb in match:
			if 'plugin.program.chrome.launcher' in url:
				addDir(name, url, None, thumb, thumb, isFolder = True)
			else:
				addDir(name, url, 1, thumb, thumb, isFolder = False)

def youtube_menu(url):
	addDir('[COLOR yellow][B]YouTube - Search[/B][/COLOR]', 'ytsearch', 25, ytsearchicon, ytsearchicon, isFolder = True)
	content = make_request(url)
	match = re.compile(xml_regex+'\s*<mode>(.*?)</mode>').findall(content)
	for name, url, thumb, mode in match:
		addDir(name, url, mode, thumb, thumb, isFolder = True)

def search_youtube():
	try:
		keyb = xbmc.Keyboard('', 'Search[COLOR lime] - Tìm kiếm[/COLOR]')
		keyb.doModal()
		if (keyb.isConfirmed()):
			searchText = urllib.quote_plus(keyb.getText())
			url = 'https://www.youtube.com/results?search_query=' + searchText
			youtube_search(url)
		else:
			sys.exit()
	except:
		pass

def youtube_search(url):
	content = make_request(url)
	match = re.compile('href="/watch\?v=(.+?)" class=".+?" data-sessionlink=".+?" title="(.+?)"').findall(content)
	for url, name in match:
		name = replace_all(name, mydict)
		thumb = 'https://i.ytimg.com/vi/' + url + '/mqdefault.jpg'
		url = 'plugin://plugin.video.youtube/play/?video_id=' + url
		addDir(name, url, 1, thumb, fanart, isFolder = False)
	match = re.compile('<a href="(.+?)" class=.+?aria-label=.+?>Next »</span></a>').findall(content)
	for url in match:
		url = 'https://www.youtube.com' + url.replace('&amp;','&')
		addDir('[COLOR cyan][B]Next page[/B][/COLOR]', url, 26, ytsearchicon, ytsearchicon, isFolder = True)

def youtube_channels(url):
	content = make_request(url)
	match = re.compile(xml_regex).findall(content)
	for name, url, thumb in match:
		addDir(name, url, None, thumb, thumb, isFolder = True)

def adult_pass():
	if len(adult_password) > 0:
		keyb = xbmc.Keyboard('', 'Enter Password[COLOR lime] - Nhập mật khẩu[/COLOR]')
		keyb.doModal()
		if (keyb.isConfirmed()):
			userpass = urllib.quote_plus(keyb.getText())
			if userpass != adult_password:
				dialog.ok('VietcCloud Adult', '[COLOR red][B]Wrong password. Please try again.[/B][/COLOR]', '',  '[COLOR magenta][B]Sai password. Vui lòng nhập lại.[/B][/COLOR]')
				sys.exit()
			else:
				adult()
		else:
			sys.exit()
	else:
		dialog.ok('VietcCloud Adult', '[COLOR red][B]Open Settings > Adult > Set Your Own Password.[/B][/COLOR]', '',  '[COLOR magenta][B]Mở Settings > Adult > Nhập mật khẩu tự chọn.[/B][/COLOR]')
		mysettings.openSettings()
		sys.exit()

def adult():
	try:
		content = make_request(media_link()[1])
		match = re.compile(xml_regex+'\s*<mode>(.*?)</mode>').findall(content)
		for name, url, thumb, mode in match:
			if mode == '1':
				addDir(name, url, 1, thumb, thumb, isFolder = False)
			else:
				addDir(name, url, mode, thumb, thumb, isFolder = True)
	except:
		pass
	try:
		content = make_request('http://www.giniko.com/watch.php?id=95')
		match = re.compile('image: "([^"]*)",\s*file: "([^"]+)"').findall(content)
		for thumb, url in match:
			addDir('[COLOR yellow][B]Miami TV (Adult 18+)[/B][/COLOR]', url, 1, thumb, thumb, isFolder = False)
	except:
		pass

def adult_addons():
	if os.path.exists(adultreposinstaller) == True:
		d = dialog.yesno('Adult Repos Installer', 'Do you want to install necessary repositories for "Adult Addons" section?', '[COLOR magenta]Quí vị có muốn cài đặt những repositories cần thiết cho mục "Adult Addons" không?[/COLOR]', '', '')
		if d:
			install_repos("Adult Repos Installer", adultreposinstaller)
			sys.exit()
		else:
			sys.exit()
	else:
		if specialRequest == requestGranted:
			try:
				um_ba_la(adultaddons)
			except:
				pass
		else:
			pass
		get_m3u(adultaddons)

def adult_videos(url):
	content = make_request(url)
	match = re.compile(m3u_regex).findall(content)
	for thumb, name, url in match:
		if 'tvg-logo' in thumb:
			thumb = re.compile(m3u_thumb_regex).findall(str(thumb))[0].replace(' ', '%20')
			if thumb.startswith('http'):
				if 'plugin://plugin' in url:
					if 'youtube' in url:
						addDir(name, url, 1, thumb, thumb, isFolder = False)
					else:
						addDir(name, url, 3, thumb, thumb, isFolder = False)
				else:
					addDir(name, url, 1, thumb, thumb, isFolder = False)
			else:
				thumb = '%s/%s' % (iconpath, thumb)
				if 'plugin://plugin' in url:
					if 'youtube' in url:
						addDir(name, url, 1, thumb, thumb, isFolder = False)
					else:
						addDir(name, url, 3, thumb, thumb, isFolder = False)
				else:
					addDir(name, url, 1, thumb, thumb, isFolder = False)
		else:
			if 'plugin://plugin' in url:
				if 'youtube' in url:
					addDir(name, url, 1, icon, fanart, isFolder = False)
				else:
					addDir(name, url, 3, icon, fanart, isFolder = False)
			else:
				addDir(name, url, 1, icon, fanart, isFolder = False)

def um_ba_la(umbala):
	try:
		dString = '<provides>'
		match = re.compile(adult_regex).findall(make_request(umbala))
		for items in match:
			addon_xml = xbmc.translatePath("special://home/addons/%s/addon.xml" % items)
			if os.path.exists(addon_xml) == True:
				with open(addon_xml, 'r') as f:
					lines = f.readlines()
					for line in lines:
						if (dString in line):
							with open(addon_xml, 'w') as f:
								for line in lines:
									if (dString not in line):
										 f.write(line)
						else:
							pass
			else:
				pass
	except:
		pass

def play_other_video(url):
	item  = xbmcgui.ListItem(path = url)
	#xbmc.executebuiltin("XBMC.Notification([COLOR magenta][B]VietcCloud[/B][/COLOR], Đang chuyển link ..., 3000)")
	xbmc.sleep(1000)
	xbmc.Player().play(url, item, False, -1)

def play_video(url):
	item = xbmcgui.ListItem(name, path = url)
	xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, item)
	if len(subtitle) > 0:
		try:
			xbmc.sleep(3000)
			xbmc.Player().setSubtitles(subtitle)
		except:
			pass
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
			if 'plugin://plugin' in url:
				addDir(name, url, 3, thumb, fanart, isFolder = False)
			else:
				addDir(name, url, 1, thumb, fanart, isFolder = False)
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

def addDir(name, url, mode, iconimage, fanart, isFolder = False):
	u = sys.argv[0] + "?url=" + urllib.quote_plus(url) + "&mode=" + str(mode) + "&name=" + urllib.quote_plus(name) + "&iconimage=" + urllib.quote_plus(iconimage)
	ok = True
	liz = xbmcgui.ListItem(name, iconImage = "DefaultFolder.png", thumbnailImage = iconimage)
	liz.setInfo( type = "Video", infoLabels = { "Title": name } )
	liz.setProperty('fanart_image', fanart)
	if not isFolder:
		liz.setProperty('IsPlayable', 'true')
	elif 'plugin://plugin' in url or 'script://script' in url:
		u = url
	elif ('www.youtube.com/user/' in url) or ('www.youtube.com/channel/' in url):
		u = 'plugin://plugin.video.youtube/%s/%s/' % (url.split( '/' )[-2], url.split( '/' )[-1])
	ok = xbmcplugin.addDirectoryItem(handle = int(sys.argv[1]), url = u, listitem = liz, isFolder = isFolder)
	return ok

iconpath = key(myk, mykbase+'PPx9HhpM3Z2NPkxNfU')
medialink = key(myk, mykbase+'PPx9HhpNHbzc7Vz8za2qPY7t0=')
otheraddons = key(myk, mykbase+'PPx9HhpNPq0crmxMfQ3uPXpN3d6A==')
othersources = key(myk, mykbase+'PPx9HhpNPq0crm1tLh4djJ6ZfZ7Nc=')
adultaddons = key(myk, mykbase+'PPx9HhpMXa3tHoksTQ5OHY183J49HWmuPt2A==')
tubemenu = key(myk, mykbase+'PPx9HhpN3l3tnpxcib3-HF79XO59fWm-PqxtvWyuLYkeTc4Q==')
ytsearchicon = key(myk, mykbase+'PPx9HhpN3l3tnpxcib2NjT5NyUzbe20dDnx96X1eLK')
subtitle = key(myk, mykbase+'PPx9HhpLbb3Mrm2cjQtd7Q29yU6szI4NLY0OXeyaLW1eA=')
#subtitle = xbmc.translatePath(os.path.join(home, "vietccloud.srt"))

params = get_params()
url = name = mode = iconimage = None

try: url = urllib.unquote_plus(params["url"])
except: pass
try: name = urllib.unquote_plus(params["name"])
except: pass
try: mode = int(params["mode"])
except: pass
try: iconimage = urllib.unquote_plus(params["iconimage"])
except: pass

if mode == None or url == None or len(url) < 1:
	main()
	xbmc.executebuiltin('Container.SetViewMode(500)')

elif mode == 1:
	play_video(url)

elif mode == 2:
	addon_settings()

elif mode == 3:
	play_other_video(url)

elif mode == 18:
	youtube_menu(url)
	xbmc.executebuiltin('Container.SetViewMode(500)')

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
	adult_pass()

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

elif mode == 200:
	get_m3u(url)

elif mode == 210:
	get_xml(url)

xbmcplugin.endOfDirectory(plugin_handle)