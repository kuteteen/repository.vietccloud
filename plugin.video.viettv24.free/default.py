#!/usr/bin/python
#coding=utf-8
import xbmc , xbmcaddon , xbmcplugin , xbmcgui , sys , urllib , urllib2 , re , os , base64 , json , shutil , zipfile
from random import randint
from itertools import imap
from math import radians , sqrt , sin , cos , atan2
from operator import itemgetter 
import xmltodict
if 64 - 64: i11iIiiIii
OO0o = 'plugin.video.viettv24.free'
Oo0Ooo = xbmcaddon . Addon ( OO0o )
Oo0Ooooo = Oo0Ooo . getLocalizedString
O0O0OO0O0O0 = xbmc . translatePath ( Oo0Ooo . getAddonInfo ( 'profile' ) )
i1I11i = xbmc . translatePath ( xbmcaddon . Addon ( ) . getAddonInfo ( 'path' ) ) . decode ( "utf-8" )
i1I11i = xbmc . translatePath ( os . path . join ( i1I11i , "temp.jpg" ) )
O0O0OO0O0 = Oo0Ooo . getAddonInfo ( 'path' )
O0O0OO0O = xbmc . translatePath ( os . path . join ( O0O0OO0O0 , 'resources' , 'thumbs' ) )
O0o0OO0 = xbmc . translatePath ( os . path . join ( O0O0OO0O0 , 'resources' , 'data' , '12345678901.txt' ) )
i1I11iiiI = Oo0Ooo . getSetting ( 'local' )
i1I11ii = Oo0Ooo . getSetting ( 'online' )
iiiii = int ( sys . argv [ 1 ] )
if 64 - 64: iIIi1iI1II111 + ii11i / oOooOoO0Oo0O 
def iI1 ( ) :
 iI111iI ( Oo0Ooooo ( 30001 ) . encode ( 'utf-8' ) , O0O0OO0O0 + Oo0Ooooo ( 30002 ) . encode ( 'utf-8' ) , 'indexgroup' , i1I11i . replace ( "temp.jpg" , "icon.png" ) )
 iI111iI ( Oo0Ooooo ( 30003 ) . encode ( 'utf-8' ) , i1I11iiiI , 'indexgroup' , O0O0OO0O + '/' + Oo0Ooooo ( 30004 ) . encode ( 'utf-8' ) )
 iI111iI ( Oo0Ooooo ( 30005 ) . encode ( 'utf-8' ) , i1I11ii , 'indexgroup' , O0O0OO0O + '/' + Oo0Ooooo ( 30006 ) . encode ( 'utf-8' ) )
 if i11Ii1 ( ) == 'windows' or i11Ii1 ( ) == 'osx' :  
  iI111iI ( Oo0Ooooo ( 30007 ) . encode ( 'utf-8' ) , 'o0oOo0o' , None , O0O0OO0O + '/' + Oo0Ooooo ( 30008 ) . encode ( 'utf-8' ) )
 if i11Ii1 ( ) == 'android' :
  iI111iI ( Oo0Ooooo ( 30014 ) . encode ( 'utf-8' ) , 'o00Oo0o00' , 'redirect' , O0O0OO0O + '/' + Oo0Ooooo ( 30015 ) . encode ( 'utf-8' ) )
  iI111iI ( Oo0Ooooo ( 30016 ) . encode ( 'utf-8' ) , 'o00O0o00' , 'red1rect' , O0O0OO0O + '/' + Oo0Ooooo ( 30017 ) . encode ( 'utf-8' ) )  
 Oo = I1ii11iIi11i ( O0o0OO0 )
 if "xml" in Oo :
  o0OOO = Oo
  for iIiiiI , Iii1ii1II11i in eval ( o0OOO ) :
   Iii1ii1II11i = xbmc . translatePath ( os . path . join ( O0O0OO0O0 , 'resources' , 'data' , Iii1ii1II11i ) )
   i1I11i11 = i1I11i . replace ( "temp.jpg" , "icon.png" )   
   if iIiiiI == Oo0Ooooo ( 30009 ) . encode ( 'utf-8' ) :
    iI111iI ( iIiiiI , Iii1ii1II11i , 'indexgroup' , O0O0OO0O + '/' + Oo0Ooooo ( 30010 ) . encode ( 'utf-8' ) )
   elif iIiiiI == Oo0Ooooo ( 30011 ) . encode ( 'utf-8' ) :	
    iI111iI ( iIiiiI , Iii1ii1II11i , 'indexgroup' , O0O0OO0O + '/' + Oo0Ooooo ( 30012 ) . encode ( 'utf-8' ) )   
   else :
    try :
     if Oo0Ooooo ( 30013 ) . encode ( 'utf-8' ) in iIiiiI : 
      Iii1ii1II11i = ( 'http:' + Iii1ii1II11i . split ( ":" ) [ -1 ] ) % i1II11i ( )
    except : pass      
    iI111iI ( iIiiiI , Iii1ii1II11i , 'indexgroup' , i1I11i11 ) 
  IiII = xbmc . getSkinDir ( )
  if IiII == 'skin.xeebo' :
   xbmc . executebuiltin ( 'Container.SetViewMode(50)' )
 else :
  iI1Ii11111iIi = xbmcgui . Dialog ( )
  iI1Ii11111iIi . ok ( "ID : %s" % O0O , Oo )
 if 41 - 41: I1II1 
