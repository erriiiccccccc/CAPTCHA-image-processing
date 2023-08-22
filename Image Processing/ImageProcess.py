import cv2
import matplotlib.pyplot as plt

img = cv2.imread('Sample.png', cv2.IMREAD_GRAYSCALE)
blurred = cv2.GaussianBlur(img, (5,5), 0) # i use gaussianblur to smoothen and remove noise from image
threshold = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)[1] 
#THRESH_BINARY seperates the black and whites
#THRESH_OTSU iterating through all the possible threshold values and calculating a measure of spread for the pixel levels each side of the threshold

cv2.imwrite('Processed.png', threshold) # saves the processed image

plt.subplot(121)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title('Original Image')
plt.xticks([])
plt.yticks([])
plt.subplot(122)
plt.imshow(threshold, "gray")
plt.title('Processed Image')
plt.xticks([])
plt.yticks([])
plt.show()