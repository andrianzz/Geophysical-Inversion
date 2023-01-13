import matplotlib.pyplot as plt
import numpy as np
import random

x = np.arange(1,10+1,1)
N = len(x)
y = 0.2 + 0.9*x

for i in range(N):
    y[i]+= random.gauss (0.0,0.1)

G = np.ones((N,2))
G[:,0] = 1
G[:,1] = x
GT = np.transpose(G)
GTGInv = np.linalg.inv(np.dot(GT,G))
GTGInvGT = np.dot(GTGInv,GT)
m = np.dot(GTGInvGT, y)
print(m)