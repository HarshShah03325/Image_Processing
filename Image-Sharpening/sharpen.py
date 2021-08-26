from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from blur import convert
#sharpening kernel
sharpening_kernel = kernel = [[1/25,1/25,1/25,1/25,1/25],[1/25,1/25,1/25,1/25,1/25],[1/25,1/25,-1,1/25,1/25],[1/25,1/25,1/25,1/25,1/25],[1/25,1/25,1/25,1/25,1/25]]
image1=np.array(Image.open("sharpen_input.png"))
sharpened=Image.fromarray(np.uint8(convert(image1, sharpening_kernel)))
sharpened.save("sharpened_image.png")
