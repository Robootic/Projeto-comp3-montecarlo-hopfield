import numpy as np
import matplotlib.pyplot as plt
import random
import math

jota = 1
mc_steps = 101
termal_steps = 101
size = [20,20]
temp_inicial = 1.53
temp_final = 3.28

nT = 50
array_Et = np.zeros(nT)
array_Mt = np.zeros(nT)
array_c = np.zeros(nT)
array_sus = np.zeros(nT)
array_T = np.linspace(temp_inicial, temp_final,nT)


#calcula a energia de flip
def flip_energy(lattice,x,y):
    close_friends = lattice[(x-1) % x_len, y]+ lattice[(x+1) % x_len, y]+ lattice[x, (y+1) % y_len] + lattice[x, (y-1) % y_len]

    energy = 2*jota*(close_friends)*lattice[x,y]
    return energy

#atualiza a grade do modelo de ising
def lattice_update(lattice):
    for i in range(x_len):
        for j in range(y_len):
            #escolhe spin para fazer o flip
            randon_x = random.randint(0,x_len-1)
            randon_y = random.randint(0,y_len-1)
            #calcula energia de flip
            E_flip = flip_energy(lattice,randon_x,randon_y)
            #atualiza ou nao o spin
            if(E_flip <= 0):
                lattice[randon_x][randon_y] = - lattice[randon_x][randon_y]
            elif(random.random() <= math.exp(-E_flip/(t))):
                lattice[randon_x][randon_y] = - lattice[randon_x][randon_y]
    return lattice

#calculando magnetizaçao
def calc_magnetization(lattice):
    mag = np.sum(lattice)
    return abs(mag/4)

#calculando E total
def calc_energyT(lattice):
    energy = 0
    for i in range(x_len):
        for j in range(y_len):
            energy += - flip_energy(lattice,i,j)  * 0.5
    return energy * 0.25


#cria array para Et e Mt
for dT in range (nT):
  #cria a grade de spins
  lattice = np.ones(size)
  x_len = len(lattice)
  y_len = len(lattice[0])
  t = array_T[dT]
  e_t = mag_t = epow_t = mag_pow_t = 0

  # indo pro equilibrio
  for i in range (mc_steps):
    lattice = lattice_update(lattice)

  for _ in range (termal_steps):
    lattice = lattice_update(lattice)
    e_t += calc_energyT(lattice)
    mag_t += calc_magnetization(lattice)
    epow_t += calc_energyT(lattice)
    mag_pow_t += calc_magnetization(lattice)**2

  #calculando M e E
  norma = termal_steps * x_len * y_len
  norma2 = termal_steps**2 * x_len * y_len

  array_Et[dT] = e_t / norma
  array_Mt[dT] = mag_t / termal_steps
  array_c[dT] = ((epow_t/norma) - (e_t**2/norma2))/(t**2)
  array_sus[dT] = (mag_pow_t/termal_steps - (mag_t/termal_steps)**2)/t

f = plt.figure(figsize=(18, 10)) # plot the calculated values

f.add_subplot(2, 2, 1 )
plt.scatter(array_T, array_Et, s=30, marker='o', color='magenta')
plt.xlabel("Temperatura (J/kb)", fontsize=16)
plt.ylabel("Energia ", fontsize=16)
plt.axis('tight')

f.add_subplot(2, 2, 2 )
plt.scatter(array_T, array_Mt, s=30, marker='o', color='lime')
plt.xlabel("Temperatura (J/kb)", fontsize=16)
plt.ylabel("Magnetização (%)", fontsize=16)
plt.axis('tight')

f.add_subplot(2, 2, 3 )
plt.scatter(array_T, array_c, s=30, marker='o', color='magenta')
plt.xlabel("Temperatura (J/kb)", fontsize=16)
plt.ylabel("Calor Específico ", fontsize=16)
plt.axis('tight')

f.add_subplot(2, 2, 4 )
plt.scatter(array_T, array_sus, s=30, marker='o', color='lime')
plt.xlabel("Temperatura (J/kb)", fontsize=16)
plt.ylabel("Suscetibilidade", fontsize=16)
plt.axis('tight')

plt.show()