from PIL import Image
import math
import numpy as np
def copy_roi(image,centerx,centery,x_out,y_out,radius):
    x_min=centerx-radius
    y_min=centery-radius
    x=x_out-radius
    y=y_out-radius
    for i in range(-radius,radius+1):
        y1=-(int)(math.sqrt((radius**2)-(i**2)))
        y2=(int)(math.sqrt((radius**2)-(i**2)))
        for j in range(y1,y2+1):
            image[x+i][y+j][:]=image[x_min+i][y_min+j][:]
    return image
gaussian_output=np.array(Image.open("gaussian_output.png"))
print("Enter point to be copied to")
x=int(input())
y=int(input())
roi_output=copy_roi(gaussian_output,1040,1190,x,y,80)
roi_image=Image.fromarray(np.uint8(roi_output))
roi_image.save('roi_output.png')
