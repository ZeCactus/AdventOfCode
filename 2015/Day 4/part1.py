import hashlib
seed = "ckczppom"
i = 0
while True:
    m = hashlib.md5()
    text = (seed + str(i)).encode()
    m.update(text)
    if m.hexdigest()[:5].count('0') == 5:
        print(i)
        break
    i += 1
