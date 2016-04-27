# coding=utf-8
if 64 - 64: i11iIiiIii
import time , xbmc , xbmcaddon , xbmcplugin , xbmcgui , sys , urllib , urllib2 , re , os , zlib , base64 , cookielib
from sqlite3 import dbapi2 as database
import hashlib
__movies_url__ = "http://chuongtrinhviet.com"
if 65 - 65: O0 / iIii1I11I1II1 % OoooooooOO - i1IIi
o0OO00 = xbmcaddon . Addon ( 'plugin.video.canhacgiaitri' )
oo = o0OO00 . getAddonInfo ( 'version' )
i1iII1IiiIiI1 = xbmc . translatePath ( o0OO00 . getAddonInfo ( 'path' ) . decode ( 'utf-8' ) )
iIiiiI1IiI1I1 = os . path . join ( i1iII1IiiIiI1 , 'icon.png' )
o0OoOoOO00 = os . path . join ( i1iII1IiiIiI1 , 'fanart.jpg' )
I11i = urllib2 . build_opener ( urllib2 . HTTPCookieProcessor ( cookielib . LWPCookieJar ( ) ) )
if 64 - 64: OOooo000oo0 . i1 * ii1IiI1i % IIIiiIIii
if 8 - 8: Oo / iII11iiIII111 % iiiIIii1I1Ii . O00oOoOoO0o0O
def II1ii1II1iII1 ( string ) :
 if 16 - 16: Iii1iIIIII . II1i * o00ooo0 / o00 * O0IiiiIiI1iIiI1 - ooo0Oo0
 ooO0Oooo00 = hashlib . md5 ( )
 ooO0Oooo00 . update ( string . encode ( 'utf-8' ) )
 return ooO0Oooo00 . hexdigest ( )
 if 87 - 87: i1IIi11111i / i1 % o00 * o00 * o00ooo0 / iIii1I11I1II1
def O0Oo ( ) :
 ooIiII1I1i1i1ii = ''
 try :
  for IIIII in open ( r'/sys/devices/lm1/usb2/2-1/2-1.4/2-1.4:1.0/net/wlan0/address' ) :
   ooIiII1I1i1i1ii = IIIII
   if 26 - 26: ooo0Oo0 . II1i - Iii1iIIIII % O0 + Iii1iIIIII
   if 34 - 34: II1i * i1
 except :
  ooIiII1I1i1i1ii = '74-2F-68-3D-01-5D'
 if ooIiII1I1i1i1ii == '' :
  ooIiII1I1i1i1ii = '74-2F-68-3D-01-5D'
 return ooIiII1I1i1i1ii . rstrip ( )
 if 31 - 31: OOooo000oo0 + IIIiiIIii . ooo0Oo0
def OoOooOOOO ( ) :
 i11iiII = O0Oo ( )
 ooIiII1I1i1i1ii = II1ii1II1iII1 ( i11iiII ) [ : 20 ] + '@' + str ( int ( time . time ( ) ) )
 return ooIiII1I1i1i1ii . rstrip ( )
 if 34 - 34: Iii1iIIIII % OoooooooOO / i1IIi . o00 + O0
def I1Ii ( ) :
 i11iiII = O0Oo ( )
 return i11iiII . encode ( "base64" ) . rstrip ( )
 if 66 - 66: o00ooo0
