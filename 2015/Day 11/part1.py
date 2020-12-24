import copy
def check(pw):
    checks = False
    forbidden = [8, 14, 11]
    for i in range(0, len(pw)-2):
        if pw[i] == pw[i+1]-1 and pw[i] == pw[i+2]-2:
            checks = True
            break
    if checks is False:
        return False
    checks = False
    if not [value for value in forbidden if value in pw]:
        checks = True
    if checks is False:
        return False
    checks = False
    i = 0
    doubles = 0
    while i in range(0, len(pw)-1) and doubles < 2:
        if pw[i] == pw[i+1]:
            doubles += 1
            i += 1
        i += 1
    if doubles > 1:
        return True
    return checks
def increase(pw, pos):
    pw = copy.copy(pw)
    if pos == 0:
        pw[0] = 0
        pw.insert(0, 0)
        return pw
    pw[pos] += 1
    if pw[pos] == 26:
        pw[pos] = 0
        pw = increase(pw, pos-1)
    return pw
def stringify(pw):
    return ''.join([string.ascii_lowercase[nr] for nr in pw])
import string
password = [string.ascii_lowercase.index(char) for char in "hxbxxyzz"]
password = increase(password, len(password)-1)
while not check(password):
    password = increase(password, len(password)-1)
print(stringify(password))
