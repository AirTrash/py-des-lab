from encrypt.key_gen import gen_pre_key, rounds_keys_by_prekey
from format_utils import align_str_zero
from viewer import binstr2hexstr

if __name__ == "__main__":
	pre_key = gen_pre_key("COMPUTER")
	print(pre_key)
	print(binstr2hexstr(pre_key, 4))
	rounds_keys_by_prekey(pre_key)
