#!/usr/bin/python
# -*- coding: latin-1 -*-

import xbmc,xbmcplugin
import xbmcgui
import sys
import urllib, urllib2
import time
import re
from htmlentitydefs import name2codepoint as n2cp
import httplib
import urlparse
from os import path, system
import socket
from urllib2 import Request, URLError, urlopen
from urlparse import parse_qs
from urllib import unquote_plus


thisPlugin = int(sys.argv[1])
addonId = "plugin.video.xhamster"
dataPath = xbmc.translatePath('special://profile/addon_data/%s' % (addonId))
if not path.exists(dataPath):
       cmd = "mkdir -p " + dataPath
       system(cmd)
       
Host = "http://xhamster.com/"

def getUrl(url):
        pass#print"Here in getUrl url =", url
	req = urllib2.Request(url)
	req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
	response = urllib2.urlopen(req)
	link=response.read()
	response.close()
	return link
	
def listSites():
        names = []
        sites = []
        urls = []
        names.append("Xhamster")
        urls.append("http://xhamster.com/")
        sites.append("1")
#        names.append("Dclip")
#        urls.append("http://www.deviantclip.com/categories")
#        sites.append("2")
        
        i = 0
        for name in names:
               pic = " "
               url = urls[i]
               site = sites[i]
               i = i+1
               addDirectoryItem(name, {"name":name, "url":url, "mode":1, "site":site}, pic)
        xbmcplugin.endOfDirectory(thisPlugin)


def showContent(name, Host, site):
    pass#print"Here in default-py site B=", site
    if site == str(1):
        content = getUrl(Host)
        pass#print"content A =", content

        pic = " "
        addDirectoryItem("Search", {"name":"Search", "url":Host, "mode":5, "site":site}, pic)           
        i1 = 0           
        if i1 == 0:
                regexcat = "><a href='http://xhamster.com/channels(.*?)'>(.*?)</a><"
                match = re.compile(regexcat,re.DOTALL).findall(content)
                pass#print"match =", match
                for url, name in match:
                        url1 = "http://xhamster.com/channels" + url
                        pic = " "
                        pass#print"Here in Showcontent url1 =", url1
                        addDirectoryItem(name, {"name":name, "url":url1, "mode":2, "site":site}, pic)
                xbmcplugin.endOfDirectory(thisPlugin)
                
    elif site == str(2):                
        content = getUrl(Host)
        #pass#print"content A =", content
        icount = 0
	start = 0
	n0 = content.find('<h2>CATEGORIES</h2>', start)
	if n0<0:
                return
        content = content[n0:]
        #pass#print"content A2 =", content            
        i1 = 0           
        if i1 == 0:
                regexcat = '<a href="(.*?)" title="(.*?)">.*?src="(.*?)"'
                match = re.compile(regexcat,re.DOTALL).findall(content)
                ##pass#print"match =", match
                for url, name, pic in match:
                        url1 = "http://www.deviantclip.com" + url
                        pic = pic
                        ##pass#print"Here in Showcontent url1 =", url1
                        addDirectoryItem(name, {"name":name, "url":url1, "mode":2, "site":site}, pic)
                xbmcplugin.endOfDirectory(thisPlugin)                

def getPage(name, urlmain, site):
    pass#print"Here in default-py site C=", site
    if site == str(1):      
                pages = [1, 2, 3, 4, 5, 6]
                n1 = urlmain.find(".html",0)
                if (n1 < 0):
                        return
                n2 = urlmain.rfind("-", 0, n1)
                if (n2 < 0):
                        return
#                pn = "2"
                url1 = urlmain[:(n2+1)]
                url2 = urlmain[n1:]
                for page in pages:
                        url = url1 + str(page) + url2
                        name = "Page " + str(page)
                        pic = " "
                        addDirectoryItem(name, {"name":name, "url":url, "mode":3, "site":site}, pic)
                xbmcplugin.endOfDirectory(thisPlugin)
    elif site == str(2):      
                pass#print"Here in default-py site D=", site
                pages = [1, 2, 3, 4, 5, 6]
                for page in pages:
                        url1 = urlmain + "/videos?p=" + str(page)
                        name = "Page " + str(page)
                        pic = " "
                        addDirectoryItem(name, {"name":name, "url":url1, "mode":3, "site":site}, pic)
                xbmcplugin.endOfDirectory(thisPlugin)

