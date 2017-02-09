##  Conrado Aguilar
##  CST 205 -- Section 2
##  Project 1
##  Github link
##  https://github.com/ConradoAguilar/205proj1section2

from PIL import Image, ImageFilter
from array import array
import numpy as np
import os

def imgcount(path):                               ##New function for counting files
    count = 0
    for f in os.listdir(path):                    ##
        if os.path.isfile(os.path.join(path, f)): ##
            count = count + 1                     ##
    return count                                  ##
    
path = "./Project1Images"
numpic = imgcount(path)

'''Initialization of Arrays and Variables'''
imgList = []                     ##list for images
imgsize = []                     ##list for size of images
varsx = []                       ##Empty for x
varsy = []                       ##Empty for y
red = 0                          ##RGB Red
green = 0                        ##RGB Green
blue = 0                         ##RGB Blue

for i in range(numpic):                                               ##Loading all 9 images 
    imgList.append(Image.open("Project1Images/" + str(i+1) + ".png")) ##Loads images into array
    
'''Finding size of all 9 images'''
for i in range(numpic):            
    imgsize.append(imgList[i].size)  ##Creating array of the sizes
    
'''Splitting the x and y axis'''
for i in range(numpic):           
    varsx.append(imgsize[i][0])      ##Splits into x values
    varsy.append(imgsize[i][1])      ##Splits into y values
    
minsox = ((sorted(varsx))[0])     ##Array for x values; Already chosen smallest value ------
minsoy = ((sorted(varsy))[0])     ##Array for y values; Already chosen smallest value ------

'''Proper median for odd and even integers'''
med = 0
if (numpic%2 == 1):
    med = int((numpic-1)/2)
else:
    med = int((numpic/2))

'''Creation of new image'''
finalimg = Image.new("RGB", (minsox, minsoy)) ##__##__## Creation of the new image
finalimgpix = finalimg.load()

'''Commencement of new picture'''
for x in range(minsox):
    for y in range(minsoy):
        vori = []    ##
        versi = []   ##
    ##Loading pixels
        for i in range(numpic):
            vori.append(imgList[i - 1].load()) ##Loads pixels

        for i in range(numpic):               
            versi = (vori[i - 1][x,y])         ##Loads RGB for specific pixel


        rojo = []      ##Arary for Red RGB
        verde = []     ##Array for Green RGB
        azul = []      ##Array for Blue RGB
        test = []      ##

        for i in range(numpic):              
            test.append(vori[i-1][x,y]) ##9 pictures; same coordinates
            rojo.append(test[i][0])     ##Red
            verde.append(test[i][1])    ##Green
            azul.append(test[i][2])     ##Blue
##Sorting
            rojo = sorted(rojo)       ##Red 
            verde = sorted(verde)     ##Green
            azul = sorted(azul)       ##Blue

        if(numpic%2 == 1):
            red = rojo[med]                                  ##Finds median of Red; Odd number of pictures
            green = verde[med]                               ##Finds median of Green; Odd number of pictures
            blue = azul[med]                                ##Finds median of Blue; Odd number of pictures
        else:
            red = int((rojo[med-1] + rojo [med])/2)         ##Finds median of Red; Even number of pictures
            green = int((verde[med-1] + verde [med])/2)     ##Finds median of Green; Even number of pictures
            blue = int((azul[med-1] + azul [med])/2)      ##Finds median of Blue; Even number of pictures
        
        finalimgpix[x,y] = (red, green, blue)                    ##Giving RGB values to pixels

finalimg.save("FinishedPicture.png", "PNG") #Saves the image
print ("Done!")                ##Is finished