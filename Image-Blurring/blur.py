from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
def convert(input_image, kernel):
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
