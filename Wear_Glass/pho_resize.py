from PIL import Image

infile = './whiteglass.png'
outfile = './whitesmallglass.png'


im = Image.open(infile)

(x,y) = im.size
x_s = 400
y_s = y*x_s/x

out=im.resize((x_s,y_s),Image.ANTIALIAS)
out.save(outfile)