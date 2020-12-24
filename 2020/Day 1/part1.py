bigger = []
smaller = []
flag1 = False
flag2 = False
with open("input.txt", "r") as input:
    for line in input:
        nr = int(line)
        if nr == 1010:
            if flag == True:
                print(1010*1010)
                flag2 = True
                break
            else:
                flag = True
        else:
            if nr > 1010:
                bigger.append(nr)
            else:
                smaller.append(nr)
if flag2 != True:
    for nr1 in bigger:
        for nr2 in smaller:
            if nr1 + nr2 == 2020:
                print(nr1 * nr2)
                flag2 = True
                break
        if flag2 == True:
            break
    
