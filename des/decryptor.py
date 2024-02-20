from viewer import binstr2hexstr
from des.tables import IPtable, table8
from format_utils import str2binstr, align_str_zero, shuffle_binstr, xor_binstr
from des.feistel import func as feistel_func
import des.key as key

def decrypt_block(bin_str, rounds_keys):
	start_block = shuffle_binstr(bin_str, IPtable)
	L, R = start_block[:32], start_block[32::]
	print("\n\n")
	print(f"L16: {binstr2hexstr(L, 8)}| R16: {binstr2hexstr(R, 8)}")
	print("\n\n")
	for i in range(15, -1, -1):
		print("round", i)
		round_key = rounds_keys[i]
		f = feistel_func(R, round_key)
		new_R = xor_binstr(L, f)
		L, R = R, new_R
		print(f"L{i}: {binstr2hexstr(L, 8)}| R{i}: {binstr2hexstr(R, 8)}")
		print("\n\n")
	print("\n\n\n")
	block = R + L
	block = shuffle_binstr(block, table8)
	print("decrypted block:")
	print(binstr2hexstr(block, 8))
	return block
	


def decrypt(chifer_binstr: str, key_text: str):
	blocks = []
	pre_key = key.gen_pre_key(key_text)
	rounds_keys = key.rounds_keys_by_prekey(pre_key)
	decrypted_block = decrypt_block(chifer_binstr, rounds_keys)
	blocks.append(decrypted_block)
	return blocks