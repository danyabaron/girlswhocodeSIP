from Myro import *
picture = makePicture("grumpycat.jpg")
show(picture)
obama_red = makeColor(217,26,33)
obama_yellow= makeColor(252,227,166)
obama_darkBlue = makeColor(0,51,76)
obama_blue = makeColor(112,150,158)

pixels = getPixels(picture) 

for pixel in pixels:
    grey =(getRed(pixel)+getGreen(pixel)+getBlue(pixel))/3
    if grey > 180:
        setColor(pixel,obama_yellow)
    elif grey > 120:
        setColor(pixel,obama_blue)
    elif grey > 60:
        setColor(pixel,obama_red)
    else: 
        setColor(pixel,obama_darkBlue)
show(picture)   
    