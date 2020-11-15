import numpy as np
import cv2
from matplotlib import pyplot as plt
from PIL import Image
import random
import string

def scratch() :
    image = cv2.imread('Image/ert.png')

    rows = image.shape[0]
    cols = image.shape[1]
    kernel = 3
    temp = []

    res = image.copy()

    for i in range(rows-kernel+1) :
        for j in range(cols-kernel+1) :
            for x in range(i,i+kernel) :
                for y in range(j,j+kernel) :
                    temp.append(image[x][y])
            
            res[i][j] = np.median(temp)
            temp.clear()

    plt.subplot(121),plt.imshow(image),plt.title('Original')
    plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(res),plt.title('Averaging')
    plt.xticks([]), plt.yticks([])
    plt.show()

def median_library(filename) :
    bgr_image = cv2.imread(filename)
    rgb_image = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2RGB)

    kernel = 9
    converted = cv2.medianBlur(rgb_image,kernel)

    file_name = ''.join(random.choice(string.ascii_lowercase) for i in range(16))
    file_name = file_name + '.jpg'

    print(file_name)

    final = Image.fromarray(converted) 
    final.save('static/Filters_images/' + file_name)

    return file_name

def median_color(filename) :
    bgr_image = cv2.imread(filename)
    rgb_image = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2RGB)

    r,g,b = cv2.split(rgb_image)

    kernel = 3
    temp_r = []
    temp_g = []
    temp_b = []

    rows = r.shape[0]
    cols = r.shape[1]

    res_r = r.copy()
    res_g = g.copy()
    res_b = b.copy()

    for i in range(rows-kernel+1) :
        for j in range(cols-kernel+1) :
            for x in range(i,i+kernel) :
                for y in range(j,j+kernel) :
                    temp_r.append(r[x][y])
            
            res_r[i][j] = np.median(temp_r)
            temp_r.clear()

    for i in range(rows-kernel+1) :
        for j in range(cols-kernel+1) :
            for x in range(i,i+kernel) :
                for y in range(j,j+kernel) :
                    temp_g.append(g[x][y])
            
            res_g[i][j] = np.median(temp_g)
            temp_g.clear()

    for i in range(rows-kernel+1) :
        for j in range(cols-kernel+1) :
            for x in range(i,i+kernel) :
                for y in range(j,j+kernel) :
                    temp_b.append(b[x][y])
            
            res_b[i][j] = np.median(temp_b)
            temp_b.clear()

    converted = cv2.merge((res_r,res_g,res_b))
    file_name = ''.join(random.choice(string.ascii_lowercase) for i in range(16))
    file_name = file_name + '.jpg'

    print(file_name)

    final = Image.fromarray(converted) 
    final.save('static/Filters_images/' + file_name)

    return file_name