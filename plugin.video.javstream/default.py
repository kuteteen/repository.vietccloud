import urllib2, re, urllib, base64, difflib, time, json, base64, HTMLParser, time, sys, cookielib, os.path
import xbmcaddon,xbmcplugin,xbmcgui
import jsunpack
import util, sexloading, ivhunter

USER_AGENT = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'

hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

headers = {'User-Agent': USER_AGENT,
           'Accept': '*/*',
           'Connection': 'keep-alive'}
           
sysarg=str(sys.argv[1])
ADDON_ID='plugin.video.javstream'
addon = xbmcaddon.Addon(id=ADDON_ID)

rootDir = addon.getAddonInfo('path')
if rootDir[-1] == ';':
    rootDir = rootDir[0:-1]
rootDir = xbmc.translatePath(rootDir)
resDir = os.path.join(rootDir, 'resources')
imgDir = os.path.join(resDir, 'images')

profileDir = addon.getAddonInfo('profile')
profileDir = xbmc.translatePath(profileDir).decode("utf-8")
cookiePath = os.path.join(profileDir, 'cookies.lwp')

if not os.path.exists(profileDir):
    os.makedirs(profileDir)

urlopen = urllib2.urlopen
cj = cookielib.LWPCookieJar()
Request = urllib2.Request

if cj != None:
    if os.path.isfile(xbmc.translatePath(cookiePath)):
        cj.load(xbmc.translatePath(cookiePath))
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
else:
    opener = urllib2.build_opener()

urllib2.install_opener(opener)

"""urlopen = urllib2.urlopen
cj = cookielib.LWPCookieJar()
Request = urllib2.Request
rootDir = addon.getAddonInfo('path')
if rootDir[-1] == ';':
    rootDir = rootDir[0:-1]
profileDir = addon.getAddonInfo('profile')
profileDir = xbmc.translatePath(profileDir).decode("utf-8")
cookiePath = os.path.join(profileDir, 'cookies.lwp')
if not os.path.exists(profileDir):
    os.makedirs(profileDir)
sysarg=str(sys.argv[1]) 

if cj != None:
    if os.path.isfile(xbmc.translatePath(cookiePath)):
        cj.load(xbmc.translatePath(cookiePath))
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
else:
    opener = urllib2.build_opener()

urllib2.install_opener(opener)"""
    
def getVids(urls) :
    for url in urls:
        if "sexloading" in url:
            param=sexloading.showVideos(url, hdr)
        elif "ivhunter" in url:
            param=ivhunter.showVideos(url, hdr)
        buildVideoMenu(param)
    xbmcplugin.endOfDirectory(int(sysarg))
   
def buildVideoMenu(param):
    loadNext=[]
    for video in param:
        if video[0]=='next':
            loadNext.append(video[1])
        else:
            u=sys.argv[0]+"?url="+video[5]+"&play="+str(4)+"&name="+urllib.quote_plus(util.makeAscii(video[0]))+"&poster="+video[6]
            liz=xbmcgui.ListItem(util.makeAscii(video[0]), iconImage="DefaultVideo.png", thumbnailImage=video[6])
            liz.setInfo( type="Video", infoLabels={ "Title": util.makeAscii(video[0]),"Plot": video[1]} )
            liz.setProperty("Fanart_Image", video[7])
            liz.setProperty("Landscape_Image", video[7])
            liz.setProperty("Poster_Image", video[6])
            ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
    
    if len(loadNext)>0:
        if len(loadNext)==1:
            util.addDir("Next Page >", loadNext[0], 1, "")
        else:
            util.addDir("Next Page >", "<split>".join(loadNext), 4, "")            
        
def buildMainMenu():
    util.addDir("JAV","JAV", 2, "")
    util.addDir("Gravure", "Gravure", 2, "")
    util.addDir("Latest JAV", "http://sexloading.com/", 1, "")
    util.addDir("Latest Gravure", "http://ivhunter.com", 1, "")
    util.addDir("Search","http://sexloading.com/?s=<split>http://ivhunter.com/?s=", 3, "")
    xbmcplugin.endOfDirectory(int(sysarg))

