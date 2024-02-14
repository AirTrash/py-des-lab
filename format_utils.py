def align_str_zero(string, count, side = "right"):
	str_l = len(string)
	if count > str_l:
		if side == "right":
			return string.rjust(count, "0")
		elif side == "left":
			return string.ljust(count, "0")
	elif str_l > count:
		if side == "right":
			return string[str_l - count::]
		elif side == "left":
			return string[:count]
	return string

def shuffle_binstr(bin_str: str, table) -> str:
	ret = ""
	for i in table:
		ret += bin_str[i - 1]
	return ret

def str2unicode(string):
	lets = []
	for let in string:
		lets.append(ord(let))
	return lets

def str2binstr(string, count = 8):
	binstr = ""
	for let in string:
		let = ord(let)
		binlet = format(let, "b")
		binlet = align_str_zero(binlet, count)
		binstr += binlet
	return binstr


def str2bin(string):
	bins = []
	for let in string:
		let = ord(let)
		bins.append(bin(let))
	return bins

def xor_binstr(binstr1, binstr2):
	if len(binstr1) != len(binstr2):
		return None
	ret = ""
	for i, byte1 in enumerate(binstr1):
		byte2 = binstr2[i]
		if byte1 == byte2:
			ret += "0"
		else:
			ret += "1"
	return ret

def split_str(binstr: str, count: int) -> list:
	ret = []
	while binstr != "":
		ret.append(binstr[:count])
		binstr = binstr[count::]
	return ret