def Ooo0OO0oOO ( url ) : 
 if url == None :
  Oo0Ooo . openSettings ( )
  sys . exit ( )
 elif url == i1I11iiiI or url == i1I11ii :
  oooO0oo0oOOOO = I1ii11iIi1 ( url )  
 else :
  oooO0oo0oOOOO = I1ii11iIi11i ( url )
 O0oO = re . compile ( '<name>(.*?)</name>' ) . findall ( oooO0oo0oOOOO )
 if len ( O0oO ) <= 1 :
  o0oO0 = re . compile ( '<item>(.+?)</item>' ) . findall ( oooO0oo0oOOOO )
  for oo00 in o0oO0 :
   o00 = ""
   Oo0oO0ooo = ""
   o0oOoO00o = ""
   if "/title" in oo00 :
    Oo0oO0ooo = re . compile ( '<title>(.+?)</title>' ) . findall ( oo00 ) [ 0 ]
   if "/link" in oo00 :
    o0oOoO00o = re . compile ( '<link>(.+?)</link>' ) . findall ( oo00 ) [ 0 ]
   if "/thumbnail" in oo00 :
    o00 = re . compile ( '<thumbnail>(.*?)</thumbnail>' ) . findall ( oo00 ) [ 0 ]
    if o00 == 'tvchina.png' :
     o00 = O0O0OO0O + '/' + 'tvchina.png'	
   i1 ( Oo0oO0ooo , o0oOoO00o , 'play' , o00 )   
  IiII = xbmc . getSkinDir ( )
  if IiII == 'skin.xeebo' :
   xbmc . executebuiltin ( 'Container.SetViewMode(52)' )
 else :
  for oOOoo00O0O in O0oO :
   if oOOoo00O0O.startswith('TV') :
    iI111iI ( oOOoo00O0O , url + "&n=" + oOOoo00O0O , 'index' , O0O0OO0O + '/' + 'tvvn.png' )
   else :
    iI111iI ( oOOoo00O0O , url + "&n=" + oOOoo00O0O , 'index' , '' )   
   if 15 - 15: I11iii11IIi
