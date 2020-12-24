inputf = open("input.txt","r")
list = [int(token) for token in inputf.read().split(",")]
list[1] = 12
list[2] = 2
for i in range(0, len(list), 4):
    if list[i] == 99:
        break
    elif list[i] == 1:
        list[list[i+3]] = list[list[i+1]] + list[list[i+2]]
    elif list[i] == 2:
        list[list[i+3]] = list[list[i+1]] * list[list[i+2]]
print(list[0])
