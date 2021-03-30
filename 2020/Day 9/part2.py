file = open("input.txt", 'r')
preamble = 25
numbers = []
for i in range(0, preamble):
    numbers.append(int(file.readline()))
i = 0
target = 0
while True:
    newnumber = int(file.readline())
    flag = False
    for j in range(0, len(numbers)):
        for k in range(j+1, len(numbers)):
            if numbers[j] + numbers[k] == newnumber:
                flag = True
    if flag == False:
        target = newnumber
        break
    else:
        numbers[i] = newnumber
        i = i + 1
        if i == preamble:
            i = 0
file.close()
file = open("input.txt", 'r')
numbers = []
for line in file:
    numbers.append(int(line))
file.close()
l = 0
h = 0
for low in range(0, len(numbers)):
    for high in range(low + 1, len(numbers)):
        result = 0
        flag = False
        for i in range(low, high+1):
            result = result + numbers[i]
            if result > target:
                flag = True
                break
        if flag == True:
            continue
        if result == target:
            min = numbers[low]
            max = numbers[low]
            for i in range(low, high + 1):
                if numbers[i] < min:
                    min = numbers[i]
                if numbers[i] > max:
                    max = numbers[i]
            print(min + max)
            break
