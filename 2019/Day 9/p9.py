from computer import intcode_computer

inputf = open("input.txt", "r")
program = [int(token) for token in inputf.read().split(",")]
inputs = [2]
intcode_computer(program, inputs)
