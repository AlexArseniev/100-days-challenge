def caesarCipherEncryptor(string, key):
    return ''.join([chr((ord(c)- 97 + key) % 26 + 97) for c in string])

string = 'abc'
key = 57
print(caesarCipherEncryptor(string, key))

#97 - 122