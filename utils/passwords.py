import hashlib

def encrypt(password):
    salt = '-------------------------'
    return hashlib.md5(salt+password).hexdigest()