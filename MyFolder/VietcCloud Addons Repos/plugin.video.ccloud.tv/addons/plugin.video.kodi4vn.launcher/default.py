#!/usr/bin/python
#coding=utf-8
from xbmcswift2 import Plugin , xbmc , xbmcgui , xbmcaddon
import requests , re , urllib , os , zipfile , json , uuid , shutil , pickle
if 64 - 64: i11iIiiIii
OO0o = Plugin ( )
Oo0Ooo = xbmcaddon . Addon ( "plugin.video.kodi4vn.launcher" )
O0O0OO0O0O0 = "plugin://plugin.video.kodi4vn.launcher"
iiiii = "http://echipstore.com:8000"
if 64 - 64: iIIi1iI1II111 + ii11i / oOooOoO0Oo0O
def iI1 ( url ) :
 i1I11i = requests . get ( url + "%st=%s" % ( "&" if "?" in url else "?" , urllib . quote_plus ( OO0o . get_setting ( "token" ) ) ) )
 i1I11i . encoding = "utf-8"
 OoOoOO00 = i1I11i . json ( )
 return OoOoOO00
 if 27 - 27: OOOo0 / Oo - Ooo00oOo00o . I1IiI
def o0OOO ( url ) :
 OoOoOO00 = iI1 ( url )
 return OoOoOO00
 if 13 - 13: ooOo + Ooo0O
def IiiIII111iI ( source , dest_dir ) :
 with zipfile . ZipFile ( source ) as IiII :
  for iI1Ii11111iIi in IiII . infolist ( ) :
   i1i1II = iI1Ii11111iIi . filename . split ( '/' )
   O0oo0OO0 = dest_dir
   for I1i1iiI1 in i1i1II [ : - 1 ] :
    iiIIIII1i1iI , I1i1iiI1 = os . path . splitdrive ( I1i1iiI1 )
    o0oO0 , I1i1iiI1 = os . path . split ( I1i1iiI1 )
    if I1i1iiI1 in ( os . curdir , os . pardir , '' ) : continue
    O0oo0OO0 = os . path . join ( O0oo0OO0 , I1i1iiI1 )
   IiII . extract ( iI1Ii11111iIi , O0oo0OO0 )
   if 100 - 100: i11Ii11I1Ii1i
@ OO0o . route ( '/warning/<s>' )
def Ooo ( s = "" ) :
 o0oOoO00o = xbmcgui . Dialog ( )
 o0oOoO00o . ok ( 'Chú ý: User %s' % OO0o . get_setting ( "email" ) , s )
 return OO0o . finish ( )
 if 43 - 43: O0OOo . II1Iiii1111i
@ OO0o . route ( '/search/' )
def i1IIi11111i ( ) :
 o000o0o00o0Oo ( "Browse" , '/search' )
 oo = OO0o . keyboard ( heading = 'Tìm kiếm' )
 if oo :
  IiII1I1i1i1ii = '%s/yts/none/video/%s/' % ( O0O0OO0O0O0 , urllib . quote_plus ( oo ) )
  IIIII = OO0o . get_storage ( 'search_history' )
  if 'keywords' in IIIII :
   IIIII [ "keywords" ] = [ oo ] + IIIII [ "keywords" ]
  else :
   IIIII [ "keywords" ] = [ oo ]
  OO0o . redirect ( IiII1I1i1i1ii )
  if 26 - 26: O00OoOoo00 . iiiI11 / oooOOOOO * IiiIII111ii / i1iIIi1
