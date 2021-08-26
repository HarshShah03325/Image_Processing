from PIL import Image
from math import sqrt
import numpy as np
def gaussian_blur(input_image):
    kernel=[[1 / 256, 4  / 256,  6 / 256,  4 / 256, 1 / 256],
            [4 / 256, 16 / 256, 24 / 256, 16 / 256, 4 / 256],
            [6 / 256, 24 / 256, 36 / 256, 24 / 256, 6 / 256],
            [4 / 256, 16 / 256, 24 / 256, 16 / 256, 4 / 256],
            [1 / 256, 4  / 256,  6 / 256,  4 / 256, 1 / 256]]
    ht = input_image.shape[0]
    wid = input_image.shape[1]
    channel = input_image.shape[2]
    
    # Middle of the kernel
    offset = len(kernel) // 2

    # Create empty output array
    output_image = np.empty((ht,wid,channel))

    # Compute convolution between value and kernels
    for x in range(offset, ht - offset):
        for y in range(offset, wid - offset):
            acc = [0] * channel
            
            for a in range(len(kernel)):
                for b in range(len(kernel)):
                    xn = x + a - offset
                    yn = y + b - offset
                    value = input_image[xn][yn]
                    for c in  range(channel):
                        acc[c] += value[c] * kernel[a][b]

            for c in  range(channel):
                output_image[x][y][c] = acc[c]
    return output_image
def sobel_edge(input_image):
    # Calculate pixel intensity as the average of red, green and blue colors.
    intensity = [[sum(input_image[x, y]) / 3 for y in range(input_image.shape[1])] for x in range(input_image.shape[0])]

    # Sobel kernels
    kernelx = [[-1, 0, 1],
               [-2, 0, 2],
               [-1, 0, 1]]
    kernely = [[1, 2, 1],
               [0, 0, 0],
               [-1, -2, -1]]

    # Create output image
    outputx = np.empty((input_image.shape[0], input_image.shape[1]))
    outputy = np.empty((input_image.shape[0], input_image.shape[1]))
    outputx.fill(0)
    outputy.fill(0)
    # Compute convolution between intensity and kernels
    for x in range(1, input_image.shape[0] - 1):
        for y in range(1, input_image.shape[1] - 1):
            for a in range(3):
                for b in range(3):
                    xn = x + a - 1
                    yn = y + b - 1
                    outputx[x][y] += intensity[xn][yn] * kernelx[a][b]
                    outputy[x][y] += intensity[xn][yn] * kernely[a][b]
    sobel=np.empty((outputx.shape[0],outputx.shape[1]))
    sobel = np.hypot(outputx, outputy)
    thetha = np.arctan2(outputy, outputx)
    return(sobel,thetha)
def non_max_suppression(img, D):
    M, N = img.shape
    Z = np.zeros((M,N), dtype=np.int32)
    angle = D * 180. / np.pi
    angle[angle < 0] += 180

    
    for i in range(1,M-1):
        for j in range(1,N-1):
            try:
                q = 255
                r = 255
                
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

                if (img[i,j] >= q) and (img[i,j] >= r):
                    Z[i,j] = img[i,j]
                else:
                    Z[i,j] = 0

            except IndexError as e:
                pass
    
    return Z
def threshold(img, lowThresholdRatio=0.05, highThresholdRatio=0.09):
    
    highThreshold = img.max() * highThresholdRatio;
    lowThreshold = highThreshold * lowThresholdRatio;
    
    M, N = img.shape
    res = np.zeros((M,N), dtype=np.int32)
    
    weak = np.int32(25)
    strong = np.int32(255)
    
    strong_i, strong_j = np.where(img >= highThreshold)
    zeros_i, zeros_j = np.where(img < lowThreshold)
    
    weak_i, weak_j = np.where((img <= highThreshold) & (img >= lowThreshold))
    
    res[strong_i, strong_j] = strong
    res[weak_i, weak_j] = weak
    
    return (res, weak, strong)
def hysteresis(img, weak, strong=255):
    M, N = img.shape  
    for i in range(1, M-1):
        for j in range(1, N-1):
            if (img[i,j] == weak):
                try:
                    if ((img[i+1, j-1] == strong) or (img[i+1, j] == strong) or (img[i+1, j+1] == strong)
                        or (img[i, j-1] == strong) or (img[i, j+1] == strong)
                        or (img[i-1, j-1] == strong) or (img[i-1, j] == strong) or (img[i-1, j+1] == strong)):
                        img[i, j] = strong
                    else:
                        img[i, j] = 0
                except IndexError as e:
                    pass
    return img
input_image = Image.open("edge-detection.png")
input_pixels = np.array(input_image)
sobel_output=sobel_edge(gaussian_blur(input_pixels))
non_max=non_max_suppression(sobel_output[0],sobel_output[1])
thresh=threshold(non_max)
canny_output=hysteresis(thresh[0],thresh[1],thresh[2])
canny=Image.fromarray(np.uint8(canny_output))
canny.save('canny_output.png')
