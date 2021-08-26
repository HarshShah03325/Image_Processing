from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from blur import convert
# Weighted Average Filter
w_average_kernel = [[1/40, 1/40, 1/40, 1/40, 1/40],
                    [1/40, 1/40, 1/40, 1/40, 1/40],
                    [1/40, 1/40,16/40, 1/40, 1/40],
                    [1/40, 1/40, 1/40, 1/40, 1/40],
                    [1/40, 1/40, 1/40, 1/40, 1/40]]
image = np.array(Image.open("blur.jpeg"))
w_average_blur = Image.fromarray(np.uint8(convert(image, w_average_kernel)))
w_average_blur.save("weighted_average_blur.png")