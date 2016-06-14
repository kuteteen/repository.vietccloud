import base64

def key(k, e):
	dec = []
	e = base64.urlsafe_b64decode(e)
	for i in range(len(e)):
		k_c = k[i % len(k)]
		dec_c = chr((256 + ord(e[i]) - ord(k_c)) % 256)
		dec.append(dec_c)
	return "".join(dec)