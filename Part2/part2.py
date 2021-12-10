from Crypto.Cipher import AES
import json
from base64 import b64encode
from Crypto.Random import get_random_bytes
import binascii

# key = '2b7e151628aed2a6abf7158809cf4f3c'
# key = binascii.unhexlify(key)
#iv = '000102030405060708090a0b0c0d0e0f'
iv = '0001020304050607'

#iv = binascii.unhexlify(iv) 
# key = "I am Adi Alageel"
key = '4920616d2041646920416c616765656c'
# message = "This is a sample test message for Adi Alageel!!"
message = '5468697320697320612073616d706c652074657374206d65737361676520666f722041646920416c616765656c2121'

#key = binascii.unhexlify(key)
plaintext = binascii.unhexlify(message)

cipher = AES.new(key.encode("utf-8"), AES.MODE_CFB, iv.encode("utf-8"), segment_size=128)
encrypted = cipher.encrypt(message.encode("utf-8"))
#encrypt(int(plaintext, base=16))
#encrypted = cipher.encrypt(int(message, base=16))
print(encrypted)
print(encrypted)
cipher2 = AES.new(key.encode("utf-8"), AES.MODE_OFB)
ct_bytes = cipher.encrypt(encrypted)
print(cipher)
print(cipher2)
decrypted = cipher.decrypt(encrypted)


#encryption
# data = b"secret"
# key = get_random_bytes(16)
# cipher = AES.new(key, AES.MODE_OFB)
# ct_bytes = cipher.encrypt(data)
# iv = b64encode(cipher.iv).decode('utf-8')
# ct = b64encode(ct_bytes).decode('utf-8')
# result = json.dumps({'iv':iv, 'ciphertext':ct})
# print(result)

#decryption

# try:
#     b64 = json.loads(json_input)
#     iv = b64decode(b64['iv'])
#     ct = b64decode(b64['ciphertext'])
#     cipher = AES.new(key, AES.MODE_OFB, iv=iv)
#     pt = cipher.decrypt(ct)
#     print("The message was: ", pt)
# except ValueError, KeyError:
#     print("Incorrect decryption")






# key = 'abcdefghijklmnop'
# cipher = AES.new(key, AES.MODE_ECB)
# msg =cipher.encrypt('TechTutorialsX!!TechTutorialsX!!')
# print (type(msg))