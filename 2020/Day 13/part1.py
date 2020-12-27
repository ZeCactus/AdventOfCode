with open("input.txt", "r") as file:
    time = int(file.readline())
    min = float("inf")
    res = 0
    for val in file.readline().strip().split(","):
        if val == "x":
            continue
        id = int(val)
        wait = id - (time % id)
        if wait < min:
            min = wait
            res = id * wait
print(res)