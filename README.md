# Image_Processing

The following operations have been performed mainly using only Numpy and Pillow library is used just to load and save image.

### 1. Image Rotation

The image can be rotated by any angle bound or inbound.It involves finding the centre of the Matrix and Shifting along the centre using Rotation Matrix.There are two methods of rotating the image following above approach
1. Using Pure Rotation Matrix
2. [Using Shearing Rotation](https://datagenetics.com/blog/august32013/index.html)

![Rotation Matrix](https://legacy.voteview.com/images/homework_1_1_18_2011.jpg)

|<img width="640" height="450" src="https://github.com/MannDoshi/Image-Processing/blob/master/Image-Rotation/image.png">| 
|:---:|
|Input Image|

**Output**
|<img width="600" height="322" src="https://github.com/MannDoshi/Image-Processing/blob/master/Image-Rotation/rotated_nobound.png">|<img width="640" height="450" src="https://github.com/MannDoshi/Image-Processing/blob/master/Image-Rotation/rotated.png">|
|:---:|:---:|
|No Bound|Bound|

### 2. Applying Kernels
Convolution is a simple mathematical operation which is fundamental to many common image processing operators. Convolution provides a way of multiplying together two arrays of numbers, generally of different sizes, but of the same dimensionality, to produce a third array of numbers of the same dimensionality.Kernels form the Second Matrix which provides effects to the Image.
![figure3](https://user-images.githubusercontent.com/35737777/68632479-95c61f80-04e6-11ea-80b2-2e86a4fcc258.jpg)

Applying 5X5 filters to do the following task
1. Blurring 
2. Sharpening

|<img width="446" height="447" src="https://github.com/MannDoshi/Image-Processing/blob/master/Image-Blurring/blur.jpeg">|
|:---:|
|Input Image|

**Output**
|<img width="640" height="450" src="https://github.com/MannDoshi/Image-Processing/blob/master/Image-Blurring/box_blur.png">|<img width="640" height="450" src="https://github.com/MannDoshi/Image-Processing/blob/master/Image-Blurring/gaussian_blur.png">|<img width="640" height="450" src="https://github.com/MannDoshi/Image-Processing/blob/master/Image-Sharpening/sharpened_image.png">|
|:---:|:---:|:---:|
|Box Filter|Gaussian Filter|Sharpen|

### 3. Edge Detection
Edge detection is an image processing technique for finding the boundaries of objects within images. It works by detecting discontinuities in brightness.

Applying Edge Detection in following sequence 
1. Vertical edge detection
2. Horizontal edge detection
3. Sobel edge detection (right, left, top, bottom)
4. Canny edge detection  

|<img width="602" height="452" src="https://github.com/MannDoshi/Image-Processing/blob/master/Edge-Detection/edge-detection.png">|
|:---:|
|Input Image|

**Output**
|<img width="602" height="452" src="https://github.com/MannDoshi/Image-Processing/blob/master/Edge-Detection/vertical-edge-output.png">|<img width="602" height="452" src="https://github.com/MannDoshi/Image-Processing/blob/master/Edge-Detection/horizontal-edge-output.png">|
|:---:|:---:|
|Vertical Edge Detection|Horizontal Edge Detection|
|<img width="602" height="452" src="https://github.com/MannDoshi/Image-Processing/blob/master/Edge-Detection/sobel-edge-output.png">|<img width="602" height="452" src="https://github.com/MannDoshi/Image-Processing/blob/master/Edge-Detection/canny_output.png">|
|Sobel Edge Detection|Canny Edge Detection|

### 4. Morphological Transformation
Morphological transformations are some simple operations based on the image shape. It is normally performed on binary images. It needs two inputs, one is our original image, second one is called structuring element or kernel which decides the nature of operation. Two basic morphological operators are Erosion and Dilation.
Applying dilation and erosion transformation to the image

**Output**
|<img width="112" height="150" src="https://github.com/MannDoshi/Image-Processing/blob/master/Morphological-Transformations/morphological.png">|<img width="112" height="150" src="https://github.com/MannDoshi/Image-Processing/blob/master/Morphological-Transformations/dilation_output.png">|<img width="112" height="150" src="https://github.com/MannDoshi/Image-Processing/blob/master/Morphological-Transformations/erosion_output.png">|<img width="112" height="150" src="https://github.com/MannDoshi/Image-Processing/blob/master/Morphological-Transformations/sobel-edge-output.png">|
|:---:|:---:|:---:|:---:|
|Input-Image|Dilation|Erosion|Edge-Detection|

### 5. Masking
Masking is an image processing method in which we define a small 'image piece' and use it to modify a larger image. Masking is the process that is underneath many types of image processing, including edge detection, motion detection, and noise reduction.
To show only blue ball a mask has been applied to the following input image
|<img width="600" height="396" src="https://github.com/MannDoshi/Image-Processing/blob/master/Masking/mask.jpg">|<img width="600" height="396" src="https://github.com/MannDoshi/Image-Processing/blob/master/Masking/BlueBall.png">|
|:---:|:---:|
|Input Image|Masked Image(output)|

### Blob detection
<img src="./Blob Detection/blob_detection.gif" width="600" />































