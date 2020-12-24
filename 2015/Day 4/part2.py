import hashlib
seed = "ckczppom"
i = 0
while True:
    m = hashlib.md5()
    text = (seed + str(i)).encode()
    m.update(text)
    if m.hexdigest()[:6].count('0') == 6:
        print(i)
        break
    i += 1
