import operator
dicts = []
for i in range(0, 8):
    dicts.append({chr(i) : 0 for i in range(97, 123)})
with open("input.txt") as f:
    for line in f:
        for i in range(0, 8):
            dicts[i][line[i]] += 1
result = ""
print(dicts[0])
for i in range(0, 8):
    result += min(dicts[i].items(), key=operator.itemgetter(1))[0]
print(result)
