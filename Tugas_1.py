import numpy as np
import matplotlib.pyplot as plt

xi = np.arange(0,2000+100,100)
G = 6.67*10**(-11)
rho1 = 2600
rho2 = 3000
rho3 = 4000
x_c1 = 1000
x_c2 = 1500
x_c3 = 300
z_c1 = 400
z_c2 = 600
z_c3 = 200
R1 = 350
R2 = 500
R3 = 100
gz1 = [0 for i in range (len(xi))]
gz2 = [0 for i in range (len(xi))]
gz3 = [0 for i in range (len(xi))]
gztot = [0 for i in range (len(xi))]
for i in range (len(xi)) :
    print(i)
    gz1[i] = ((G*1.33*np.pi*(R1**3)*rho1*z_c1)/(((i*100 - x_c1)**2 + z_c1**2)**(3/2)))*10**(5)
    gz2[i] = ((G * 1.33 * np.pi * (R2 ** 3) * rho2 * z_c2) / (((i * 100 - x_c2) ** 2 + z_c2 ** 2) ** (3 / 2))) * 10 ** (5)
    gz3[i] = ((G * 1.33 * np.pi * (R3 ** 3) * rho3 * z_c3) / (((i * 100 - x_c3) ** 2 + z_c3 ** 2) ** (3 / 2))) * 10 ** (
        5)
    gztot[i] = gz1[i] + gz2[i] + gz3[i]

plt.plot(xi,gztot)
plt.xlabel("Meter")
plt.ylabel("mGal")
plt.title("Respon Model")
plt.show()