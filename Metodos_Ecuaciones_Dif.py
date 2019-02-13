import numpy as np

def MetEuler(x0, y0, x2):

 del2 = .001
 x = np.arange(x0, x2, del2)
 y = [y0]
 npun = len(x)

 y1 = y0
 for i in range(npun-1):
   y2 = y1 + del2 * 3 * y1
   y.append(y2)
   y1 = y2

 return {'x': x, 'y':y}

