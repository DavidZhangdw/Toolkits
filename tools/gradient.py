import math
import numpy as np
import cv2
import torch
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

def tp(x):
    return -1/(1+np.exp(x))

x = np.linspace(-5,5,100)
y=[]

for i in x:
    y.append(tp(i))

mesh = np.tile(y, (100, 1))

heat_map = cv2.resize(mesh, (400, 400))

mesh_map = np.uint8(255 * heat_map)
mesh_map = cv2.applyColorMap(mesh_map, cv2.COLORMAP_JET)
cv2.imshow('gradient_map', mesh_map)
cv2.waitKey(0)

plt.plot(x, y, linewidth=2.2, label='$\partial{T}/\partial{p}$')

plt.grid()
plt.ylim(-1.05,0.05)
plt.xlim(-5,5)
legend = plt.legend(loc='best', fontsize=10.5, edgecolor='black', handlelength=3)

plt.show()
