import cv2
from PIL import Image
import numpy as np
import random
import string
from matplotlib import pyplot as plt

def scratch() :
    bgr_image = cv2.imread('Image/cup.jpg')
    rgb_image = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2RGB)
    image = cv2.cvtColor(rgb_image, cv2.COLOR_RGB2GRAY)

    res = image.copy()

    rows = image.shape[0]
    cols = image.shape[1]

    mask = [[1,2,1],[2,4,2],[1,2,1]]
    mask = np.array(mask).astype('float32')/16
    kernel = 3

    for i in range(1,rows-kernel+1) :
        for j in range(1,cols-kernel+1) :
            local_box = image[i-1:i+kernel-1, j-1:j+kernel-1]
            print(local_box)
            sum = ((local_box*mask).sum())
            res[i][j] = sum


    res = cv2.cvtColor(res, cv2.COLOR_GRAY2RGB)

    plt.subplot(121),plt.imshow(rgb_image),plt.title('Original')
    plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(res),plt.title('Averaging')
    plt.xticks([]), plt.yticks([])
    plt.show()

def gaussian_library(filename) :
    bgr_image = cv2.imread(filename)
    rgb_image = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2RGB)

    kernel = (9,9)
    converted =cv2.GaussianBlur(rgb_image,kernel,0)

    file_name = ''.join(random.choice(string.ascii_lowercase) for i in range(16))
    file_name = file_name + '.jpg'

    print(file_name)

    final = Image.fromarray(converted) 
    final.save('static/Filters_images/' + file_name)

    return file_name

def gaussian_color(filename) :
    bgr_image = cv2.imread(filename)
    rgb_image = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2RGB)

    r,g,b = cv2.split(rgb_image)

    rows = r.shape[0]
    cols = r.shape[1]
    
    mask = [[1,2,1],[2,4,2],[1,2,1]]
    mask = np.array(mask).astype('float32')/16
    kernel = 3

    res_r = r.copy()
    res_g = g.copy()
    res_b = b.copy()

    for i in range(1,rows-kernel+1) :
        for j in range(1,cols-kernel+1) :
            local_box = r[i-1:i+kernel-1, j-1:j+kernel-1]
            sum = ((local_box*mask).sum())
            res_r[i][j] = sum

    for i in range(1,rows-kernel+1) :
        for j in range(1,cols-kernel+1) :
            local_box = g[i-1:i+kernel-1, j-1:j+kernel-1]
            sum = ((local_box*mask).sum())
            res_g[i][j] = sum

    for i in range(1,rows-kernel+1) :
        for j in range(1,cols-kernel+1) :
            local_box = b[i-1:i+kernel-1, j-1:j+kernel-1]
            sum = ((local_box*mask).sum())
            res_b[i][j] = sum
    
    converted = cv2.merge((res_r,res_g,res_b))

    file_name = ''.join(random.choice(string.ascii_lowercase) for i in range(16))
    file_name = file_name + '.jpg'

    print(file_name)

    final = Image.fromarray(converted) 
    final.save('static/Filters_images/' + file_name)

    return file_name
