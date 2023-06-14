from Cryptodome.Cipher import AES
from binascii import b2a_hex, a2b_hex


class PrpCrypt:
    def __init__(self, key):
        self.key = key.encode('utf-8')
        self.mode = AES.MODE_CBC

    # 加密 不足16位數會自動補足
    def encrypt(self, text):
        text = text.encode('utf-8')
        cryptor = AES.new(self.key, self.mode, b'imedtac-imedtac-')
        # 這裡密鑰匙長度必須為16（AES-128）,24（AES-192）,或者32 （AES-256）Bytes
        # 目前AES-128 足夠目前使用
        length = 16
        count = len(text)
        if count < length:
            add = (length - count)
            text = text + ('\0' * add).encode('utf-8')
        elif count > length:
            add = (length - (count % length))
            text = text + ('\0' * add).encode('utf-8')
        ciphertext = cryptor.encrypt(text)
        # 因AES加密得到的字符串不一定，所以統一把加密後的字串轉為16進位
        return b2a_hex(ciphertext)

    # 解密 去掉加密時補的空格
    def decrypt(self, text):
        cryptor = AES.new(self.key, self.mode, b'imedtac-imedtac-')
        plain_text = cryptor.decrypt(a2b_hex(text))
        return bytes.decode(plain_text).rstrip('\0')
