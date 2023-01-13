import numpy as np
import matplotlib.pyplot as plt
import random

#Data sintetik
#Koordinat Gempa km
xp = 13
yp = 11
#Koordinat Stasiun km
x = [3, 5, 9, 11, 15, 17]
y = [7, 10, 13, 6, 9, 17]
#Waktu Observasi
T = [1.64, 1.78, 0.6, 0.85, 0.6, 1.3]
T_sin = [ 0 for i in range(len(T))]
#Kecepatan km/s
vp = 6

#Travel time
def travel_time(xe,ye):
    return (1/vp)*np.sqrt((xp-xe)**2 + (yp-ye)**2)

#Make Grid
dx = 0.2
dy = 0.2
grid_x = np.arange(0,20,dx)
grid_y = np.arange(3,20,dy)
N = 50
val_x = [0 for i in range(N)]
val_y = [0 for i in range(N)]
TT = [0 for i in range(N)]
for i in range(N):
    val_x[i] = random.choice(grid_x)
    val_y[i] = random.choice(grid_y)
    TT[i] = travel_time(val_x[i],val_y[i])

X,Y = np.meshgrid(sorted(val_x, key = lambda x:float(x)),sorted(val_y, key = lambda x:float(x)))
Z = travel_time(X,Y)
plt.scatter(val_x,val_y,s=200,c=TT,cmap="gray",label="Random Point")
cbar = plt.colorbar()
cbar.set_label(label="Jarak Dengan Epicenter Asli")
plt.scatter(x,y,s=200,marker="v",color="red",label="Stasiun")
plt.scatter(xp,yp,s=200,marker="*",color="blue",label="Epicenter")
plt.scatter(val_x[np.argmin(TT)],val_y[np.argmin(TT)],color="green",label="Jarak Minimum")
plt.contour(X,Y,Z,cmap="gray")
plt.title("Random Point : "+str(N))
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.show()