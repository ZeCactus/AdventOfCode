import copy
sum = 0
dict0 = { chr(i) : 0 for i in range(97, 123)}
with open("input.txt") as f:
    for line in f:
        room = line.rsplit('-', 1)
        string = room[0].replace('-', '')
        id = int(room[1].split('[')[0])
        checksum = room[1].split('[')[1][:-2]
        dict1 = copy.deepcopy(dict0)
        for ch in string:
            dict1[ch] += 1
        dict1 = {k: v for k, v in sorted(dict1.items(), key=lambda item: item[1])}
        print(dict1)
            
print(sum)
