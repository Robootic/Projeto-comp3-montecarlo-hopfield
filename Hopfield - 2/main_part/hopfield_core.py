import numpy as np
import random
import math

#* CÓDIGO RELATIVO À MALHA DE ENERGIA - PRINCIPAL

#^ Calcula energia de flip de 1 spin
def flip_energy(lattice, x, y, jota, y_len):
    lattice_1d = lattice.flatten()
    # Índice 1D do spin atual
    idx = x * y_len + y
    # Calcula a energia de interação considerando todos os spins
    close_friends_energy = 0
    for j in range(len(lattice_1d)):
        close_friends_energy += jota[idx, j] * lattice_1d[idx] * lattice_1d[j]
    return 2 * close_friends_energy


#^ Atualização do lattice, com uma abordagem de Monte Carlo - Metropolis
def lattice_update(lattice, jota, x_len, y_len, t):
    """Atualiza a grade do modelo de Ising."""
    for _ in range(x_len * y_len):
        random_x = random.randint(0, x_len - 1)
        random_y = random.randint(0, y_len - 1)
        E_flip = flip_energy(lattice, random_x, random_y, jota, y_len)

        if E_flip <= 0 or random.random() <= math.exp(-E_flip):
            lattice[random_x][random_y] = - lattice[random_x][random_y]

    return lattice

#^ Calcula a energia total com interações globais
def total_energy(lattice, jota):
    """
    Calcula a energia total da rede considerando interações globais.
    """
    lattice_1d = lattice.flatten()  # Converte o lattice 2D para 1D
    energy = 0  # Inicializa a energia total

    # Itera sobre os pares (i, j) apenas uma vez
    for i in range(len(lattice_1d)):
        for j in range(i + 1, len(lattice_1d)):  # Começa em i+1 para evitar duplicatas
            energy += -jota[i, j] * lattice_1d[i] * lattice_1d[j]

    return energy

#^ Combina as matrizes j (jotinha) criando a matriz J (jotão)
def j_combiner(lattice, patterns, js):
    """Combina as matrizes J ponderadas pelas energias dos padrões."""
    energies = [
        total_energy(lattice, js[i]) for i in range(len(patterns))
    ]
    

    energies = np.array(energies)
    sum_energies = np.sum(np.abs(energies[energies < 0]))
    #Calcula os pesos da combinação
    weights = [
        (abs(energies[i]) / sum_energies) if energies[i] < 0 else 0
        for i in range(len(patterns))
    ]
    print("Pesos:", weights)

    # Dados para a tabela
    dados = {
        "Padrão": [f"Padrão {i+1}" for i in range(len(patterns))],
        "Energia da malha": energies,
        "Peso": weights
    }

    j_comb = sum(weights[i] * js[i] for i in range(len(patterns)))
    return j_comb