def getVideos(name1, urlmain, site):
    if site == str(1):      
	content = getUrl(urlmain)
#	pass#print"content B =", content
        pos0 = content.find("Promoted Videos", 0)
        if (pos0 < 0):
                return
	pos1 = content.find("<div class='video'", pos0)
        if (pos1 < 0):
                return
        content = content[pos1:]
	
	regexvideo = "><a href='(.*?)'.*?><img src='(.*?)'.*?alt=(.*?)/>"
	match = re.compile(regexvideo,re.DOTALL).findall(content)
        pass#print"match =", match
        for url, pic, name in match:
                 name = name.replace('"', '')
                 if "new-british" in url:
                        name = "British"
                 pic = pic 
                 pass#print"Here in getVideos url =", url
	         addDirectoryItem(name, {"name":name, "url":url, "mode":4, "site":site}, pic)
        xbmcplugin.endOfDirectory(thisPlugin)	         
    if site == str(2):      
	content = getUrl(urlmain)
#	pass#print"content B =", content

	regexvideo = 'thumb_container video.*?href="(.*?)" title="(.*?)">.*?src="(.*?)"'
	match = re.compile(regexvideo,re.DOTALL).findall(content)
        ##pass#print"match =", match
        for url, name, pic in match:
                 name = name.replace('"', '')
                 url = "http://www.deviantclip.com" + url
                 pic = pic 
                 ##pass#print"Here in getVideos url =", url
	         addDirectoryItem(name, {"name":name, "url":url, "mode":4, "site":site}, pic)
        xbmcplugin.endOfDirectory(thisPlugin)	         
                
def getVideos2(name, url, site):
    if site == str(1):      
                f = open("/tmp/xbmc_search.txt", "r")
                icount = 0
                for line in f.readlines(): 
                    sline = line
                    icount = icount+1
                    if icount > 0:
                           break

                name = sline.replace(" ", "+")
                url1 = "http://xhamster.com/search.php?q=" + name + "&qcat=video" 
                pages = [1, 2, 3, 4, 5, 6]
                for page in pages:
                        url = url1 + "&page=" + str(page)
                        pass#print"Here in getVideos2 url =", url
                        name = "Page " + str(page)
                        pic = " "
                        addDirectoryItem(name, {"name":name, "url":url, "mode":6, "site":site}, pic)
                xbmcplugin.endOfDirectory(thisPlugin)


        		
def getVideos3(name, url):
    if site == str(1):      
        pass#print"Here in getVideos3 url =", url
        content = getUrl(url)
	pass#print"content B2 =", content

 	
	regexvideo = "><div class='video'><a href='(.*?)'.*?alt=(.*?)/>"
	match = re.compile(regexvideo,re.DOTALL).findall(content)
        pass#print"match =", match
        for url, name in match:
                 name = name.replace('"', '')
                 pic = " " 
	         addDirectoryItem(name, {"name":name, "url":url, "mode":4, "site":site}, pic)

        xbmcplugin.endOfDirectory(thisPlugin)	

        
def getVideos4X(name1, urlmain):
        n1 = urlmain.find(".html",0)
        if (n1 < 0):
                return
        n2 = urlmain.rfind("-", 0, n1)
        if (n2 < 0):
                return
        pn = "4"
        url1 = urlmain[:(n2+1)]
        url2 = urlmain[n1:]
        pass#print"Here in getVideos2 url1 =", url1
        pass#print"Here in getVideos2 url2 =", url2
        url = url1 + pn + url2
        pass#print"Here in getVideos2 url =", url
        content = getUrl(url)
	pass#print"content B2 =", content
        pos0 = content.find("Promoted Videos", 0)
        if (pos0 < 0):
                return
	pos1 = content.find("<div class='video'", pos0)
        if (pos1 < 0):
                return
        content = content[pos1:]
	
	regexvideo = "><a href='(.*?)'.*?alt=(.*?)/>"
	match = re.compile(regexvideo,re.DOTALL).findall(content)
        pass#print"match =", match
        for url, name in match:
                 name = name.replace('"', '')
                 pic = " " 
	         addDirectoryItem(name, {"name":name, "url":url, "mode":3}, pic)
	name = "More videos"
	addDirectoryItem(name, {"name":name, "url":urlmain, "mode":7}, pic)
        xbmcplugin.endOfDirectory(thisPlugin)	

