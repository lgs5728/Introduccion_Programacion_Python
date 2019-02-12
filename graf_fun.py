import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 10, .1)
y = np.sin(x)

x0 = 2
y0 = np.sin(x0)

dx = np.cos(x0)

del1 = .5
xx = np.arange(x0-del1, x0+del1,.1)
yy = dx*(xx-x0) + y0

plt.plot(x,y)
plt.plot(xx, yy)


plt.show()




