# -*- coding: utf-8 -*-

import xbmc, xbmcaddon

mysettings = xbmcaddon.Addon(id = 'plugin.video.ccloud.tv')
auto_run = mysettings.getSetting('enable_autorun')

if auto_run == 'true':
	xbmc.executebuiltin("RunAddon(plugin.video.ccloud.tv)")