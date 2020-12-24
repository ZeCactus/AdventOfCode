import copy
def opcomp(list, a1, a2):
    list[1] = a1
    list[2] = a2
    try:
        for i in range(0, len(list), 4):
            if list[i] == 99:
                break
            elif list[i] == 1:
                list[list[i+3]] = list[list[i+1]] + list[list[i+2]]
            elif list[i] == 2:
                list[list[i+3]] = list[list[i+1]] * list[list[i+2]]
        return list[0]
    except IndexError:
        return -1

inputf = open("input.txt","r")
listz = [int(token) for token in inputf.read().split(",")]
for i in range(0,99):
    for j in range(0,99):
        listcopy = copy.deepcopy(listz)
        if opcomp(listcopy,i,j) == 19690720:
            print(100 * i + j)