def O00o0o0000o0o ( url ) :
 O0Oo = url . split ( "&n=" ) [ 1 ]
 url = url . split ( "&n=" ) [ 0 ]
 if url == i1I11iiiI or url == i1I11ii :
  oooO0oo0oOOOO = I1ii11iIi1 ( url )
 else : 
  oooO0oo0oOOOO = I1ii11iIi11i ( url )  
 oo = re . compile ( '<channel>(.+?)</channel>' ) . findall ( oooO0oo0oOOOO )
 for IiII1I1i1i1ii in oo :
  if O0Oo in IiII1I1i1i1ii :
   o0oO0 = re . compile ( '<item>(.+?)</item>' ) . findall ( IiII1I1i1i1ii )
   for oo00 in o0oO0 :
    o00 = ""
    Oo0oO0ooo = ""
    o0oOoO00o = ""
    if "/title" in oo00 :
     Oo0oO0ooo = re . compile ( '<title>(.+?)</title>' ) . findall ( oo00 ) [ 0 ]
    if "/link" in oo00 :
     o0oOoO00o = re . compile ( '<link>(.+?)</link>' ) . findall ( oo00 ) [ 0 ] 
    if "/thumbnail" in oo00 :
     o00 = re . compile ( '<thumbnail>(.*?)</thumbnail>' ) . findall ( oo00 ) [ 0 ]
     if o00 == 'tvvn.png' :
      o00 = O0O0OO0O + '/' + 'tvvn.png'  
    i1 ( Oo0oO0ooo , o0oOoO00o , 'play' , o00 )
 IiII = xbmc . getSkinDir ( )
 if IiII == 'skin.xeebo' :
  xbmc . executebuiltin ( 'Container.SetViewMode(52)' )
  if 44 - 44: OOo0o0 / OOoOoo00oo - iI1OoOooOOOO + i1iiIII111ii + i1iIIi1  
def i1II11i ( ) :
 return ':' . join ( [ '%02x' %x for x in imap ( lambda x : randint ( 0 , 255 ) , range ( 6 ) ) ] )  
def I1IiI ( k , e ) :
 ii11iIi1I = [ ]
 e = base64 . urlsafe_b64decode ( e )
 for iI111I11I1I1 in range ( len ( e ) ) :
  OOooO0OOoo = k [ iI111I11I1I1 % len ( k ) ]
  iIii1 = chr ( ( 256 + ord ( e [ iI111I11I1I1 ] ) - ord ( OOooO0OOoo ) ) % 256 )
  ii11iIi1I . append ( iIii1 )
 return "" . join ( ii11iIi1I )
 if 71 - 71: IiI1I1 
def OoO000 ( source , dest_dir ) :
 with zipfile . ZipFile ( source ) as IIiiIiI1 :
  for iiIiIIi in IIiiIiI1 . infolist ( ) :
   ooOoo0O = iiIiIIi . filename . split ( '/' )
   i1I11i = dest_dir
   for OooO0 in ooOoo0O [ : - 1 ] :
    II11iiii1Ii , OooO0 = os . path . splitdrive ( OooO0 )
    OO0oOoo , OooO0 = os . path . split ( OooO0 )
    if OooO0 in ( os . curdir , os . pardir , '' ) : continue
    i1I11i = os . path . join ( i1I11i , OooO0 )
   IIiiIiI1 . extract ( iiIiIIi , i1I11i )
   if 68 - 68: oOo00Oo00O + I11i1I + o0o0OOO0o0 % IIII % o0O0 . o0
def I11II1i ( url ) :
 i1I11i = xbmc . translatePath ( xbmcaddon . Addon ( ) . getAddonInfo ( 'path' ) ) . decode ( "utf-8" )
 IIIII = xbmc . translatePath ( os . path . join ( i1I11i , "tmp" ) )
 if os . path . exists ( IIIII ) :
  shutil . rmtree ( IIIII )
 os . makedirs ( IIIII )
 if ".zip" in url :
  ooooooO0oo = xbmc . translatePath ( os . path . join ( IIIII , "temp.zip" ) )
  urllib . urlretrieve ( url , ooooooO0oo )
  OoO000 ( ooooooO0oo , IIIII )
 else :
  IIiiiiiiIi1I1 = xbmc . translatePath ( os . path . join ( IIIII , "temp.jpg" ) )
  urllib . urlretrieve ( url , IIiiiiiiIi1I1 )
 xbmc . executebuiltin ( "SlideShow(%s,recursive)" % IIIII )
 if 13 - 13: OOoo0O0 + Ii + OOo0o0 - ii11i * oOo00Oo00O % IIII
