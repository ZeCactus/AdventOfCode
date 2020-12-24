inputf = open("input.txt", "r")
nice = 0
vowels = "aeiou"
forbidden = ["ab", "cd", "pq", "xy"]
for line in inputf.read().split():
    naughty = [group in line for group in forbidden]
    if True in naughty:
        continue
    naughty = 0
    for vowel in vowels:
        naughty += line.count(vowel)
    if naughty < 3:
        continue
    naughty = True
    for i in range(0, len(line)-1):
        if line[i] == line[i+1]:
            naughty = False
            break
    if naughty == True:
        continue
    nice += 1
