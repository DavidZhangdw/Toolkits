import math
import numpy as np
import cv2
import torch
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

def logist_tp(x):
    return -1/(1+np.exp(x))

def logist_tn(x):
    return 1/(1+np.exp(-x))

def triple_tp(x):
    return -1/(1+np.exp(x))

def triple_tn(x):
    return 1/(1+np.exp(x))

def t_sigmoid(x):
    return -1/(np.exp(x)-1)

x = np.linspace(-5,5,101)

y_p=[]
y_n=[]
y_t_p=[]
y_t_n=[]
y_s_p=[]
y_s_n=[]

# ------------------ logist loss --------------------
for i in x:
    y_p.append(logist_tp(i))
    y_n.append(logist_tn(i))

yp_mesh = np.tile(y_p, (101, 1))
yn_mesh = np.transpose(np.tile(y_n[::-1], (101, 1)))   # y=y[::-1] 逆向
ypn_mesh = 0.5 * (yp_mesh - yn_mesh)

# ------------------- triple loss -----------------------
for i in x:
    for j in x:
        y_t_p.append(triple_tp(j-i))
        y_t_n.append(triple_tn(j-i))

y_t_p = np.array(y_t_p)
y_t_p = y_t_p.reshape(101, 101)
y_tp = np.ones([101, 101])

y_t_n = np.array(y_t_n)
y_t_n = y_t_n.reshape(101, 101)
y_tn = np.ones([101, 101])

for i in range(101):
    y_tp[100-i,:] = y_t_p[i,:]
    y_tn[100-i,:] = y_t_n[i,:]

y_t_p_mesh = y_tp
y_t_n_mesh = y_tn
y_t_pn_mesh = 0.5*(y_tp - y_tn)

# ------------------------ triple sigmoid -------------------
for i in x:
    for j in x:
        t = j - i if j > i else 0
        y_s_p.append(t_sigmoid(t))

y_s_p = np.array(y_s_p)
y_s_p = y_s_p.reshape(101, 101)
y_sp = np.ones([101, 101])
for i in range(101):
    y_sp[100-i,:] = y_s_p[i,:]

y_s_p_mesh = y_sp + yp_mesh
y_s_n_mesh = yn_mesh - y_sp
y_s_pn_mesh = 2*y_sp + yp_mesh - yn_mesh

# --------------------------------------------------------------------------
#二维的数组的热力图，横轴和数轴的ticklabels要加上去的话，既可以通过将array转换成有column
#和index的DataFrame直接绘图生成，也可以后续再加上去。后面加上去的话，更灵活，包括可设置labels大小方向等。

f,ax=plt.subplots(figsize=(8,5))
sns.heatmap(y_s_pn_mesh, vmax=1.0, vmin = -1.0, xticklabels=50, yticklabels=50)
# vmax=1.0,vmin = -1.0, cmap='rocket'
# ax.set_title('二维数组热力图', fontsize = 18)

ax.set_yticklabels(['5', '0', '-5'], fontsize = 12.5, rotation = 360, horizontalalignment='center')
ax.set_xticklabels(['-5', '0', '5'], fontsize = 12.5, horizontalalignment='center')
ax.set_ylabel('negative_value', fontsize = 12.5)
ax.set_xlabel('positive_value', fontsize = 12.5) #横变成y轴，跟矩阵原始的布局情况是一样的
plt.show()