@ OO0o . route ( '/searchlist/' )
def ii11iIi1I ( ) :
 o000o0o00o0Oo ( "Browse" , '/searchlist' )
 OoOoOO00 = [ ]
 iI111I11I1I1 = [ {
 "label" : "[B]Search[/B]" ,
 "path" : "%s/search" % ( O0O0OO0O0O0 ) ,
 "thumbnail" : "https://lh3.googleusercontent.com/jH1IxHp7MbOx62G1aboX2kj1vgtt3kercFVPYTxh7Yr0kMoVZARVNZIYjFZQOY1FzK7DisXyfHo=s256-no"
 } ]
 IIIII = OO0o . get_storage ( 'search_history' )
 if 'keywords' in IIIII :
  for OOooO0OOoo in IIIII [ 'keywords' ] :
   iIii1 = [ {
 "label" : OOooO0OOoo ,
 "path" : '%s/yts/none/video/%s/' % ( O0O0OO0O0O0 , urllib . quote_plus ( OOooO0OOoo ) ) ,
 "thumbnail" : "https://lh3.googleusercontent.com/jH1IxHp7MbOx62G1aboX2kj1vgtt3kercFVPYTxh7Yr0kMoVZARVNZIYjFZQOY1FzK7DisXyfHo=s256-no"
 } ]
   OoOoOO00 += iIii1
 OoOoOO00 = iI111I11I1I1 + OoOoOO00
 return OO0o . finish ( OoOoOO00 )
 if 71 - 71: IiI1I1
@ OO0o . route ( '/login' )
def OoO000 ( ) :
 o000o0o00o0Oo ( "Login" , "/login" )
 xbmc . executebuiltin ( 'Dialog.Close(busydialog)' )
 try :
  IIiiIiI1 = requests . get ( "http://echipstore.com/get-code/?nocache=true" ) . json ( )
  iiIiIIi = IIiiIiI1 [ "message" ] % IIiiIiI1 [ "user_code" ] . upper ( )
  ooOoo0O = xbmcgui . DialogProgress ( )
  ooOoo0O . create ( 'Login' , iiIiIIi )
  if 76 - 76: i1II1I11 / i11iIiiIii / ii11i . O0OOo % OOOo0
  OO0oOoo = 0
  while OO0oOoo < 60 :
   O0o0Oo = int ( ( OO0oOoo / 60.0 ) * 100 )
   if ooOoo0O . iscanceled ( ) :
    break
   ooOoo0O . update ( O0o0Oo , "" )
   OO0oOoo = OO0oOoo + 1
   xbmc . sleep ( 5000 )
   i1I11i = requests . get ( "http://echipstore.com/device?device_code=%s&nocache=true" % urllib . quote_plus ( IIiiIiI1 [ "device_code" ] ) )
   if "token" in i1I11i . text :
    Oo0Ooo . setSetting ( "token" , i1I11i . json ( ) [ "token" ] )
    Oo0Ooo . setSetting ( "email" , i1I11i . json ( ) [ "email" ] )
    break
  ooOoo0O . close ( )
  del ooOoo0O
  xbmc . executebuiltin ( 'XBMC.Container.Update(%s)' % O0O0OO0O0O0 )
 except :
  Oo00OOOOO = xbmcgui . Dialog ( )
  Oo00OOOOO . ok ( "Oops!" , "Có lỗi xảy ra. Xin quý vị vui lòng login vào dịp khác" )
  if 85 - 85: i1II1I11 . IiiIII111ii - ooOo % i1II1I11 % Oo
@ OO0o . route ( '/' )
def OO0o00o ( ) :
 o000o0o00o0Oo ( )
 dir ( "0" )
 if 89 - 89: II1Iiii1111i + I1IiI
@ OO0o . route ( '/ytslive/<order>/' , name = "ytslive_firstpage" )
@ OO0o . route ( '/ytslive/<order>/<page>' )
def Ii1I ( order = "viewcount" , page = "" ) :
 o000o0o00o0Oo ( "Browse YT Live News" , "/ytslive/%s/%s" % ( order , page ) )
 OoOoOO00 = o0OOO ( "%s/ytslive/%s/%s" % ( iiiii , order , page ) )
 for iIii1 in OoOoOO00 :
  iIii1 [ "path" ] = O0O0OO0O0O0 + iIii1 [ "path" ]
 if OO0o . get_setting ( 'thumbview' , bool ) :
  if xbmc . getSkinDir ( ) in ( 'skin.confluence' , 'skin.eminence' ) :
   return OO0o . finish ( OoOoOO00 , view_mode = 500 )
  elif xbmc . getSkinDir ( ) == 'skin.xeebo' :
   return OO0o . finish ( OoOoOO00 , view_mode = 52 )
  else :
   return OO0o . finish ( OoOoOO00 )
 else :
  return OO0o . finish ( OoOoOO00 )
  if 89 - 89: i11iIiiIii / iIIi1iI1II111 * Ooo0O % O00OoOoo00 % II1Iiii1111i
