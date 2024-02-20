from viewer import binstr2hexstr
from des.tables import IPtable, table8
from format_utils import str2binstr, align_str_zero, shuffle_binstr, xor_binstr
from des.feistel import func as feistel_func
import des.key as key

def encrypt_block(bin_str, rounds_keys):
	start_block = shuffle_binstr(bin_str, IPtable)
	L, R = start_block[:32], start_block[32::]
	print("\n\n")
	print(f"L0: {binstr2hexstr(L, 8)}| R0: {binstr2hexstr(R, 8)}")
	print("\n")
	for i in range(16):
		round_idx = i + 1
		print("round", round_idx)
		round_key = rounds_keys[i]
		f = feistel_func(R, round_key)
		new_R = xor_binstr(L, f)
		L, R = R, new_R
		print(f"L{round_idx}: {binstr2hexstr(L, 8)}| R{round_idx}: {binstr2hexstr(R, 8)}")
		print("\n\n")
	print("\n\n\n")
	chifer_block = R + L
	chifer_block = shuffle_binstr(chifer_block, table8)
	print("chifer block:")
	print(binstr2hexstr(chifer_block, 8))
	return chifer_block
	


def encrypt(text, key_text):
	blocks = []
	binstr = str2binstr(text)
	binstr = align_str_zero(binstr, 64, "left")
	print("input block:", binstr2hexstr(binstr, 8), "\n\n")
	pre_key = key.gen_pre_key(key_text)
	rounds_keys = key.rounds_keys_by_prekey(pre_key)
	chifer_block = encrypt_block(binstr, rounds_keys)
	blocks.append(chifer_block)
	return blocks