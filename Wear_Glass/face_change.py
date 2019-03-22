import urllib3,base64
import urllib
import json
from PIL import Image


# lefteyex=finallresult['result']['face_list'][0]['landmark'][0]['x']
# lefteyey=finallresult['result']['face_list'][0]['landmark'][0]['y']
# righteyex=finallresult['result']['face_list'][0]['landmark'][1]['x']
# righteyey=finallresult['result']['face_list'][0]['landmark'][1]['y']
# rotation=finallresult['result']['face_list'][0]['location']['rotation']
# facepoint=finallresult['result']['face_list'][0]['landmark72']
# print facepoint[0]['x']
# print lefteyex
# print lefteyey
# print righteyex
# print righteyey
# print rotation


distance = righteyex - lefteyex
img1 = img1.rotate(rotation)
glass = Image.open('whiteglass.png')
ratio = distance/400
(x,y) = glass.size
print glass.size[0]
x_s = int(glass.size[0]*ratio)
y_s = y*x_s/x
out=glass.resize((x_s,y_s),Image.ANTIALIAS)
placex=int((lefteyex+righteyex)/2-(out.size[0]/2))
placey=int((lefteyey+righteyey)/2-(out.size[1]/2))
img1.paste(out,(placex,placey+15),mask=out)
img1.show()


