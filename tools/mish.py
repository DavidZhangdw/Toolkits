import math
import numpy as np
from matplotlib import pyplot as plt

def Relu(x):
    y = 0 if x < 0 else x
    return y

def Mish(x):
    return x * math.tanh(math.log(1+math.exp(x)))
    # x = x * (torch.tanh(torch.softplus(x)))

def ln_e(x):
    return math.log(1+math.exp(x))

def GELU(x):
    return 0.5*x*(1+math.tanh(math.sqrt(2/math.pi)*(x+0.044715*x**3)))
    
x = np.linspace(-10,10,1000)
y=[]
z=[]
l=[]
r=[]
for i in x:
    y.append(Mish(i))
    z.append(GELU(i))
    l.append(ln_e(i))
    r.append(Relu(i))
plt.plot(x, y, linewidth=2.2, label='Mish')
plt.plot(x, l, linewidth=2.2, label='Ln_e')
plt.plot(x, z, linewidth=2.2, label='Gelu')
plt.plot(x, r, linewidth=2.2, label='Relu')

plt.grid()
plt.ylim(-1,6)
plt.xlim(-7,7)
legend = plt.legend(loc='best', fontsize=10.5, edgecolor='black', handlelength=3)

plt.show()