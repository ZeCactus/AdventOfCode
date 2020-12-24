inputf = open("input.txt", "r")
from PIL import Image
layer = []
final = []
for i in range(0, 6):
    final.append([2 for i in range(0,25)])
text = inputf.read(150)
for i in range(0, 150, 25):
    layer.append([int(char) for char in text[i:i+25]])
while len(text) != 0:
    for i in range(0, 6):
        for j in range(0, 25):
            if layer[i][j] != 2 and final[i][j] == 2:
                final[i][j] = layer[i][j]
    layer = []
    text = inputf.read(150)
    for i in range(0, 150, 25):
        layer.append([int(char) for char in text[i:i+25]])
img = Image.new("RGB", (50, 12), "blue")
pixels = img.load()
for i in range(0, 6):
    for j in range(0, 25):
        if final[i][j] == 0:
            pixels[j*2, i*2] = (0, 0, 0)
            pixels[j*2, i*2+1] = (0, 0, 0)
            pixels[j*2+1, i*2] = (0, 0, 0)
            pixels[j*2+1, i*2+1] = (0, 0, 0)
        else:
            pixels[j*2, i*2] = (255, 255, 255)
            pixels[j*2, i*2+1] = (255, 255, 255)
            pixels[j*2+1, i*2] = (255, 255, 255)
            pixels[j*2+1, i*2+1] = (255, 255, 255)
            
img.show()
