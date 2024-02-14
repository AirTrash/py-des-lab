from viewer import binstr2hexstr
from encrypt.tables import IPtable
from format_utils import str2binstr, align_str_zero, shuffle_binstr, xor_binstr
from encrypt.feistel import func as feistel_func
import encrypt.key as key

def encrypt_block(bin_str, rounds_keys):
	start_block = shuffle_binstr(bin_str, IPtable)
	L, R = start_block[:32], start_block[32::]
	print("\n\n")
	print(f"L0: {binstr2hexstr(L, 8)}| R0: {binstr2hexstr(R, 8)}")
	print("\n\n")
	for i in range(16):
		round_idx = i + 1
		print("round", round_idx)
		round_key = rounds_keys[i]
		f = feistel_func(R, round_key)
		new_R = xor_binstr(L, f)
		L, R = R, new_R
		print(f"L{round_idx}: {binstr2hexstr(L, 8)}| R{round_idx}: {binstr2hexstr(R, 8)}")
		print("\n\n")
	


def encrypt(text, key_text):
	pre_key = key.gen_pre_key("COMPUTER")
	rounds_keys = key.rounds_keys_by_prekey(pre_key)
	binstr = str2binstr(text)
	binstr = align_str_zero(binstr, 64, "left")
	encrypt_block(binstr, rounds_keys)