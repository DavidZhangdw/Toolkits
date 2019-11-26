import numpy as np
import matplotlib
import matplotlib.pyplot as plt 

x = np.linspace(0, 1, 500)

y_0 = - np.power(1-x, 0) * np.log(x)
y_1 = - np.power(1-x, 0.5) * np.log(x)
y_2 = - np.power(1-x, 1) * np.log(x)
y_3 = - np.power(1-x, 2) * np.log(x)
y_4 = - np.power(1-x, 5) * np.log(x)

x0 = ([0.6, 0.62, 0.785, 0.8, 0.815, 0.98, 1])
y0 = ([0.65, 0.75, 0.77, 0.95, 0.77, 0.75, 0.65])

plt.figure(figsize=(7, 5))
plt.plot(x, y_0, linewidth=2.2, label='$\gamma = 0$')
plt.plot(x, y_1, linewidth=2.2, label='$\gamma = 0.5$')
plt.plot(x, y_2, linewidth=2.2, label='$\gamma = 1$')
plt.plot(x, y_3, linewidth=2.2, label='$\gamma = 2$')
plt.plot(x, y_4, linewidth=2.2, label='$\gamma = 5$')
plt.plot(x0, y0, linewidth=1.8)

plt.xlim(0, 1.0)
plt.ylim(0, 5.1)
plt.tick_params(labelsize=12)
plt.xlabel('proability of positive class', fontsize=12)
plt.ylabel('loss', fontsize=12)

ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

plt.text(0.12, 4.2, r'$\mathrm{CELoss}(p_{t}) = - \log(p_{t})$', fontsize=12.8)
plt.text(0.12, 3.7, r'$\mathrm{FocalLoss}(p_{t}) = -(1 - p_{t})^{\gamma} \log(p_{t})$', fontsize=12.8)
plt.text(0.704, 1.42, r'easy and well', fontsize=12)
plt.text(0.67, 1.08, r'-classified examples', fontsize=12)

legend = plt.legend(loc='best', fontsize=10.5, edgecolor='black', handlelength=3)

plt.show()