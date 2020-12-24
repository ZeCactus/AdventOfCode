
total = 0
import json
def parse_list(l):
    global total
    for item in l:
        if type(item) == list:
            parse_list(item)
        if type(item) == dict:
            parse_dict(item)
        if type(item) == int:
            total += item

def parse_dict(d):
    global total
    if "red" not in d.values():
        for value in d.values():
            if type(value) == list:
                parse_list(value)
            if type(value) == dict:
                parse_dict(value)
            if type(value) == int:
                total += value


inputf = open("input.txt", "r")
text = inputf.read()
j = json.loads(text)
parse_dict(j)
print(total)
