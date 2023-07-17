"""
This is a program to excute POD
The fulid field data reduced order
"""
import imageio
import pandas as pd
import scipy.io as scio
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.ticker import MaxNLocator
from matplotlib import cm
from post import plot_cylinder
from pod import pod_M

nx = 199
ny = 449

#Data reading
data = scio.loadmat('./DATA/DATA/FLUIDS/CYLINDER_ALL.mat')
#print(data.keys())
vort = np.array(data['VORTALL'])
maxvort = np.max(vort)
minvort = np.min(vort)

u = np.array(data['UALL'])
maxu = np.max(u)
minu = np.min(u)

#dynamic fluent u
def pltU():
    im = []
    for i in range(0,151):
        U = u[:, i].reshape(ny, nx)
        U = U.transpose(1, 0)
        name = 'U'
        im = plot_cylinder(U, im, maxu, minu, name)
    imageio.mimsave('pic/picU.gif', im, duration=0.05)

#dynamic fluent VORT
def pltVORT():
    im = []
    for i in range(0,151):
        VORT = vort[:, i].reshape(ny, nx)
        VORT = VORT.transpose(1, 0)
        name = 'VORT'
        im = plot_cylinder(VORT, im, maxvort, minvort, name)
    imageio.mimsave('pic/picVORT.gif', im, duration=0.05)

def recon():
    k = 10
    im = []
    (a, vector, mean) = pod_M(vort, k)
    f = np.zeros((89351, 151))
    for t in range(151):
        for x in range(89351):
            for i in range(k):
                f[x, t] = f[x, t] + a[i, t] * vector[x, i]
    f = mean + f/151
    for i in range(0,151):
        F = f[:, i].reshape(ny, nx)
        F = F.transpose(1, 0)
        name = 'F'
        im = plot_cylinder(F, im, maxvort, minvort, name)
    imageio.mimsave('pic/picVORTPOD_mode3.gif', im, duration=0.05)
    
recon()

# pltU()
# pltVORT()

#Martix generate



#Claculate