
inputf = open("input.txt", "r")
containers = [int(x) for x in inputf.read().split()]
import itertools
numbers = [1, 2, 3, 7, 7, 9, 10]
result = [seq for i in range(len(containers), 0, -1) for seq in itertools.combinations(containers, i) if sum(seq) == 150 and len(seq) == 4]
minim = float("inf")
print(len(result))
