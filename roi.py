import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as img
from PIL import Image as im
import math

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

