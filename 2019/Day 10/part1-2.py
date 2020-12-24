import copy

def find_visible(x,y):
    
inputf = open("part1.txt", "r")
asteroids = [list(line) for line in inputf.read().split()]
##for y in range(len(asteroids)):
##    for x in range(len(asteroids[y])):
##        if asteroids[y][x] == '#':
##            
