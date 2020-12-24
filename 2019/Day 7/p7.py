import itertools
import threading
import copy
from feedback import intcode_computerz


inputf = open("input.txt", "r")
program = [int(token) for token in inputf.read().split(",")]
perms = list(itertools.permutations([5,6,7,8,9]))
max = float("-inf")
for perm in perms:
    valuess = [list(), list(), list(), list(), list()]
    available = []
    finished = []
    for i in range(5, 10):
        available.append(threading.Event())
        finished.append(threading.Event())
    threads = []
    valuess = [[], [], [], [], []]
    for i in range(0, 5):
        valuess[i].append(perm[i])
    valuess[0].append(0)
    for i in range(0, 4):
        thread = threading.Thread(target = intcode_computerz,\
                                  kwargs = {'program' : list(program),\
                                            'inputs' : valuess[i],\
                                            'outputs' : valuess[i+1],\
                                            'event1' : available[i],\
                                            'values' : valuess,\
                                            'event2' : available[i+1],\
                                            'finished' : finished[i],\
                                            'z' : i})
        thread.start()
    thread = threading.Thread(target = intcode_computerz,\
                              kwargs = {'program' : list(program),\
                                            'inputs' : valuess[4],\
                                            'outputs' : valuess[0],\
                                            'event1' : available[4],\
                                            'values' : valuess,\
                                            'event2' : available[0],\
                                            'finished' : finished[4],\
                                            'z' : 0})
    thread.start()
    for k in finished:
        k.wait()
    new = valuess[0].pop()
    if new > max:
        max = new
print(max)