def getVideos5X(name1, urlmain):
        n1 = urlmain.find(".html",0)
        if (n1 < 0):
                return
        n2 = urlmain.rfind("-", 0, n1)
        if (n2 < 0):
                return
        pn = "5"
        url1 = urlmain[:(n2+1)]
        url2 = urlmain[n1:]
        pass#print"Here in getVideos2 url1 =", url1
        pass#print"Here in getVideos2 url2 =", url2
        url = url1 + pn + url2
        pass#print"Here in getVideos2 url =", url
        content = getUrl(url)
	pass#print"content B2 =", content
        pos0 = content.find("Promoted Videos", 0)
        if (pos0 < 0):
                return
	pos1 = content.find("<div class='video'", pos0)
        if (pos1 < 0):
                return
        content = content[pos1:]
	
	regexvideo = "><a href='(.*?)'.*?alt=(.*?)/>"
	match = re.compile(regexvideo,re.DOTALL).findall(content)
        pass#print"match =", match
        for url, name in match:
                 name = name.replace('"', '')
                 pic = " " 
	         addDirectoryItem(name, {"name":name, "url":url, "mode":3}, pic)
        xbmcplugin.endOfDirectory(thisPlugin)	

                
def playVideo(name, url, site):
    if site == str(1):      
           pass#print"Here in playVideo url =", url
           fpage = getUrl(url)
	   pass#print"fpage C =", fpage
           start = 0
           pos1 = fpage.find(".flv", start)
           if (pos1 < 0):
                           return
  	   pos2 = fpage.find("a href", pos1)
 	   if (pos2 < 0):
                           return
           pos3 = fpage.find('"', (pos2+10))
 	   if (pos3 < 0):
                           return                
           url = fpage[(pos2+8):pos3]
           playVideo2(name, url)
    if site == str(2):      
           ##pass#print"Here in playVideo url =", url
           fpage = getUrl(url)
	   ##pass#print"fpage C =", fpage
           start = 0
           pos1 = fpage.find("source src", start)
           if (pos1 < 0):
                           return
  	   pos2 = fpage.find("http", pos1)
 	   if (pos2 < 0):
                           return
           pos3 = fpage.find('"', (pos2+5))
 	   if (pos3 < 0):
                           return                
           url = fpage[(pos2):(pos3)]
           playVideo2(name, url)
           

def playVideo2(name, url):                    
           pic = "DefaultFolder.png"
           pass#print"Here in playVideo url B=", url
           li = xbmcgui.ListItem(name,iconImage="DefaultFolder.png", thumbnailImage=pic)
           player = xbmc.Player()
           player.play(url, li)

std_headers = {
	'User-Agent': 'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.6) Gecko/20100627 Firefox/3.6.6',
	'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.7',
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	'Accept-Language': 'en-us,en;q=0.5',
}  

def addDirectoryItem(name, parameters={},pic=""):
    li = xbmcgui.ListItem(name,iconImage="DefaultFolder.png", thumbnailImage=pic)
    url = sys.argv[0] + '?' + urllib.urlencode(parameters)
    return xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=url, listitem=li, isFolder=True)


def parameters_string_to_dict(parameters):
    ''' Convert parameters encoded in a URL to a dict. '''
    paramDict = {}
    if parameters:
        paramPairs = parameters[1:].split("&")
        for paramsPair in paramPairs:
            paramSplits = paramsPair.split('=')
            if (len(paramSplits)) == 2:
                paramDict[paramSplits[0]] = paramSplits[1]
    return paramDict

params = parameters_string_to_dict(sys.argv[2])
name =  str(params.get("name", ""))
url =  str(params.get("url", ""))
url = urllib.unquote(url)
mode =  str(params.get("mode", ""))
site =  str(params.get("site", ""))
pass#print"Here in default-py site =", site
pass#print"Here in default-py mode =", mode
if not sys.argv[2]:
#	ok = showContent()
        ok = listSites()
else:
	if mode == str(1):
	        pass#print"Here in default-py mode B=", mode
		ok = showContent(name, url, site)

	elif mode == str(2):
                pass#print"Here in default-py mode C=", mode
		ok = getPage(name, url, site)
        elif mode == str(3):
		ok = getVideos(name, url, site)        	
	elif mode == str(4):
		ok = playVideo(name, url, site)	
	elif mode == str(5):
		ok = getVideos2(name, url, site)	
	elif mode == str(6):
		ok = getVideos3(name, url)



