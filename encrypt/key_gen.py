from format_utils import str2unicode, str2bin, align_str_zero
from encrypt.tables import table5, table6, table7
from viewer import binstr2hexstr


def t5_shuffle(bin_str: str) -> str:
	ret = ""
	for i in table5:
		ret += bin_str[i - 1]
	return ret


def gen_pre_key(string):
	bins = str2bin(string)
	pre_key = ""
	for elem in bins:
		pre_key += align_str_zero(elem[2::], 8)

	pre_key = t5_shuffle(pre_key)
	return pre_key

def rounds_keys_by_prekey(pre_key: str) -> str:
	keys = []
	for bais in table6:
		c = pre_key[0:28]
		d = pre_key[28::]
		print(d)
		c, d = int(c, 2), int(d, 2)
		print(d)
		c, d = c << bais, d << bais
		c, d = str(bin(c))[2::], str(bin(d))[2::]
		c, d = align_str_zero(c, 28), align_str_zero(d, 28)
		print(d)
		pre_key = c + d
		print(pre_key)
		print(binstr2hexstr(pre_key, 4))
		quit()