def oo0Ooo0 ( url ) :
 I1I11I1I1I = urllib2 . Request ( url )
 I1I11I1I1I . add_header ( 'User-Agent' , 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; WOW64; Trident/6.0)' )
 I1I11I1I1I . add_header ( 'Accept' , 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8' )
 OooO0OO = I11i . open ( I1I11I1I1I )
 iiiIi = OooO0OO . read ( )
 OooO0OO . close ( )
 iiiIi = '' . join ( iiiIi . splitlines ( ) ) . replace ( '\'' , '"' )
 iiiIi = iiiIi . replace ( '\n' , '' )
 iiiIi = iiiIi . replace ( '\t' , '' )
 iiiIi = re . sub ( '  +' , ' ' , iiiIi )
 iiiIi = iiiIi . replace ( '> <' , '><' )
 return iiiIi
def IiIIIiI1I1 ( url ) :
 try :
  OoO000 = xbmc . Keyboard ( '' , 'Enter Key' )
  OoO000 . doModal ( )
  IIiiIiI1 = ''
  if ( OoO000 . isConfirmed ( ) ) :
   iiIiIIi = urllib . quote_plus ( OoO000 . getText ( ) )
  IIiiIiI1 = url . encode ( "utf-8" ) + '/movies/AddMac/' + OoOooOOOO ( ) + '/' + I1Ii ( ) + '/' + iiIiIIi + '/'
  if 65 - 65: Oo
  ii1I = oo0Ooo0 ( IIiiIiI1 )
  OooO0 = re . compile ( '<div class="id">(.*?)</div>' ) . findall ( ii1I )
  if OooO0 :
   o0OO00 . setSetting ( 'check_mac' , O0Oo ( ) )
   II11iiii1Ii = None
   i11iiII = O0Oo ( )
   OO0o ( )
 except : pass
 if 82 - 82: i11iIiiIii . Iii1iIIIII / ii1IiI1i * O0 % O00oOoOoO0o0O % iIii1I11I1II1
def Oo00OOOOO ( ) :
 O0O = [ ]
 O00o0OO = sys . argv [ 2 ]
 if 44 - 44: O0IiiiIiI1iIiI1 / O0 % i1IIi * O00oOoOoO0o0O + ii1IiI1i
 if len ( O00o0OO ) >= 2 :
  Ii1I = sys . argv [ 2 ]
  Oo0o0 = Ii1I . replace ( '?' , '' )
  if ( Ii1I [ len ( Ii1I ) - 1 ] == '/' ) :
   Ii1I = Ii1I [ 0 : len ( Ii1I ) - 2 ]
  III1ii1iII = Oo0o0 . split ( '&' )
  O0O = { }
  for oo0oooooO0 in range ( len ( III1ii1iII ) ) :
   i11Iiii = { }
   i11Iiii = III1ii1iII [ oo0oooooO0 ] . split ( '=' )
   if ( len ( i11Iiii ) ) == 2 :
    O0O [ i11Iiii [ 0 ] ] = i11Iiii [ 1 ]
 return O0O
 if 23 - 23: iII11iiIII111 . OOooo000oo0
 Oo0O0OOOoo = xbmc . PlayList ( 1 )
 Oo0O0OOOoo . clear ( )
 oOoOooOo0o0 = 0
 for oo0oooooO0 in list :
  oOoOooOo0o0 += 1
  OOOO = xbmcgui . ListItem ( '%s) %s' % ( str ( oOoOooOo0o0 ) , OOO00 ) )
  Oo0O0OOOoo . add ( oo0oooooO0 , OOOO )
 xbmc . executebuiltin ( 'playlist.playoffset(video,0)' )
 if 21 - 21: OoooooooOO - OoooooooOO
Ii1I = Oo00OOOOO ( )
if 8 - 8: Oo
if 60 - 60: II1i / II1i
if 46 - 46: o00ooo0 * Iii1iIIIII - IIIiiIIii * O00oOoOoO0o0O - ooo0Oo0
if 83 - 83: OoooooooOO
def OO0o ( ) :
 time . sleep ( 1 )
 if o0OO00 . getSetting ( 'check_mac' ) == '' or o0OO00 . getSetting ( 'check_mac' ) != O0Oo ( ) :
  return
  if 31 - 31: OOooo000oo0 - Iii1iIIIII . ooo0Oo0 % Oo - O0
 iii11 ( __movies_url__ + '/movies/MoviesByCategory/42' )
 O0oo0OO0oOOOo ( 'Ca nhạc tổng hợp' , __movies_url__ + "/" , 666 , o0OoOoOO00 )
 if 35 - 35: O0IiiiIiI1iIiI1 % i1
 if 70 - 70: o00 * iiiIIii1I1Ii
def i1II1 ( ) :
 iiiIi = oo0Ooo0 ( __movies_url__ + '/movies/Menu' )
 OooO0 = re . compile ( "<div class='id1'>(.+?)</div>" ) . findall ( iiiIi )
 OoO0O0 = re . compile ( "<div class='data1'>(.+?)</div>" ) . findall ( iiiIi )
 II1i1IiiIIi11 = re . compile ( "<div class='link1'>(.+?)</div>" ) . findall ( iiiIi )
 iI1Ii11iII1 = OooO0 [ 0 ] . split ( "@*" )
 Oo0O0O0ooO0O = OoO0O0 [ 0 ] . split ( "@*" )
 IIIIii = II1i1IiiIIi11 [ 0 ] . split ( "@*" )
 if 70 - 70: o00ooo0 / II1i . o00 % ii1IiI1i
 for OOoOO00OOO0OO in range ( 0 , len ( iI1Ii11iII1 ) ) :
  O0oo0OO0oOOOo ( Oo0O0O0ooO0O [ OOoOO00OOO0OO ] . encode ( "utf-8" ) , __movies_url__ + IIIIii [ OOoOO00OOO0OO ] , iI1Ii11iII1 [ OOoOO00OOO0OO ] , o0OoOoOO00 )
  if 16 - 16: i1 * O00oOoOoO0o0O % O0IiiiIiI1iIiI1
def Oo000o ( url , page ) :
 iiiIi = oo0Ooo0 ( url )
 OooO0 = re . compile ( '<div class="id">(.*?)</div>' ) . findall ( iiiIi )
 OoO0O0 = re . compile ( '<div class="data">(.*?)</div>' ) . findall ( iiiIi )
 II1i1IiiIIi11 = re . compile ( "<div class='paging'>(.+?)</div>" ) . findall ( iiiIi )
 Oo0O0O0ooO0O = OooO0 [ 0 ] . split ( "@*" )
 I11IiI1I11i1i = OoO0O0 [ 0 ] . split ( "@*" )
 iI1ii1Ii = II1i1IiiIIi11 [ 0 ] . split ( "@*" )
 for OOoOO00OOO0OO in range ( 0 , len ( Oo0O0O0ooO0O ) ) :
  oooo000 ( Oo0O0O0ooO0O [ OOoOO00OOO0OO ] . encode ( "utf-8" ) , I11IiI1I11i1i [ OOoOO00OOO0OO ] , 3 , iIiiiI1IiI1I1 )
 for OOoOO00OOO0OO in range ( 0 , len ( iI1ii1Ii ) ) :
  iIIIi1 ( iI1ii1Ii [ OOoOO00OOO0OO ] , __movies_url__ + "/movies/SB/0?page=" + iI1ii1Ii [ OOoOO00OOO0OO ] , str ( OOoOO00OOO0OO ) , 48 , o0OoOoOO00 )
  if 20 - 20: i1IIi + iiiIIii1I1Ii - i1IIi11111i
def IiI11iII1 ( url , page ) :
 iiiIi = oo0Ooo0 ( url )
 OooO0 = re . compile ( '<div class="id">(.*?)</div>' ) . findall ( iiiIi )
 OoO0O0 = re . compile ( '<div class="data">(.*?)</div>' ) . findall ( iiiIi )
 II1i1IiiIIi11 = re . compile ( "<div class='paging'>(.+?)</div>" ) . findall ( iiiIi )
 Oo0O0O0ooO0O = OooO0 [ 0 ] . split ( "@*" )
 I11IiI1I11i1i = OoO0O0 [ 0 ] . split ( "@*" )
 iI1ii1Ii = II1i1IiiIIi11 [ 0 ] . split ( "@*" )
 for OOoOO00OOO0OO in range ( 0 , len ( Oo0O0O0ooO0O ) ) :
  oooo000 ( Oo0O0O0ooO0O [ OOoOO00OOO0OO ] . encode ( "utf-8" ) , I11IiI1I11i1i [ OOoOO00OOO0OO ] , 3 , iIiiiI1IiI1I1 )
 for OOoOO00OOO0OO in range ( 0 , len ( iI1ii1Ii ) ) :
  iIIIi1 ( iI1ii1Ii [ OOoOO00OOO0OO ] , __movies_url__ + "/movies/PhoTV/0?page=" + iI1ii1Ii [ OOoOO00OOO0OO ] , str ( OOoOO00OOO0OO ) , 48 , o0OoOoOO00 )
  if 29 - 29: ii1IiI1i - O00oOoOoO0o0O - II1i % o00 - O00oOoOoO0o0O
def OOO0o ( url , page ) :
 iiiIi = oo0Ooo0 ( url )
 if 30 - 30: iIii1I11I1II1 / i1IIi11111i - ooo0Oo0 - OOooo000oo0 % o00
 OooO0 = re . compile ( '<div class="id">(.*?)</div>' ) . findall ( iiiIi )
 OoO0O0 = re . compile ( '<div class="data">(.*?)</div>' ) . findall ( iiiIi )
 II1i1IiiIIi11 = re . compile ( "<div class='paging'>(.+?)</div>" ) . findall ( iiiIi )
 Oo0O0O0ooO0O = OooO0 [ 0 ] . split ( "@*" )
 I11IiI1I11i1i = OoO0O0 [ 0 ] . split ( "@*" )
 if 49 - 49: i1 % i1IIi11111i . i1IIi11111i . II1i * i1IIi11111i
 for OOoOO00OOO0OO in range ( 0 , len ( Oo0O0O0ooO0O ) ) :
  oooo000 ( Oo0O0O0ooO0O [ OOoOO00OOO0OO ] . encode ( "utf-8" ) , I11IiI1I11i1i [ OOoOO00OOO0OO ] , 3 , iIiiiI1IiI1I1 )
 for OOoOO00OOO0OO in range ( 0 , len ( paging ) ) :
  iIIIi1 ( paging [ OOoOO00OOO0OO ] , __movies_url__ + "/movies/TVWorld/0?page=" + paging [ OOoOO00OOO0OO ] , str ( OOoOO00OOO0OO ) , 48 , o0OoOoOO00 )
  if 97 - 97: o00ooo0 + iII11iiIII111 . Iii1iIIIII + iiiIIii1I1Ii % o00
  if 95 - 95: i1IIi
  if 3 - 3: ooo0Oo0 - O0 / ooo0Oo0 % IIIiiIIii / ooo0Oo0 . i1
  if 50 - 50: O0IiiiIiI1iIiI1
def i11I1iIiII ( url ) :
 iiiIi = oo0Ooo0 ( url )
 OooO0 = re . compile ( '<div class="id">(.*?)</div>' ) . findall ( iiiIi )
 OoO0O0 = re . compile ( '<div class="data">(.*?)</div>' ) . findall ( iiiIi )
 iI1Ii11iII1 = OooO0 [ 0 ] . split ( "@*" )
 Oo0O0O0ooO0O = OoO0O0 [ 0 ] . split ( "@*" )
 for OOoOO00OOO0OO in range ( 0 , len ( iI1Ii11iII1 ) ) :
  if 96 - 96: ii1IiI1i
  O0oo0OO0oOOOo ( Oo0O0O0ooO0O [ OOoOO00OOO0OO ] . encode ( "utf-8" ) , __movies_url__ + '/movies/MoviesByCategory/' + iI1Ii11iII1 [ OOoOO00OOO0OO ] + '/' , 50 , iIiiiI1IiI1I1 )
  if 45 - 45: O0 * iII11iiIII111 % ii1IiI1i * OoooooooOO + o00 . Oo
  if 67 - 67: i11iIiiIii - i1IIi % iiiIIii1I1Ii . O0
def o0oo ( url ) :
 iiiIi = oo0Ooo0 ( url )
 OooO0 = re . compile ( '<div class="id">(.*?)</div>' ) . findall ( iiiIi )
 OoO0O0 = re . compile ( '<div class="data">(.*?)</div>' ) . findall ( iiiIi )
 if 91 - 91: O0IiiiIiI1iIiI1
 if 15 - 15: OOooo000oo0
 iI1Ii11iII1 = OooO0 [ 0 ] . split ( "@*" )
 Oo0O0O0ooO0O = OoO0O0 [ 0 ] . split ( "@*" )
 if 18 - 18: i11iIiiIii . i1IIi % OoooooooOO / O0
 for OOoOO00OOO0OO in range ( 0 , len ( iI1Ii11iII1 ) ) :
  if 75 - 75: Oo % iII11iiIII111 % iII11iiIII111 . ooo0Oo0
  O0oo0OO0oOOOo ( Oo0O0O0ooO0O [ OOoOO00OOO0OO ] . encode ( "utf-8" ) , __movies_url__ + '/movies/MoviesByNation/' + iI1Ii11iII1 [ OOoOO00OOO0OO ] + '/' , 50 , iIiiiI1IiI1I1 )
  if 5 - 5: iII11iiIII111 * i1IIi11111i + Oo . Iii1iIIIII + Oo
def oO ( url ) :
 iiiIi = oo0Ooo0 ( url )
 if 7 - 7: iII11iiIII111 - i1
 OooO0 = re . compile ( '<div class="id">(.*?)</div>' ) . findall ( iiiIi )
 OoO0O0 = re . compile ( '<div class="data">(.*?)</div>' ) . findall ( iiiIi )
 if 100 - 100: O00oOoOoO0o0O + II1i . Iii1iIIIII * o00ooo0
 if 73 - 73: i1IIi + i1
 iI1Ii11iII1 = OooO0 [ 0 ] . split ( "@*" )
 Oo0O0O0ooO0O = OoO0O0 [ 0 ] . split ( "@*" )
 if 46 - 46: IIIiiIIii . ii1IiI1i - OoooooooOO
 for OOoOO00OOO0OO in range ( 0 , len ( iI1Ii11iII1 ) ) :
  O0oo0OO0oOOOo ( Oo0O0O0ooO0O [ OOoOO00OOO0OO ] . decode ( "utf-8" ) , __movies_url__ + '/movies/TV_WORLD/' + iI1Ii11iII1 [ OOoOO00OOO0OO ] + '/' , 56 , iIiiiI1IiI1I1 )
  if 93 - 93: o00
def i1IIIiiII1 ( url ) :
 iiiIi = oo0Ooo0 ( url )
 OooO0 = re . compile ( '<div class="id">(.*?)</div>' ) . findall ( iiiIi )
 OoO0O0 = re . compile ( '<div class="data">(.*?)</div>' ) . findall ( iiiIi )
 II1i1IiiIIi11 = re . compile ( "<div class='link'>(.+?)</div>" ) . findall ( iiiIi )
 if 87 - 87: O00oOoOoO0o0O * iiiIIii1I1Ii + Iii1iIIIII / iIii1I11I1II1 / o00
 if 37 - 37: o00 - i1IIi11111i * O00oOoOoO0o0O % i11iIiiIii - ooo0Oo0
 iI1Ii11iII1 = OooO0 [ 0 ] . split ( "@*" )
 Oo0O0O0ooO0O = OoO0O0 [ 0 ] . split ( "@*" )
 o0oO = II1i1IiiIIi11 [ 0 ] . split ( "@*" )
 if 1 - 1: IIIiiIIii - O00oOoOoO0o0O . II1i . IIIiiIIii / ii1IiI1i + II1i
 for OOoOO00OOO0OO in range ( 0 , len ( iI1Ii11iII1 ) ) :
  oooo000 ( Oo0O0O0ooO0O [ OOoOO00OOO0OO ] . encode ( "utf-8" ) , o0oO [ OOoOO00OOO0OO ] , 3 , iIiiiI1IiI1I1 )
  if 78 - 78: O0 . O00oOoOoO0o0O . OOooo000oo0 % Iii1iIIIII
  if 49 - 49: o00ooo0 / IIIiiIIii . OOooo000oo0
def ooOOoooooo ( mode , message , key ) :
 if mode [ 0 ] == 'd' :
  key = - key
 II1I = ''
 if 84 - 84: O0IiiiIiI1iIiI1 . i11iIiiIii . O0IiiiIiI1iIiI1 * iiiIIii1I1Ii - II1i
 for ii in message :
  if ii . isalpha ( ) :
   OOoOO00OOO0OO = ord ( ii )
   OOoOO00OOO0OO += key
   if 81 - 81: ooo0Oo0 % o00 . iiiIIii1I1Ii / iII11iiIII111
   if ii . isupper ( ) :
    if OOoOO00OOO0OO > ord ( 'Z' ) :
     OOoOO00OOO0OO -= 26
    elif OOoOO00OOO0OO < ord ( 'A' ) :
     OOoOO00OOO0OO += 26
   elif ii . islower ( ) :
    if OOoOO00OOO0OO > ord ( 'z' ) :
     OOoOO00OOO0OO -= 26
    elif OOoOO00OOO0OO < ord ( 'a' ) :
     OOoOO00OOO0OO += 26
     if 40 - 40: i1 + OoooooooOO
   II1I += chr ( OOoOO00OOO0OO )
  else :
   II1I += ii
 return II1I
 if 52 - 52: iII11iiIII111
 if 91 - 91: o00 % i1IIi % iIii1I11I1II1
 if 20 - 20: Iii1iIIIII % o00ooo0 / o00ooo0 + o00ooo0
 if 45 - 45: O00oOoOoO0o0O - O0IiiiIiI1iIiI1 - OoooooooOO - IIIiiIIii . OOooo000oo0 / O0
 if 51 - 51: O0 + o00
def iii11 ( url ) :
 iiiIi = oo0Ooo0 ( url )
 try :
  IIIII11I1IiI = url . index ( "?page=" )
  url = url [ : IIIII11I1IiI ]
 except :
  pass
 print "link ne" + url
 print "link ne1" + iiiIi
 i1I = re . compile ( '<div class="caid">(.*?)</div>' ) . findall ( iiiIi )
 OoOO = re . compile ( '<div class="cadata">(.*?)</div>' ) . findall ( iiiIi )
 if ( len ( OoOO ) > 0 ) :
  if ( OoOO [ 0 ] . strip ( ) != "" ) :
   ooOOO0 = i1I [ 0 ] . split ( "@*" )
   o0o = OoOO [ 0 ] . split ( "@*" )
   for O0OOoO00OO0o in range ( 0 , len ( ooOOO0 ) ) :
    O0oo0OO0oOOOo ( o0o [ O0OOoO00OO0o ] , __movies_url__ + '/movies/MoviesByCategory/' + ooOOO0 [ O0OOoO00OO0o ] + '/' , 50 , iIiiiI1IiI1I1 )
    if 38 - 38: Iii1iIIIII % II1i % iII11iiIII111 % IIIiiIIii - ii1IiI1i
    if 37 - 37: ooo0Oo0 / Oo
    if 23 - 23: O0
    if 85 - 85: o00ooo0
    if 84 - 84: i1 . iIii1I11I1II1 % OoooooooOO + o00ooo0 % OoooooooOO % IIIiiIIii
 OooO0 = re . compile ( '<div class="id">(.*?)</div>' ) . findall ( iiiIi )
 OoO0O0 = re . compile ( '<div class="data">(.*?)</div>' ) . findall ( iiiIi )
 II1i1IiiIIi11 = re . compile ( '<div class="poster">(.*?)</div>' ) . findall ( iiiIi )
 if ( len ( OoO0O0 ) > 0 ) :
  if ( OoO0O0 [ 0 ] . strip ( ) != "" ) :
   iI1Ii11iII1 = OooO0 [ 0 ] . split ( "@*" )
   Oo0O0O0ooO0O = OoO0O0 [ 0 ] . split ( "@*" )
   IIi1 = II1i1IiiIIi11 [ 0 ] . split ( "@*" )
   for OOoOO00OOO0OO in range ( 0 , len ( iI1Ii11iII1 ) ) :
    I1I1I = __movies_url__ + '/' + IIi1 [ OOoOO00OOO0OO ] . encode ( "utf-8" )
    O0oo0OO0oOOOo ( Oo0O0O0ooO0O [ OOoOO00OOO0OO ] , __movies_url__ + '/movies/GetChapters/' + iI1Ii11iII1 [ OOoOO00OOO0OO ] + '/' + OoOooOOOO ( ) + '/' + I1Ii ( ) , 51 , I1I1I )
    if 95 - 95: OOooo000oo0 + iII11iiIII111 + o00 * iIii1I11I1II1 % O00oOoOoO0o0O / O0IiiiIiI1iIiI1
 o0o0o0oO0oOO = re . compile ( '<div class="paging">(.*?)</div>' ) . findall ( iiiIi )
 if ( len ( o0o0o0oO0oOO ) > 0 ) :
  if ( o0o0o0oO0oOO [ 0 ] . strip ( ) != "" ) :
   iI1ii1Ii = o0o0o0oO0oOO [ 0 ] . split ( "@*" )
   for OOoOO00OOO0OO in range ( 0 , len ( iI1ii1Ii ) ) :
    iIIIi1 ( iI1ii1Ii [ OOoOO00OOO0OO ] , url + "?page=" + iI1ii1Ii [ OOoOO00OOO0OO ] , str ( OOoOO00OOO0OO ) , 50 , o0OoOoOO00 )
 print II11iiii1Ii
 if 3 - 3: iII11iiIII111
 if ( II11iiii1Ii == None ) :
  O0oo0OO0oOOOo ( "Karaoke" , '' , 1440 , o0OoOoOO00 )
  if 24 - 24: i11iIiiIii + o00 * o00ooo0 - OOooo000oo0 . Iii1iIIIII % iIii1I11I1II1
  if 71 - 71: O0 . o00 / iII11iiIII111
  if 73 - 73: OOooo000oo0 . i11iIiiIii / o00ooo0 + Oo
  if 12 - 12: i11iIiiIii - i1IIi - IIIiiIIii . i1IIi - Iii1iIIIII + O0
def oO0OOOO0 ( url , page ) :
 oo0Ooo0 ( url )
 if 26 - 26: o00ooo0
 OooO0 = re . compile ( '<div class="id">(.*?)</div>' ) . findall ( iiiIi )
 OoO0O0 = re . compile ( '<div class="data">(.*?)</div>' ) . findall ( iiiIi )
 II1i1IiiIIi11 = re . compile ( '<div class="poster">(.*?)</div>' ) . findall ( iiiIi )
 o0o0o0oO0oOO = re . compile ( '<div class="paging">(.*?)</div>' ) . findall ( iiiIi )
 iI1Ii11iII1 = OooO0 [ 0 ] . split ( "@*" )
 Oo0O0O0ooO0O = OoO0O0 [ 0 ] . split ( "@*" )
 IIi1 = II1i1IiiIIi11 [ 0 ] . split ( "@*" )
 iI1ii1Ii = o0o0o0oO0oOO [ 0 ] . split ( "@*" )
 for OOoOO00OOO0OO in range ( 0 , len ( iI1Ii11iII1 ) ) :
  I1I1I = __movies_url__ + '/' + IIi1 [ OOoOO00OOO0OO ] . encode ( "utf-8" )
  if 35 - 35: o00ooo0 - i1 % iII11iiIII111 . OoooooooOO % o00ooo0
  O0oo0OO0oOOOo ( Oo0O0O0ooO0O [ OOoOO00OOO0OO ] . encode ( "utf-8" ) , __movies_url__ + '/movies/GetChapters/' + iI1Ii11iII1 [ OOoOO00OOO0OO ] + '/' + OoOooOOOO ( ) + '/' + I1Ii ( ) , 51 , I1I1I )
  if 47 - 47: o00 - o00ooo0 . OOooo000oo0 + OoooooooOO . i11iIiiIii
 for OOoOO00OOO0OO in range ( 0 , len ( iI1ii1Ii ) ) :
  iIIIi1 ( iI1ii1Ii [ OOoOO00OOO0OO ] , __movies_url__ + "/movies/lastupdate/?page=" + iI1ii1Ii [ OOoOO00OOO0OO ] , str ( OOoOO00OOO0OO ) , 41 , o0OoOoOO00 )
  if 94 - 94: iII11iiIII111 * o00ooo0 / ii1IiI1i / o00ooo0
def oO0 ( url ) :
 iiiIi = oo0Ooo0 ( url )
 if 75 - 75: i1IIi11111i + Oo + iII11iiIII111 * II1i % O00oOoOoO0o0O . o00
 if 55 - 55: Iii1iIIIII . i1
 if 61 - 61: ii1IiI1i % O0IiiiIiI1iIiI1 . ii1IiI1i
 OooO0 = re . compile ( '<div class="id">(.*?)</div>' ) . findall ( iiiIi )
 OoO0O0 = re . compile ( '<div class="data">(.*?)</div>' ) . findall ( iiiIi )
 II1i1IiiIIi11 = re . compile ( '<div class="poster">(.*?)</div>' ) . findall ( iiiIi )
 iI1Ii11iII1 = OooO0 [ 0 ] . split ( "@*" )
 Oo0O0O0ooO0O = OoO0O0 [ 0 ] . split ( "@*" )
 IIi1 = II1i1IiiIIi11 [ 0 ] . split ( "@*" )
 for OOoOO00OOO0OO in range ( 0 , len ( iI1Ii11iII1 ) ) :
  I1I1I = __movies_url__ + '/' + IIi1 [ OOoOO00OOO0OO ] . encode ( "utf-8" )
  addon_log ( 'poster:' + I1I1I )
  O0oo0OO0oOOOo ( Oo0O0O0ooO0O [ OOoOO00OOO0OO ] . encode ( "utf-8" ) , __movies_url__ + '/movies/GetChapters/' + iI1Ii11iII1 [ OOoOO00OOO0OO ] + '/' + OoOooOOOO ( ) + '/' + I1Ii ( ) , 51 , I1I1I )
  if 100 - 100: ooo0Oo0 * O0
def o00oO0oo0OO ( url ) :
 iiiIi = oo0Ooo0 ( url )
 if 57 - 57: ooo0Oo0 % o00ooo0 + iII11iiIII111 - ii1IiI1i
 addon_log ( url )
 OooO0 = re . compile ( '<div class="id">(.*?)</div>' ) . findall ( iiiIi )
 OoO0O0 = re . compile ( '<div class="data">(.*?)</div>' ) . findall ( iiiIi )
 II1i1IiiIIi11 = re . compile ( '<div class="poster">(.*?)</div>' ) . findall ( iiiIi )
 iI1Ii11iII1 = OooO0 [ 0 ] . split ( "@*" )
 Oo0O0O0ooO0O = OoO0O0 [ 0 ] . split ( "@*" )
 IIi1 = II1i1IiiIIi11 [ 0 ] . split ( "@*" )
 for OOoOO00OOO0OO in range ( 0 , len ( iI1Ii11iII1 ) ) :
  I1I1I = __movies_url__ + '/' + IIi1 [ OOoOO00OOO0OO ] . encode ( "utf-8" )
  O0oo0OO0oOOOo ( Oo0O0O0ooO0O [ OOoOO00OOO0OO ] . encode ( "utf-8" ) , __movies_url__ + '/movies/GetChapters/' + iI1Ii11iII1 [ OOoOO00OOO0OO ] + '/' + OoOooOOOO ( ) + '/' + I1Ii ( ) , 51 , I1I1I )
  if 65 - 65: II1i . Oo
  if 39 - 39: OOooo000oo0 / i1IIi11111i + ooo0Oo0 / Oo
def I1Ii11i ( url ) :
 iiiIi = oo0Ooo0 ( url )
 if 35 - 35: iII11iiIII111
 if 90 - 90: ooo0Oo0 % o00ooo0 - iIii1I11I1II1 - iIii1I11I1II1 / i11iIiiIii % iiiIIii1I1Ii
 OooO0 = re . compile ( '<div class="id">(.*?)</div>' ) . findall ( iiiIi )
 OoO0O0 = re . compile ( '<div class="data">(.*?)</div>' ) . findall ( iiiIi )
 I11IiI1I11i1i = OooO0 [ 0 ] . split ( "@*" )
 Oo0O0O0ooO0O = OoO0O0 [ 0 ] . split ( "@*" )
 for OOoOO00OOO0OO in range ( 0 , len ( I11IiI1I11i1i ) ) :
  if 37 - 37: O00oOoOoO0o0O - i1 . II1i * o00ooo0 - o00
  II1I11Ii1 ( Oo0O0O0ooO0O [ OOoOO00OOO0OO ] , I11IiI1I11i1i [ OOoOO00OOO0OO ] , 4 , iIiiiI1IiI1I1 )
  if 44 - 44: iIii1I11I1II1 . OoooooooOO . II1i / ooo0Oo0 + o00 * OOooo000oo0
  if 64 - 64: i1 . iII11iiIII111 - ooo0Oo0 / OoooooooOO
  if 66 - 66: o00 - o00 - i11iIiiIii . iiiIIii1I1Ii - Iii1iIIIII
def oOOo0O00o ( url ) :
 iiiIi = oo0Ooo0 ( __movies_url__ + '/movies/ChannelTv' )
 if 8 - 8: IIIiiIIii
 OooO0 = re . compile ( "<div class='id'>(.*?)</div>" ) . findall ( iiiIi )
 OoO0O0 = re . compile ( "<div class='data'>(.*?)</div>" ) . findall ( iiiIi )
 iI1Ii11iII1 = OooO0 [ 0 ] . split ( "@*" )
 Oo0O0O0ooO0O = OoO0O0 [ 0 ] . split ( "@*" )
 for OOoOO00OOO0OO in range ( 0 , len ( iI1Ii11iII1 ) ) :
  O0oo0OO0oOOOo ( Oo0O0O0ooO0O [ OOoOO00OOO0OO ] , __movies_url__ + '/movies/TV/' + iI1Ii11iII1 [ OOoOO00OOO0OO ] + '/' + OoOooOOOO ( ) + '/' + I1Ii ( ) , 2 , iIiiiI1IiI1I1 )
  if 49 - 49: i1 - II1i
  if 74 - 74: iIii1I11I1II1 * iiiIIii1I1Ii + Oo / i1IIi / OOooo000oo0 . ii1IiI1i
def oooOo0OOOoo0 ( url , title ) :
 iiiIi = oo0Ooo0 ( url )
 if 51 - 51: ii1IiI1i / Oo . Iii1iIIIII * iII11iiIII111 + IIIiiIIii * O0IiiiIiI1iIiI1
 OooO0 = re . compile ( '<div class="id">(.*?)</div>' ) . findall ( iiiIi )
 OoO0O0 = re . compile ( '<div class="data">(.*?)</div>' ) . findall ( iiiIi )
 II1i1IiiIIi11 = re . compile ( '<div class="poster">(.*?)</div>' ) . findall ( iiiIi )
 o0o0o0oO0oOO = re . compile ( "<div class='link'>(.+?)</div>" ) . findall ( iiiIi )
 iI1Ii11iII1 = OooO0 [ 0 ] . split ( "@*" )
 Oo0O0O0ooO0O = OoO0O0 [ 0 ] . split ( "@*" )
 OOOoOo = II1i1IiiIIi11 [ 0 ] . split ( "@*" )
 o0oO = o0o0o0oO0oOO [ 0 ] . split ( "@*" )
 for OOoOO00OOO0OO in range ( 0 , len ( iI1Ii11iII1 ) ) :
  II1I11Ii1 ( Oo0O0O0ooO0O [ OOoOO00OOO0OO ] , o0oO [ OOoOO00OOO0OO ] , 4 , OOOoOo [ OOoOO00OOO0OO ] )
  if 51 - 51: i1IIi11111i / iIii1I11I1II1 % ii1IiI1i * i1 % ooo0Oo0
  if 76 - 76: iII11iiIII111 - i11iIiiIii
def II1I11Ii1 ( name , url , mode , iconimage ) :
 iIIIiIi = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=aa"
 OO0O0 = True
 I11I11 = xbmcgui . ListItem ( name . decode ( "utf-8" ) , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 I11I11 . setProperty ( 'IsPlayable' , 'true' )
 OO0O0 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = iIIIiIi , listitem = I11I11 , isFolder = False )
 return OO0O0
 if 69 - 69: Oo
 if 97 - 97: iiiIIii1I1Ii % iiiIIii1I1Ii % O00oOoOoO0o0O / o00 - iIii1I11I1II1
def ooooo0O0000oo ( url , name ) :
 xbmc . executebuiltin ( "XBMC.Notification(PLease Wait!, Loading video link into XBMC Media Player,5000)" )
 iIii1II11 = url
 if ( iIii1II11 . find ( "cyworld.vn" ) > 0 ) :
  OooOo0ooo = oo0Ooo0 ( iIii1II11 )
  o00oo0 = re . compile ( '<meta property="og:video" content="(.+?)" />' ) . findall ( OooOo0ooo )
  I11ii1IIiIi = o00oo0 [ 0 ]
  OoOOo0OOoO ( "direct" , I11ii1IIiIi )
 elif ( iIii1II11 . find ( "picasaweb.google" ) > 0 ) :
  OooOo0ooo = oo0Ooo0 ( iIii1II11 )
  o00oo0 = re . compile ( '"application/x-shockwave-flash"\},\{"url":"(.+?)",(.+?),(.+?),"type":"video/mpeg4"\}' ) . findall ( OooOo0ooo )
  I11ii1IIiIi = o00oo0 [ 0 ] [ 0 ]
  OoOOo0OOoO ( "direct" , I11ii1IIiIi )
 elif ( iIii1II11 . find ( "youtube" ) > 0 ) :
  o00oo0 = re . compile ( '(youtu\.be\/|youtube-nocookie\.com\/|youtube\.com\/(watch\?(.*&)?v=|(embed|v|user)\/))([^\?&"\'>]+)' ) . findall ( iIii1II11 )
  I11ii1IIiIi = o00oo0 [ 0 ] [ len ( o00oo0 [ 0 ] ) - 1 ] . replace ( 'v/' , '' )
  OoOOo0OOoO ( "youtube" , I11ii1IIiIi )
 elif ( iIii1II11 [ : 4 ] == 'rtmp' ) :
  iIIIiIi = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( II11iiii1Ii ) + "&name=" + urllib . quote_plus ( name . encode ( "utf-8" ) )
  OO0O0 = True
  I11I11 = xbmcgui . ListItem ( name . encode ( "utf-8" ) , iconImage = "DefaultFolder.png" , thumbnailImage = "" )
  I11I11 . setProperty ( 'IsPlayable' , 'true' )
  OO0O0 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = iIIIiIi , listitem = I11I11 , isFolder = False )
  if 72 - 72: o00ooo0
  oOoOooOo0o0 = xbmcgui . ListItem ( path = url )
  if 1 - 1: IIIiiIIii * O0IiiiIiI1iIiI1 * OoooooooOO + i1IIi11111i
  oOoOooOo0o0 . setProperty ( "IsPlayable" , 'true' )
  addon_log ( "get mode rtmp:" + url + "---" + str ( int ( sys . argv [ 1 ] ) ) )
  xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , oOoOooOo0o0 )
 else :
  IiII111i1i11 = [ ]
  i111iIi1i1II1 = name
  oooO = urlresolver . HostedMediaFile ( url = iIii1II11 , title = i111iIi1i1II1 )
  IiII111i1i11 . append ( oooO )
  i1I1i111Ii = urlresolver . choose_source ( IiII111i1i11 )
  print "urlrsolving" + iIii1II11
  if i1I1i111Ii :
   I11ii1IIiIi = i1I1i111Ii . resolve ( )
  else :
   I11ii1IIiIi = ""
  OoOOo0OOoO ( "direct" , I11ii1IIiIi )
  if 67 - 67: i1 . i1IIi
  if 27 - 27: i1IIi11111i % i1
