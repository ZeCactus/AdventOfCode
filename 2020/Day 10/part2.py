import copy
numbers = []
with open("input.txt", "r") as file:
    for line in file:
        numbers.append(int(line))
numbers.sort()
device = numbers[-1]+3
numbers.append(device)
combinations = [([0], copy.deepcopy(numbers))]
newcombinations = []
print("start")
while True:
    print(len(combinations))
    newcombinations = []
    flag = False
    for combination in combinations:
        chain = copy.deepcopy(combination[0])
        numbers = copy.deepcopy(combination[1])
        if chain[-1] == device:
            newcombinations.append((copy.deepcopy(chain), copy.deepcopy(numbers)))
            continue
        else:
            flag = True
            current = chain[-1]
            kap = 0
            for i in range(0, len(numbers)):
                diff = numbers[i] - current
                if diff < 4:
                    newnumbers = copy.deepcopy(numbers)
                    newchain = copy.deepcopy(chain)
                    newchain.append(numbers[i])
                    newnumbers = copy.deepcopy(numbers[i+1:])
                    newcombinations.append((copy.deepcopy(newchain), copy.deepcopy(newnumbers)))
                else:
                    break
                kap = kap+1
    combinations = copy.deepcopy(newcombinations)
    if flag == False:
        break

print(len(combinations))
