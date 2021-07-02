import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as img
from PIL import Image as im
import math

img=im.open("orignal_assets/rotate.png")
hexme=np.array(img)
h,w,c=hexme.shape
print(c)
radians=math.pi/180*int(input("enter your angle: "))
new_h=int(h*math.cos(radians)+w*math.sin(radians))
new_w=int(w*math.cos(radians)+h*math.sin(radians))
don=np.zeros((new_h,new_w,c),dtype=np.uint8)
c, s = math.cos(radians), math.sin(radians)
lol = np.array([[c, s], [-s, c]])
for i in range(2,new_h):
    if(radians==math.pi):
        don=hexme[::-1]
        break
    for j in range(2,new_w):
        n=np.array([i+h/2,j+w/2]).reshape(2,1)
        m=np.dot(lol,n)
        x,y=int(m[0]),int(m[1])
        # don[i,j]=hexme[i,j]
        if(x>=0 and y>=0 and x<h and y<w):
            don[i,j]=hexme[x,y]
# for i in range(1,h):
#     for j in range(1,w):
#         # print(don[i][j]==0)
#         if(don[i][j].all()==0):
#             don[i][j]=don[i-1][j-1]

po = im.fromarray(don)
po.save("rotate.png")
im._show(po)
