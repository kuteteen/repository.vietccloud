# -*- coding: utf-8 -*-

import os, re, shutil
from viphome import vip, vipName
so_regex = '<setting id="SO (.+?)".+?value="(.*?)" />'
sr_regex = '<setting id="SR (.+?)".+?value="(.*?)" />'

def sor_vip():
	try:
		f = open(vip, 'r')
		content = f.read()
		f.close()
		match = re.compile(so_regex).findall(content)
		for soNum, soCode in match:
			if soCode == '':
				pass
			else:
				soPass = soCode.split('//')[-1]
				soTicket = (('%s/%s') % (vipName, soPass))
				if os.path.exists(soTicket) == True:
					try:
						shutil.rmtree(soTicket)
					except:
						pass
				else:
					pass
		match = re.compile(sr_regex).findall(content)
		for srNum, srCode in match:
			if srCode == '':
				pass
			else:
				srPass = srCode.split('//')[-1]
				srTicket = (('%s/%s') % (vipName, srPass))
				if os.path.exists(srTicket) == True:
					try:
						os.remove('%s/start.py' % srTicket)
					except:
						pass
				else:
					pass
	except:
		pass

if __name__ == "__main__":
	sor_vip()