def II11iII ( url , title ) :
 if ( "youtube" in url ) :
  OoOo = re . compile ( '(youtu\.be\/|youtube-nocookie\.com\/|youtube\.com\/(watch\?(.*&)?v=|(embed|v|user)\/))([^\?&"\'>]+)' ) . findall ( url )
  iI = OoOo [ 0 ] [ len ( OoOo [ 0 ] ) - 1 ] . replace ( 'v/' , '' )
  url = "plugin://plugin.video.youtube/play/?video_id=%s" % iI
  xbmc . executebuiltin ( "xbmc.PlayMedia(" + url + ")" )
 else :
  if url . isdigit ( ) or url . isalpha ( ) or url . isalnum ( ) :
   o00O = "http://www.viettv24.com/main/getStreamingServer.php"
   I1IiI = urllib . urlencode ( { 'strname' : '%s-' % url } )
   url = urllib2 . urlopen ( o00O , data = I1IiI ) . read ( )
  title = urllib . unquote_plus ( title )
  OOO0OOO00oo = xbmc . PlayList ( 1 )
  OOO0OOO00oo . clear ( )
  Iii111II = xbmcgui . ListItem ( title , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
  Iii111II . setInfo ( 'video' , { 'Title' : title } )
  iiii11I = xbmc . Player ( )
  OOO0OOO00oo . add ( url , Iii111II )
  iiii11I . play ( OOO0OOO00oo )
  if 96 - 96: I11iii11IIi % IIII . I11i1I + oOooOoO0Oo0O * oOo00Oo00O - i1iiIII111ii 
def I1ii11iIi1 ( url ) :
 o0oOoO00o = ""
 if os . path . exists ( url ) :
  o0oOoO00o = open ( url ) . read ( )
 else :
  oO0OOoO0 = urllib2 . Request ( url )
  oO0OOoO0 . add_header ( 'User-Agent' , 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; WOW64; Trident/6.0)' )
  I111Ii111 = urllib2 . urlopen ( oO0OOoO0 ) 
  o0oOoO00o = I111Ii111 . read ( )
  I111Ii111 . close ( )
  if 5 - 5: oOo00Oo00O
 o0oOoO00o = '' . join ( o0oOoO00o . splitlines ( ) ) . replace ( '\'' , '"' )
 o0oOoO00o = o0oOoO00o . replace ( '\n' , '' )
 o0oOoO00o = o0oOoO00o . replace ( '\t' , '' )
 o0oOoO00o = re . sub ( '  +' , ' ' , o0oOoO00o )
 o0oOoO00o = o0oOoO00o . replace ( '> <' , '><' )
 return o0oOoO00o  
def I1ii11iIi11i ( url ) :
 o0oOoO00o = ""
 if os . path . exists ( url ) == True :
  o0oOoO00o = open ( url ) . read ( )
 else :
  oO0OOoO0 = urllib2 . Request ( url )
  oO0OOoO0 . add_header ( 'User-Agent' , 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; WOW64; Trident/6.0)' )
  I111Ii111 = urllib2 . urlopen ( oO0OOoO0 ) 
  o0oOoO00o = I111Ii111 . read ( )
  I111Ii111 . close ( )
  if 4 - 4: oOo00Oo00O
 if ( "xml" in url ) or ( "txt" in url ):
  o0oOoO00o = I1IiI ( "umbala" , o0oOoO00o )
 o0oOoO00o = '' . join ( o0oOoO00o . splitlines ( ) ) . replace ( '\'' , '"' )
 o0oOoO00o = o0oOoO00o . replace ( '\n' , '' )
 o0oOoO00o = o0oOoO00o . replace ( '\t' , '' )
 o0oOoO00o = re . sub ( '  +' , ' ' , o0oOoO00o )
 o0oOoO00o = o0oOoO00o . replace ( '> <' , '><' )
 return o0oOoO00o
 if 93 - 93: iI1OoOooOOOO % oOo00Oo00O . iI1OoOooOOOO * OOoo0O0 % IIII . I11iii11IIi
def iIi ( ) :
 xbmc . executebuiltin ( 'StartAndroidActivity ( com.viettv24.iptv )' )
 sys . exit ( )
 if 34 - 34: I11iii11IIi - I11i1I - i11iIiiIii % i1iiIII111ii - I11iii11IIi * IIII  
def i1i ( ) :
 xbmc . executebuiltin ( 'StartAndroidActivity ( com.vietuu.hlsplayer )' )
 sys . exit ( )
 if 35 - 35: I11iii11IIi - I11i1I - i11iIiiIii % i1iiIII111ii - I11iii11IIi * IIII 
def i1 ( name , url , mode , iconimage ) :
 iI1ii1Ii = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage )
 oooo000 = xbmcgui . ListItem ( name , iconImage = "DefaultVideo.png" , thumbnailImage = iconimage )
 oooo000 . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 if ( "youtube.com/user/" in url ) or ( "youtube.com/channel/" in url ) :
  iI1ii1Ii = "plugin://plugin.video.youtube/%s/%s/" % ( url . split ( "/" ) [ - 2 ] , url . split ( "/" ) [ - 1 ] )
  return xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = iI1ii1Ii , listitem = oooo000 , isFolder = True ) 
 return xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = iI1ii1Ii , listitem = oooo000 )
 if 16 - 16: IiI1I1 + iI1OoOooOOOO - I11iii11IIi
