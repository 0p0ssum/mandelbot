
import matplotlib.pyplot as plt
from pylab import *
import numpy as np
from numpy import linspace

x_list = linspace(-2.0,4.0,13)
y_list = linspace(-2.0,2.0,5)

xvalues = linspace(-2.25,0.75,1000)
yvalues = linspace(-1.5,1.5,1000)

xlen = len(xvalues)
ylen = len(yvalues)

atlas = np.empty((xlen,ylen))

def mandel(c, maxiter):
    z = complex(0,0)
    for iteration in xrange(maxiter):
        z = (z * z) + c
        if abs(z) > 4:
            break
            pass
        pass
    return iteration
        
for ix in xrange(xlen):
    for iy in xrange(ylen):
        cx = xvalues[ix]
        cy = yvalues[iy]
        c = complex(cx,cy)

        atlas [ix,iy] = mandel(c,40)
        pass
    pass
plt.plot(atlas)
#plt.imshow(atlas.T, interpolation = "nearest")
plt.show()
