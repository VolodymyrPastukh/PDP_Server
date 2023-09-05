import random
from Crypto.Cipher import AES
from base64 import b64encode, b64decode
from string import ascii_lowercase
from os import environ


_key = environ.get('CRPT_KEY')
_salt = 'SlTKeYOpHygTYkP3'.encode('utf8')
_enc_dec_method = 'utf-8'

def encrypt(str_to_enc):
    try:
        aes_obj = AES.new(_key.encode('utf-8'), AES.MODE_CFB, _salt)
        hx_enc = aes_obj.encrypt(str_to_enc.encode('utf8'))
        mret = b64encode(hx_enc).decode(_enc_dec_method)
        return mret
    except ValueError as value_error:
        if value_error.args[0] == 'IV must be 16 bytes long':
            raise ValueError('Encryption Error: SALT must be 16 characters long')
        elif value_error.args[0] == 'AES key must be either 16, 24, or 32 bytes long':
            raise ValueError('Encryption Error: Encryption key must be either 16, 24, or 32 characters long')
        else:
            raise ValueError(value_error)

def decrypt(enc_str):
    try:
        aes_obj = AES.new(_key.encode('utf8'), AES.MODE_CFB, _salt)
        str_tmp = b64decode(enc_str.encode(_enc_dec_method))
        str_dec = aes_obj.decrypt(str_tmp)
        mret = str_dec.decode(_enc_dec_method)
        return mret
    except ValueError as value_error:
        if value_error.args[0] == 'IV must be 16 bytes long':
            raise ValueError('Decryption Error: SALT must be 16 characters long')
        elif value_error.args[0] == 'AES key must be either 16, 24, or 32 bytes long':
            raise ValueError('Decryption Error: Encryption key must be either 16, 24, or 32 characters long')
        else:
            raise ValueError(value_error)

def access_key(length=30):
   letters = ascii_lowercase
   return ''.join(random.choice(letters) for i in range(length))
