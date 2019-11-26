import numpy as np
import cv2


kernel=cv2.getGaussianKernel(127,5)
kernel=kernel*kernel.T
#scales all the values and make the center vaule of kernel to be 1.0
kernel=kernel/np.max(kernel)

img = cv2.imread('./001.jpg')
heatmap = cv2.resize(kernel, (img.shape[1], img.shape[0]))

heatmap = np.uint8(255 * heatmap)
heatmap = cv2.applyColorMap(heatmap, cv2.COLORMAP_JET)  # cv2.COLORMAP_JET/cv2.COLORMAP_HOT
cv2.imshow('heatmap',heatmap)


# 0.4 here is a heatmap intensity factor
superimposed_img = heatmap * 0.5 + img
# Save the image to disk
cv2.imwrite('./xx.jpg', superimposed_img)

cv2.waitKey(0)


# ----------------------------------------------
'''
def colormap_name(id):
    switcher = {
       0 : "COLORMAP_AUTUMN",
        1 : "COLORMAP_BONE",
        2 : "COLORMAP_JET",
        3 : "COLORMAP_WINTER",
        4 : "COLORMAP_RAINBOW",
        5 : "COLORMAP_OCEAN",
        6 : "COLORMAP_SUMMER",
        7 : "COLORMAP_SPRING",
        8 : "COLORMAP_COOL",
        9 : "COLORMAP_HSV",
        10: "COLORMAP_PINK",
        11: "COLORMAP_HOT" 
    }
    return switcher.get(id, 'NONE')
 
img = cv2.imread('./001.jpg', cv2.IMREAD_GRAYSCALE)
# im_out = np.zeros((600, 800, 3), np.uint8)
 
for i in range(0, 4):
    for j in range(0, 3):
        k = i + j * 4
        im_color = cv2.applyColorMap(img, k)
        cv2.putText(im_color, colormap_name(k), (30, 180),
                   cv2.FONT_HERSHEY_DUPLEX, 0.5, (255, 255, 255),1)
        ix200 = i * 200
        jx200 = j * 200
        im_out = im_color
        cv2.imshow('result', im_out)
        # cv2.imwrite('result.jpg', im_out)
        cv2.waitKey(0)

cv2.destroyAllWindows()
'''