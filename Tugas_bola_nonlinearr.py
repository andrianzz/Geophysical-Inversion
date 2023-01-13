import numpy as np
import matplotlib.pyplot as plt

#Constant
rho = 2670 #kg/m3, densitas
G = 6.674*10**(-11) #Nm2/kg2, konstanta gravitasi
r = 20 #m, jari jari
const = (4/3)*G*np.pi*rho*r**(3)

#Koordinat
x = [10,20,30,40,50,60,70,80,90,100,120,130,140,150,160,170,180,190,200]

#Posisi Pusat Bola Homogen Model
x0 = 40
h = 60
N = len(x)

#iterasi
iter = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
niter = 20

#g_obs
g_obs = [0 for i in range(N)]
for i in range(N):
    g_obs[i] = const*h*((x[i]-x0)**2 + h**2)**(-3/2)

xm = [0 for i in range(niter)]
hm = [0 for i in range(niter)]

#tebakan awal
xm[0] = 40
hm[0] = 30

#jacobian matrix (dm)
def fcht(i):
    fcht = np.ones((N,2))
    for k in range(N):
        fcht[k,0] = const*hm[i]*3*(x[k]-xm[i])*((x[k]-xm[i])**2 + hm[i]**2)**(-5/2)
        fcht[k,1] = const*(((x[k]-xm[i])**2 - 2*hm[i]**2)/(((x[k]-xm[i]))**2 + hm[i]**2)**(5/2))
    FT = np.transpose(fcht)
    FTF = np.dot(FT, fcht)
    FTF_Inv = np.linalg.inv(FTF)
    return np.dot(FTF_Inv, FT)

def eror(i):
    eror = [0 for k in range(N)]
    for k in range(N):
        eror[k] = g_obs[k] - const*hm[i]*((x[k]-xm[i])**2 + hm[i]**2)**(-3/2)
    return eror
rms = [0 for i in range(niter)]

for i in range (niter-1) :
    xm[i+1] = xm[i] + np.dot(fcht(i),eror(i))[0]
    hm[i+1] = hm[i] + np.dot(fcht(i),eror(i))[1]
    for k in range(N):
        rms[0] = np.sqrt(np.mean((eror(0)[k])**2))
        rms[i+1] = np.sqrt(np.mean((eror(i+1)[k])**2))

print("koordinat X hingga iterasi ke : " + str(niter),xm)
print("koordinat h hingga iterasi ke : " + str(niter),hm)
fig, axes = plt.subplots(figsize=(10,10))
ax0 = plt.subplot2grid((2,1), (0,0), rowspan=1)
ax1 = plt.subplot2grid((2,1), (1,0), rowspan=1)
ax0.plot(xm,hm)
ax0.scatter(xm,hm)
ax1.plot(iter,rms)
ax0.set_xlabel("X")
ax0.set_ylabel("Keadalaman (h)")
ax0.set_xlim(0,100)
ax0.set_ylim(100,0)
ax1.set_xlabel("Iterasi")
ax1.set_ylabel("RMS")
ax0.set_title("Posisi Pusat Bola Homogen Setiap Iterasi")
plt.show()