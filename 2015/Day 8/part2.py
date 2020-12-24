import copy
inputf = open("input.txt", "r")
added = 0
for string in inputf.read().split():
    added += 2
    added += string.count("\"")
    added += string.count("\\")
print(added)