@ OO0o . route ( '/yts/<order>/<t>/<q>/' , name = 'yts_firstpage' )
@ OO0o . route ( '/yts/<order>/<t>/<q>/<page>' )
def Ii1 ( order , t , q = "" , page = "" ) :
 o000o0o00o0Oo ( "Browse YT by topics %s" % q , "/yts/%s/%s/%s/%s" % ( order , t , q , page ) )
 OoOoOO00 = [ ]
 if t in [ "channel" , "playlist" ] and order == "date" :
  order = "videocount"
 OoOoOO00 = o0OOO ( "%s/yts/%s/%s?q=%s&page=%s" % ( iiiii , order , t , q , page ) )
 for iIii1 in OoOoOO00 :
  if "plugin://" not in iIii1 [ "path" ] :
   iIii1 [ "path" ] = O0O0OO0O0O0 + iIii1 [ "path" ]
 if t == "video" :
  III1i1i = [ {
 "label" : "[B]Channels[/B]" ,
 "path" : "%s/yts/%s/channel/%s" % ( O0O0OO0O0O0 , order , q ) ,
 "thumbnail" : "http://thong.viettv24.com/kodi4vn/images/yt.png"
 } ]
  iiI1 = [ {
 "label" : "[B]Playlist[/B]" ,
 "path" : "%s/yts/%s/playlist/%s" % ( O0O0OO0O0O0 , order , q ) ,
 "thumbnail" : "https://lh3.googleusercontent.com/184S-U4BBN7f55qcTQFUQSsBjYlJZ246A01J-n_BKa4bwe74nANMPkj58I8DSPzlxYyWocyYYYj89D-1qHXfEkVENdA6O1weJZOVZAMCAIhK8vfZ9bgKpw-eY4pwpaCzfQ0MS4wlwnjZE28jmTZejHIVRflEUcPS-SLJ6xGTAVIHXbIP1uEKugegwL9ULD0vfwD92FWzz9_abZ70VNeBTBRCjE3-gfQ-IKVUmGJlnJeEJcS1fUAo6_qvrBf9NX1n0gLp24lVdTj-ml6VmDtr5bVwQBBes-7zTKthqeLqZoo-Zr0ZDY2hhw871xrXDeUtlwVeK-EnAEgFRAWyRa9HjijEEED81GDYkCc5r0qK3xjqqPvo3aJ-urdVH2TcOkbmTgx2l7jHIMo4WuE9-d8hAMzGXJfLp4NNGty3vYLk-0RG_MjvUp4qeNcmPMHrX8fWih2z-hAXhfvjXZ1SJq_BEnFzSgVCyW44inHkLUallDmcbFyz5EuYgEAVYHMUikabDj2eLrsMbHTM94a_ljcBV9X4jS0Dz5EMjLl5veXQmCA=w175-h107-no"
 } ]
  OoOoOO00 = III1i1i + iiI1 + OoOoOO00
 if OO0o . get_setting ( 'thumbview' , bool ) :
  if xbmc . getSkinDir ( ) in ( 'skin.confluence' , 'skin.eminence' ) :
   return OO0o . finish ( OoOoOO00 , view_mode = 500 )
  elif xbmc . getSkinDir ( ) == 'skin.xeebo' :
   return OO0o . finish ( OoOoOO00 , view_mode = 52 )
  else :
   return OO0o . finish ( OoOoOO00 )
 else :
  return OO0o . finish ( OoOoOO00 )
  if 19 - 19: iiiI11 + i1II1I11
