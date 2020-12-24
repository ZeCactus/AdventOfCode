numbers = []
with open("input.txt", "r") as file:
    for item in file.readlines():
        numbers.append(int(item.strip()))
for i in range(0, len(numbers)):
    for j in range(i+1, len(numbers)):
        for k in range(j+1, len(numbers)):
            if numbers[i] + numbers[j] + numbers[k] == 2020:
                print(numbers[i]*numbers[j]*numbers[k])
