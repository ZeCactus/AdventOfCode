inputf = open("input.txt", "r")
text = inputf.read().split("\n")
text = [text[i].split() for i in range(0, len(text))]
for i in range(0, len(text)):
    for j in range(0, len(text[i])):
        if text[i][j].isdigit():
            text[i][j] = int(text[i][j])
i = 0
distance = {item[0]:0 for item in text}
points = {item[0]:0 for item in text}
while i < 2503:
    for item in text:
        cycle = item[2] + item[3]
        time = i % cycle
        if time < item[2]:
            distance[item[0]] += item[1]
    max_distance = max(list(distance.values()))
    for key in distance:
        if distance[key] == max_distance:
            points[key] += 1
    
    i += 1
