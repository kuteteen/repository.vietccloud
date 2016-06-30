# -*- coding: utf-8 -*-

import base64
mycode = base64.b64decode

def key(k, e):
	dec = []
	e = base64.urlsafe_b64decode(e)
	for i in range(len(e)):
		k_c = k[i % len(k)]
		dec_c = chr((256 + ord(e[i]) - ord(k_c)) % 256)
		dec.append(dec_c)
	return "".join(dec)

mykbase = mycode('M3QzWjVOYWRtNTdueGUyWHpOM1h5\2\n\LUhSNnRmYjI4amowZGZSM2VtUzJkalNvOGJQMi1U\
                  WjBOX2MyYVB\6\n\WeU56ZTZNM3EyTmZ0a2RuVjMtSE42ZDJVNGNUVzROVG5rOFBpcS0\?\=\4')

myk = mycode('dmlld\1\n\GNjbG91ZA=\2\=\?')
