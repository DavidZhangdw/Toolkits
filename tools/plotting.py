import matplotlib.pyplot as plt
import numpy as np
import torch
import cv2


def draw_figure(fig):
    fig.canvas.draw()
    fig.canvas.flush_events()
    plt.pause(0.001)


def show_tensor(a_np: torch.Tensor, fig_num = None, title = None, range=(None, None)):
    """Display a 2D tensor.
    args:
        fig_num: Figure number.
        title: Title of figure.
    """
    #a_np = a.squeeze().cpu().clone().detach().numpy()
    if a_np.ndim == 3:
        a_np = np.transpose(a_np, (1, 2, 0))
    fig = plt.figure(fig_num)
    plt.tight_layout()
    plt.cla()
    plt.imshow(a_np, vmin=range[0], vmax=range[1])
    plt.axis('off')
    plt.axis('equal')
    if title is not None:
        plt.title(title)
    draw_figure(fig)


def plot_graph(a: torch.Tensor, fig_num = None, title = None):
    """Plot graph. Data is a 1D tensor.
    args:
        fig_num: Figure number.
        title: Title of figure.
    """
    a_np = a.squeeze().cpu().clone().detach().numpy()
    if a_np.ndim > 1:
        raise ValueError
    fig = plt.figure(fig_num)
    # plt.tight_layout()
    plt.cla()
    plt.plot(a_np)
    if title is not None:
        plt.title(title)
    draw_figure(fig)


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
print(labels.shape)
show_tensor(labels)