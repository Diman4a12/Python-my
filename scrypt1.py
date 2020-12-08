passwr = []
with open("encrypted.bin", "rb") as inp:
    encrypted = inp.read()
with open("passwords.txt", "r") as ps:
    for s in ps:
        passwr.append(s.strip())
from simplecrypt import decrypt, DecryptionException
for i in passwr:
    
    try:
        norm = decrypt(i, encrypted)
        print(norm.decode('utf8'))
    except DecryptionException:
        pass
