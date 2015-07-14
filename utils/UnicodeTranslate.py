# -*- coding: utf-8 -*-


def trancChar(v_str,v_len):
	try:
		decode_str = v_str.decode('utf-8')
		if len(decode_str) > v_len:
			return decode_str[0:v_len].encode('utf-8')+'...'
		else:
			return v_str
	except Exception as e:
		print e
		return None