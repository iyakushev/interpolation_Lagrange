import numpy as np
import matplotlib.pyplot as mp
import matplotlib.patches as legend
from math import sin,cos,tan

def interpolation(y,x,t):
    """
    Evaluates Interpolation of fx in Lagrange form
    :param y: DataSet of Y values
    :param x: DataSet of X values
    :param t: Interpolation node
    :return:
    """
    sums = 0
    k = len(y)
    for i in range(k):
        product = 1
        for j in range(k):
            if i != j:
                product *= (t-x[j])/(x[i]-x[j])
        sums += y[i]*product
    return sums

n = 10
x = [i for i in np.arange(-1.5,1.5,0.1)]
y = [tan(i) for i in x]
nx = [i for i in np.linspace(np.min(x),np.max(x),n)]
print nx
p = [interpolation(y,x,i) for i in nx]
mp.xlabel("X")
mp.ylabel("Y")
mp.plot(x,y,color="#ca9942")
mp.plot(nx,p,color="lightblue")
mp.legend(handles = [legend.Patch(color = "#ca9942",label = "Original function"),
                     legend.Patch(color = "lightblue",label = "Interpolation")])
mp.show()
