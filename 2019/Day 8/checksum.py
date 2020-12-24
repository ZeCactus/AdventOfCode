inputf = open("input.txt", "r")
layer = [int(char) for char in inputf.read(150)]
fewest_zeroes = float("inf")
while layer:
    zeroes = sum(token == 0 for token in layer)
    if zeroes < fewest_zeroes:
        fewest_zeroes = zeroes
        fewest_layer = layer
    layer = [int(char) for char in inputf.read(150)]
print(sum(token == 1 for token in fewest_layer) * sum(token == 2 for token in fewest_layer))
