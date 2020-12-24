inputf = open("input.txt", "r")
text = inputf.read().split("\n")
text = [text[i].split() for i in range(0, len(text))]
for i in range(0, len(text)):
    for j in range(0, len(text[i])):
        if text[i][j].isdigit():
            text[i][j] = int(text[i][j])
max_distance = float("-inf")
time = 2503
for item in text:
    distance = 0
    cycle = item[2] + item[3]
    times = int(time/cycle)
    extra = int(time%cycle)
    if extra >= item[2]:
        times += 1
    else:
        distance += item[1] * extra
    distance += item[1] * item[2] * times
    if distance > max_distance:
        max_distance = distance
print(max_distance)
