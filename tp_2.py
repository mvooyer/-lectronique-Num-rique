import numpy as np
import matplotlib.pyplot as plt


# 1 kOhm
R = 1e3
# 1 mF
C = 1e-3
v_0 = 3.3

# base de temps
t = np.linspace(0, 10, 1000)

# expression exacte de q(t)
q = v_0 * C * (1 - np.exp(-t / (R * C)))
# i = dq(t) / dt
i = v_0 * np.exp(-t / (R * C)) / R
# U = C * q
u = v_0 * (1 - np.exp(-t / (R * C)))

# calcul de u(t) avec la methode de Runge Kutta d ordre 4 (temps de charge)
h = 10 / 999
u_r = np.zeros(1000)
for j in range(1, 1000):
    k1 = v_0 / R / C - 1 / R / C * u_r[j-1]
    k2 = v_0 / R / C - 1 / R / C * (u_r[j-1] + h / 2 * k1)
    k3 = v_0 / R / C - 1 / R / C * (u_r[j-1] + h / 2 * k2)
    k4 = v_0 / R / C - 1 / R / C * (u_r[j-1] + h * k3)
    u_r[j] = u_r[j-1] + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)

# expression exacte de u_d(t) pour la decharge
u_d = v_0 * np.exp(-t / R / C)
# calcul de u_d(t) avec la methode de Runge Kutta d'ordre 4 (temps de decharge)
u_dr = np.zeros(1000)
u_dr[0] = v_0
for j in range(1, 1000):
    k1b = - u_dr[j-1] / R / C
    k2b = - (u_dr[j-1] + h / 2 * k1b) / R / C
    k3b = - (u_dr[j-1] + h / 2 * k2b) / R / C
    k4b = - (u_dr[j-1] + h * k3b) / R / C
    u_dr[j] = u_dr[j-1] + h / 6 * (k1b + 2 * k2b + 2 * k3b + k4b)
plt.figure()

# cree un subplot qui trace la charge en fonction du temps
plt.subplot(2, 2, 1)
plt.plot(t, q, label='Charge du condensateur initialement déchargé')
plt.ylabel('Charge (en Coulomb)')
plt.xlabel('Temps (en seconde)')
plt.title('Évolution de la charge au cours du temps')
plt.legend()

# cree un subplot qui trace le courant en fonction du temps
plt.subplot(2, 2, 2)
plt.plot(t, i, label='Courant du condensateur initialement déchargé', color='r')
plt.ylabel('Courant (en Ampère)')
plt.xlabel('Temps (en seconde)')
plt.title('Évolution du courant au cours du temps')
plt.legend()

# cree un subplot qui trace la tension en fonction du temps
plt.subplot(2, 2, 3)
plt.plot(t, u, 'r', label='Tension exacte')
plt.plot(t, u_r, 'g--', label='Tension Runge Kutta')
plt.ylabel('Tension (en Volt)')
plt.xlabel('Temps (en seconde)')
plt.title('Tension de charge du condensateur au cours du temps')
plt.legend()

# cree un subplot et trace la tension de decharge au cours du temps
plt.subplot(2, 2, 4)
plt.plot(t, u_d, 'b', label='Tension exacte')
plt.plot(t, u_dr, 'r--', label='Tension méthode de Runge Kutta d ordre 4')
plt.ylabel('Tension (en Volt)')
plt.xlabel('Temps (en seconde)')
plt.title('Tension de décharge du condensateur au cours du temps')
plt.legend()
plt.show()