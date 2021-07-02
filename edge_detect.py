import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as img
from PIL import Image as im
import math


img=im.open("Original_assets/edge-detection.png")
img=np.array(img)
h,w,c=img.shape
# print(hexme)

def gray_me(hexme):
    gray=np.zeros((h,w))
    for i in range(h):
        for j in range(w):
            gray[i,j]=0.3*hexme[i,j,0]+0.59*hexme[i,j,1]+0.11*hexme[i,j,2]
    return gray

def apply_kernel(kernel,img):
    print(kernel)
    new_img=np.zeros_like(img)
    h,w=img.shape
    for i in range(3,h-3):
        for j in range(3,w-3):
            x=np.sum(img[i:i+3, j:j+3]*kernel)
            if(x<0):x=0
            elif(x>255):x=255
            new_img[i][j]=x
            
    new_img=new_img/new_img.max()*255
    return new_img

def suppress_nonmax(img,angle):
    new_img=np.zeros_like(img)
    for i in range(1,h-1):
        for j in range(1,w-1):
            #angle 0
            if (0 <= angle[i,j] < 22.5) or (157.5 <= angle[i,j] <= 180):
                q = img[i, j+1]
                r = img[i, j-1]
            #angle 45
            elif (22.5 <= angle[i,j] < 67.5):
                q = img[i+1, j-1]
                r = img[i-1, j+1]
            #angle 90
            elif (67.5 <= angle[i,j] < 112.5):
                q = img[i+1, j]
                r = img[i-1, j]
            #angle 135
            elif (112.5 <= angle[i,j] < 157.5):
                q = img[i-1, j-1]
                r = img[i+1, j+1]
            if(img[i][j]>=q and img[i][j]>=q):
                new_img=img
    return new_img
            

def threshold(img,low=0.05,high=0.09):
    hight=img.max()*high
    lowt=hight*low
    strongi,strongj=np.where(img >= hight)
    weaki,weakj=np.where((img>=lowt) & (img<=hight))
    new_img=np.zeros_like(img)
    new_img[strongi,strongj]=255
    new_img[weaki,weakj]=25
    kernel=np.array([[1,1,1],[1,0,1],[1,1,1]])
    new_img2=np.zeros_like(img)
    for i in range(3,h-3):
        for j in range(3,w-3):
            if(new_img[i,j]==25):
                x=np.sum(new_img[i:i+3, j:j+3]*kernel)
                if(x>=255):
                    new_img2[i,j]=255
            elif(new_img[i,j]==255):
                new_img2[i,j]=255
    return new_img2
                
img=gray_me(img)
# smoothning
kernel=np.array([[1/16,2/16,1/16],[1/8,1/4,1/8],[1/16,2/16,1/16]])
img=apply_kernel(kernel,img)
#vertical
kernel=np.array([[-1,0,1], [-2,0,2], [-1,0,1]])
imgy=apply_kernel(kernel,img)
#horizontal
kernel= np.array([[-1,-2,-1], [0,0,0], [1,2,1]])
imgx=apply_kernel(kernel,img)
##SOBEL
img=np.sqrt(np.square(imgx)+np.square(imgy))
##canny
# theta=np.arctan2(imgy,imgx)
# img=suppress_nonmax(img,theta)
# img=threshold(img)

img=img.astype(np.uint8)
po = im.fromarray(imgy)
# po.save("horizontal.png")
im._show(po)
