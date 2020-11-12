import cv2
import numpy as np
from PIL import Image
import random
import string
from matplotlib import pyplot as plt

def sobe_filter(filename) :
	bgr_image = cv2.imread(filename)
	rgb_image = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2RGB)
	image = cv2.cvtColor(rgb_image, cv2.COLOR_RGB2GRAY)


	sobel_vertical = [[-1, -2, -1], [0, 0, 0], [1, 2, 1]]
	sobel_horizontal = [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]

	rows, cols = image.shape
	res = image.copy()
	kernel = 3

	for r in range(1,rows-kernel+1):
	    for c in range(1,cols-kernel+1):
	        local_box = image[r-1:r+2, c-1:c+2]
	        vertical = ((local_box*sobel_vertical).sum())/4
	        horizontal = ((local_box*sobel_horizontal).sum())/4
	        combined_grad = (vertical**2 + horizontal**2)**0.5
	        res[r,c] = int(combined_grad)

	file_name = ''.join(random.choice(string.ascii_lowercase) for i in range(16))
	file_name = file_name + '.jpg'

	
	print(file_name)

	final = Image.fromarray(res) 
	final.save('static/Filters_images/' + file_name)

	return file_name


# plt.subplot(121),plt.imshow(rgb_image),plt.title('Original')
# plt.xticks([]), plt.yticks([])
# plt.subplot(122),plt.imshow(res),plt.title('Averaging')
# plt.xticks([]), plt.yticks([])
# plt.show()