from format_utils import str2unicode, str2bin, align_str_zero
from encrypt.tables import table5, table6, table7
from viewer import binstr2hexstr
from table_help import shuffle_binstr


def gen_pre_key(string):
	bins = str2bin(string)
	pre_key = ""
	for elem in bins:
		pre_key += align_str_zero(elem[2::], 8)

	pre_key = shuffle_binstr(pre_key, table5)
	return pre_key

def left_bais(string, count):
	return string[count::] + string[:count]


def rounds_keys_by_prekey(pre_key: str) -> str:
	keys = []
	for bais in table6:
		c = pre_key[0:28]
		d = pre_key[28::]
		c, d = left_bais(c, bais), left_bais(d, bais)
		pre_key = c + d
		keys.append(shuffle_binstr(pre_key, table7))
	for binstr in keys:
		print(binstr2hexstr(binstr, 8))