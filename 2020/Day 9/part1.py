file = open("input.txt", 'r')
preamble = 25
numbers = []
for i in range(0, preamble):
    numbers.append(int(file.readline()))
i = 0
while True:
    newnumber = int(file.readline())
    flag = False
    for j in range(0, len(numbers)):
        for k in range(j+1, len(numbers)):
            if numbers[j] + numbers[k] == newnumber:
                flag = True
    if flag == False:
        print(newnumber)
        break
    else:
        numbers[i] = newnumber
        i = i + 1
        if i == preamble:
            i = 0
