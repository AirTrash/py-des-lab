from des.encryptor import encrypt
from des.decryptor import decrypt
from format_utils import align_str_zero
from viewer import binstr2hexstr

if __name__ == "__main__":
	blocks = encrypt("Sys12COM", "CRYPTA12")
	print(binstr2hexstr(blocks[0], 8))
	decrypt(blocks[0], "CRYPTA12")

