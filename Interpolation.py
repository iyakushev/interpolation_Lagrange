import numpy as np
import matplotlib.pyplot as mp
from math import sin,cos,tan

def interpolation(f,x,n,a,b):
    sample = [i for i in np.arange(a,b,(b-a)/float(n))]
    sums=0
    for i in range(0,n):
        product=1
        for j in range(0,n):
            if i!=j:
                product*=(x-sample[j])/(sample[i]-sample[j])
        sums+=f(sample[i])*product
    return sums

x = [i for i in np.arange(-1.5,1.5,0.1)]
y = [tan(i) for i in x]
yi = [interpolation(lambda x:tan(x),i,30,-1.5,1.5) for i in x]
mp.plot(x,y,color="r")
mp.plot(x,yi,color="b")
mp.grid(True)
mp.show()