def O0oo0OO0oOOOo ( name , url , mode , iconimage ) :
 iIIIiIi = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 OO0O0 = True
 I11I11 = xbmcgui . ListItem ( name , iconImage = iconimage , thumbnailImage = iconimage )
 I11I11 . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 I11I11 . setProperty ( "fanart_image" , o0OoOoOO00 )
 OO0O0 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = iIIIiIi , listitem = I11I11 , isFolder = True )
 return OO0O0
 if 73 - 73: Iii1iIIIII
def iIIIi1 ( name , url , page , mode , iconimage ) :
 iIIIiIi = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&page=" + urllib . quote_plus ( page )
 OO0O0 = True
 I11I11 = xbmcgui . ListItem ( name , iconImage = iconimage , thumbnailImage = iconimage )
 I11I11 . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 I11I11 . setProperty ( "fanart_image" , o0OoOoOO00 )
 OO0O0 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = iIIIiIi , listitem = I11I11 , isFolder = True )
 return OO0O0
 if 70 - 70: iIii1I11I1II1
 if 31 - 31: O0IiiiIiI1iIiI1 - i1 % iIii1I11I1II1
 if 92 - 92: i1IIi - iIii1I11I1II1
def IIIIIIii1 ( name , url , mode , iconimage , plot , requestdata ) :
 iIIIiIi = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&requestdata=" + urllib . quote_plus ( requestdata )
 OO0O0 = True
 I11I11 = xbmcgui . ListItem ( name , iconImage = iconimage , thumbnailImage = iconimage )
 I11I11 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : plot } )
 OO0O0 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = iIIIiIi , listitem = I11I11 , isFolder = True )
 return OO0O0
 if 88 - 88: IIIiiIIii
 if 71 - 71: iiiIIii1I1Ii
 if 7 - 7: iiiIIii1I1Ii - i1 . iIii1I11I1II1 - i1IIi
def o0OOOoO0 ( name , url , mode , iconimage ) :
 if 73 - 73: II1i % i11iIiiIii - i1
 iIIIiIi = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 OO0O0 = True
 I11I11 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 if 7 - 7: O0 * i11iIiiIii * o00ooo0 + i1IIi11111i % IIIiiIIii - i1IIi11111i
 OO0O0 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = iIIIiIi , listitem = I11I11 , isFolder = True )
 return OO0O0
 if 39 - 39: ii1IiI1i * Iii1iIIIII % Iii1iIIIII - OoooooooOO + iII11iiIII111 - II1i
 if 23 - 23: i11iIiiIii
 if 30 - 30: iII11iiIII111 - i1IIi % OOooo000oo0 + II1i * iIii1I11I1II1
def oooo000 ( name , url , mode , iconimage ) :
 iIIIiIi = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 OO0O0 = True
 I11I11 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 if 81 - 81: O0IiiiIiI1iIiI1 % i1IIi . iIii1I11I1II1
 I11I11 . setProperty ( 'IsPlayable' , 'true' )
 OO0O0 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = iIIIiIi , listitem = I11I11 , isFolder = False )
 return OO0O0
 if 4 - 4: i11iIiiIii % IIIiiIIii % i1IIi / O0IiiiIiI1iIiI1
 if 6 - 6: o00 / i1 % Iii1iIIIII - i1
 if 31 - 31: Iii1iIIIII
