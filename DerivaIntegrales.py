import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 10, .1)
print(x)
y = np.sin(x)

plt.plot(x,y)

x0 = 2
y0 = np.sin(x0)

der = np.cos(x0)

del1 = .5
xx = np.arange(x0-del1, x0+del1, .1)
yy = y0 + der*(xx-x0)

plt.plot(xx, yy)


plt.show()