@ OO0o . route ( '/dir/<url>' )
def dir ( url ) :
 OoOoOO00 = [ ]
 o000o0o00o0Oo ( "Browse Kodi4vn Launcher Menu %s" % url , "/dir/%s" % url )
 try :
  if "://" in url :
   pass
  else :
   OoOoOO00 = o0OOO ( "%s/dir/%s" % ( iiiii , urllib . quote_plus ( url ) ) )
   for iIii1 in OoOoOO00 :
    if "plugin://" not in iIii1 [ "path" ] :
     iIii1 [ "path" ] = O0O0OO0O0O0 + iIii1 [ "path" ]
   ooo = ( "" if OO0o . get_setting ( "email" ) == "" else ( "Chào %s. " % OO0o . get_setting ( "email" ) ) )
   ii1I1i1I = [ {
 "label" : "[COLOR yellow][B]%sVào đây để Login/Relogin[/B][/COLOR]" % ooo ,
 "path" : O0O0OO0O0O0 + "/login" ,
 "thumbnail" : "https://cdn3.iconfinder.com/data/icons/gray-toolbar-2/512/login_user_profile_account-512.png"
 } ]
   OoOoOO00 = OoOoOO00 + ii1I1i1I
 except :
  O0oo0OO0 = xbmc . translatePath ( xbmcaddon . Addon ( ) . getAddonInfo ( 'path' ) ) . decode ( "utf-8" )
  OOoo0O0 = xbmc . translatePath ( os . path . join ( O0oo0OO0 , "error_icon.jpg" ) )
  iiiIi1i1I = xbmc . translatePath ( os . path . join ( O0oo0OO0 , "error_bg.jpg" ) )
  oOO00oOO = xbmc . translatePath ( os . path . join ( O0oo0OO0 , "error_fullscreen.jpg" ) )
  if 75 - 75: OOOo0 / oOooOoO0Oo0O - iIIi1iI1II111 / Ooo0O . Oo - OOOo0
  O000OO0 = [ {
 "label" : "Chưa Internet? Xin xem hướng dẫn đi kèm" ,
 "path" : "%s/showimage/%s" % ( O0O0OO0O0O0 , urllib . quote_plus ( oOO00oOO ) ) ,
 "thumbnail" : OOoo0O0 ,
 "properties" : { 'fanart_image' : iiiIi1i1I }
 } ]
  OoOoOO00 += O000OO0
 return OO0o . finish ( OoOoOO00 )
 if 43 - 43: IiI1I1 - iIIi1iI1II111 % Ooo00oOo00o . iiiI11
@ OO0o . route ( '/ytp/<pid>' , name = 'ytp_firstpage' )
@ OO0o . route ( '/ytp/<pid>/<page>' )
def o00 ( pid , page = "" ) :
 o000o0o00o0Oo ( "Browse YT Videos by PlaylistID %s" % pid , "/ytp/%s/%s" % ( pid , page ) )
 OoOoOO00 = o0OOO ( "%s/ytp/%s/%s" % ( iiiii , pid , page ) )
 for iIii1 in OoOoOO00 :
  iIii1 [ "path" ] = O0O0OO0O0O0 + iIii1 [ "path" ]
 if OO0o . get_setting ( 'thumbview' , bool ) :
  if xbmc . getSkinDir ( ) in ( 'skin.confluence' , 'skin.eminence' ) :
   return OO0o . finish ( OoOoOO00 , view_mode = 500 )
  elif xbmc . getSkinDir ( ) == 'skin.xeebo' :
   return OO0o . finish ( OoOoOO00 , view_mode = 52 )
  else :
   return OO0o . finish ( OoOoOO00 )
 else :
  return OO0o . finish ( OoOoOO00 )
  if 95 - 95: iIIi1iI1II111 + ooOo . Oo / iIIi1iI1II111
@ OO0o . route ( '/ytu/<uid>' )
def O000oo0O ( uid ) :
 OOOO = requests . get ( "%s/ytu/%s" % ( iiiii , uid ) ) . text
 i11i1 ( OOOO , "" )
 if 29 - 29: O0OOo % Ooo00oOo00o + i1II1I11 / i11Ii11I1Ii1i + O00OoOoo00 * i11Ii11I1Ii1i
