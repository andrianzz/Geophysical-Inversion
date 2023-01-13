import numpy as np
import matplotlib.pyplot as plt
import random

#xmin = 0, xmax = 20
x = np.arange(0,20+1,1)
N = len(x)

#Model parameter d = m1 + m2x + m3x^(2)
# m1 = 3
# m2 = 2
# m3 = 1
m = [3,2,1]

#Matriks Kernel G
# [ 1 x x^(2)]
# [ 1 x1 x2^(2)]
# [ 1 .. ..    ]
# [ 1 .. ..    ]
# [ 1 xn xn^(2)]

G = np.ones((N,3))
G[:,1] = x
G[:,2] = x**2

# d = G.m
d = np.dot(G,m)

#Penambahan noise
# 0 = Distribusi normal
# 10 = Standar Deviasi
# N = Banyaknya array noise sama dengan banyaknya array data
d_noise = [0 for i in range(N)]
noise = np.random.normal(0,10,N)
for i in range(N):
    d_noise[i] = d[i] + noise[i]

print("Data Sintetik : ", d)
print("Noise : ", noise)
print("Data dengan noise : ", d_noise)

plt.plot(x,d,"-", label = "Data sintetik")
plt.plot(x,d_noise,"ko", label = "Data sintetik dengan noise")
plt.xlabel("x", fontsize=20)
plt.ylabel("y", fontsize=20)
plt.legend(loc="upper left")
plt.show()

