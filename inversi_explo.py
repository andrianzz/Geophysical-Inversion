import numpy as np
import matplotlib.pyplot as plt
import random

x_est = np.arange(0,1+0.1,0.1)
N = len(x_est)
#print(x_est)
#print(N)
d = 1 + 2*(x_est) + 3*(x_est)**2
#print(d)
for i in range(N):
    d[i]+= random.gauss (0.0,0.1)

#Inversi Berbobot
#ForWeight
d[1] = 2*d[1]
d[4] = 2*d[4]
d[7] = 2*d[5]

C = np.identity(N)
C[1][1] = (2*C[1][1])**2
C[4][4] = (2*C[4][4])**2
C[7][7] = (2*C[7][7])**2
CInv = np.linalg.inv(C)
G = np.ones((N,3))
G[:,1] = x_est
G[:,2] = x_est**2
GT = np.transpose(G)
GTCInvGinv = np.linalg.inv(np.dot(np.dot(GT,CInv),G))
GTCInvD = np.dot(np.dot(GT,CInv),d)
m_est = np.dot(GTCInvGinv,GTCInvD)
print(m_est)

#Inversi tidak menggunakan bobot
G = np.ones((N,3))
G[:,1] = x_est
G[:,2] = x_est**2
GT = np.transpose(G)
GTGInv = np.linalg.inv(np.dot(GT,G))
GTD = np.dot(GT,d)
m_est_normal = np.dot(GTGInv,GTD)

#Predicted
x = np.arange(0,max(x_est)+0.1,0.1)
y = m_est[0] + m_est[1]*x + m_est[2]*x**2
y_normal = m_est_normal[0] + m_est_normal[1]*x + m_est_normal[2]*x**2
xtrue = np.arange(0,1+0.1,0.1)
ytrue = 1 + 2*(xtrue) + 3*(xtrue)**2

plt.subplots(figsize=(15,10))
plt.plot(x_est,d,"ko",markersize=7)
plt.plot(x,y,label="Hasil Invesi berbobot")
plt.plot(x,y_normal,label="Hasil Invesi tidak berbobot")
plt.plot(xtrue,ytrue,label="Real Data")
plt.grid()
plt.xlabel(r"$x$",fontsize=20)
plt.ylabel(r"$d_i^{obs}$",fontsize=20)
plt.legend()
plt.show()