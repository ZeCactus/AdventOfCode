from __future__ import annotations
class Node:
    next: Node
    val: int
    def __init__(self, v: int):
        self.val = v

x=712643589
#x = 389125467
cups = []
while x != 0:
    cups.append(x%10)
    x = int(x/10)
for i in range(10, 1000001):
    cups.append(i)
cups.reverse()
picked = []
curr = 0
label = cups[curr]
for i in range(0, 10000000):
    for j in range(1, 4):
        try:
            picked.append(cups.pop(curr + 1))
        except IndexError:
            picked.append(cups.pop(0))
    labelcopy = label
    while True:
        try:
            if label - 1 == 0:
                label = 1000001;
            destination = cups.index(label-1)
            break
        except ValueError:
            label = label - 1
            continue
    for k in range(0, 3):
        cups.insert(destination+1, picked.pop(-1))
    curr = cups.index(labelcopy) + 1
    if curr == 1000000:
        curr = 0
    label = cups[curr]
    if i%10000 == 0 :
        print(i)
