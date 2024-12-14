import numpy as np
import random
import math
from config_mc import x_len, y_len

#Código relativo à malha de energia

def flip_energy(lattice, x, y, jota, x_len, y_len):
    lattice_1d = lattice.flatten()
    # Índice 1D do spin atual
    idx = x * y_len + y
    # Calcula a energia de interação considerando todos os spins
    close_friends_energy = 0
    for j in range(len(lattice_1d)):
        close_friends_energy += jota[idx, j] * lattice_1d[idx] * lattice_1d[j]
    return 2 * close_friends_energy



def lattice_update(lattice, jota, x_len, y_len, t):
    """Atualiza a grade do modelo de Ising."""
    for _ in range(x_len * y_len):
        random_x = random.randint(0, x_len - 1)
        random_y = random.randint(0, y_len - 1)
        E_flip = flip_energy(lattice, random_x, random_y, jota, x_len, y_len)

        if E_flip <= 0 or random.random() <= math.exp(-E_flip):
            lattice[random_x][random_y] = - lattice[random_x][random_y]

    return lattice


def total_energy(lattice, jota, x_len, y_len):
    """Calcula a energia total da grade."""
    energy = 0
    for x in range(x_len):
        for y in range(y_len):
            i = x * y_len + y
            neighbors = [
                ((x-1) % x_len, y),
                ((x+1) % x_len, y),
                (x, (y+1) % y_len),
                (x, (y-1) % y_len)
            ]
            for (nx, ny) in neighbors:
                j = nx * y_len + ny
                energy += -jota[i, j] * lattice[x, y] * lattice[nx, ny]

    return energy / 2


def j_combinado(lattice, patterns, js):
    """Combina as matrizes J ponderadas pelas energias dos padrões."""
    energies = [
        total_energy(lattice, js[i], x_len, y_len) for i in range(len(patterns))
    ]

    print("Energias:", energies)

    sum_energies = np.sum(np.abs(energies))
    pesos = [
        (abs(energies[i]) / sum_energies) if energies[i] < 0 else 0
        for i in range(len(patterns))
    ]

    j_comb = sum(pesos[i] * js[i] for i in range(len(patterns)))
    return j_comb