# -*- coding: utf-8 -*-


def trancChar(v_str,v_len,v_full=True):
	'''
	v_str translate string
	v_len substring length
	v_full return full translated string or "..." 
	'''
	try:
		decode_str = v_str.decode('utf-8')
		print len(decode_str) 
		if len(decode_str) > v_len:
			if v_full:
				return decode_str[0:v_len].encode('utf-8').decode('utf-8')
			return decode_str[0:v_len].encode('utf-8')+'...'.decode('utf-8')
		else:
			return v_str
	except Exception as e:
		print e
		return None