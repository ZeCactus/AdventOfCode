import copy
numbers = []
with open("test.txt", "r") as file:
    for line in file:
        numbers.append(int(line))
numbers.sort()
device = numbers[-1]+3
numbers.append(device)
combinations = [([0], copy.deepcopy(numbers))]
while True:
    flag = False
    for combination in combinations:
        chain = combination[0]
        if chain[-1] == device:
            continue
        flag = True
        current = chain[-1]
        arr = combination[1]
        for i in range(0, len(arr)):
            diff = arr[i] - current
            if diff not in range(0, 4):
                break
            else:
                arrcopy = copy.deepcopy(arr)
                chaincopy = copy.deepcopy(chain)
                chaincopy.append(arrcopy[i])
                arrcopy = arrcopy[i:]
                i = 0
                combinations.append(copy.deepcopy((chaincopy, arrcopy)))
    if flag == False:
        break
    print(combinations, "\n\n\n")
print(combinations)
