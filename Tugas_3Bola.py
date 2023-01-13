import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,1000+10,10)
N = len(x)
G = 6.67*10**(-11)
#jari2
r1 = 100
r2 = 50
r3 = 300

#Kedalaman z
z1 = 500
z2 = 300
z3 = 700

#posisi bola
x1 = 300
x2 = 500
x3 = 700

#misal reference density = 2000 kg/m3
#kontras densitas model
drho1 = 800
drho2 = 400
drho3 = 600

#kontras densitas akan dicari dengan persamaan matrix dari data model yang telah diberi noise
g_model = [0 for i in range(N)]
for i in range (N):
    g_model[i] = G*(4/3)*np.pi*((r1**3)*z1*drho1/(((x[i]-x1)**2 + z1**2)**(3/2))
                                + (r2**3)*z2*drho2/(((x[i]-x2)**2 + z2**2)**(3/2))
                                + (r3**3)*z3*drho3/(((x[i]-x3)**2 + z3**2)**(3/2)))*10**5
#Menambah model dengan noise
g_noise = [0 for i in range(N)]
noise = np.random.normal(0,0.01,N)
for i in range (N):
    g_noise[i] = g_model[i] + noise[i]

#Proses inversi mencari drho
#membuat matriks kernel G
gamma = G*(4/3)*np.pi
G = np.ones((N,3))
G[:,0] = gamma*((r1**3)*z1/(((x-x1)**2 + z1**2)**(3/2)))*10**5
G[:,1] = gamma*((r2**3)*z2/(((x-x2)**2 + z2**2)**(3/2)))*10**5
G[:,2] = gamma*((r3**3)*z3/(((x-x3)**2 + z3**2)**(3/2)))*10**5

#print(G)
#Melakukan perhitungan persamaan invesi m = [GTG]^-1 GT.d
#dengan d merupakan g_model yang telah diberi noise
#m merupakan rho yang di estimasi
GT = np.transpose(G)
GTGInv = np.linalg.inv(np.dot(GT,G))
GTGInvGT = np.dot(GTGInv,GT)
m = np.dot(GTGInvGT, g_noise)

print(m)
fig, axes = plt.subplots(figsize=(10,10))
ax0 = plt.subplot2grid((2,2), (0,0), rowspan=1)
ax1 = plt.subplot2grid((2,2), (1,0), rowspan=1)
ax2 = plt.subplot2grid((2,2), (0,1), rowspan=1)
ax3 = plt.subplot2grid((2,2), (1,1), rowspan=1)

#ploting
ax0.plot(x,g_model)
ax0.set_xlabel("Data")
ax0.set_ylabel("mGal")
ax1.add_patch(plt.Circle((x1,-z1),r1,color='b'))
ax1.add_patch(plt.Circle((x2,-z2),r2,color='b'))
ax1.add_patch(plt.Circle((x3,-z3),r3,color='b'))
ax1.set_ylabel("Depth")
ax2.plot(x,g_noise)
ax2.set_xlabel("Data dengan noise")
ax3.add_patch(plt.Circle((x1,-z1),r1,color='r'))
ax3.add_patch(plt.Circle((x2,-z2),r2,color='r'))
ax3.add_patch(plt.Circle((x3,-z3),r3,color='r'))
ax1.set_ylim(-1000,0)
ax1.set_xlim(0,1000)
ax1.set_xlabel("Model density lingkaran (kiri-kanan) rho 1 = "+str(drho1)+ " rho 2 = "+str(drho2)+" rho 3 = "+str(drho3))
ax3.set_ylim(-1000,0)
ax3.set_xlim(0,1000)
ax3.set_xlabel("Hasil inversi rho 1 = "+str(m[0])+ " rho 2 = "+str(m[1])+" rho 3 = "+str(m[2]))
plt.show()