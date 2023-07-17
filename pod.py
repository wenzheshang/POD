#pod
import re
import numpy as np
import math

def pod_M(mtx, k):
    time_p = mtx.shape[1] #列数
    #value_p = mtx.shape[0] #行数
    vtx_mean = np.average(mtx, axis=1)
    mtx_mean = np.tile(vtx_mean,(time_p,1)).transpose(1,0) #时均流场
    mtx_fluctuate = mtx - mtx_mean #脉动流场
    R = (mtx_fluctuate.transpose(1,0) @ mtx_fluctuate)/time_p #获取快照POD的R矩阵
    eigenvalue, featurevector = np.linalg.eig(R) #获取特征值和特征向量

    recon_vector = (mtx_fluctuate @ featurevector[:,0])/math.sqrt(eigenvalue[0])
    for i in range(1, len(eigenvalue)):
        mid = (mtx_fluctuate @ featurevector[:,i])/math.sqrt(eigenvalue[i]) #获取pod特征向量
        recon_vector = np.column_stack((recon_vector, mid))

    #a = mtx_fluctuate.transpose(1, 0) @ recon_vector #获取时间系数 N*1
    a = recon_vector.transpose(1, 0) @ mtx_fluctuate

    sorted_indices = np.argsort(eigenvalue) #排序
    topk_evector = recon_vector[:, sorted_indices[:-k-1:-1]] #取前k个特征向量?
    topk_a = a[sorted_indices[:-k-1:-1], :] #取前k个时间系数?

    return topk_a, topk_evector, mtx_mean

# test = np.array(([1, 2, 4, 9],
#                  [3, 5, 7, 9],
#                  [5, 4, 12, 8],
#                  [7, 2, 3, 14],
#                  [1, 1, 9, 7],
#                  [8, 16, 56, 81],
#                  [15, 26, 8, 17],
#                  [11, 17, 24, 48]))

# k = 2
# (a, vector, mean) = pod_M(test, k)

# f = np.zeros((8, 4))

# for t in range(4):
#     for x in range(8):
#         for i in range(k):
#             f[x, t] = f[x, t] + a[i, t] * vector[x, i]
# #m = test - mean
# f = mean + f/4

# print(f)