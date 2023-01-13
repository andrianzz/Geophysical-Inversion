import numpy as np
import matplotlib.pyplot as plt

x1 = [ -2.20, -0.25, 0.0, 1.00, 1.25, 5.25]
x2 = [ -2.25, -1.20, 0.0, -1.00, 4.25, 5.00]
y = [ 7.37376, 1.79669, 0.137058, -0.456891, 11.9378, 11.0596]
N = len(x1)

#Kernel Matrix
G = np.ones((N,3))
G[:,1] = x1
for i in range (N):
    G[i,2] = x2[i]**(2)

GT = np.transpose(G)
GTGInv = np.linalg.inv(np.dot(GT,G))

#menghitung a0 a1 a2
m_est = np.dot(GTGInv,np.dot(GT,y))
print("Hasil Inversi a0 a1 a2 :", m_est)

#menghitung misfit
misfit = 0
for i in range(N):
    misfit = misfit + y[i]-(m_est[0] + m_est[1]*x1[i] + m_est[2]*x2[i]**(2))

print("misfit :", misfit)

#Laju Perubahan data
dydx1 = m_est[1] + m_est[2]*(0.5)**(2)
dydx2 = 2*m_est[2]*(0.5)**(2)
print("Laju perubahan terhadap sumbu x1 : ", dydx1)
print("Laju perubahan terhadap sumbu x2 : ",dydx2)

#Menghitung nilai y pada koordinat (-1.5;-1.5),(-2;0.5),(3,5;4.0)
y1 = m_est[0] + m_est[1]*(-1.5) + m_est[2]*(-1.5)**(2)
y2 = m_est[0] + m_est[1]*(-2) + m_est[2]*(0.5)**(2)
y3 = m_est[0] + m_est[1]*(3.5) + m_est[2]*(4.0)**(2)
print("y dalam koordinat (-1.5;-1.5) : ", y1)
print("y dalam koordinat (-2;0.5): ", y2)
print("y dalam koordinat (3.5;4.0): ", y3)

#Ploting data hasil inversi dan data awal
y_est = [0 for i in range(N)]
for i in range(N):
    y_est[i] = m_est[0] + m_est[1] * (x1[i]) + m_est[2] * (x2[i]) ** (2)
fig = plt.figure(figsize=(4,4))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x1,x2,y, label="Data Observasi")
ax.scatter(x1,x2,y_est,label="Hasil estimasi")
ax.set_xlabel("x1")
ax.set_ylabel("x2")
ax.set_zlabel("y")
ax.legend()
plt.show()