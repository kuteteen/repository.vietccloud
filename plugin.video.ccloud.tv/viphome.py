# -*- coding: utf-8 -*-

import xbmc, xbmcaddon, os

Addon_ID = xbmcaddon.Addon().getAddonInfo('id')
mysettings = xbmcaddon.Addon(Addon_ID)
profile = mysettings.getAddonInfo('profile')

vip = xbmc.translatePath(os.path.join(profile, 'settings.xml'))
vipName = xbmc.translatePath('special://home/addons')