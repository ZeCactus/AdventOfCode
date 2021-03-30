def evaluate(arr):
    while "(" in arr:
        parantheses = 0
        for i in range(0, len(arr)):
            if arr[i] == "(":
                parantheses = 1
                break
        for j in range(i+1, len(arr)):
            ex = arr[j]
            if arr[j] == "(":
                parantheses = parantheses + 1
            if arr[j] == ")":
                parantheses = parantheses - 1
            if parantheses == 0:
                break
        arr[i:j+1] = [evaluate(arr[i+1:j])]
    while len(arr) > 1:
        if arr[1] == "+":
            arr[0:3] = [arr[0] + arr[2]]
        else:
            arr[0:3] = [arr[0] * arr[2]]
    return arr[0]


sum = 0
with open("input.txt", "r") as file:
    for line in file:
        arr = []
        for character in line.strip().replace(" ", ""):
            try:
                arr.append(int(character))
            except ValueError:
                arr.append(character)
        sum = sum + evaluate(arr)
print(sum)