import numpy as np
import matplotlib.pyplot as plt
import random

#xmin = -5, xmax = 5
x = np.arange(-5,5+0.5,0.5)
N = len(x)
print(x)
#Model parameter d = m1 + m2x + m3x^(2) + m4x^(3) + m5x^(4)
# m1 = 5
# m2 = 4
# m3 = 3
# m4 = 2
# m5 = 1
m = [5,4,3,2,1]

#Matriks Kernel G
# [ 1 x x^(2) x^(3) x^(4)]
# [ 1 x1 x2^(2) x2^(3) x2^(4)]
# [ 1 ..    ..    ..    .. ]
# [ 1 ..    ..    ..    .. ]
# [ 1 xn xn^(2) xn^(3) xn^(4)]

G = np.ones((N,5))
G[:,1] = x
G[:,2] = x**2
G[:,3] = x**3
G[:,4] = x**4

# d = G.m
d = np.dot(G,m)

#Penambahan noise
# 0 = Distribusi normal
# 20 = Standar Deviasi
# N = Banyaknya array noise sama dengan banyaknya array data
d_noise = [0 for i in range(N)]
noise = np.random.normal(0,20,N)
for i in range(N):
    d_noise[i] = d[i] + noise[i]

#Persamaan Inversi mencari model (m) m = ((GTG)^(-1)).GT.d

GT = np.transpose(G) # G Transpose
GTG = np.dot(GT,G) # GT.G
GTG_Inv = np.linalg.inv(GTG) # GTG^(-1)
GTd = np.dot(GT,d_noise) # GT dikalikan dengan matriks data yang memiliki noise
m_count = np.dot(GTG_Inv,GTd) # Mencari m dari data yang memiliki noise dengan persamaan inversi

#Persamaan Pemodelan Inversi d = G.m

d_new = np.dot(G,m_count) # Mencarri d baru dari m hasil estimasi

print("Data Sintetik : ", d)
print("Noise : ", noise)
print("Data dengan noise : ", d_noise)
print("Hasil m perhitungan : ", m_count)

#Plot Data
plt.plot(x,d,"-", label = "Data sintetik")
plt.plot(x,d_new,"r-", label = "Data hasil pemodelan inversi")
plt.plot(x,d_noise,"ko", label = "Data sintetik dengan noise")
plt.legend(loc="upper left")
plt.xlabel("x", fontsize=20)
plt.ylabel("y", fontsize=20)

fig, ax = plt.subplots(2)
ax[0].plot(x,d,"-", label = "Data sintetik")
ax[0].plot(x,d_noise,"ko", label = "Data sintetik dengan noise")
ax[0].legend(loc="upper left")
ax[0].set_xlabel("x", fontsize=20)
ax[0].set_ylabel("y", fontsize=20)
ax[1].plot(x,d_new,"r-", label = "Data hasil pemodelan inversi")
ax[1].plot(x,d_noise,"ko", label = "Data sintetik dengan noise")
ax[1].legend(loc="upper left")
ax[1].set_xlabel("x", fontsize=20)
ax[1].set_ylabel("y", fontsize=20)
plt.show()