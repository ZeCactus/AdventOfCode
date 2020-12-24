import copy
inputf = open("input.txt", "r")
tcode_length = 0
tstr_length = 0
for string in inputf.read().split():
    code_length = 0
    str_length = 0
    code_length = len(string)
    str_length = len(string) - 2
    cstring = copy.copy(string[1:-1])
    str_length -= cstring.count("\\\\")
    cstring = cstring.replace("\\\\", "")
    str_length -= cstring.count("\\\"")
    str_length -= (cstring.count("\\x")) * 3
    tcode_length += code_length
    tstr_length += str_length    
print(tcode_length - tstr_length)

