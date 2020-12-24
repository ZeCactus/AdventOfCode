import copy
old = [char for char in "1113222113"]
for i in range(0, 50):
    new = []
    digit = old[0]
    times = 1
    for j in range(1, len(old)):
        if old[j] == old[j-1]:
            times += 1
        else:
            new.append(str(times))
            new.append(digit)
            digit = old[j]
            times = 1
    new.append(str(times))
    new.append(digit)
    old = copy.copy(new)
print(len(old))
