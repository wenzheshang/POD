import numpy as np
from matplotlib import pyplot as plt

plt.ion()
for index in range(50):
    plt.cla()

    plt.title("动态散点图")
    plt.grid(True)

    point_count = 5
    x_index = np.random.random(point_count)
    y_index = np.random.random(point_count)
  
    color_list = np.random.random(point_count)
    scale_list = np.random.random(point_count) * 100

    plt.scatter(x_index, y_index, s=scale_list, c=color_list, marker="^")

    plt.pause(0.2)

plt.ioff()

plt.show()