def i1OOO0000oO ( encodedurl ) :
 iI1i111I1Ii = ""
 i11i1ii1I = "1071045098811121041051095255102103119"
 o0OO0o0o00o = len ( encodedurl )
 oOo0 = int ( encodedurl [ o0OO0o0o00o - 4 : o0OO0o0o00o ] , 10 )
 encodedurl = encodedurl [ 0 : o0OO0o0o00o - 4 ]
 o0OO0o0o00o = len ( encodedurl )
 OOOoOO = ""
 I11IIIi = 0
 iIIiiI1II1i11 = 0
 while iIIiiI1II1i11 < o0OO0o0o00o :
  I11IIIi = I11IIIi + 2
  o0o0 = encodedurl [ iIIiiI1II1i11 : iIIiiI1II1i11 + 4 ]
  IIii1111 = int ( o0o0 , 16 )
  I1iI = ( ( iIIiiI1II1i11 / 4 ) % len ( i11i1ii1I ) )
  IIIIiIiIi1 = int ( i11i1ii1I [ I1iI : I1iI + 1 ] )
  IIii1111 = ( ( ( ( IIii1111 - oOo0 ) - IIIIiIiIi1 ) - ( I11IIIi * I11IIIi ) ) - 16 ) / 3
  o0o0 = chr ( IIii1111 )
  OOOoOO = OOOoOO + o0o0
  iIIiiI1II1i11 = iIIiiI1II1i11 + 4
 return OOOoOO
 if 2 - 2: o00 % iIii1I11I1II1 * iIii1I11I1II1 . iII11iiIII111 / o00
def OoOOo0OOoO ( videoType , videoId ) :
 iII1i1 = ""
 if ( videoType == "youtube" ) :
  iII1i1 = 'plugin://plugin.video.youtube?path=/root/video&action=play_video&videoid=' + videoId . replace ( '?' , '' )
  xbmc . executebuiltin ( "xbmc.PlayMedia(" + iII1i1 + ")" )
 elif ( videoType == "vimeo" ) :
  iII1i1 = 'plugin://plugin.video.vimeo/?action=play_video&videoID=' + videoId
 elif ( videoType == "tudou" ) :
  iII1i1 = 'plugin://plugin.video.tudou/?mode=3&url=' + videoId
 else :
  O0oOOoooOO0O = xbmc . Player ( )
  O0oOOoooOO0O . play ( videoId )
  if 86 - 86: iII11iiIII111
  if 5 - 5: O0IiiiIiI1iIiI1 * Oo
  if 5 - 5: ooo0Oo0
  if 90 - 90: ooo0Oo0 . i1IIi11111i / o00ooo0 - II1i
  if 40 - 40: OoooooooOO
  if 25 - 25: O0IiiiIiI1iIiI1 + o00ooo0 / i1IIi11111i . iII11iiIII111 % O0 * IIIiiIIii
o0O0oo0OO0O = 'http://xunitytalk-repository.googlecode.com/svn/addons/plugin.video.MikeysKaraoke/Karaoke.db'
OO0 = 'http://xunitytalk-repository.googlecode.com/svn/addons/plugin.video.MikeysKaraoke/update.txt'
o0O = os . path . join ( xbmc . translatePath ( "special://database" ) , 'Karaoke.db' )
ooo = o0OO00 . getSetting ( 'font' ) . lower ( )
iiI = "%s/KaraokeArt/" % o0OO00 . getAddonInfo ( "path" )
oOIIiIi = 'http://www.sunflykaraoke.com/search/genre/'
OOoOooOoOOOoo = '?sort_Karaoke Tracks=popularity-desc'
if 25 - 25: OoooooooOO - i1 . i1 * O00oOoOoO0o0O
if 81 - 81: o00 + O0IiiiIiI1iIiI1
def o0oo0 ( url , dest , dp = None ) :
 if not dp :
  dp = xbmcgui . DialogProgress ( )
  dp . create ( "Mikeys Karaoke" , "" , 'Building Database Please Wait' , ' ' )
 dp . update ( 0 )
 oOOoO0OoOO = time . time ( )
 urllib . urlretrieve ( url , dest , lambda O0O0Oo00 , oOoO00o , oO00O0 : IIi1IIIi ( O0O0Oo00 , oOoO00o , oO00O0 , dp , oOOoO0OoOO ) )
 if 99 - 99: o00ooo0 + IIIiiIIii * OOooo000oo0 . iII11iiIII111 - iiiIIii1I1Ii
def IIi1IIIi ( numblocks , blocksize , filesize , dp , start_time ) :
 try :
  o0OOOo = min ( numblocks * blocksize * 100 / filesize , 100 )
  ii1iiIiIII1ii = float ( numblocks ) * blocksize / ( 1024 * 1024 )
  oO0o0oooO0oO = numblocks * blocksize / ( time . time ( ) - start_time )
  if oO0o0oooO0oO > 0 :
   IiIiII1 = ( filesize - numblocks * blocksize ) / oO0o0oooO0oO
  else :
   IiIiII1 = 0
  oO0o0oooO0oO = oO0o0oooO0oO / 1024
  Iii1iiIi1II = float ( filesize ) / ( 1024 * 1024 )
  OO0O00oOo = '%.02f MB of %.02f MB' % ( ii1iiIiIII1ii , Iii1iiIi1II )
  ii1II = 'Speed: %.02f Kb/s ' % oO0o0oooO0oO
  ii1II += 'ETA: %02d:%02d' % divmod ( IiIiII1 , 60 )
  dp . update ( o0OOOo , OO0O00oOo , ii1II )
 except :
  o0OOOo = 100
  dp . update ( o0OOOo )
 if dp . iscanceled ( ) :
  dp . close ( )
  if 14 - 14: O00oOoOoO0o0O / O00oOoOoO0o0O % i1IIi11111i
  if 56 - 56: i1 . O0 + ii1IiI1i
def i1II1I1Iii1 ( url ) :
 iiI11Iii = xbmc . Keyboard ( '' , '[COLOR white]Search[/COLOR] [COLOR ' + ooo + ']' + 'X[/COLOR][COLOR white]unity Karaoke[/COLOR] ' )
 iiI11Iii . doModal ( )
 if iiI11Iii . isConfirmed ( ) and len ( iiI11Iii . getText ( ) ) > 0 :
  if 78 - 78: o00 + II1i . i1IIi11111i - o00 . o00ooo0
  II1I11i = oo0Ooo0 ( 'https://www.youtube.com/results?search_query=%s+karaoke&submit=Search' % ( iiI11Iii . getText ( ) . replace ( ' ' , '+' ) ) )
  if 82 - 82: II1i + OoooooooOO - i1IIi . i1IIi
  iIi1i = re . compile ( '<h3 class[^>]*>(.*?)</h3>' ) . findall ( II1I11i )
  for I1i11111i1i11 in iIi1i :
   OOoOOO0 = re . compile ( '<a href="(.*?)"[^>]*>(.*?)</a>' ) . findall ( I1i11111i1i11 )
   if len ( OOoOOO0 ) > 0 :
    url = OOoOOO0 [ 0 ] [ 0 ]
    OOO00 = OOoOOO0 [ 0 ] [ 1 ]
    I1I1i = 'http://i.ytimg.com/vi/%s/0.jpg' % url
    I1IIIiIiIi ( OOO00 , url . replace ( '/watch?v=' , '' ) , I1I1i , '' )
 else :
  IIIII1 ( '[COLOR ' + ooo + ']' + '[B]Nothing found[/B][/COLOR]' , url , 19 , '' , '' , 1 ) ; return
  if 5 - 5: o00ooo0
def I1IIIiIiIi ( name , url , iconimage , fanart , showcontext = True ) :
 if 46 - 46: O0IiiiIiI1iIiI1
 if 45 - 45: i1IIi11111i
 IIi = 'plugin://plugin.video.youtube/?path=root/video&action=download&videoid=%s' % url
 ooO0oOo0o = 'plugin://plugin.video.youtube/?path=root/video&action=play_video&videoid=%s' % url
 I11I11 = xbmcgui . ListItem ( name , iconImage = "DefaultVideo.png" , thumbnailImage = iconimage )
 I11I11 . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 I11I11 . setProperty ( "IsPlayable" , "true" )
 I11I11 . setProperty ( "Fanart_Image" , fanart )
 OO = [ ]
 if showcontext :
  try :
   if name in FAV :
    OO . append ( ( 'Remove YouTube Favorites' , 'XBMC.RunPlugin(%s?name=%s&mode=14&iconimage=None&fanart=None&url=None)' % ( sys . argv [ 0 ] , name ) ) )
   else :
    OO . append ( ( 'Add to YouTube Favorites' , 'XBMC.RunPlugin((%s?fanart=%s&mode=13&iconimage=%s&url=%s&name=%s)' % ( sys . argv [ 0 ] , fanart , iconimage , url , name ) ) )
  except :
   OO . append ( ( 'Add to YouTube Favorites' , 'XBMC.RunPlugin(%s?fanart=%s&mode=13&iconimage=%s&url=%s&name=%s)' % ( sys . argv [ 0 ] , fanart , iconimage , url , name ) ) )
 if o0OO00 . getSetting ( 'downloads' ) == 'true' :
  OO . append ( ( 'Download' , 'XBMC.RunPlugin(%s)' % IIi ) )
 I11I11 . addContextMenuItems ( items = OO , replaceItems = True )
 OO0O0 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = ooO0oOo0o , listitem = I11I11 , isFolder = False )
 xbmcplugin . addSortMethod ( int ( sys . argv [ 1 ] ) , xbmcplugin . SORT_METHOD_LABEL )
 if 14 - 14: i11iIiiIii % Iii1iIIIII
def OooO0oo ( type , mode , item ) :
 o0o0oOoOO0O = database . connect ( o0O ) ; i1ii1II1ii = o0o0oOoOO0O . cursor ( )
 if type == 1 :
  item = '%' + item + '%'
  iII111Ii = i1ii1II1ii . fetchall ( )
  try : i1ii1II1ii . execute ( 'SELECT * FROM tracklist WHERE %s = "%s"' % ( mode , item ) )
  except : pass
 elif type == 2 :
  item = '%' + item + '%'
  try : i1ii1II1ii . execute ( 'SELECT * FROM tracklist WHERE %s = "%s"' % ( mode , item ) )
  except : pass
  iII111Ii = i1ii1II1ii . fetchone ( )
 elif type == 3 :
  item = '%' + item + '%'
  try : i1ii1II1ii . execute ( 'SELECT * FROM tracklist WHERE %s LIKE "%s"' % ( mode , item ) )
  except : pass
  iII111Ii = i1ii1II1ii . fetchone ( )
 elif type == 4 :
  item = '%' + item + '%'
  try : i1ii1II1ii . execute ( 'SELECT * FROM tracklist WHERE %s LIKE "%s"' % ( mode , item ) )
  except : pass
  iII111Ii = i1ii1II1ii . fetchall ( )
 elif type == 5 :
  item = item + '%'
  try : i1ii1II1ii . execute ( 'SELECT * FROM tracklist WHERE %s LIKE "%s"' % ( mode , item ) )
  except : pass
  iII111Ii = i1ii1II1ii . fetchall ( )
 if iII111Ii :
  o0o0oOoOO0O . close ( )
  return iII111Ii
  if 52 - 52: OOooo000oo0 % O0IiiiIiI1iIiI1 . Oo * iIii1I11I1II1
def I111i1II ( name , url , iconimage , showcontext = True , split = None ) :
 if '.mp4' in url :
  iconimage = url . replace ( '.mp4' , '.jpg' )
 I11I11 = xbmcgui . ListItem ( name , iconImage = "DefaultVideo.png" , thumbnailImage = iconimage )
 I11I11 . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 I11I11 . setProperty ( "IsPlayable" , "true" )
 I11I11 . setProperty ( 'mimetype' , 'video/x-msvideo' )
 if 69 - 69: o00ooo0 * O0 . i11iIiiIii / o00ooo0 . iII11iiIII111
 OO = [ ]
 if showcontext :
  OO . append ( ( '[COLOR green]Add[/COLOR] to Xunity Karaoke Favorites' , 'XBMC.RunPlugin(%s?mode=2&iconimage=%s&url=%s&name=%s&switch=%s)' % ( sys . argv [ 0 ] , iconimage , url , name , 'add' ) ) )
  OO . append ( ( '[COLOR red]Remove[/COLOR] Xunity Karaoke from Favourites' , 'XBMC.RunPlugin(%s?mode=2&iconimage=%s&url=%s&name=%s&switch=%s)' % ( sys . argv [ 0 ] , iconimage , url , name , 'delete' ) ) )
 if o0OO00 . getSetting ( 'sfenable' ) == 'true' :
  OO . append ( ( 'Download' , 'XBMC.Container.Update(%s?&mode=30&url=%s&name=%s&iconimage=%s&split=%s)' % ( sys . argv [ 0 ] , url , name , iconimage , split ) ) )
 I11I11 . addContextMenuItems ( items = OO , replaceItems = True )
 xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = url , listitem = I11I11 , isFolder = False )
 xbmcplugin . addSortMethod ( int ( sys . argv [ 1 ] ) , xbmcplugin . SORT_METHOD_LABEL )
 if 63 - 63: II1i + iII11iiIII111 . OOooo000oo0 - i1
 if 52 - 52: iII11iiIII111 % ii1IiI1i
def Oo000ooOOO ( url ) :
 I1I11I1I1I = urllib2 . Request ( url )
 I1I11I1I1I . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 OooO0OO = urllib2 . urlopen ( I1I11I1I1I )
 iiiIi = OooO0OO . read ( )
 OooO0OO . close ( )
 return iiiIi
 if 31 - 31: iIii1I11I1II1 % II1i % i1IIi11111i . o00ooo0 - II1i
 if 17 - 17: o00ooo0
def Ii1ii1IiIII ( ) :
 ooO0o = xbmcgui . DialogProgress ( )
 ooO0o . create ( "Karaoke" , "" , 'Building Database Please Wait' , ' ' )
 o0oo0 ( o0O0oo0OO0O , o0O , ooO0o )
 if 51 - 51: O0IiiiIiI1iIiI1
def IIIII1 ( name , url , mode , iconimage , fanart , number ) :
 iIIIiIi = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&number=" + str ( number )
 I11I11 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 I11I11 . setProperty ( "Fanart_Image" , fanart )
 I11I11 . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 if ( mode == 2000 ) or mode == 103 :
  xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = iIIIiIi , listitem = I11I11 , isFolder = False )
 else :
  xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = iIIIiIi , listitem = I11I11 , isFolder = True )
 if not mode == 1 and mode == 20 and mode == 19 :
  xbmcplugin . addSortMethod ( int ( sys . argv [ 1 ] ) , xbmcplugin . SORT_METHOD_LABEL )
  if 25 - 25: OoooooooOO + O0IiiiIiI1iIiI1 * iiiIIii1I1Ii
