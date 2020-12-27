numbers = [0]
with open("input.txt", "r") as file:
    for line in file:
        numbers.append(int(line))
numbers.sort()
dif1 = 0
dif3 = 1
for i in range(1, len(numbers)):
    dif = numbers[i] - numbers[i-1]
    if dif == 1:
        dif1 = dif1 + 1
    if dif == 3:
        dif3 = dif3 + 1
print(dif1 * dif3)
