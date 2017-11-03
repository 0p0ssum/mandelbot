
import numpy as np
import matplotlib.pyplot as plt

def count_iter_until_divergent(c, maxiter):
    z = complex(0,0)
    for iteration in xrange(maxiter):
        z = (z * z) + c
        if abs(z) > 4:
            break
            pass
        pass
    return iteration

def mandelbrot_maker(threshold, density):

    xvalues = np.linspace(-2.25,0.75,1000)
    yvalues = np.linspace(-1.5,1.5,1000)

    xlen = len(xvalues)
    ylen = len(yvalues)

    atlas = np.empty((xlen,ylen))
    for ix in xrange(xlen):
        for iy in xrange(ylen):
            cx = xvalues[ix]
            cy = yvalues[iy]
            c = complex(cx,cy)

            atlas [ix,iy] = count_iter_until_divergent(c,threshold)
            pass
        pass

    plt.imshow(atlas.T, interpolation = "nearest")
    plt.show()

mandelbrot_maker(120,300)