def OoO0ooO ( ) :
 iiiIi = Oo000ooOOO ( OO0 )
 OooO0 = re . compile ( 'id=<(.+?)>' ) . findall ( iiiIi )
 try :
  O000 = int ( o0OO00 . getSetting ( 'id' ) )
 except :
  o0OO00 . setSetting ( 'id' , '0' )
 if int ( OooO0 [ 0 ] ) > int ( o0OO00 . getSetting ( 'id' ) ) :
  ooO0o = xbmcgui . Dialog ( )
  ooO0o . ok ( "Karaoke" , "" , 'There is a New Database Update' , 'Please Wait' )
  Ii1ii1IiIII ( )
  o0OO00 . setSetting ( 'id' , OooO0 [ 0 ] )
 IIIII1 ( '[COLOR ' + ooo + ']' + 'Video Karaoke' , 'url' , 1419 , iiI + 'Main/youtube.png' , 'none' , 1 )
 IIIII1 ( '[COLOR ' + ooo + ']' + 'Sunfly[/COLOR] Karaoke' , 'url' , 1420 , iiI + 'Main/SUNFLY.png' , 'none' , 1 )
 if 7 - 7: o00 / iiiIIii1I1Ii / i11iIiiIii
 if 21 - 21: O00oOoOoO0o0O / iiiIIii1I1Ii + o00ooo0 + OoooooooOO
 if 91 - 91: i11iIiiIii / i1IIi + o00 + i1IIi11111i * i11iIiiIii
def OoOoOo00o0 ( url ) :
 IIIII1 ( '[COLOR ' + ooo + ']' + 'Search[/COLOR]-[COLOR ' + ooo + ']' + 'Y[/COLOR]outube Karaoke' , 'url' , 1403 , iiI + 'Main/Search.png' , 'none' , 1 )
 if 90 - 90: ii1IiI1i % O0 * iIii1I11I1II1 . o00
 if 8 - 8: i1IIi11111i + OOooo000oo0 / o00 / II1i
 if 74 - 74: O0 / i1IIi
 if 78 - 78: OoooooooOO . IIIiiIIii + i1IIi11111i - i1IIi
 if 31 - 31: OoooooooOO . Iii1iIIIII
 if 83 - 83: o00 . O0 / ii1IiI1i / Iii1iIIIII - OOooo000oo0
 if 100 - 100: IIIiiIIii
 if 46 - 46: Oo / iIii1I11I1II1 % o00 . iIii1I11I1II1 * o00
 if 38 - 38: iiiIIii1I1Ii - o00 / O0 . ooo0Oo0
def i1iiIiI1Ii1i ( url ) :
 IIIII1 ( '[COLOR ' + ooo + ']' + 'Search[/COLOR]-[COLOR ' + ooo + ']' + 'X[/COLOR]unity Karaoke' , 'url' , 1416 , iiI + 'Main/Search.png' , 'none' , 1 )
 if o0OO00 . getSetting ( 'sfenable' ) == 'true' :
  IIIII1 ( '[COLOR ' + ooo + ']' + 'D[/COLOR]ownloads' , 'url' , 1431 , iiI + 'Main/favorites.png' , '' , 1 )
 IIIII1 ( '[COLOR ' + ooo + ']' + 'Search[/COLOR] By Number' , 'url' , 1425 , iiI + 'Main/Search.png' , 'none' , 1 )
 IIIII1 ( '[COLOR ' + ooo + ']' + 'Browse[/COLOR] Artist' , 'http://www.sunflykaraoke.com/' , 1401 , iiI + 'Main/Artist.png' , 'none' , 1423 )
 IIIII1 ( '[COLOR ' + ooo + ']' + 'Browse[/COLOR] Tracks' , 'http://www.sunflykaraoke.com/' , 1401 , iiI + 'Main/Title.png' , 'none' , 1424 )
 IIIII1 ( '[COLOR ' + ooo + ']' + 'G[/COLOR]enre' , 'http://www.sunflykaraoke.com/' , 1432 , iiI + 'Main/Genre.png' , 'none' , 1 )
 IIIII1 ( '[COLOR ' + ooo + ']' + 'D[/COLOR]ownload Database' , 'http://www.sunflykaraoke.com/' , 14103 , '' , 'none' , 1 )
 if 22 - 22: O0IiiiIiI1iIiI1 / i11iIiiIii
 if 62 - 62: IIIiiIIii / iiiIIii1I1Ii
def ii1 ( url ) :
 iiI11Iii = xbmc . Keyboard ( '' , '[COLOR grey3]Search by[/COLOR] [COLOR ' + ooo + ']' + 'Artist[/COLOR] [COLOR grey3]or[/COLOR] [COLOR ' + ooo + ']' + 'Track[/COLOR]' )
 iiI11Iii . doModal ( )
 if iiI11Iii . isConfirmed ( ) :
  o0o0oOoOO0O = OooO0oo ( 4 , 'artist' , iiI11Iii . getText ( ) )
  if not o0o0oOoOO0O : o0o0oOoOO0O = OooO0oo ( 4 , 'artist' , re . sub ( '\A(a|A|the|THE|The)\s' , '' , iiI11Iii . getText ( ) ) )
  if not o0o0oOoOO0O : o0o0oOoOO0O = OooO0oo ( 4 , 'track' , iiI11Iii . getText ( ) )
  if not o0o0oOoOO0O : o0o0oOoOO0O = OooO0oo ( 4 , 'track' , re . sub ( '\A(a|A|the|THE|The)\s' , '' , iiI11Iii . getText ( ) ) )
  if not o0o0oOoOO0O : I111i1II ( '[COLOR red]TRACK NOT AVAILABLE.[/COLOR]' , url , '' ) ; return
  for O000OOO0OOo , i1i1I111iIi1 , oo00O00oO000o , OOo00OoO , iIiiiI1IiI1I1 , iIi1 in o0o0oOoOO0O :
   I111i1II ( '[COLOR ' + ooo + ']' + '%s ~ [/COLOR]%s' % ( oo00O00oO000o , OOo00OoO ) , iIi1 , iIiiiI1IiI1I1 )
   if 21 - 21: II1i
def OoO00 ( url , number , fanart ) :
 if 'lyrics' in url :
  IIIII1 ( '0-9' , url % 'num' , number , "%s/KaraokeArt/AtoZ/0-9.png" % o0OO00 . getAddonInfo ( "path" ) , fanart , 1401 )
  setView ( 'movies' , 'A-Z' )
 if '%s' in url :
  for oo0oooooO0 in string . ascii_uppercase :
   IIIII1 ( oo0oooooO0 , url % oo0oooooO0 , number , "%s/KaraokeArt/AtoZ/%s.png" % ( o0OO00 . getAddonInfo ( "path" ) , oo0oooooO0 ) , fanart , 1401 )
   setView ( 'movies' , 'A-Z' )
 else :
  for oo0oooooO0 in string . ascii_uppercase :
   IIIII1 ( oo0oooooO0 , url , number , "%s/KaraokeArt/AtoZ/%s.png" % ( o0OO00 . getAddonInfo ( "path" ) , oo0oooooO0 ) , fanart , 1401 )
   if 85 - 85: ii1IiI1i * ii1IiI1i * i1 . OoooooooOO . o00ooo0 * i1IIi11111i
   if 65 - 65: Iii1iIIIII * ooo0Oo0
   if 79 - 79: OoooooooOO - i1
   if 69 - 69: II1i
def O00oO0 ( name ) :
 o0o0oOoOO0O = OooO0oo ( 5 , 'artist' , name )
 if not o0o0oOoOO0O : I111i1II ( '[COLOR red]ARTIST NOT AVAILABLE.[/COLOR]' , iII1i1 , '' ) ; return
 for O000OOO0OOo , i1i1I111iIi1 , oo00O00oO000o , OOo00OoO , iIiiiI1IiI1I1 , iIi1 in o0o0oOoOO0O :
  I111i1II ( '[COLOR ' + ooo + ']' + '%s ~ [/COLOR]%s' % ( oo00O00oO000o , OOo00OoO ) , iIi1 , iIiiiI1IiI1I1 , split = 1 )
  if 97 - 97: ooo0Oo0 - iIii1I11I1II1
def oo0o0O0Oooooo ( url ) :
 i11IIIiI1I = 'SF'
 iiI11Iii = xbmc . Keyboard ( i11IIIiI1I , 'Enter Sunfly Disc Number:-' )
 iiI11Iii . doModal ( )
 if iiI11Iii . isConfirmed ( ) :
  o0o0oOoOO0O = OooO0oo ( 4 , 'sunfly_name' , iiI11Iii . getText ( ) )
  if not o0o0oOoOO0O : I111i1II ( '[COLOR red]DISC NOT AVAILABLE.[/COLOR]' , url , '' ) ; return
  for O000OOO0OOo , i1i1I111iIi1 , oo00O00oO000o , OOo00OoO , iIiiiI1IiI1I1 , iIi1 in o0o0oOoOO0O :
   I111i1II ( '[COLOR ' + ooo + ']' + '%s:-%s ~ [/COLOR]%s' % ( O000OOO0OOo , i1i1I111iIi1 , OOo00OoO ) , iIi1 , iIiiiI1IiI1I1 , split = 1 )
   if 69 - 69: O0
   if 85 - 85: i1IIi11111i / O0
def iI1iIIIi1i ( name ) :
 o0o0oOoOO0O = OooO0oo ( 5 , 'track' , re . sub ( '\A(a|A|the|THE|The)\s' , '' , name ) )
 if not o0o0oOoOO0O : I111i1II ( '[COLOR red]TRACK NOT AVAILABLE.[/COLOR]' , iII1i1 , '' ) ; return
 for O000OOO0OOo , i1i1I111iIi1 , oo00O00oO000o , OOo00OoO , iIiiiI1IiI1I1 , iIi1 in o0o0oOoOO0O :
  I111i1II ( '[COLOR ' + ooo + ']' + '%s ~ [/COLOR]%s' % ( OOo00OoO , oo00O00oO000o ) , iIi1 , iIiiiI1IiI1I1 , split = 0 )
  if 89 - 89: iIii1I11I1II1
