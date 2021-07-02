import numpy as np

import matplotlib.pyplot as plt
import matplotlib.image as img
from PIL import Image as im

img=im.open("SRA-Assignments/img_processing/filter.png")
hexme=np.array(img)
h,w,c=hexme.shape


########box filter ---- smoothning spatial --noise gets removed at the cost of sharpness of image---spatial low pass filter
def mean_filter(hexme):
    sumi=np.zeros((5,5),dtype=np.uint32)
    for i in range(h):
        for j in range(w):
            if(i==0 and j==0):
                sumi=hexme[:2,:2]
            elif(i==0):sumi=hexme[:3,j-2:j+3]
            elif(j==0):sumi=hexme[i-2:i+3,:3]
            else:
                sumi=hexme[i-2:i+3,j-2:j+3]
            sumi=np.sum(sumi,axis=0)
            sumi=np.sum(sumi,axis=0)
            sumi=sumi//25
            # print(sumi)
            hexme[i,j]=sumi
    return hexme



def weighted_filter(hexme):
    sumi=np.zeros((5,5,3),dtype=np.uint32)
    weight=np.array([1,4,6,4,1,4,16,24,16,4,6,24,36,24,6,4,16,24,16,4,1,4,6,4,1,1,4,6,4,1,4,16,24,16,4,6,24,36,24,6,4,16,24,16,4,1,4,6,4,1,1,4,6,4,1,4,16,24,16,4,6,24,36,24,6,4,16,24,16,4,1,4,6,4,1])
    # weight=np.reshape(weight,(5,5))
    weight.shape=(5,5,3)
    # print(weight.shape)
    # print(hexme)
    # print(weight)
    for i in range(h):
        for j in range(w):
            if(i<=5 or j<=5 or i>=h-5 or j>=w-5):
                continue
            else:
                sumi=hexme[i-2:i+3,j-2:j+3]
                sumi=sumi*weight
            sumi=np.sum(sumi,axis=0)
            sumi=np.sum(sumi,axis=0)//256
            # print(sumi)
            hexme[i,j]=sumi
    # print(hexme)
    return hexme


##this median filter removes the noise with minimal smoothning
def median_filter(hexme):
    sumi=np.zeros((5,5,3),dtype=np.uint32)
    for i in range(h):
        for j in range(w):
            if(i<=5 or j<=5 or i>=h-5 or j>=w-5):
                continue
            else:
                sumi=hexme[i-2:i+3,j-2:j+3]
                sumi=np.median(sumi,axis=0)
                sumi=np.median(sumi,axis=0)
                hexme[i,j]=sumi
    return hexme


#####laplacian sharpning whith negative center
def laplacian_sharpning(hexme):
    sumi=np.zeros((5,5,3),dtype=np.uint32)
    weight=np.array([-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,9,9,9,9,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1])
    # weight=np.reshape(weight,(5,5))
    weight.shape=(3,3,4)
    print(weight)
    # print(weight.shape)
    # print(hexme)
    # print(weight)
    for i in range(h):
        for j in range(w):
            if(i<=5 or j<=5 or i>=h-5 or j>=w-5):
                continue
            else:
                sumi=hexme[i-1:i+2,j-1:j+2]
                sumi=sumi*weight
                # print(sumi)
            sumi=np.sum(sumi,axis=0)
            sumi=np.sum(sumi,axis=0)
            if(sumi[0]>255):sumi[0]=255
            elif(sumi[0]<0):sumi[0]=0
            if(sumi[1]>255):sumi[1]=255
            elif(sumi[1]<0):sumi[1]=0
            if(sumi[2]>255):sumi[2]=255
            elif(sumi[2]<0):sumi[2]=0
            if(sumi[3]>255):sumi[3]=255
            elif(sumi[3]<0):sumi[3]=0
            # print(sumi)
            hexme[i,j]=sumi
            # print(hexme[i,j])
            # print("sumi",sumi.shape)
            # print("hexme",hexme[i,j].shape)
    # print(hexme)
    return hexme


# hexme=mean_filter(hexme)
# hexme=weighted_filter(hexme)
# hexme=median_filter(hexme)
hexme=laplacian_sharpning(hexme)
po = im.fromarray(hexme)
im._show(po)
