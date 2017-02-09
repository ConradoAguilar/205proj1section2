##  Conrado Aguilar
##  CST 205 -- Section 2
##  Project 1

from PIL import Image, ImageFilter
from array import array
import numpy as np
import os

count = 0

def fcount(path):
    count = 0
    for f in os.listdir(path):
        if os.path.isfile(os.path.join(path, f)):
            count = count + 1
    return count
    
path = "./Project1Images"
hiso = fcount(path)

'''Initialization of Arrays and Variables'''
imgList = []                     ##list for images
dim = []                         ##list for size of images
varsx = []                       ##Empty for x
varsy = []                       ##Empty for y
red = 0                          ##RGB Red
green = 0                        ##RGB Green
blue = 0                         ##RGB Blue

for i in range(hiso):               ##Loading all 9 images 
    imgList.append(Image.open("Project1Images/" + str(i+1) + ".png"))
    
'''Finding size of all 9 images'''
for i in range(hiso):            
    dim.append(imgList[i].size)  ##Creating array of the sizes
    
'''Splitting the x and y axis'''
for i in range(hiso):           
    varsx.append(dim[i][0])      ##
    varsy.append(dim[i][1])      ##
minsox = ((sorted(varsx))[0])    ##Array for x values; Already chosen smallest value ------
minsoy = ((sorted(varsy))[0])    ##Array for y values; Already chosen smallest value ------

'''Proper median for odd and even integers'''
med = 0
if (hiso%2 == 1):
    med = int((hiso-1)/2)
else:
    med = int((hiso/2))

'''Creation of new image'''
testo = Image.new("RGB", (minsox, minsoy))##__##__## Creation of the merged image
testopix = testo.load()

'''Commencement of new picture'''
for x in range(minsox):
    for y in range(minsoy):
        vori = []  
        versi = []
    ##Loading pixels
        for i in range(hiso):
            vori.append(imgList[i - 1].load())

        for i in range(hiso):               ##Spliting colors
            versi = (vori[i - 1][x,y])


        hujye = []
        cerdye = []
        suitye = []
        test = []

        for i in range(hiso):              
            test.append(vori[i-1][x,y]) ##9 pictures; same coordinates
            hujye.append(test[i][0])    ##Red
            cerdye.append(test[i][1])   ##Green
            suitye.append(test[i][2])   ##Blue
##Sorting
            hujye = sorted(hujye)       ##Red 
            cerdye = sorted(cerdye)     ##Green
            suitye = sorted(suitye)     ##Blue

        if(hiso%2 == 1):
            red = hujye[med]                                  ##Finds median of Red; Odd number of pictures
            green = cerdye[med]                               ##Finds median of Green; Odd number of pictures
            blue = suitye[med]                                ##Finds median of Blue; Odd number of pictures
        else:
            red = int((hujye[med-1] + hujye [med])/2)         ##Finds median of Red; Even number of pictures
            green = int((cerdye[med-1] + cerdye [med])/2)     ##Finds median of Green; Even number of pictures
            blue = int((suitye[med-1] + suitye [med])/2)      ##Finds median of Blue; Even number of pictures
        
        testopix[x,y] = (red, green, blue)                    ##Giving RGB values to pixels

testo.save("testo.png", "PNG") #Saves the image
print ("Done!")                ##Is finished