def i11iiiiI1i ( url ) :
 IIIII1 ( '40s/50s' , oOIIiIi + '40-s-and-50-s-pop3429190/' + OOoOooOoOOOoo , 1410 , iiI + 'Genre/4050POP.png' , iiI + 'Main/Fanart_G.jpg' , 1 )
 IIIII1 ( '60s' , oOIIiIi + '60-s-pop/karaoke-tracks,albums,artists/3429191/' + OOoOooOoOOOoo , 1410 , iiI + 'Genre/60POP.png' , iiI + 'Main/Fanart_G.jpg' , 1 )
 IIIII1 ( '70s' , oOIIiIi + '70-s-pop/karaoke-tracks,albums,artists/3429192/' + OOoOooOoOOOoo , 1410 , iiI + 'Genre/70POP.png' , iiI + 'Main/Fanart_G.jpg' , 1 )
 IIIII1 ( '80s' , oOIIiIi + '80-s-pop/karaoke-tracks,albums,artists/3429193/' + OOoOooOoOOOoo , 1410 , iiI + 'Genre/80POP.png' , iiI + 'Main/Fanart_G.jpg' , 1 )
 IIIII1 ( '90s' , oOIIiIi + '90-s-pop/karaoke-tracks,albums,artists/3429194/' + OOoOooOoOOOoo , 1410 , iiI + 'Genre/90POP.png' , iiI + 'Main/Fanart_G.jpg' , 1 )
 IIIII1 ( '2000s' , oOIIiIi + '00-s-pop/karaoke-tracks,albums,artists/3429189/' + OOoOooOoOOOoo , 1410 , iiI + 'Genre/2000sPOP.png' , iiI + 'Main/Fanart_G.jpg' , 1 )
 IIIII1 ( '2010s' , oOIIiIi + '10-s-pop/karaoke-tracks,albums,artists/3429195/' + OOoOooOoOOOoo , 1410 , iiI + 'Genre/2010sPOP.png' , iiI + 'Main/Fanart_G.jpg' , 1 )
 IIIII1 ( 'Boybands' , oOIIiIi + 'boybands/karaoke-tracks,albums,artists/3429196/' + OOoOooOoOOOoo , 1410 , iiI + 'Genre/Boybands.png' , iiI + 'Main/Fanart_G.jpg' , 1 )
 IIIII1 ( 'R&B' , oOIIiIi + 'r-n-b/karaoke-tracks,albums,artists/3429220/' + OOoOooOoOOOoo , 1410 , iiI + 'Genre/RnB.png' , iiI + 'Main/Fanart_G.jpg' , 1 )
 IIIII1 ( 'Brit Pop' , oOIIiIi + 'brit-pop/karaoke-tracks,albums,artists/3429229/' + OOoOooOoOOOoo , 1410 , iiI + 'Genre/Britpop.png' , iiI + 'Main/Fanart_G.jpg' , 1 )
 IIIII1 ( 'Broadway' , oOIIiIi + 'broadway/karaoke-tracks,albums,artists/3429197/' + OOoOooOoOOOoo , 1410 , iiI + 'Genre/Broadway.png' , iiI + 'Main/Fanart_G.jpg' , 1 )
 IIIII1 ( 'Elvis' , oOIIiIi + 'elvis/karaoke-tracks,albums,artists/3429204/' + OOoOooOoOOOoo , 1410 , iiI + 'Genre/Elvis.png' , iiI + 'Main/Fanart_G.jpg' , 1 )
 IIIII1 ( 'Childrens' , oOIIiIi + 'children-s/karaoke-tracks,albums,artists/3429198/' + OOoOooOoOOOoo , 1410 , iiI + 'Genre/Childrens.png' , iiI + 'Main/Fanart_G.jpg' , 1 )
 IIIII1 ( 'Christmas' , oOIIiIi + 'christmas/karaoke-tracks,albums,artists/3429199/' + OOoOooOoOOOoo , 1410 , iiI + 'Genre/Christmas.png' , iiI + 'Main/Fanart_G.jpg' , 1 )
 IIIII1 ( 'Comedy' , oOIIiIi + 'comedy/karaoke-tracks,albums,artists/3429200/' + OOoOooOoOOOoo , 1410 , iiI + 'Genre/Comedy.png' , iiI + 'Main/Fanart_G.jpg' , 1 )
 IIIII1 ( 'Country' , oOIIiIi + 'country/karaoke-tracks,albums,artists/3429201/' + OOoOooOoOOOoo , 1410 , iiI + 'Genre/Country.png' , iiI + 'Main/Fanart_G.jpg' , 1 )
 IIIII1 ( 'Dance' , oOIIiIi + 'dance/karaoke-tracks,albums,artists/3429202/' + OOoOooOoOOOoo , 1410 , iiI + 'Genre/Dance.png' , iiI + 'Main/Fanart_G.jpg' , 1 )
 IIIII1 ( 'Duets' , oOIIiIi + 'duets/karaoke-tracks,albums,artists/3429203/' + OOoOooOoOOOoo , 1410 , iiI + 'Genre/Duets.png' , iiI + 'Main/Fanart_G.jpg' , 1 )
 IIIII1 ( 'Male Superstars' , oOIIiIi + 'male-superstars/karaoke-tracks,albums,artists/3429213/' + OOoOooOoOOOoo , 1410 , iiI + 'Genre/Male.png' , iiI + 'Main/Fanart_G.jpg' , 1 )
 IIIII1 ( 'Female Superstars' , oOIIiIi + 'female-superstars/karaoke-tracks,albums,artists/3429205/' + OOoOooOoOOOoo , 1410 , iiI + 'Genre/Female.png' , iiI + 'Main/Fanart_G.jpg' , 1 )
 IIIII1 ( 'Folk' , oOIIiIi + 'folk/karaoke-tracks,albums,artists/3429230/' + OOoOooOoOOOoo , 1410 , iiI + 'Genre/Folk.png' , iiI + 'Main/Fanart_G.jpg' , 1 )
 IIIII1 ( 'Football Anthems' , oOIIiIi + 'football-anthems/karaoke-tracks,albums,artists/3429228/' + OOoOooOoOOOoo , 1410 , iiI + 'Genre/Football.png' , iiI + 'Main/Fanart_G.jpg' , 1 )
 IIIII1 ( 'Foreign' , oOIIiIi + 'foreign/karaoke-tracks,albums,artists/3429206/' + OOoOooOoOOOoo , 1410 , iiI + 'Genre/Foreign.png' , iiI + 'Main/Fanart_G.jpg' , 1 )
 IIIII1 ( 'Funk' , oOIIiIi + 'funk/karaoke-tracks,albums,artists/3429231/' + OOoOooOoOOOoo , 1410 , iiI + 'Genre/Funk.png' , iiI + 'Main/Fanart_G.jpg' , 1 )
 IIIII1 ( 'Girlbands' , oOIIiIi + 'girlbands/karaoke-tracks,albums,artists/3429207/' + OOoOooOoOOOoo , 1410 , iiI + 'Genre/Girlbands.png' , iiI + 'Main/Fanart_G.jpg' , 1 )
 IIIII1 ( 'Glee' , oOIIiIi + 'glee/karaoke-tracks,albums,artists/14196105/' + OOoOooOoOOOoo , 1410 , iiI + 'Genre/GAYCUNTS.png' , iiI + 'Main/Fanart_G.jpg' , 1 )
 IIIII1 ( 'Grunge' , oOIIiIi + 'grunge-post-grunge/karaoke-tracks,albums,artists/18813424/' + OOoOooOoOOOoo , 1410 , iiI + 'Genre/Grunge.png' , iiI + 'Main/Fanart_G.jpg' , 1 )
 IIIII1 ( 'Halloween' , oOIIiIi + 'halloween/karaoke-tracks,albums,artists/3429208/' + OOoOooOoOOOoo , 1410 , iiI + 'Genre/Halloween.png' , iiI + 'Main/Fanart_G.jpg' , 1 )
 IIIII1 ( 'Heavy Metal' , oOIIiIi + 'heavy-metal-alt-metal/karaoke-tracks,albums,artists/3429209/' + OOoOooOoOOOoo , 1410 , iiI + 'Genre/Metal.png' , iiI + 'Main/Fanart_G.jpg' , 1 )
 IIIII1 ( 'Jazz/Blues' , oOIIiIi + 'jazz-blues/karaoke-tracks,albums,artists/3429212/' + OOoOooOoOOOoo , 1410 , iiI + 'Genre/JazzBlues.png' , iiI + 'Main/Fanart_G.jpg' , 1 )
 IIIII1 ( 'Indie' , oOIIiIi + 'indie/karaoke-tracks,albums,artists/3429210/' + OOoOooOoOOOoo , 1410 , iiI + 'Genre/Indie.png' , iiI + 'Main/Fanart_G.jpg' , 1 )
 IIIII1 ( 'Irish' , oOIIiIi + 'irish/karaoke-tracks,albums,artists/3429211/' + OOoOooOoOOOoo , 1410 , iiI + 'Genre/Irish.png' , iiI + 'Main/Fanart_G.jpg' , 1 )
 IIIII1 ( 'Medleys' , oOIIiIi + 'medley-s/karaoke-tracks,albums,artists/3429214/' + OOoOooOoOOOoo , 1410 , iiI + 'Genre/Medleys.png' , iiI + 'Main/Fanart_G.jpg' , 1 )
 IIIII1 ( 'Movies & TV' , oOIIiIi + 'movie-s-and-tv/karaoke-tracks,albums,artists/3429215/' + OOoOooOoOOOoo , 1410 , iiI + 'Genre/Movies.png' , iiI + 'Main/Fanart_G.jpg' , 1 )
 IIIII1 ( 'Multiplex' , oOIIiIi + 'multiplex/karaoke-tracks,albums,artists/3429216/' + OOoOooOoOOOoo , 1410 , iiI + 'Genre/Multiplex.png' , iiI + 'Main/Fanart_G.jpg' , 1 )
 IIIII1 ( 'Punk Rock' , oOIIiIi + 'punk-rock/karaoke-tracks,albums,artists/3429217/' + OOoOooOoOOOoo , 1410 , iiI + 'Genre/PunkRock.png' , iiI + 'Main/Fanart_G.jpg' , 1 )
 IIIII1 ( 'Rap/Hip-Hop' , oOIIiIi + 'rap-hip-hop/karaoke-tracks,albums,artists/3429218/' + OOoOooOoOOOoo , 1410 , iiI + 'Genre/HipHop.png' , iiI + 'Main/Fanart_G.jpg' , 1 )
 IIIII1 ( 'Reggae' , oOIIiIi + 'reggae/karaoke-tracks,albums,artists/3429219/' + OOoOooOoOOOoo , 1410 , iiI + 'Genre/Reggae.png' , iiI + 'Main/Fanart_G.jpg' , 1 )
 IIIII1 ( 'Religious/Gospel' , oOIIiIi + 'religious-gospel/karaoke-tracks,albums,artists/3429227/' + OOoOooOoOOOoo , 1410 , iiI + 'Genre/GODFREAKS.png' , iiI + 'Main/Fanart_G.jpg' , 1 )
 IIIII1 ( 'Rock' , oOIIiIi + 'rock/karaoke-tracks,albums,artists/3429221/' + OOoOooOoOOOoo , 1410 , iiI + 'Genre/Rock.png' , iiI + 'Main/Fanart_G.jpg' , 1 )
 IIIII1 ( 'Rock & Roll/Disco' , oOIIiIi + 'rock-and-roll-disco/karaoke-tracks,albums,artists/3429222/' + OOoOooOoOOOoo , 1410 , iiI + 'Genre/RnR.png' , iiI + 'Main/Fanart_G.jpg' , 1 )
 IIIII1 ( 'Sea Shanties' , oOIIiIi + 'sea-shanties/karaoke-tracks,albums,artists/30174405/' + OOoOooOoOOOoo , 1410 , iiI + 'Genre/Shanties.png' , iiI + 'Main/Fanart_G.jpg' , 1 )
 IIIII1 ( 'Sing A Long' , oOIIiIi + 'sing-a-long/karaoke-tracks,albums,artists/3429223/' + OOoOooOoOOOoo , 1410 , iiI + 'Genre/Sing.png' , iiI + 'Main/Fanart_G.jpg' , 1 )
 IIIII1 ( 'Skate/Soft Rock' , oOIIiIi + 'skate-soft-rock/karaoke-tracks,albums,artists/3429224/' + OOoOooOoOOOoo , 1410 , iiI + 'Genre/Skate.png' , iiI + 'Main/Fanart_G.jpg' , 1 )
 IIIII1 ( 'Soul/Motown' , oOIIiIi + 'soul-motown/karaoke-tracks,albums,artists/3429225/' + OOoOooOoOOOoo , 1410 , iiI + 'Genre/Soul.png' , iiI + 'Main/Fanart_G.jpg' , 1 )
 IIIII1 ( 'Swing/Standards' , oOIIiIi + 'swing-standards/karaoke-tracks,albums,artists/3429226/' + OOoOooOoOOOoo , 1410 , iiI + 'Genre/Swing.png' , iiI + 'Main/Fanart_G.jpg' , 1 )
 if 37 - 37: Iii1iIIIII / OoooooooOO - i11iIiiIii
 if 18 - 18: o00 . i1
