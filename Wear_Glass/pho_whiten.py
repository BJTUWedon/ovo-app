from PIL import Image

img = Image.open("./round_glass.jpg")
img = img.convert("RGBA")
datas = img.getdata()
newData = list()
for item in datas:
    if item[0] >220 and item[1] > 220 and item[2] > 220:
        newData.append(( 255, 255, 255, 0))
    else:
        newData.append(item)

img.putdata(newData)
img.save("whiteglass.png","png")