

with open('cleanedinput.txt') as f:
    for line in f:
        room = line.rsplit('-', 1)
        string = room[0].replace('-', ' ')
        rotation = int(room[1].split('[')[0])
        newstring = ""
        for char in string:
            newstring += chr((ord(char)-97 + rotation)%26+97) if char != ' ' else ' '
        if "north" in newstring:
            print(newstring, rotation)