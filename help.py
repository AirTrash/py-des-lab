def align_str_zero(string, count):
	str_l = len(string)
	if count > str_l:
		return string.rjust(count, "0")
	elif str_l > count:
		return string[str_l - count::]
	else:
		return string


def str2unicode(string):
	lets = []
	for let in string:
		lets.append(ord(let))
	return lets


def str2bin(string):
	bins = []
	for let in string:
		let = ord(let)
		bins.append(bin(let))
	return bins
