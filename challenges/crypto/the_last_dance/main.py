know_message = b"Our counter agencies have intercepted your messages and a lot "
know_ciphertext = bytes.fromhex("7aa34395a258f5893e3db1822139b8c1f04cfab9d757b9b9cca57e1df33d093f07c7f06e06bb6293676f9060a838ea138b6bc9f20b08afeb73120506e2ce7b9b9dcd9e4a421584cfaba2481132dfbdf4216e98e3facec9ba199ca3a97641e9ca9782868d0222a1d7c0d3119b867edaf2e72e2a6f7d344df39a14edc39cb6f960944ddac2aaef324827c36cba67dcb76b22119b43881a3f1262752990")
know_flag = bytes.fromhex("7d8273ceb459e4d4386df4e32e1aecc1aa7aaafda50cb982f6c62623cf6b29693d86b15457aa76ac7e2eef6cf814ae3a8d39c7")

## https://pycryptodome.readthedocs.io/en/latest/src/cipher/chacha20.html
## https://www.geeksforgeeks.org/python-bitwise-operators/
## https://www.geeksforgeeks.org/zip-in-python/

def xor(a: bytes, b: bytes) -> bytes:
    '''
    The key is the xor of the known message and the known ciphertext
    The flag is the xor of the key and the known flag
    '''
    return bytes([x ^ y for x, y in zip(a, b)])

def decrypt_content():
    key = xor(know_message, know_ciphertext)
    flag = xor(know_flag, key)
    print(flag)

if __name__ == "__main__":
    decrypt_content()