def shuffle_binstr(bin_str: str, table) -> str:
	ret = ""
	for i in table:
		ret += bin_str[i - 1]
	return ret