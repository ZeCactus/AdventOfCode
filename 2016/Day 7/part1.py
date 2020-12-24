amount = 0
with open("input.txt") as file:
    for ip in file:
        ip = ip.strip()
        count = ip.count('[')
        inside = []
        outside = []
        for i in range(0, count):
            outside.append(ip.split('[', 1)[0])
            inside.append(ip.split('[', 1)[1].split(']', 1)[0])
            ip = ip.split(']', 1)[1]
        if ip != "":
            outside.append(ip)
        check = True
        for part in inside:
            for i in range(0, len(part)-4):
                if part[i] == part[i+3] and part[i+1] == part[i+2] and part[i] != part[i+1]:
                    check = False
                    break
            if check == False:
                break
        if check == False:
            continue
        check = False
        for part in outside:
            for i in range(0, len(part)-3):
                if part[i] == part[i+3] and part[i+1] == part[i+2] and part[i] != part[i+1]:
                    check = True
                    break
            if check == True:
                break
        if check == False:
            continue
        amount += 1
print(amount)
        
