import numpy as np
import matplotlib.pyplot as plt

xi = np.arange(0,2000+1,1)
G = 6.67*10**(-11)
R = 100
dRho = 400 #kg/m3

x = [100, 300, 500, 700, 900, 1100, 1300, 1500, 1700, 1900]
z = [-500, -700, -1000, -1200]

gz1 = [0 for i in range(len(xi))]
gz2 = [0 for i in range(len(xi))]
gz3 = [0 for i in range(len(xi))]
gz4 = [0 for i in range(len(xi))]
gztot = [0 for i in range(len(xi))]

fig, axes = plt.subplots(figsize=(7,10))
ax0 = plt.subplot2grid((2,1), (0,0), rowspan=1)
ax1 = plt.subplot2grid((2,1), (1,0), rowspan=1)

for i in range (5):
        ax1.add_patch(plt.Circle((x[i],z[2]),100,color='b'))
        for j in range(len(xi)):
                gz1[j] = ((G*1.33*np.pi*(R**3)*dRho*(-z[2])) / (((j - x[i]) ** 2 + z[2]**2) ** (3 / 2))) * 10 ** (5)
        if i <= 3 :
                ax1.add_patch(plt.Circle((x[i],z[3]),100,color='b'))
                for j in range(len(xi)):
                        gz2[j] = ((G * 1.33 * np.pi * (R ** 3) * dRho * -z[3]) / (((j - x[i]) ** 2 + z[3] ** 2) ** (3 / 2))) * 10 ** (5)

for i in range (6,10):
        ax1.add_patch(plt.Circle((x[i],z[1]),100,color='b'))
        for j in range(len(xi)):
                gz3[j] = ((G * 1.33 * np.pi * (R ** 3) * dRho * -z[1]) / (
                                ((j - x[i]) ** 2 + z[1] ** 2) ** (3 / 2))) * 10 ** (5)
        if i >= 7 :
                ax1.add_patch(plt.Circle((x[i],z[0]),100,color='b'))
                for j in range(len(xi)):
                        gz4[j] = ((G * 1.33 * np.pi * (R ** 3) * dRho * -z[0]) / (
                                ((j - x[i]) ** 2 + z[0] ** 2) ** (3 / 2))) * 10 ** (5)
for i in range(len(xi)):
        gztot[i] = gz1[i] + gz2[i] + gz3[i] + gz4[i]

ax0.plot(xi,gztot)
ax0.set_ylabel("mGal")
ax0.set_xlabel("Lintasan (m)")
ax0.set_title("Fault Respon Model")
ax1.set_ylabel("Kedalaman (m)")
ax1.set_ylim(-1500,0)
ax1.set_xlim(0,2000)
plt.show()