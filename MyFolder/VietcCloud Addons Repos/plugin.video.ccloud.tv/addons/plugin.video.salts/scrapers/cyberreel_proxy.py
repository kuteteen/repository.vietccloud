"""
    SALTS XBMC Addon
    Copyright (C) 2014 tknorris

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
from salts_lib import log_utils
import proxy

class CyberReel_Proxy(proxy.Proxy):
    try:
        from cyberreel_scraper import CyberReel_Scraper as real_scraper
    except Exception as e:
        real_scraper = None
        log_utils.log('import failed: %s' % (e), log_utils.LOGDEBUG)
