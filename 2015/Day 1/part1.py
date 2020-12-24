inputf = open("input.txt", "r")
par = [char for char in inputf.read()]
print(par.count('(') - par.count(')'))
