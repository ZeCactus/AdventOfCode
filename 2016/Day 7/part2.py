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
        abas = []
        for part in outside:
            for i in range(0, len(part)-2):
                if part[i] == part[i+2] and part[i] != part[i+1]:
                    abas.append(part[i:i+3])
        if len(abas) == 0:
            continue
        check = False
        for part in inside:
            for aba in abas:
                bab = ""
                bab += aba[1] + aba[0] + aba[1]
                if bab in part:
                    check = True
        if check == True:
            amount += 1
print(amount)
        