@ OO0o . route ( '/ytc/<cid>' , name = 'ytc_firstpage' )
@ OO0o . route ( '/ytc/<cid>/<page>' )
def i11i1 ( cid , page = "" ) :
 o000o0o00o0Oo ( "Browse YT Videos by ChannelID %s" % cid , "/ytc/%s/%s" % ( cid , page ) )
 OoOoOO00 = [ {
 "label" : "[B]Playlist[/B]" ,
 "path" : "%s/ytcp/%s/%s" % ( O0O0OO0O0O0 , cid . split ( "@" ) [ 0 ] , "" ) ,
 "thumbnail" : "https://lh3.googleusercontent.com/184S-U4BBN7f55qcTQFUQSsBjYlJZ246A01J-n_BKa4bwe74nANMPkj58I8DSPzlxYyWocyYYYj89D-1qHXfEkVENdA6O1weJZOVZAMCAIhK8vfZ9bgKpw-eY4pwpaCzfQ0MS4wlwnjZE28jmTZejHIVRflEUcPS-SLJ6xGTAVIHXbIP1uEKugegwL9ULD0vfwD92FWzz9_abZ70VNeBTBRCjE3-gfQ-IKVUmGJlnJeEJcS1fUAo6_qvrBf9NX1n0gLp24lVdTj-ml6VmDtr5bVwQBBes-7zTKthqeLqZoo-Zr0ZDY2hhw871xrXDeUtlwVeK-EnAEgFRAWyRa9HjijEEED81GDYkCc5r0qK3xjqqPvo3aJ-urdVH2TcOkbmTgx2l7jHIMo4WuE9-d8hAMzGXJfLp4NNGty3vYLk-0RG_MjvUp4qeNcmPMHrX8fWih2z-hAXhfvjXZ1SJq_BEnFzSgVCyW44inHkLUallDmcbFyz5EuYgEAVYHMUikabDj2eLrsMbHTM94a_ljcBV9X4jS0Dz5EMjLl5veXQmCA=w175-h107-no"
 } ]
 if "@" not in cid :
  cid = requests . get ( "%s/ytc/%s" % ( iiiii , cid ) ) . text
 if "@" in cid :
  III1i1i = o0OOO ( "%s/ytp/%s/%s" % ( iiiii , cid . split ( "@" ) [ 1 ] , page ) )
  for iIii1 in III1i1i :
   iIii1 [ "path" ] = O0O0OO0O0O0 + iIii1 [ "path" ]
  OoOoOO00 += III1i1i
 if OO0o . get_setting ( 'thumbview' , bool ) :
  if xbmc . getSkinDir ( ) in ( 'skin.confluence' , 'skin.eminence' ) :
   return OO0o . finish ( OoOoOO00 , view_mode = 500 )
  elif xbmc . getSkinDir ( ) == 'skin.xeebo' :
   return OO0o . finish ( OoOoOO00 , view_mode = 52 )
  else :
   return OO0o . finish ( OoOoOO00 )
 else :
  return OO0o . finish ( OoOoOO00 )
  if 42 - 42: oooOOOOO + II1Iiii1111i
@ OO0o . route ( '/ytcp/<cid>' , name = 'ytcp_firstpage' )
@ OO0o . route ( '/ytcp/<cid>/<page>' )
def o0O0o0Oo ( cid , page = "" ) :
 o000o0o00o0Oo ( "Browse YT Playlist by ChannelID %s" % cid , "/ytcp/%s/%s" % ( cid , page ) )
 OoOoOO00 = o0OOO ( "%s/ytcp/%s/%s" % ( iiiii , cid , page ) )
 for iIii1 in OoOoOO00 :
  iIii1 [ "path" ] = O0O0OO0O0O0 + iIii1 [ "path" ]
 if OO0o . get_setting ( 'thumbview' , bool ) :
  if xbmc . getSkinDir ( ) in ( 'skin.confluence' , 'skin.eminence' ) :
   return OO0o . finish ( OoOoOO00 , view_mode = 500 )
  elif xbmc . getSkinDir ( ) == 'skin.xeebo' :
   return OO0o . finish ( OoOoOO00 , view_mode = 52 )
  else :
   return OO0o . finish ( OoOoOO00 )
 else :
  return OO0o . finish ( OoOoOO00 )
  if 16 - 16: iIIi1iI1II111 - IiI1I1 * ii11i + IiiIII111ii
