from PIL import Image, ImageFilter
from array import array
import numpy as np

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

pix1 = im1.load()
pix2 = im2.load()
pix3 = im3.load()
pix4 = im4.load()
pix5 = im5.load()
pix6 = im6.load()
pix7 = im7.load()
pix8 = im8.load()
pix9 = im9.load()

xaz = 190 #Must keep changing 
yaz = 190 #Must keep changing

counter = 1

gashim = 0

hujye = []
cerdye = []
suitye = []



tatsunom = [pix1[xaz, yaz], pix2[xaz, yaz], pix3[xaz, yaz], pix4[xaz, yaz], pix5[xaz, yaz], pix6[xaz, yaz], pix7[xaz, yaz], pix8[xaz, yaz], pix9[xaz, yaz], ]

while(gashim < 9):
    hujye.append(tatsunom[gashim][0])
    cerdye.append(tatsunom[gashim][1])
    suitye.append(tatsunom[gashim][2])
    gashim = gashim + 1
    
print ("Tutom")
print (tatsunom)
print ("Saishi")
print (tatsunom[1][0])

print "Hujye"
red = (sorted(hujye))
print "Cerdye"
green = (sorted(cerdye))
print "Suitye"
blue = (sorted(suitye))
rojo =  red[4]
verde = green[4]
azul = blue[4]

testo = Image.new("RGB", (128, 128))
testopix = testo.load()

for x in range(128):
    for y in range(128):
        testopix[x,y] = (rojo, verde, azul)

testo.save("testo.png", "PNG")


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
print (hizo)
print (fizo)

xi = 0
yi = 0
nu = 0

chatsu = []

'''
while (xi < 495 and yi < 557):
    print (pix1[xi,yi])
    #chatsu.append(pix1[xi, 0])
    xi = xi+ 1
    if(xi >= 495):
        xi = 0
        yi = yi + 1
'''