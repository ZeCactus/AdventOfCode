import sys
inputf = open("input.txt", "r")
ingredients = inputf.read().split("\n")
inputf.close()
ingredients = [ingredient.split() for ingredient in ingredients]
ingredients = [[int(x) if x.isdigit() or '-' in x else x for x in ingredient] for ingredient in ingredients]
inputf = open("results.txt", "r")
results = [[int(x) for x in result.split()] for result in inputf.read().split("\n")]
max_score = float("-inf")
outputf = open("test.txt", "w")
for result in results:
    score = 1
    for i in range(1, 5):
        current_score = 0
        for j in range(0, 4):
            current_score += ingredients[j][i] * result[j]
        if current_score < 0:
            score = 0
            break
        score *= current_score
    if score > max_score:
        calories = 0
        for i in range(0, 4):
            calories += ingredients[i][5] * result[i]
        if calories == 500:
            max_score = score
print(max_score)
