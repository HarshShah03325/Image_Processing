from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from blur import convert
# Box Blur kernel
box_kernel = [[1 / 25, 1 / 25, 1 / 25, 1 / 25, 1 / 25],
              [1 / 25, 1 / 25, 1 / 25, 1 / 25, 1 / 25],
              [1 / 25, 1 / 25, 1 / 25, 1 / 25, 1 / 25],
              [1 / 25, 1 / 25, 1 / 25, 1 / 25, 1 / 25],
              [1 / 25, 1 / 25, 1 / 25, 1 / 25, 1 / 25]]
image = np.array(Image.open("blur.jpeg"))
box_blur = Image.fromarray(np.uint8(convert(image, box_kernel)))
box_blur.save("box_blur.png")
