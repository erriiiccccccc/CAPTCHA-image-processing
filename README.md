<h1 align="center">✨ Image Processing with OpenCV ✨</h1>

<p align="center">
  <b><small>This repository contains a simple Python script for image processing using the OpenCV library. The script reads an input image, performs Gaussian blurring for noise reduction, applies thresholding to segment the image into black and white regions, and then saves the processed image. The original and processed images are displayed using matplotlib for visualization.<b><small>
</p>
    
## Prerequisites
Before running the script, make sure you have the following prerequisites installed:

1. Python 3.x
2. OpenCV (cv2)
3. Matplotlib (matplotlib)
4. You can install the required packages using the following command:

```
pip install opencv-python-headless matplotlib
```

## Usage
Clone the repository to your local machine:
```
git clone https://github.com/erriiiccccccc/CAPTCHA-image-processing.git
cd ./CAPTCHA-image-processing
```
Place the image you want to process in the same directory as the script and name it Sample.png.

Run the script using the following command:

```
python image_processing.py
```
The processed image will be saved as Processed.png in the same directory.

## Explanation
The script performs the following steps:

1. Reads the input image Sample.png in grayscale mode.
2. Applies Gaussian blurring to the image using a kernel size of (5, 5) to reduce noise.
3. Uses Otsu's thresholding method to segment the image into black and white regions.
4. Saves the processed image as Processed.png.
5. Displays the original and processed images side by side using matplotlib.

The original image and the processed image are displayed using matplotlib subplots.
