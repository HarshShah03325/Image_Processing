import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
import matplotlib.image as img
from PIL import Image as im
import math

hsv=cv.imread("SRA-Assignments/img_processing/roi.jpg",1)
# hexme=np.array(img)
h,w,c=hsv.shape
kent=np.zeros_like(hsv)
# print(hsv.shape)
hsv=cv.cvtColor(hsv,cv.COLOR_BGR2HSV)
for i in range(h):
    for j in range(w):
        if(hsv[i,j,0]>15 and hsv[i,j,0]<40 and  hsv[i,j,1]>0 and hsv[i,j,2]>0):
            kent[i,j]=hsv[i,j]



img=cv.cvtColor(kent,cv.COLOR_HSV2BGR)
img=cv.cvtColor(kent,cv.COLOR_BGR2RGB)
po = im.fromarray(img)
im._show(po)
