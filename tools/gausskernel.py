import numpy as np
import cv2
import torch
import matplotlib.pyplot as plt

def gauss(kernel_size, sigma):
    
    kernel = np.zeros((kernel_size, kernel_size))
    center = kernel_size//2
    if sigma<=0:
        sigma = ((kernel_size-1)*0.5-1)*0.3+0.8
    
    s = sigma**2
    sum_val =  0
    for i in range(kernel_size):
        for j in range(kernel_size):
            x, y = i-center, j-center
            
            kernel[i, j] = np.exp(-(x**2+y**2)/2*s)
            sum_val += kernel[i, j]
    
    kernel = kernel/sum_val

    return kernel

def gaussian_kernel_2d_opencv(kernel_size = 3,sigma = 0):
    kx = cv2.getGaussianKernel(kernel_size,sigma)
    ky = cv2.getGaussianKernel(kernel_size,sigma)
    kernel = np.multiply(kx,np.transpose(ky))
    kernel = kernel / np.max(kernel)
    kernel = torch.from_numpy(kernel).float()
    return kernel

# gauss_kernel = gauss(6, 1.2)
gauss_kernel = gaussian_kernel_2d_opencv(6, 1.2)
g_att = torch.ones(1,1,6,6) * gauss_kernel
#print(gauss_kernel)
#print(g_att)
#plt.imshow(gauss_kernel)

#---------------------------------------------------
kernel=cv2.getGaussianKernel(127,25)
kernel=kernel*kernel.T
#scales all the values and make the center vaule of kernel to be 1.0
kernel=kernel/np.max(kernel)

heatmap = cv2.resize(kernel, (6, 6))

heatmap = np.uint8(255 * heatmap)
heatmap = cv2.applyColorMap(heatmap, cv2.COLORMAP_JET)  # cv2.COLORMAP_JET/cv2.COLORMAP_HOT
cv2.imshow('heatmap',heatmap)
cv2.imwrite('./66.jpg', heatmap)
cv2.waitKey(0)