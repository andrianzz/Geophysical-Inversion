import numpy as np
import matplotlib.pyplot as plt
#Perhitungan berdasarkan metode tomografi waktu tempuh, bukan delay time tomografi
#Koordinat
s = [ 300, 100, 0]
Rx = [ 400, 400, 300, 100]
Rz = [ 200, 400, 400, 400]
#waktu
timeobs = [ 0.2364, 0.2111, 0.2235, 0.1999, 0.2368, 0.2836, 0.2069]

#Matrix kernel G
#untuk simplifikasi lintasan ray hanya dibagi 2, tidak ditentukan pjg setiap ray pada kotak
G = np.ones((7,4))
G[0,1] = G[0,3] = np.sqrt((s[0]-Rx[2])**(2) + Rz[2]**(2))/2
G[1,1] = G[1,2] = np.sqrt((s[0]-Rx[3])**(2) + Rz[3]**(2))/2
G[2,0] = G[2,3] = np.sqrt((s[1]-Rx[2])**(2) + Rz[2]**(2))/2
G[3,0] = G[3,2] = np.sqrt((s[1]-Rx[3])**(2) + Rz[3]**(2))/2
G[4,0] = G[4,1] = np.sqrt((s[2]-Rx[0])**(2) + Rz[0]**(2))/2
G[5,0] = G[5,3] = np.sqrt((s[2]-Rx[1])**(2) + Rz[1]**(2))/2
G[6,0] = G[6,2] = np.sqrt((s[2]-Rx[3])**(2) + Rz[3]**(2))/2
GT = np.transpose(G)

#membuat matrix peredam dg peredam 0.1
e = np.identity(4)
for i in range(4):
    e[i][i] = 0.01*e[i][i]

#menghitung m_est
GTG_e_Inv = np.linalg.inv(np.dot(GT,G) + e)
m_est = np.dot(GTG_e_Inv, np.dot(GT,timeobs))

#Karena hasi yang dihasilkan adalah s atau slowness
#maka akan dicari v1 v2 v3 v4
print ("V1 hasil inversi (m/s) : ",1/m_est[0])
print ("V2 hasil inversi (m/s) : ",1/m_est[1])
print ("V3 hasil inversi (m/s) : ",1/m_est[2])
print ("V4 hasil inversi (m/s) : ",1/m_est[3])