@ OO0o . route ( '/play/<url>' )
def Ii11iII1 ( url ) :
 o000o0o00o0Oo ( "Play %s" % url , "/play/%s" % url )
 ooOoo0O = xbmcgui . DialogProgress ( )
 ooOoo0O . create ( 'Kodi4VN Launcher' , 'Loading video. Please wait...' )
 OO0o . set_resolved_url ( Oo0O0O0ooO0O ( url ) )
 ooOoo0O . close ( )
 del ooOoo0O
 if 15 - 15: O0OOo + Ooo0O - oOooOoO0Oo0O / O00OoOoo00
def Oo0O0O0ooO0O ( url ) :
 if "youtube" in url :
  oo000OO00Oo = re . compile ( '(youtu\.be\/|youtube-nocookie\.com\/|youtube\.com\/(watch\?(.*&)?v=|(embed|v|user)\/))([^\?&"\'>]+)' ) . findall ( url )
  O0OOO0OOoO0O = oo000OO00Oo [ 0 ] [ len ( oo000OO00Oo [ 0 ] ) - 1 ] . replace ( 'v/' , '' )
  return 'plugin://plugin.video.youtube/?action=play_video&videoid=%s' % O0OOO0OOoO0O
 elif "://" not in url :
  O00Oo000ooO0 = "http://www.viettv24.com/main/getStreamingServer.php"
  OoO0O00 = { 'strname' : '%s-' % url }
  return requests . post ( O00Oo000ooO0 , data = OoO0O00 ) . text . strip ( )
 else :
  return url
  if 5 - 5: I1IiI / i11Ii11I1Ii1i . oooOOOOO - iIIi1iI1II111 / i1iIIi1
@ OO0o . route ( '/showimage/<url>' )
def ooOooo000oOO ( url ) :
 O0oo0OO0 = xbmc . translatePath ( xbmcaddon . Addon ( ) . getAddonInfo ( 'path' ) ) . decode ( "utf-8" )
 Oo0oOOo = xbmc . translatePath ( os . path . join ( O0oo0OO0 , "tmp" ) )
 if os . path . exists ( Oo0oOOo ) :
  shutil . rmtree ( Oo0oOOo )
 os . makedirs ( Oo0oOOo )
 if ".zip" in url :
  Oo0OoO00oOO0o = xbmc . translatePath ( os . path . join ( Oo0oOOo , "temp.zip" ) )
  urllib . urlretrieve ( url , Oo0OoO00oOO0o )
  IiiIII111iI ( Oo0OoO00oOO0o , Oo0oOOo )
  xbmc . executebuiltin ( "SlideShow(%s,recursive)" % Oo0oOOo )
 else :
  xbmc . executebuiltin ( "ShowPicture(%s)" % url )
 return OO0o . finish ( )
 if 80 - 80: II1Iiii1111i + O00OoOoo00 - O00OoOoo00 % IiiIII111ii
def o000o0o00o0Oo ( title = "Home" , page = "/" ) :
 try :
  OoOO0oo0o = "http://www.google-analytics.com/collect"
  II11i1I11Ii1i = open ( O000O0oOO0 ) . read ( )
  O0ooo0O0oo0 = {
 'v' : '1' ,
 'tid' : 'UA-52209804-5' ,
 'cid' : II11i1I11Ii1i ,
 't' : 'pageview' ,
 'dp' : page ,
 'dt' : title
 }
  requests . post ( OoOO0oo0o , data = urllib . urlencode ( O0ooo0O0oo0 ) )
 except :
  pass
  if 91 - 91: ii11i + IiI1I1
i1i = xbmc . translatePath ( 'special://userdata' )
if os . path . exists ( i1i ) == False :
 os . mkdir ( i1i )
O000O0oOO0 = os . path . join ( i1i , 'cid' )
I1I1iIiII1 = os . path . join ( i1i , 'search.p' )
if 4 - 4: i1II1I11 + iIIi1iI1II111 * O00OoOoo00
if os . path . exists ( O000O0oOO0 ) == False :
 with open ( O000O0oOO0 , "w" ) as OOoo0O :
  OOoo0O . write ( str ( uuid . uuid1 ( ) ) )
  if 67 - 67: i11iIiiIii - OOOo0 % O0OOo . iIIi1iI1II111
if __name__ == '__main__' :
 OO0o . run ( )
 if 77 - 77: i1iIIi1 / Ooo00oOo00o
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
