from table_help import shuffle_binstr
from encrypt.tables import IPtable
import encrypt.key as key

def encrypt_block(bin_str, round_keys):
	start_block = shuffle_binstr(bin_str, IPtable)
	L, R = start_block[:32], start_block[32::]


def encrypt(text, key_text):
	pre_key = key.gen_pre_key("COMPUTER")