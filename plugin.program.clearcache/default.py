# -*- coding: utf-8 -*-

import urllib, urllib2, sys, re, os, shutil
import xbmc, xbmcgui, xbmcplugin, xbmcaddon

plugin_handle = int(sys.argv[1])
mysettings = xbmcaddon.Addon(id = 'plugin.program.clearcache')
profile = mysettings.getAddonInfo('profile')
home = mysettings.getAddonInfo('path')
fanart = xbmc.translatePath(os.path.join(home, 'icon.png'))
icon = xbmc.translatePath(os.path.join(home, 'icon.png'))
xbmc_cache_path = os.path.join(xbmc.translatePath('special://temp'))

def main():
	addDir('[COLOR yellow][B]Clear Cache[/B][/COLOR]', 'ClearCache', 1, icon, fanart)

def clear_cache():  #### plugin.video.xbmchubmaintenance ####
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
	dialog.ok("Delete Kodi Cache Files", "", "Done Clearing Cache files.")
	#sys.exit()

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

def addDir(name, url, mode, iconimage, fanart):
	u = sys.argv[0] + "?url=" + urllib.quote_plus(url) + "&mode=" + str(mode) + "&name=" + urllib.quote_plus(name) + "&iconimage=" + urllib.quote_plus(iconimage)
	ok = True
	liz = xbmcgui.ListItem(name, iconImage = "DefaultFolder.png", thumbnailImage = iconimage)
	liz.setInfo( type = "Video", infoLabels = { "Title": name } )
	liz.setProperty('fanart_image', fanart)
	ok = xbmcplugin.addDirectoryItem(handle = int(sys.argv[1]), url = u, listitem = liz, isFolder = True)
	return ok

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

elif mode == 1:
	clear_cache()

xbmcplugin.endOfDirectory(plugin_handle)