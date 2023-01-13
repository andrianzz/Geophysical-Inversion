import numpy as np
import matplotlib.pyplot as plt

#Constant
rho = 2500 #kg/m3, densitas
G = 6.674*10**(-11) #Nm2/kg2, konstanta gravitasi
const = (4/3)*G*np.pi*rho*10**(5) #in gal

#Koordinat
x = [-500,-425,-350,-275,-200,-125,-50,25,100,175,250,325,400,475]
N = len(x)

#g_obs
g_obs = [0.0425,0.054,0.091,0.1517,0.2244,0.3725,0.6037,1.0675,1.5797,1.7118,1.2544,0.7637,0.4422,0.2612]

#iterasi
iter = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
niter = 20

xm = [0 for i in range(niter)]
zm = [0 for i in range(niter)]
rm = [0 for i in range(niter)]

#tebakan awal
xm[0] = 200
zm[0] = 150
rm[0] = 125

#jacobian matrix (dm)
def fcht(i):
    fcht = np.ones((N,3))
    for k in range(N):
        fcht[k,0] = (rm[i]**(3))*const*zm[i]*3*(x[k]-xm[i])*((x[k]-xm[i])**2 + zm[i]**2)**(-5/2)
        fcht[k,1] = (rm[i]**(3))*const*(((x[k]-xm[i])**2 - 2*zm[i]**2)/(((x[k]-xm[i]))**2 + zm[i]**2)**(5/2))
        fcht[k,2] = 3*(rm[i]**(2))*const*(zm[0]/(((x[k]-xm[i])**2 + (zm[i])**2)**(3/2)))
    FT = np.transpose(fcht)
    FTF = np.dot(FT, fcht)
    FTF_Inv = np.linalg.inv(FTF)
    return np.dot(FTF_Inv, FT)

def eror(i):
    eror = [0 for k in range(N)]
    for k in range(N):
        eror[k] = g_obs[k] - (rm[i]**(3))*const*zm[i]*((x[k]-xm[i])**2 + zm[i]**2)**(-3/2)
    return eror
rms = [0 for i in range(niter)]

for i in range (niter-1) :
    xm[i+1] = xm[i] + np.dot(fcht(i),eror(i))[0]
    zm[i+1] = zm[i] + np.dot(fcht(i),eror(i))[1]
    rm[i+1] = rm[i] + np.dot(fcht(i), eror(i))[2]
    for k in range(N):
        rms[0] = np.sqrt(np.mean((eror(0)[k])**2))
        rms[i+1] = np.sqrt(np.mean((eror(i+1)[k])**2))

#get value latest R
A = rm[19]
print("koordinat X hingga iterasi ke : " + str(niter),xm)
print("koordinat Z hingga iterasi ke : " + str(niter),zm)
print("Nilai R hingga iterasi ke : " + str(niter),rm)
fig, axes = plt.subplots(figsize=(10,10))
ax0 = plt.subplot2grid((2,1), (0,0), rowspan=1)
ax1 = plt.subplot2grid((2,1), (1,0), rowspan=1)
ax0.plot(xm,zm)
ax0.scatter(xm,zm)
ax1.plot(iter,rms)
ax0.set_xlabel("X")
ax0.set_ylabel("Keadalaman (Z)")
ax0.set_xlim(-550,500)
ax0.set_ylim(500,0)
ax1.set_xlabel("Iterasi")
ax1.set_ylabel("RMS")
ax0.set_title("Posisi Pusat Bola Homogen Setiap Iterasi dengan R akhir : "+ str(A))
plt.show()