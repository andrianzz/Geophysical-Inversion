import numpy as np
import matplotlib.pyplot as plt
import random

#Data sintetik
#Koordinat Gempa km
xp = 11
yp = 13
#Koordinat Stasiun km
x = [3, 5, 9, 11, 15, 17]
y = [7, 10, 13, 6, 9, 17]
#Waktu Observasi
T = [1.64, 1.78, 0.6, 0.85, 0.6, 1.3]

#Kecepatan km/s
vp = 6

#Travel time
def travel_time(xe,ye):
    return (1/vp)*np.sqrt((m-x[k])**2 + (n-y[k])**2)

def rms(m,n):
    eror2 = 0
    for k in range(len(x)):
        eror2 += (T[k] - (1/vp)*np.sqrt((m-x[k])**2 + (n-y[k])**2))**2
    return np.sqrt((eror2)/len(T))

#make grid
dx = 0.25
dy = 0.25

xi = np.arange(0,25,dx)
yi = np.arange(0,25,dy)
xv, yv = np.meshgrid(xi,yi)
zv = np.zeros((len(xi),len(yi)))
for i in range(len(xi)):
    for j in range(len(yi)):
        zv[i][j] = rms(xi[i],yi[j])

print(zv)
plt.scatter(xp,yp)
plt.contourf(xv,yv,zv,cmap="gray")
cbar = plt.colorbar()
plt.show()