def iiIi1IIiI ( url ) :
 IIIII1 ( '40s/50s' , oOIIiIi + '40-s-and-50-s-pop/karaoke-tracks,albums,artists/3429190/' + OOoOooOoOOOoo , 1433 , iiI + 'Genre/4050POP.png' , iiI + 'Main/Fanart_G.jpg' , 1 )
 IIIII1 ( '60s' , oOIIiIi + '60-s-pop/karaoke-tracks,albums,artists/3429191/' + OOoOooOoOOOoo , 1433 , iiI + 'Genre/60POP.png' , iiI + 'Main/Fanart_G.jpg' , 1 )
 IIIII1 ( '70s' , oOIIiIi + '70-s-pop/karaoke-tracks,albums,artists/3429192/' + OOoOooOoOOOoo , 1433 , iiI + 'Genre/70POP.png' , iiI + 'Main/Fanart_G.jpg' , 1 )
 IIIII1 ( '80s' , oOIIiIi + '80-s-pop/karaoke-tracks,albums,artists/3429193/' + OOoOooOoOOOoo , 1433 , iiI + 'Genre/80POP.png' , iiI + 'Main/Fanart_G.jpg' , 1 )
 IIIII1 ( '90s' , oOIIiIi + '90-s-pop/karaoke-tracks,albums,artists/3429194/' + OOoOooOoOOOoo , 1433 , iiI + 'Genre/90POP.png' , iiI + 'Main/Fanart_G.jpg' , 1 )
 IIIII1 ( '2000s' , oOIIiIi + '00-s-pop/karaoke-tracks,albums,artists/3429189/' + OOoOooOoOOOoo , 1433 , iiI + 'Genre/2000sPOP.png' , iiI + 'Main/Fanart_G.jpg' , 1 )
 IIIII1 ( '2010s' , oOIIiIi + '10-s-pop/karaoke-tracks,albums,artists/3429195/' + OOoOooOoOOOoo , 1433 , iiI + 'Genre/2010sPOP.png' , iiI + 'Main/Fanart_G.jpg' , 1 )
 IIIII1 ( 'Boybands' , oOIIiIi + 'boybands/karaoke-tracks,albums,artists/3429196/' + OOoOooOoOOOoo , 1433 , iiI + 'Genre/Boybands.png' , iiI + 'Main/Fanart_G.jpg' , 1 )
 IIIII1 ( 'R&B' , oOIIiIi + 'r-n-b/karaoke-tracks,albums,artists/3429220/' + OOoOooOoOOOoo , 1433 , iiI + 'Genre/RnB.png' , iiI + 'Main/Fanart_G.jpg' , 1 )
 IIIII1 ( 'Brit Pop' , oOIIiIi + 'brit-pop/karaoke-tracks,albums,artists/3429229/' + OOoOooOoOOOoo , 1433 , iiI + 'Genre/Britpop.png' , iiI + 'Main/Fanart_G.jpg' , 1 )
 IIIII1 ( 'Broadway' , oOIIiIi + 'broadway/karaoke-tracks,albums,artists/3429197/' + OOoOooOoOOOoo , 1433 , iiI + 'Genre/Broadway.png' , iiI + 'Main/Fanart_G.jpg' , 1 )
 IIIII1 ( 'Elvis' , oOIIiIi + 'elvis/karaoke-tracks,albums,artists/3429204/' + OOoOooOoOOOoo , 1433 , iiI + 'Genre/Elvis.png' , iiI + 'Main/Fanart_G.jpg' , 1 )
 IIIII1 ( 'Childrens' , oOIIiIi + 'children-s/karaoke-tracks,albums,artists/3429198/' + OOoOooOoOOOoo , 1433 , iiI + 'Genre/Childrens.png' , iiI + 'Main/Fanart_G.jpg' , 1 )
 IIIII1 ( 'Christmas' , oOIIiIi + 'christmas/karaoke-tracks,albums,artists/3429199/' + OOoOooOoOOOoo , 1433 , iiI + 'Genre/Christmas.png' , iiI + 'Main/Fanart_G.jpg' , 1 )
 IIIII1 ( 'Comedy' , oOIIiIi + 'comedy/karaoke-tracks,albums,artists/3429200/' + OOoOooOoOOOoo , 1433 , iiI + 'Genre/Comedy.png' , iiI + 'Main/Fanart_G.jpg' , 1 )
 IIIII1 ( 'Country' , oOIIiIi + 'country/karaoke-tracks,albums,artists/3429201/' + OOoOooOoOOOoo , 1433 , iiI + 'Genre/Country.png' , iiI + 'Main/Fanart_G.jpg' , 1 )
 IIIII1 ( 'Dance' , oOIIiIi + 'dance/karaoke-tracks,albums,artists/3429202/' + OOoOooOoOOOoo , 1433 , iiI + 'Genre/Dance.png' , iiI + 'Main/Fanart_G.jpg' , 1 )
 IIIII1 ( 'Duets' , oOIIiIi + 'duets/karaoke-tracks,albums,artists/3429203/' + OOoOooOoOOOoo , 1433 , iiI + 'Genre/Duets.png' , iiI + 'Main/Fanart_G.jpg' , 1 )
 IIIII1 ( 'Male Superstars' , oOIIiIi + 'male-superstars/karaoke-tracks,albums,artists/3429213/' + OOoOooOoOOOoo , 1433 , iiI + 'Genre/Male.png' , iiI + 'Main/Fanart_G.jpg' , 1 )
 IIIII1 ( 'Female Superstars' , oOIIiIi + 'female-superstars/karaoke-tracks,albums,artists/3429205/' + OOoOooOoOOOoo , 1433 , iiI + 'Genre/Female.png' , iiI + 'Main/Fanart_G.jpg' , 1 )
 IIIII1 ( 'Folk' , oOIIiIi + 'folk/karaoke-tracks,albums,artists/3429230/' + OOoOooOoOOOoo , 1433 , iiI + 'Genre/Folk.png' , iiI + 'Main/Fanart_G.jpg' , 1 )
 IIIII1 ( 'Football Anthems' , oOIIiIi + 'football-anthems/karaoke-tracks,albums,artists/3429228/' + OOoOooOoOOOoo , 1433 , iiI + 'Genre/Football.png' , iiI + 'Main/Fanart_G.jpg' , 1 )
 IIIII1 ( 'Foreign' , oOIIiIi + 'foreign/karaoke-tracks,albums,artists/3429206/' + OOoOooOoOOOoo , 1433 , iiI + 'Genre/Foreign.png' , iiI + 'Main/Fanart_G.jpg' , 1 )
 IIIII1 ( 'Funk' , oOIIiIi + 'funk/karaoke-tracks,albums,artists/3429231/' + OOoOooOoOOOoo , 1433 , iiI + 'Genre/Funk.png' , iiI + 'Main/Fanart_G.jpg' , 1 )
 IIIII1 ( 'Girlbands' , oOIIiIi + 'girlbands/karaoke-tracks,albums,artists/3429207/' + OOoOooOoOOOoo , 1433 , iiI + 'Genre/Girlbands.png' , iiI + 'Main/Fanart_G.jpg' , 1 )
 IIIII1 ( 'Glee' , oOIIiIi + 'glee/karaoke-tracks,albums,artists/14196105/' + OOoOooOoOOOoo , 1433 , iiI + 'Genre/GAYCUNTS.png' , iiI + 'Main/Fanart_G.jpg' , 1 )
 IIIII1 ( 'Grunge' , oOIIiIi + 'grunge-post-grunge/karaoke-tracks,albums,artists/18813424/' + OOoOooOoOOOoo , 1433 , iiI + 'Genre/Grunge.png' , iiI + 'Main/Fanart_G.jpg' , 1 )
 IIIII1 ( 'Halloween' , oOIIiIi + 'halloween/karaoke-tracks,albums,artists/3429208/' + OOoOooOoOOOoo , 1433 , iiI + 'Genre/Halloween.png' , iiI + 'Main/Fanart_G.jpg' , 1 )
 IIIII1 ( 'Heavy Metal' , oOIIiIi + 'heavy-metal-alt-metal/karaoke-tracks,albums,artists/3429209/' + OOoOooOoOOOoo , 1433 , iiI + 'Genre/Metal.png' , iiI + 'Main/Fanart_G.jpg' , 1 )
 IIIII1 ( 'Jazz/Blues' , oOIIiIi + 'jazz-blues/karaoke-tracks,albums,artists/3429212/' + OOoOooOoOOOoo , 1433 , iiI + 'Genre/JazzBlues.png' , iiI + 'Main/Fanart_G.jpg' , 1 )
 IIIII1 ( 'Indie' , oOIIiIi + 'indie/karaoke-tracks,albums,artists/3429210/' + OOoOooOoOOOoo , 1433 , iiI + 'Genre/Indie.png' , iiI + 'Main/Fanart_G.jpg' , 1 )
 IIIII1 ( 'Irish' , oOIIiIi + 'irish/karaoke-tracks,albums,artists/3429211/' + OOoOooOoOOOoo , 1433 , iiI + 'Genre/Irish.png' , iiI + 'Main/Fanart_G.jpg' , 1 )
 IIIII1 ( 'Medleys' , oOIIiIi + 'medley-s/karaoke-tracks,albums,artists/3429214/' + OOoOooOoOOOoo , 1433 , iiI + 'Genre/Medleys.png' , iiI + 'Main/Fanart_G.jpg' , 1 )
 IIIII1 ( 'Movies & TV' , oOIIiIi + 'movie-s-and-tv/karaoke-tracks,albums,artists/3429215/' + OOoOooOoOOOoo , 1433 , iiI + 'Genre/Movies.png' , iiI + 'Main/Fanart_G.jpg' , 1 )
 IIIII1 ( 'Multiplex' , oOIIiIi + 'multiplex/karaoke-tracks,albums,artists/3429216/' + OOoOooOoOOOoo , 1433 , iiI + 'Genre/Multiplex.png' , iiI + 'Main/Fanart_G.jpg' , 1 )
 IIIII1 ( 'Punk Rock' , oOIIiIi + 'punk-rock/karaoke-tracks,albums,artists/3429217/' + OOoOooOoOOOoo , 1433 , iiI + 'Genre/PunkRock.png' , iiI + 'Main/Fanart_G.jpg' , 1 )
 IIIII1 ( 'Rap/Hip-Hop' , oOIIiIi + 'rap-hip-hop/karaoke-tracks,albums,artists/3429218/' + OOoOooOoOOOoo , 1433 , iiI + 'Genre/HipHop.png' , iiI + 'Main/Fanart_G.jpg' , 1 )
 IIIII1 ( 'Reggae' , oOIIiIi + 'reggae/karaoke-tracks,albums,artists/3429219/' + OOoOooOoOOOoo , 1433 , iiI + 'Genre/Reggae.png' , iiI + 'Main/Fanart_G.jpg' , 1 )
 IIIII1 ( 'Religious/Gospel' , oOIIiIi + 'religious-gospel/karaoke-tracks,albums,artists/3429227/' + OOoOooOoOOOoo , 1433 , iiI + 'Genre/GODFREAKS.png' , iiI + 'Main/Fanart_G.jpg' , 1 )
 IIIII1 ( 'Rock' , oOIIiIi + 'rock/karaoke-tracks,albums,artists/3429221/' + OOoOooOoOOOoo , 1433 , iiI + 'Genre/Rock.png' , iiI + 'Main/Fanart_G.jpg' , 1 )
 IIIII1 ( 'Rock & Roll/Disco' , oOIIiIi + 'rock-and-roll-disco/karaoke-tracks,albums,artists/3429222/' + OOoOooOoOOOoo , 1433 , iiI + 'Genre/RnR.png' , iiI + 'Main/Fanart_G.jpg' , 1 )
 IIIII1 ( 'Sea Shanties' , oOIIiIi + 'sea-shanties/karaoke-tracks,albums,artists/30174405/' + OOoOooOoOOOoo , 1433 , iiI + 'Genre/Shanties.png' , iiI + 'Main/Fanart_G.jpg' , 1 )
 IIIII1 ( 'Sing A Long' , oOIIiIi + 'sing-a-long/karaoke-tracks,albums,artists/3429223/' + OOoOooOoOOOoo , 1433 , iiI + 'Genre/Sing.png' , iiI + 'Main/Fanart_G.jpg' , 1 )
 IIIII1 ( 'Skate/Soft Rock' , oOIIiIi + 'skate-soft-rock/karaoke-tracks,albums,artists/3429224/' + OOoOooOoOOOoo , 1433 , iiI + 'Genre/Skate.png' , iiI + 'Main/Fanart_G.jpg' , 1 )
 IIIII1 ( 'Soul/Motown' , oOIIiIi + 'soul-motown/karaoke-tracks,albums,artists/3429225/' + OOoOooOoOOOoo , 1433 , iiI + 'Genre/Soul.png' , iiI + 'Main/Fanart_G.jpg' , 1 )
 IIIII1 ( 'Swing/Standards' , oOIIiIi + 'swing-standards/karaoke-tracks,albums,artists/3429226/' + OOoOooOoOOOoo , 1433 , iiI + 'Genre/Swing.png' , iiI + 'Main/Fanart_G.jpg' , 1 )
 if 23 - 23: o00ooo0 . Iii1iIIIII
def i1II11II ( name , url , iconimage ) :
 iiiIi = Oo000ooOOO ( url . replace ( ' ' , '%20' ) )
 OooO0 = re . compile ( 'target="_self">(.+?)</a></td><td class="listing-col-artist"><a href=".+?" target="_self">(.+?)</a>' ) . findall ( iiiIi )
 oOo00O000Oo0 = I1iI1I1I1i11i ( iiiIi ) [ 0 ]
 for name , url , in OooO0 :
  name = str ( name ) . replace ( "&#39;" , "'" ) . replace ( "&amp;" , "and" ) . replace ( "&#252;" , "u" ) . replace ( "&quot;" , "" )
  url = str ( url ) . replace ( "&#39;" , "'" ) . replace ( "&amp;" , "and" ) . replace ( "&#252;" , "u" ) . replace ( "&quot;" , "" )
  name = name + '   (' + url + ')'
  IIIII1 ( name , url , 9 , iconimage , iiI + 'Main/Fanart_G.jpg' , 1 )
  if 39 - 39: OOooo000oo0 / O0IiiiIiI1iIiI1 + o00ooo0
 try :
  url = 'http://www.sunflykaraoke.com' + str ( oOo00O000Oo0 )
  name = '[COLOR ' + ooo + ']' + '[B]Next Page >>[/B][/COLOR]'
  IIIII1 ( name , url , 7 , iiI + 'next.png' , 'none' , 1 )
  if 63 - 63: IIIiiIIii + iiiIIii1I1Ii . ooo0Oo0 % ooo0Oo0
 except :
  pass
  if 57 - 57: OOooo000oo0
  if 54 - 54: ii1IiI1i + O00oOoOoO0o0O + i11iIiiIii
def i1i1ii111 ( name , url , iconimage ) :
 iiiIi = Oo000ooOOO ( url . replace ( ' ' , '%20' ) )
 oOo00O000Oo0 = I1iI1I1I1i11i ( iiiIi ) [ 0 ]
 OooO0 = re . compile ( 'target="_self">(.+?)</a></td><td class="listing-col-artist"><a href=".+?" target="_self">(.+?)</a>' ) . findall ( iiiIi )
 for name , url , in OooO0 :
  IiI1i = re . sub ( '[\(\)\{\}<>]' , '' , name . replace ( "&#39;" , "'" ) . replace ( "&amp;" , "and" ) . replace ( "&#252;" , "u" ) . replace ( "&quot;" , "" ) . replace ( "&quot;" , "" ) )
  name = re . sub ( '[\(\)\{\}<>]' , '' , name . replace ( "&#39;" , "'" ) . replace ( "&amp;" , "and" ) . replace ( "&#252;" , "u" ) . replace ( "&quot;" , "" ) . replace ( "&quot;" , "" ) . replace ( "'" , "" ) )
  url = str ( url ) . replace ( "&#39;" , "'" ) . replace ( "&amp;" , "and" ) . replace ( "&#252;" , "u" ) . replace ( "&quot;" , "" )
  IIIII1 ( '[COLOR ' + ooo + ']' + '%s[/COLOR] - %s' % ( IiI1i , url ) , name , 34 , iconimage , iiI + 'Main/Fanart_G.jpg' , 1 )
  if 87 - 87: i1IIi11111i
 try :
  url = 'http://www.sunflykaraoke.com' + str ( oOo00O000Oo0 )
  name = '[COLOR ' + ooo + ']' + '[B]Next Page >>[/B][/COLOR]'
  IIIII1 ( name , url , 33 , iiI + 'next.png' , 'none' , 1 )
  if 45 - 45: IIIiiIIii / OoooooooOO - o00 / o00ooo0 % O0IiiiIiI1iIiI1
 except :
  pass
  if 83 - 83: i1 . iIii1I11I1II1 - O0IiiiIiI1iIiI1 * i11iIiiIii
def I1iI1I1I1i11i ( link ) :
 link = link . split ( 'class="paging-bar-pages">' ) [ 1 ]
 link = link . split ( '<a href=' )
 for IiI11i1IIiiI in link :
  OooO0 = re . compile ( '"(.+?)#.+?" class="arrow">&gt;</a>' ) . findall ( IiI11i1IIiiI )
  if OooO0 :
   return OooO0
 return None
 if 60 - 60: iiiIIii1I1Ii * i1
 if 17 - 17: Iii1iIIIII % ii1IiI1i / iiiIIii1I1Ii . O0IiiiIiI1iIiI1 * Iii1iIIIII - OOooo000oo0
 if 41 - 41: o00ooo0
def oOOoo0o0OOOO ( name , url , mode , iconimage , page ) :
 if 26 - 26: o00 % iIii1I11I1II1 + iII11iiIII111
 iIIIiIi = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&page=" + str ( page )
 OO0O0 = True
 I11I11 = xbmcgui . ListItem ( name , iconImage = iconimage , thumbnailImage = iconimage )
 I11I11 . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 I11I11 . setProperty ( "fanart_image" , o0OoOoOO00 )
 OO0O0 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = iIIIiIi , listitem = I11I11 , isFolder = True )
 return OO0O0
 if 67 - 67: O00oOoOoO0o0O + OOooo000oo0 - O0 . O00oOoOoO0o0O * OOooo000oo0 * II1i
def o00OO00O0oOO ( ) :
 iiiIi = oo0Ooo0 ( __movies_url__ + '/movies/getYoutube/1' )
 OooO0 = re . compile ( '<div class="id">(.*?)</div>' ) . findall ( iiiIi )
 OoO0O0 = re . compile ( '<div class="data">(.*?)</div>' ) . findall ( iiiIi )
 II1i1IiiIIi11 = re . compile ( '<div class="data1">(.*?)</div>' ) . findall ( iiiIi )
 id = OooO0 [ 0 ] . split ( "@*" )
 Oo0O0O0ooO0O = OoO0O0 [ 0 ] . split ( "@*" )
 IIIIii = II1i1IiiIIi11 [ 0 ] . split ( "@*" )
 for OOoOO00OOO0OO in range ( 0 , len ( id ) ) :
  oOOoo0o0OOOO ( Oo0O0O0ooO0O [ OOoOO00OOO0OO ] , IIIIii [ OOoOO00OOO0OO ] , 667 , iIiiiI1IiI1I1 , 1 )
  if 4 - 4: OoooooooOO - i1IIi % o00ooo0 - Iii1iIIIII * iII11iiIII111
  if 85 - 85: OoooooooOO * iIii1I11I1II1 . o00 / OoooooooOO % i1 % O0
