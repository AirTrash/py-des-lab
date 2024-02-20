from format_utils import shuffle_binstr, xor_binstr, split_str, align_str_zero
from des.tables import table2, table3, table4

from viewer import binstr2hexstr

def s_transformation(b_block, table):
	i = int(b_block[0] + b_block[5], 2)
	j = int(b_block[1:5], 2)
	binstr = format(table[i][j], "b")
	return align_str_zero(binstr, 4)

def func(R, round_key):
	extended_R = shuffle_binstr(R, table2)
	print("extended_R:", binstr2hexstr(extended_R, 8))
	r_xor_k = xor_binstr(extended_R, round_key)
	print("extended_R xor round_key:", binstr2hexstr(r_xor_k, 8))
	b_blocks = split_str(r_xor_k, 6)
	print("B_blocks:", b_blocks)
	ret = ""
	for i, block in enumerate(b_blocks):
		s_out = s_transformation(block, table3[i])
		ret += s_out
	print("after s transformation:", binstr2hexstr(ret, 4))
	ret = shuffle_binstr(ret, table4)
	print("feistel func:", binstr2hexstr(ret, 8))
	return ret