def buildSubMenu(params):
    if params['url']=='JAV':
        util.addDir("Genres", "http://sexloading.com/faq/", 5, "")
        util.addDir("Censored", "http://sexloading.com/censored/", 1, "")
        util.addDir("Uncensored", "http://sexloading.com/uncensored/", 1, "")
        util.addDir("Most Popular JAV", "http://sexloading.com/", 6, "")
        util.addDir("Latest JAV", "http://sexloading.com/", 1, "")
        util.addDir("Search", "http://sexloading.com/?s=", 3, "")
    elif params['url']=="Gravure":
        util.addDir("Studios", "http://ivhunter.com/note/", 7, "")
        util.addDir("Idols", "http://ivhunter.com/idols-library/", 8, "")
        util.addDir("Most Popular Gravure", "http://ivhunter.com/", 9, "")
        util.addDir("Latest Gravure", "http://ivhunter.com", 1, "")
        util.addDir("Search", "http://ivhunter.com/?s=", 3, "")
    xbmcplugin.endOfDirectory(int(sysarg))
        
def search(urls):
    toSend=[]
    term=util.searchBox()
    for url in urls:
        xbmc.log(url+term, xbmc.LOGERROR)
        toSend.append(url+term)
    getVids(toSend)

def resolve(url):
    html=util.getURL(url, hdr)
    try:
        O = {
            '___': 0,
            '$$$$': "f",
            '__$': 1,
            '$_$_': "a",
            '_$_': 2,
            '$_$$': "b",
            '$$_$': "d",
            '_$$': 3,
            '$$$_': "e",
            '$__': 4,
            '$_$': 5,
            '$$__': "c",
            '$$_': 6,
            '$$$': 7,
            '$___': 8,
            '$__$': 9,
            '$_': "constructor",
            '$$': "return",
            '_$': "o",
            '_': "u",
            '__': "t",
        }
        result = re.search('<video.*?<script[^>]*>(.*?)</script>.*?</video>', html, re.DOTALL).group(1)
        result = result.replace(' ','')
        
        decodetest = re.search(r"decodeURIComponent\('([^']+)'\)", result, re.DOTALL).group(1)
        decoderesult = "'" + urllib2.unquote(decodetest).decode('utf8') + "'"
        
        result = re.sub(r"(?si)decodeURIComponent\('[^']+'\)", decoderesult, result)
        result = jsunpack.unpack(result)
        result = re.search('O\.\$\(O\.\$\((.*?)\)\(\)\)\(\);', result, re.DOTALL | re.IGNORECASE)
        
        s1 = result.group(1)

        s1 = s1.replace('\'+\'', '')
        s1 = s1.replace(' ', '')
        s1 = s1.replace('\n', '')
        s1 = s1.replace('\r', '')
        s1 = s1.replace('\t', '')
        s1 = s1.replace('(![]+"")', 'false')
        s1 = s1.replace('\\\\', '\\')
        s3 = ''
        for s2 in s1.split('+'):
            if s2.startswith('o.'):
                s3 += str(O[s2[2:]])
            elif '[' in s2 and ']' in s2:
                key = s2[s2.find('[') + 3:-1]
                s3 += s2[O[key]]
            else:
                s3 += s2[1:-1]

        s3 = s3.replace('\\\\', '\\')
        s3 = s3.decode('unicode_escape')
        s3 = s3.replace('\\/', '/')
        s3 = s3.replace('\\\\"', '"')
        s3 = s3.replace('\\"', '"')
        url = re.search('<source.*?src="([^"]+)', s3).group(1)
        return url
    except:
        return "error"
    
