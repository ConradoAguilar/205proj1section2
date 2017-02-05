from PIL import Image, ImageFilter
from array import array
import numpy as np

counter = 1




''''
try:
    # Load an image from the hard drive
    original = Image.open("9.png")

    blurred = original.filter(ImageFilter.BLUR)     # Blur the image

    blurred.save("no.png")     # save the new image



except:
    print ("Unable to load image")
    '''
#response = input("How many pictures are there?\n")

im1 = Image.open("1.png") 
im2 = Image.open("2.png")
im3 = Image.open("3.png")
im4 = Image.open("4.png") 
im5 = Image.open("5.png")
im6 = Image.open("6.png") 
im7 = Image.open("7.png")
im8 = Image.open("8.png")
im9 = Image.open("9.png")

#while(counter <= 10):
    

pix1 = im1.load()
pix2 = im2.load()
pix3 = im3.load()
pix4 = im4.load()
pix5 = im5.load()
pix6 = im6.load()
pix7 = im7.load()
pix8 = im8.load()
pix9 = im9.load()

agrio1 = (im1.size) 
agrio2 = (im2.size)

loyetude1 = (agrio1) #hanotso vem fazotso
loyetude2 = (agrio2)
hano = loyetude1[0], loyetude2[0]
fazo = loyetude1[1], loyetude2[1]
hizo =  (min(hano))
fizo =  (min(fazo))

tutom = []
tutom.append(loyetude1[0]);
tutom.append(loyetude2[0]);
print (tutom[0])
xi = 0
yi = 0

im = Image.new("RGB", (hizo, fizo))
pix = im.load()
for x in range(hizo):
    for y in range(fizo):
        pix[x,y] = (255, 20, 147)

im.save("test.png")


chatsu = []

while (xi < 495):
    print (pix1[xi,yi])
    #chatsu.append(pix1[xi, 0])
    xi = xi+ 1
    if(xi >= 495):
        xi = 0
        yi = yi + 1
    #Get the RGBA Value of the a pixel of an image
#im9.save("kaji.png")