from help import str2unicode, str2bin, align_str_zero


def gen_key(string):
	bins = str2bin(string)
	pre_key = ""
	for elem in bins:
		pre_key += align_str_zero(elem[2::], 8)