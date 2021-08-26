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
rotated=np.empty((ht,wid,4))
rotated.fill(0)
for i, row in enumerate(img):
    for j, col in enumerate(row):
        pixel_data = img[i, j, :]
        i_out=(ht//2)+(int)((i-ht//2)*math.cos(radian)-(j-wid//2)*math.sin(radian))
        j_out=(wid//2)+(int)((i-ht//2)*math.sin(radian)+(j-wid//2)*math.cos(radian))
        if((0<=i_out<ht) and (0<=j_out<wid)):
            if(not any(rotated[i_out][j_out][:])):
                rotated[i_out][j_out][:]=pixel_data
for i in range(rotated.shape[0]):
    prev = [rotated[i][0][0], rotated[i][0][1], rotated[i][0][2], rotated[i][0][3]]
    for j in range(rotated.shape[1]-1):
        if (not any(rotated[i][j][:])) and (any(rotated[i][j+1][:])):
            rotated[i][j][:] = prev
        else:
            prev = rotated[i][j][:]
rotate=Image.fromarray(np.uint8(rotated))
rotate.save('rotated_nobound.png')