def iI111iI ( name , url , mode , iconimage ) :
 iI1ii1Ii = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage )
 oOoOO0 = True
 oooo000 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 oooo000 . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 if 'o0oOo0o' in url :
  iI1ii1Ii = 'plugin://plugin.program.chrome.launcher/?kiosk=no&mode=showSite&stopPlayback=no&url=http%3A%2F%2Fwww.viettv24.com%2Fmain%2F%3Flanguage%3Dvi'
 oOoOO0 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = iI1ii1Ii , listitem = oooo000 , isFolder = True )
 return oOoOO0
 if 30 - 30: I11iii11IIi - I11i1I - i11iIiiIii % i1iiIII111ii - I11iii11IIi * IIII
def oO00O0O0O ( parameters ) :
 i1ii1iiI = { }
 if 98 - 98: o0O0 * o0O0 / o0O0 + o0o0OOO0o0
 if parameters :
  ii111111I1iII = parameters [ 1 : ] . split ( "&" )
  for O00ooo0O0 in ii111111I1iII :
   i1iIi1iIi1i = O00ooo0O0 . split ( '=' )
   if ( len ( i1iIi1iIi1i ) ) == 2 :
    i1ii1iiI [ i1iIi1iIi1i [ 0 ] ] = i1iIi1iIi1i [ 1 ]
 return i1ii1iiI
 if 46 - 46: OOoo0O0 % o0o0OOO0o0 + iI1OoOooOOOO . i1iiIII111ii . iI1OoOooOOOO
def i11Ii1 ( ) :
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
I1Ii = oO00O0O0O ( sys . argv [ 2 ] )
O0oo00o0O = I1Ii . get ( 'mode' )
i1I1I = I1Ii . get ( 'url' )
oOOoo00O0O = I1Ii . get ( 'name' )
i111iI1I = I1Ii . get ( 'iconimage' )
if type ( i111iI1I ) == type ( str ( ) ) :
 iconimage = urllib . unquote_plus ( i111iI1I ) 
if type ( i1I1I ) == type ( str ( ) ) :
 i1I1I = urllib . unquote_plus ( i1I1I )
if type ( oOOoo00O0O ) == type ( str ( ) ) :
 oOOoo00O0O = urllib . unquote_plus ( oOOoo00O0O )
 if 12 - 12: i11iIiiIii / iI1OoOooOOOO
o0O = str ( sys . argv [ 1 ] )
if O0oo00o0O == 'index' :
 O00o0o0000o0o ( i1I1I )
elif O0oo00o0O == 'indexgroup' :
 Ooo0OO0oOO ( i1I1I )
elif O0oo00o0O == 'redirect' :
 iIi ( )
elif O0oo00o0O == 'red1rect' :
 i1i ( ) 
elif O0oo00o0O == 'play' :
 if any ( x in i1I1I for x in [ ".jpg" , ".zip" ] ) :
  I11II1i ( i1I1I )
 else :
  IiIIii1iII1II = xbmcgui . DialogProgress ( )
  IiIIii1iII1II . create ( 'Brought to you by VietTV24.com' , 'Loading video. Please wait...' )
  II11iII ( i1I1I , oOOoo00O0O )
  IiIIii1iII1II . close ( )
  del IiIIii1iII1II
else :
 iI1 ( )
xbmcplugin . endOfDirectory ( int ( o0O ) )