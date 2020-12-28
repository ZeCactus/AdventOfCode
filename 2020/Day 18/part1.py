def evaluate(arr):
    op = ""
    parantheses = 0
    while len(arr) > 2:
        op = arr[1]
        if arr[0] == "(":
            parantheses = 1
            for i in range(1, len(arr)):
                if parantheses == 0:
                    break
                if arr[i] == ")":
                    parantheses = parantheses - 1
                if arr[i] == "(":
                    parantheses = parantheses + 1
            arr[0:i] = [evaluate(arr[1:i-1])]

        elif arr[2] == "(":
            parantheses = 1
            for i in range(3, len(arr)):
                if parantheses == 0:
                    break
                if arr[i] == ")":
                    parantheses = parantheses - 1
                if arr[i] == "(":
                    parantheses = parantheses + 1
            if i == len(arr) - 1:
                arr[2:i+1] = [evaluate(arr[3:i])]
            else:
                arr[2:i] = [evaluate(arr[3:i-1])]
        else:
            if op == "+":
                arr[0:3] = [int(arr[0]) + int(arr[2])]
            else:
                arr[0:3] = [int(arr[0]) * int(arr[2])]
    return arr[0]


sum = 0
with open("input.txt", "r") as file:
    for line in file:
        arr = []
        for character in line.strip().replace(" ", ""):
            arr.append(character)
        sum = sum + evaluate(arr)
print(sum)