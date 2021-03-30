import copy
sum = 0
originalDict = { chr(i) : 0 for i in range(97, 123)}
with open("input.txt") as f:
    g = open("cleanedinput.txt", 'a')
    for line in f:
        room = line.rsplit('-', 1)
        string = room[0].replace('-', '')
        id = int(room[1].split('[')[0])
        checksum = room[1].split('[')[1][:-2]
        dict1 = copy.deepcopy(originalDict)
        for ch in string:
            dict1[ch] += 1
        dict1 = {k: v for k, v in sorted(dict1.items(), key=lambda item: item[1], reverse=True)}
        dict1 = dict(filter(lambda x: x[1] != 0, dict1.items()))
        check = "".join(list(dict1.keys())[0:len(checksum)])
        if check == checksum:
            sum += id
            g.write(line)
print(sum)
g.close()
