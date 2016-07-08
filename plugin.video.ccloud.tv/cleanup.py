import xbmc, xbmcaddon, os

Addon_ID = xbmcaddon.Addon().getAddonInfo('id')
mysettings = xbmcaddon.Addon(Addon_ID)
profile = mysettings.getAddonInfo('profile')
xFile = xbmc.translatePath(os.path.join(profile, 'settings.xml'))

def startCleaning():
	if os.path.exists(xFile) == True:
		try:
			os.remove(xFile)
		except:
			pass

if __name__ == '__main__':
	startCleaning()