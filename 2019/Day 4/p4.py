inputf = open("input.txt", "r")
low,high = [int(token) for token in inputf.read().split("-")]
passwords = 0
#low = 100
#high = 300
outputf = open("output.txt", "w")
while low - 1 <= high:
    i = str(low)
    dif = 1
    changed = True
    while changed:
        changed = False
        i = str(low)
        for j in range(len(i)-1,0,-1):
            if i[j] < i[j-1]:
                dif = int(i[j-1]) - int(i[j])
                dif = dif * pow(10,len(i)-j-1)
                low = low + dif
                changed = True
    if low > high:
        break
    i = str(low)
    double = False
    for j in range(0,len(i)-1):
        if (i[j] == i[j+1])\
           and (j == 0 or i[j-1] != i[j])\
           and (j == len(i) - 2 or i[j+2] != i[j]):
            double = True
    if double == True:
        passwords += 1
    low += 1
print(passwords)
