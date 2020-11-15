import cv2
import numpy as np
from matplotlib import pyplot as plt

bgr_image = cv2.imread("../Images/hj.png")
rgb_image = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2RGB)

# kernel = np.ones((8,8),np.float32)/64
# converted = cv2.filter2D(rgb_image,-1,kernel)


kernel = 9
converted = cv2.medianBlur(rgb_image,kernel)

# kernel = (9,9)
# converted =cv2.GaussianBlur(rgb_image,kernel,0)

plt.subplot(121),plt.imshow(rgb_image),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(converted),plt.title('Averaging')
plt.xticks([]), plt.yticks([])
plt.show()


# r,g,b = cv2.split(rgb_image)

# kernel = 3
# rows = r.shape[0]
# cols = r.shape[1]
# mask = np.array([[-1,-1,-1], [-1, 8,-1], [-1,-1,0]])/3

# res_r = r.copy()
# res_g = g.copy()
# res_b = b.copy()

# for i in range(1,rows-kernel+1) :
#     for j in range(1,cols-kernel+1) :
#         local_box = r[i-1:i+kernel-1, j-1:j+kernel-1]
#         print(local_box)
#         sum = ((local_box*mask).sum())
#         res_r[i][j] = sum

# for i in range(1,rows-kernel+1) :
#     for j in range(1,cols-kernel+1) :
#         local_box = g[i-1:i+kernel-1, j-1:j+kernel-1]
#         print(local_box)
#         sum = ((local_box*mask).sum())
#         res_g[i][j] = sum

# for i in range(1,rows-kernel+1) :
#     for j in range(1,cols-kernel+1) :
#         local_box = b[i-1:i+kernel-1, j-1:j+kernel-1]
#         print(local_box)
#         sum = ((local_box*mask).sum())
#         res_b[i][j] = sum

# converted = cv2.merge((res_r,res_g,res_b))

# plt.subplot(221),plt.imshow(bgr_image),plt.title('BGR')
# plt.xticks([]), plt.yticks([])
# plt.subplot(222),plt.imshow(rgb_image),plt.title('RGB')
# plt.xticks([]), plt.yticks([])
# plt.subplot(223),plt.imshow(converted),plt.title('new')
# plt.xticks([]), plt.yticks([])
# plt.show()
