import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as img
from PIL import Image as im
import math


img=im.open("SRA-Assignments/img_processing/morphological.png")
hexme=np.array(img)
h,w,c=hexme.shape

def horizontal_edge(hexme):
    # hexme=gray_me(hexme)
    # hexme=weighted_filter(hexme)
    sumi=np.zeros((5,5,3),dtype=np.uint32)
    weight=np.array([-1,-1,-1,0,0,0,1,1,1])
    weight.shape=(3,3)
    print(weight)
    for i in range(h):
        for j in range(w):
            if(i<=5 or j<=5 or i>=h-5 or j>=w-5):
                continue
            else:
                sumi=hexme[i-1:i+2,j-1:j+2]
                # print(hexme[i-1:i+2,j-1:j+2])
                sumi=sumi*weight
            sumi=np.sum(sumi,axis=0)
            sumi=np.sum(sumi,axis=0)
            # print(sumi)
            if(sumi>200):sumi=255
            elif(sumi<50):sumi=0
            hexme[i,j]=sumi
    # print(hexme)
    return hexme

def sobel_edge(hexme):
    # hexme=gray_me(hexme)
    # hexme=weighted_filter(hexme)
    sumx=np.zeros((3,3),dtype=np.uint32)
    sumy=np.zeros((3,3),dtype=np.uint32)
    gx=np.array([1,0,-1,2,0,-2,1,0,-1])
    gy=np.array([-1,-2,-1,0,0,0,1,2,1])
    gx.shape=(3,3)
    gy.shape=(3,3)
    print(hexme.shape)
    print(gx)
    print(gy)
    for i in range(h):
        for j in range(w):
            if(i<=5 or j<=5 or i>=h-5 or j>=w-5):
                continue
            else:
                sumx=hexme[i-1:i+2,j-1:j+2]
                sumy=hexme[i-1:i+2,j-1:j+2]
                sumx =sumx*gx
                sumy =sumx*gy
            sumx=np.sum(sumx,axis=0)
            sumx=np.sum(sumx,axis=0)
            sumy=np.sum(sumy,axis=0)
            sumy=np.sum(sumy,axis=0)
            sumi=int(math.sqrt(sumx**2+sumy**2))
            # if(sumi>200):sumi=255
            # elif(sumi<50):sumi=0
            hexme[i,j]=sumy
    return hexme


def gray_me(hexme):
    gray=np.zeros((h,w))
    for i in range(h):
        for j in range(w):
            gray[i,j]=0.3*hexme[i,j,0]+0.59*hexme[i,j,1]+0.11*hexme[i,j,2]
    return gray

def dialition(hexme):
    hexme=gray_me(hexme)
    newme=np.zeros_like(hexme)
    weight=np.array([[255,255],[0,0]])
    hexme[hexme>125]=255
    hexme[hexme<=125]=0
    for i in range(h):
        for j in range(w):
            if(i<=5 or j<=5 or i>=h-5 or j>=w-5):
                continue
            if(hexme[i,j]==255):newme[i,j],newme[i,j+1]=255,255
    return newme


def erosion(hexme):
    hexme=gray_me(hexme)
    newme=np.zeros_like(hexme)
    newme[:]=255
    weight=np.array([[255,255],[0,0]])
    hexme[hexme>125]=255
    hexme[hexme<=125]=0
    for i in range(h):
        for j in range(w):
            if(i<=5 or j<=5 or i>=h-5 or j>=w-5):
                continue
            sumi=hexme[i:i+2,j:j+1]
            if(weight.all()==sumi.all()):
                newme[i,j]=0
    return newme

# hexme=dialition(hexme)
hexme=erosion(hexme)
# hexme=horizontal_edge(hexme)
po = im.fromarray(hexme)
im._show(po)