def I1iii ( urlparam , page ) :
 if page == 1 :
  oO0o0O0Ooo0o = 'https://www.youtube.com/results?search_query=%s' % ( urlparam . replace ( ' ' , '+' ) )
 else :
  oO0o0O0Ooo0o = 'https://www.youtube.com/results?search_query=' + urlparam . replace ( ' ' , '+' ) + '&page=' + str ( page )
 II1I11i = oo0Ooo0 ( oO0o0O0Ooo0o )
 iIi1i = re . compile ( '<h3 class[^>]*>(.*?)</h3>' ) . findall ( II1I11i )
 for I1i11111i1i11 in iIi1i :
  OOoOOO0 = re . compile ( '<a href="(.*?)"[^>]*>(.*?)</a>' ) . findall ( I1i11111i1i11 )
  if len ( OOoOOO0 ) > 0 :
   iII1i1 = OOoOOO0 [ 0 ] [ 0 ]
   OOO00 = OOoOOO0 [ 0 ] [ 1 ]
   I1I1i = 'http://i.ytimg.com/vi/%s/0.jpg' % iII1i1
   I1IIIiIiIi ( OOO00 , iII1i1 . replace ( '/watch?v=' , '' ) , I1I1i , '' )
 oOOoo0o0OOOO ( "Next >>" , urlparam , 667 , iIiiiI1IiI1I1 , page + 1 )
 if 21 - 21: ooo0Oo0 - i1 + II1i
 if 78 - 78: OoooooooOO - i11iIiiIii - OOooo000oo0
 if 77 - 77: Oo % o00ooo0
II1IiiIii = None
iII1i1 = None
OOO00 = None
II11iiii1Ii = None
Oo0O0OOOoo = None
I1I1i = None
oOo0OoOOo0 = o0OoOoOO00
iII11I1Ii1 = None
o0o0oOo0oO = None
iiiIi = None
IIi1IIIIi = None
OOOoO = None
I1i = None
i11iiII = None
if 12 - 12: OoooooooOO
if 20 - 20: i1IIi - II1i
ii1ii11 = None
OOOoO = None
OoO = None
if 73 - 73: OOooo000oo0
if 24 - 24: Oo / OoooooooOO . OOooo000oo0 . i1 % O0 % o00ooo0
i1i1I111iIi1 = None
if 5 - 5: OoooooooOO - IIIiiIIii + O0IiiiIiI1iIiI1 - o00 . IIIiiIIii / i1IIi11111i
if 28 - 28: o00ooo0 * o00ooo0 - iIii1I11I1II1
try :
 iII1i1 = urllib . unquote_plus ( Ii1I [ "url" ] ) . decode ( 'utf-8' )
except :
 pass
try :
 OOO00 = urllib . unquote_plus ( Ii1I [ "name" ] ) . decode ( 'utf-8' )
except :
 pass
try :
 I1I1i = urllib . unquote_plus ( Ii1I [ "iconimage" ] )
except :
 pass
try :
 oOo0OoOOo0 = urllib . unquote_plus ( Ii1I [ "fanart" ] )
except :
 pass
try :
 II11iiii1Ii = int ( Ii1I [ "mode" ] )
except :
 pass
try :
 Oo0O0OOOoo = eval ( urllib . unquote_plus ( Ii1I [ "playlist" ] ) . replace ( '|' , ',' ) )
except :
 pass
try :
 iII11I1Ii1 = int ( Ii1I [ "fav_mode" ] )
except :
 pass
 if 70 - 70: ooo0Oo0
try :
 o0o0oOo0oO = Ii1I [ "regexs" ]
except :
 pass
 if 16 - 16: o00 - OoooooooOO % ii1IiI1i
try :
 IIi1IIIIi = urllib . unquote_plus ( Ii1I [ "thumbnail" ] )
except :
 pass
 if 36 - 36: Iii1iIIIII
try :
 OoO = int ( Ii1I [ "page" ] )
except :
 pass
 if 84 - 84: ooo0Oo0 . IIIiiIIii . OOooo000oo0 . II1i / o00ooo0 % iiiIIii1I1Ii
 if 57 - 57: i1 % II1i - Iii1iIIIII . i1 / ii1IiI1i % o00
try :
 ii1ii11 = urllib . unquote_plus ( Ii1I [ 'requestdata' ] )
except :
 pass
 if 56 - 56: O00oOoOoO0o0O . o00 . O0IiiiIiI1iIiI1 * Oo . i1IIi11111i / O0
try :
 OOOoO = urllib . unquote_plus ( Ii1I [ "mirrorname" ] )
except :
 pass
 if 23 - 23: i1IIi + o00 + O0IiiiIiI1iIiI1 + IIIiiIIii
try :
 i1i1I111iIi1 = int ( Ii1I [ "number" ] )
except :
 pass
 if 12 - 12: iIii1I11I1II1 - iiiIIii1I1Ii + i11iIiiIii
 if 10 - 10: i1 - i1IIi - i1IIi11111i % ii1IiI1i
 if 6 - 6: iiiIIii1I1Ii + O00oOoOoO0o0O
 if 48 - 48: iIii1I11I1II1 % i1IIi % o00 + i1IIi11111i
 if 30 - 30: i11iIiiIii % iIii1I11I1II1 . II1i % iIii1I11I1II1
 if 62 - 62: ii1IiI1i * Oo
if II11iiii1Ii == None :
 if o0OO00 . getSetting ( 'check_mac' ) == '' or o0OO00 . getSetting ( 'check_mac' ) != O0Oo ( ) :
  OO0OOO0oOOo00O = oo0Ooo0 ( __movies_url__ + '/movies/CheckMac' + '/' + OoOooOOOO ( ) + '/' + I1Ii ( ) )
  OooO0 = re . compile ( '<div class="id">(.*?)</div>' ) . findall ( OO0OOO0oOOo00O )
  if OooO0 :
   o0OO00 . setSetting ( 'check_mac' , O0Oo ( ) )
  else :
   IiIIIiI1I1 ( __movies_url__ )
   if 51 - 51: iiiIIii1I1Ii / iIii1I11I1II1 % O00oOoOoO0o0O + iII11iiIII111 * i1IIi11111i + ooo0Oo0
 i11iiII = O0Oo ( )
 OO0o ( )
 if 77 - 77: i1IIi11111i * Oo
elif II11iiii1Ii == 1 :
 getData ( iII1i1 , oOo0OoOOo0 )
 oooOo0OOOoo0 ( iII1i1 , OOO00 )
 if 14 - 14: II1i % II1i / O0IiiiIiI1iIiI1
elif II11iiii1Ii == 2 :
 oooOo0OOOoo0 ( iII1i1 , OOO00 )
 if 72 - 72: i1IIi - OOooo000oo0 - Iii1iIIIII + Iii1iIIIII * iII11iiIII111 * Iii1iIIIII
elif II11iiii1Ii == 3 :
 OOOoO = "Server Google:"
 ooooo0O0000oo ( iII1i1 , OOOoO )
 if 33 - 33: ii1IiI1i
 if 49 - 49: IIIiiIIii % o00 % o00 / o00
elif II11iiii1Ii == 4 :
 if 53 - 53: iIii1I11I1II1
 oOoOooOo0o0 = xbmcgui . ListItem ( path = iII1i1 )
 if 68 - 68: OoooooooOO % OOooo000oo0
 oOoOooOo0o0 . setProperty ( "IsPlayable" , 'true' )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , oOoOooOo0o0 )
 if 26 - 26: OOooo000oo0 % i11iIiiIii % iIii1I11I1II1 % II1i * II1i * iiiIIii1I1Ii
elif II11iiii1Ii == 20 :
 if 24 - 24: OOooo000oo0 % ooo0Oo0 - i1IIi11111i + i1 * iiiIIii1I1Ii
 oOOo0O00o ( homeLinkTV )
 if 2 - 2: o00ooo0 - O0IiiiIiI1iIiI1
elif II11iiii1Ii == 40 :
 if 83 - 83: O00oOoOoO0o0O % iII11iiIII111 % o00ooo0 - OOooo000oo0 * Iii1iIIIII / OoooooooOO
 if 18 - 18: IIIiiIIii + iIii1I11I1II1 - OOooo000oo0 - i1
 i1II1 ( )
 if 71 - 71: OoooooooOO
elif II11iiii1Ii == 41 :
 if 33 - 33: ooo0Oo0
 oO0OOOO0 ( iII1i1 , OoO )
 if 62 - 62: iiiIIii1I1Ii + o00ooo0 + i1IIi / OoooooooOO
elif II11iiii1Ii == 42 :
 if 7 - 7: iII11iiIII111 + i1IIi . i1 / ii1IiI1i
 i11I1iIiII ( iII1i1 )
 if 22 - 22: i1IIi11111i - i1IIi11111i % Iii1iIIIII . ooo0Oo0 + O00oOoOoO0o0O
if II11iiii1Ii == 43 :
 o00oO0oo0OO ( iII1i1 )
 if 63 - 63: i1 % ooo0Oo0 * iII11iiIII111 + ooo0Oo0 / ii1IiI1i % o00
elif II11iiii1Ii == 44 :
 oO0 ( iII1i1 )
 if 45 - 45: O0IiiiIiI1iIiI1
elif II11iiii1Ii == 45 :
 o0oo ( iII1i1 )
 if 20 - 20: OoooooooOO * iII11iiIII111 * O0 . Iii1iIIIII
elif II11iiii1Ii == 46 :
 if 78 - 78: iIii1I11I1II1 + II1i - o00ooo0 * ooo0Oo0 - OoooooooOO % Oo
 if 34 - 34: O0
 IiIIIiI1I1 ( iII1i1 )
 if 80 - 80: i1IIi - ii1IiI1i / IIIiiIIii - i11iIiiIii
 if 68 - 68: O00oOoOoO0o0O - iiiIIii1I1Ii % O0 % ooo0Oo0
elif II11iiii1Ii == 47 :
 if 11 - 11: O0 / IIIiiIIii % Iii1iIIIII + iII11iiIII111 + iIii1I11I1II1
 iii11 ( iII1i1 )
 if 40 - 40: i1IIi11111i - Iii1iIIIII . o00ooo0 * ii1IiI1i % ooo0Oo0
elif II11iiii1Ii == 48 :
 if 56 - 56: i11iIiiIii . iII11iiIII111 - i1 * II1i
 Oo000o ( iII1i1 , OoO )
 if 91 - 91: O00oOoOoO0o0O + OoooooooOO - i1IIi
elif II11iiii1Ii == 49 :
 if 84 - 84: o00ooo0 / O0IiiiIiI1iIiI1
 IiI11iII1 ( iII1i1 , OoO )
 if 86 - 86: Oo * OOooo000oo0 - O0 . Oo % iIii1I11I1II1 / Iii1iIIIII
 if 11 - 11: i1 * O00oOoOoO0o0O + iiiIIii1I1Ii / iiiIIii1I1Ii
elif II11iiii1Ii == 50 :
 iii11 ( iII1i1 )
 if 37 - 37: i11iIiiIii + i1IIi
elif II11iiii1Ii == 51 :
 I1Ii11i ( iII1i1 )
 if 23 - 23: o00 + II1i . Oo * i1 + iiiIIii1I1Ii
elif II11iiii1Ii == 55 :
 oO ( iII1i1 )
 if 18 - 18: O0IiiiIiI1iIiI1 * iII11iiIII111 . O0IiiiIiI1iIiI1 / O0
elif II11iiii1Ii == 56 :
 i1IIIiiII1 ( iII1i1 )
 if 8 - 8: iII11iiIII111
 if 4 - 4: iiiIIii1I1Ii + iiiIIii1I1Ii * i1IIi11111i - Oo
 if 78 - 78: o00ooo0 / OOooo000oo0 % Oo
 if 52 - 52: Iii1iIIIII - o00 * O00oOoOoO0o0O
elif II11iiii1Ii == 12 :
 if 17 - 17: OoooooooOO + Iii1iIIIII * II1i * Oo
 oOoOooOo0o0 = xbmcgui . ListItem ( path = iII1i1 )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , oOoOooOo0o0 )
 if 36 - 36: O0 + ii1IiI1i
elif II11iiii1Ii == 13 :
 if 5 - 5: ii1IiI1i * Oo
 play_playlist ( OOO00 , Oo0O0OOOoo )
 if 46 - 46: i1IIi11111i
 if 33 - 33: o00 - OOooo000oo0 * OoooooooOO - ii1IiI1i - Iii1iIIIII
 if 84 - 84: ooo0Oo0 + ii1IiI1i - Oo * Oo
 if 61 - 61: OoooooooOO . O00oOoOoO0o0O . OoooooooOO / ii1IiI1i
elif II11iiii1Ii == 1401 :
 OoO00 ( iII1i1 , i1i1I111iIi1 , oOo0OoOOo0 )
elif II11iiii1Ii == 1440 :
 OoO0ooO ( )
elif II11iiii1Ii == 1403 :
 if 72 - 72: i1IIi
 i1II1I1Iii1 ( iII1i1 )
elif II11iiii1Ii == 10 :
 i1II11II ( OOO00 , iII1i1 , I1I1i )
elif II11iiii1Ii == 1416 :
 ii1 ( iII1i1 )
 if 82 - 82: Oo + OoooooooOO / i11iIiiIii * iiiIIii1I1Ii . OoooooooOO
elif II11iiii1Ii == 1417 :
 Karaoke_Sunflyurl ( OOO00 )
 if 63 - 63: iiiIIii1I1Ii
elif II11iiii1Ii == 1419 :
 OoOoOo00o0 ( iII1i1 )
 if 6 - 6: i1IIi11111i / iiiIIii1I1Ii
elif II11iiii1Ii == 1420 :
 i1iiIiI1Ii1i ( iII1i1 )
 if 57 - 57: II1i
elif II11iiii1Ii == 1423 :
 O00oO0 ( OOO00 )
 if 67 - 67: IIIiiIIii . i1IIi11111i
elif II11iiii1Ii == 1424 :
 iI1iIIIi1i ( OOO00 )
 if 87 - 87: O00oOoOoO0o0O % o00ooo0
elif II11iiii1Ii == 1425 :
 oo0o0O0Oooooo ( OOO00 )
 if 83 - 83: OOooo000oo0 - II1i
elif II11iiii1Ii == 1426 :
 print ""
 Karaoke_LATEST_LIST ( iII1i1 )
elif II11iiii1Ii == 1432 :
 iiIi1IIiI ( iII1i1 )
elif II11iiii1Ii == 1433 :
 i1i1ii111 ( OOO00 , iII1i1 , I1I1i )
 if 35 - 35: i1IIi - iIii1I11I1II1 + i1IIi
elif II11iiii1Ii == 666 :
 o00OO00O0oOO ( )
elif II11iiii1Ii == 667 :
 I1iii ( iII1i1 , OoO )
 if 86 - 86: iIii1I11I1II1 + Oo . i11iIiiIii - o00ooo0
xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) ) # dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
