from PIL import Image
import numpy as np
import string
import math
degrees=int(input("Enter angle of rotation"))
radian=math.radians(degrees)
image = Image.open('image.png')
img=np.array(image)
ht=img.shape[0]
wid=img.shape[1]
output_coor=[]
i_min=0
i_max=0
j_min=0
j_max=0
for i in range(ht):
    for j in range(wid):
        pixel_data = img[i, j, :]
        i_out=(int)(round(i*math.cos(radian)-j*math.sin(radian)))
        j_out=(int)(round(i*math.sin(radian)+j*math.cos(radian)))
        output_coor.append((i_out,j_out,pixel_data))
        if(i_out<i_min):
            i_min=i_out
        if(i_out>i_max):
            i_max=i_out
        if(j_out<j_min):
            j_min=j_out
        if(j_out>j_max):
            j_max=j_out
ht_out=i_max-i_min
wid_out=j_max-j_min
rotated=np.empty((ht_out+1,wid_out+1,4))
rotated.fill(0)
x_offset = abs(i_min)
y_offset = abs(j_min)
for out in output_coor:
    x=out[0]
    y=out[1]
    pixel=out[2]
    if (rotated[x_offset+ x][y_offset + y][0] == 0) & (rotated[x_offset + x][y_offset + y][1] == 0) & (rotated[x_offset + x][y_offset + y][2] == 0) & (rotated[x_offset + x][y_offset + y][3] == 0):
        rotated[x_offset + x][y_offset + y][0] = pixel[0]
        rotated[x_offset + x][y_offset + y][1] = pixel[1]
        rotated[x_offset + x][y_offset + y][2] = pixel[2]
        rotated[x_offset + x][y_offset + y][3] = pixel[3]
for i in range(rotated.shape[0]):
    prev = [rotated[i][0][0], rotated[i][0][1], rotated[i][0][2], rotated[i][0][3]]
    for j in range(rotated.shape[1]-1):
        if (not any(rotated[i][j][:])) and (any(rotated[i][j+1][:])):
            rotated[i][j][:] = prev
        else:
            prev = rotated[i][j][:]
rotate=Image.fromarray(np.uint8(rotated))
rotate.save('rotated.png')