def playVideo(params):
    content=util.getURL(params['url'].encode('utf-8'), hdr)
    if content!=False:
        
        """if "https://openload" in content:
            xbmc.log("openload", xbmc.LOGERROR)
            download=util.extract(content, '<iframe src="https://openload', '"')
            openloadurl ='http://openload'+download.encode('utf-8')
            videourl=resolve(openloadurl)
            ol=util.getURL(openloadurl, hdr)
            videourl=util.extract(ol, '<source type="video/mp4" src="', '"')  """
            
        if 'videourl' not in locals() and "http://videowood.tv/embed/" in content:
            xbmc.log("videowood", xbmc.LOGERROR)
            download=util.extract(content, 'http://videowood.tv/embed/', '"')
            videowoodurl='http://videowood.tv/embed/'+download
            vw=util.getURL(videowoodurl, hdr)
            #xbmc.log(vw, xbmc.LOGERROR)
            videourls=util.extractAll(vw, "file: '", "',")
            for vid in videourls:
                if '.mp4' in vid:
                    videourl=vid
                    break
            try:
                videourl
            except:
                result="eval("+util.extract(vw, "eval(", "</script")
                xbmc.log(result, xbmc.LOGERROR)
                result=jsunpack.unpack(result)
                xbmc.log(result, xbmc.LOGERROR)
                
        if 'videourl' not in locals() and "videomega.tv" in content:
            xbmc.log("videomega", xbmc.LOGERROR)
            videosource=content
            if re.search("videomega.tv/iframe.js", videosource, re.DOTALL | re.IGNORECASE):
                hashref = re.compile("""javascript["']>ref=['"]([^'"]+)""", re.DOTALL | re.IGNORECASE).findall(videosource)
            elif re.search("videomega.tv/iframe.php", videosource, re.DOTALL | re.IGNORECASE):
                hashref = re.compile(r"iframe\.php\?ref=([^&]+)&", re.DOTALL | re.IGNORECASE).findall(videosource)
            else:
                hashkey = re.compile("""hashkey=([^"']+)""", re.DOTALL | re.IGNORECASE).findall(videosource)
                if len(hashkey) > 1:
                    i = 1
                    hashlist = []
                    for x in hashkey:
                        hashlist.append('Part ' + str(i))
                        i += 1
                    vmvideo = dialog.select('Multiple parts found', hashlist)
                    hashkey = hashkey[vmvideo]
                else: hashkey = hashkey[0]
                hashpage = getHtml('http://videomega.tv/validatehash.php?hashkey='+hashkey, params['url'].encode('utf-8'))
                hashref = re.compile('ref="([^"]+)', re.DOTALL | re.IGNORECASE).findall(hashpage)
            videopage = getHtml('http://videomega.tv/view.php?ref='+hashref[0], params['url'].encode('utf-8'))
            videourl = re.compile('<source src="([^"]+)"', re.DOTALL | re.IGNORECASE).findall(videopage)
            videourl = videourl[0]
        
        xbmc.log(videourl, xbmc.LOGERROR)
        
        util.playMedia(params['name'], params['poster'],videourl, "Video")

def getHtml(url, referer, hdr=None):
    referer=urllib2.quote(referer).replace("%3A", ":")
    if not hdr:
        req = Request(url, '', headers)
    else:
        req = Request(url, '', hdr)
    if len(referer) > 1:
        req.add_header('Referer', referer)
    response = urlopen(req, timeout=60)
    data = response.read()
    cj.save(cookiePath)
    response.close()
    return data
        
parameters=util.parseParameters()
try:
    mode=int(parameters["mode"])
except:
    mode=None
    
if mode==1:
    getVids([parameters['url'].encode('utf-8')])
elif mode==2:
    buildSubMenu(parameters)
elif mode==3:
    search(parameters['url'].split('<split>'))
elif mode==4:
    getVids(parameters['url'].split('<split>'))
elif mode==5:
    sexloading.getGenres(parameters['url'], hdr)
elif mode==6:
    buildVideoMenu(sexloading.getPopular(parameters['url'], hdr))
    xbmcplugin.endOfDirectory(int(sysarg))
elif mode==7:
    ivhunter.getStudios(parameters['url'], hdr);
elif mode==8:
    ivhunter.getIdols(parameters['url'], hdr);
elif mode==9:
    buildVideoMenu(ivhunter.getPopular(parameters['url'], hdr))
    xbmcplugin.endOfDirectory(int(sysarg))
elif 'play' in parameters:
    playVideo(parameters)
else:
    buildMainMenu()
