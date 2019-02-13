import numpy as np
import matplotlib.pyplot as plt
import Metodos_Ecuaciones_Dif as sol

x0 = 0
y0 = 1

'''
del2 = .001
x = np.arange(0, 5, del2)

y = [y0]

npun = len(x)

y1 = y0
for i in range(npun-1):
   y2 = y1 + del2 * 3 * y1
   y.append(y2)
   y1 = y2

plt.plot(x,y)

ya = y0 + np.exp(3*(x-x0))
'''
res = sol.MetEuler(x0, y0, 4)

plt.plot(res['x'],res['y'])

#plt.plot(x, ya, color='red')

plt.show()



