from format_utils import align_str_zero

def binstr2hexstr(bin_str: str, count: int, bit_depth: int = 2) -> str:
	ret = ""
	new_binstr = ""
	for i, elem in enumerate(bin_str):
		new_binstr += elem
		if (i + 1) % count == 0:
			new_hex = str(hex(int(new_binstr, 2))).replace("x", "")
			ret += align_str_zero(new_hex, 2) + " "
			new_binstr = ""
	return ret