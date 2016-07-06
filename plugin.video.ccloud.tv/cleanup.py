# -*- coding: utf-8 -*-

import xbmc, xbmcaddon, os

AddonID = 'plugin.video.ccloud.tv'
mysettings = xbmcaddon.Addon(AddonID)
profile = mysettings.getAddonInfo('profile')
xFile = xbmc.translatePath(os.path.join(profile, 'settings.xml'))

if os.path.exists(xFile) == True:
	try:
		os.remove(xFile)
	except:
		pass
else:
	pass