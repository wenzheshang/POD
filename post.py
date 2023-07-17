#CFD POST
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import MaxNLocator
import numpy as np
import imageio 
import math
def plot_cylinder(para, im, max, min, name):
    X0 = np.linspace(0, 448, 449)
    Y0 = np.linspace(0, 198, 199)
    X, Y = np.meshgrid(X0, Y0)
    #plot
    plt.figure(figsize = (12, 8))

    xticks = np.array([1, 50, 100, 150, 200, 250, 300, 350, 400, 449])
    yticks = np.array([1, 50, 100, 150, 199])
    xticklabel = ['-1','0','1','2','3','4','5','6','7','8']
    yticklabel = ['2','1','0','-1','-2']

    bartick = np.linspace(math.ceil(min), math.floor(max), 7)

    plt.axis('equal')
    plt.xticks(xticks, xticklabel)
    plt.yticks(yticks, yticklabel)
 
    plt.xlabel('X')
    plt.ylabel('Y')

    #c = cm.get_cmap('RdBu',256)
    #nor = plt.Normalize(min, max)

    levels = MaxNLocator(nbins=100).tick_values(min, max)

    plt.contourf(X, Y, para, levels = levels, cmap = cm.get_cmap('RdBu'))

    #sm = cm.ScalarMappable(norm=nor, cmap=c)
    cbar = plt.colorbar()
    cbar.set_label(name,rotation=-90,va='bottom',fontsize=12)
    cbar.set_ticks(bartick)

    #cylinder
    theta = np.linspace(0, 2*np.pi,100)
    x = 49 + 25*np.sin(theta)
    y = 99 + 25*np.cos(theta)

    plt.fill(x, y, 'black')

    plt.savefig('pic/temp2.png')

    im.append(imageio.imread('pic/temp2.png'))

    return im