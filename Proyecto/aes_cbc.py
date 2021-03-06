#Cifrador por bloques
import json
from base64 import b64encode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes

def convBytes(m):
    cb = bytes.fromhex(m)
    return cb

def convHexa(b):
    h = []
    for i in range(b):
        a = ord(b)
        h.append("{0:0>2X}".format(a))
    print(h)

KEY = "0000000000000000000000000000000000000000000000000000000000000000"
KEY = convBytes(KEY)

IV = "00000000000000000000000000000000"
IV = convBytes(IV)

PLAINTEXT = "014730f80ac625fe84f026c60bfd547d"
print("Mensaje: ", PLAINTEXT)
PLAINTEXT = convBytes(PLAINTEXT)

#Creacion del cifrador
cipher = AES.new(KEY, AES.MODE_CBC, iv=IV)
#Cirfado de una cadena de bytes
ct_bytes = (cipher.encrypt(PLAINTEXT))
#ct_bytes = cipher.encrypt(pad(PLAINTEXT, AES.block_size))
print(len(ct_bytes))
h = ct_bytes.hex()
print("Mensaje cifrado: ", h)
iv = b64encode(cipher.iv).decode('utf-8')
ct = b64encode(ct_bytes).decode('utf-8')
result = json.dumps({'iv':iv, 'TextoCifrado': ct})
print(result)
print(len(ct))

#Descifrado del Mensaje
descipher = AES.new(KEY, AES.MODE_CBC, iv=IV)
msj = descipher.decrypt(ct_bytes)
h = msj.hex()
print("Mensaje descifrado: ", h)
