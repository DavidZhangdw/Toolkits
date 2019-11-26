import numpy as np
import cv2
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns

def logistic_labels(x, y, r_pos, r_neg):
    dist = np.abs(x) + np.abs(y)  # block distance
    labels = np.where(dist <= r_pos, np.ones_like(x), np.where(dist < r_neg, np.ones_like(x) * 0.5, np.zeros_like(x)))
    return labels

# distances along x- and y-axis
n, c, h, w = 1, 1, 17, 17
x = np.arange(w) - (w - 1) / 2
y = np.arange(h) - (h - 1) / 2
x, y = np.meshgrid(x, y)

# create logistic labels
r_pos = 16 / 8
r_neg = 0 / 8
labels = logistic_labels(x, y, r_pos, r_neg)
updown = cv2.resize(labels, (272, 272))

# repeat to size
# labels = labels.reshape((1, 1, h, w))

# ----------------------------------------------------------
f,ax=plt.subplots(figsize=(7,5))
sns.heatmap(updown, vmax=1.0, vmin = 0, xticklabels=2, yticklabels=2) #,  cmap='hot_r'

label_y = ax.get_yticklabels()
plt.setp(label_y, rotation=360, horizontalalignment='center')
plt.show()

'''
heatmap = cv2.resize(labels, (272, 272))
heatmap = np.uint8(255 * heatmap)
heatmap = cv2.applyColorMap(heatmap, cv2.COLORMAP_JET)  # cv2.COLORMAP_JET/cv2.COLORMAP_HOT
cv2.imshow('heatmap',heatmap)
cv2.waitKey(0)
'''

print(labels)
print(labels.shape)
