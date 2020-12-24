from computer import intcode_computer
import computer
output = []
inputf = open("input.txt", "r")
program = [int(token) for token in inputf.read().split(",")]
inputf.close()
intcode_computer(program, [])
