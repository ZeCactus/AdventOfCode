inputf = open("input.txt", "r")
par = [char for char in inputf.read()]
floor = 0
for i in range(0, len(par)):
    if par[i] == '(':
        floor += 1
    if par[i] == ')':
        floor -= 1
    if floor < 0:
        print(i)
        break
