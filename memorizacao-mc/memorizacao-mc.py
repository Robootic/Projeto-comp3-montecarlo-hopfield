import numpy as np
import random
import math
import matplotlib.pyplot as plt

# Parâmetros do modelo
x_len = 10
y_len = 10
t = 1
iterations = 10

matriz_A = np.array([
    [-1, -1, -1, -1, 1, 1, -1, -1, -1, -1],
    [-1, -1, -1, 1, 1, 1, 1, -1, -1, -1],
    [-1, -1, 1, 1, -1, -1, 1, 1, -1, -1],
    [-1, 1, 1, -1, -1, -1, -1, 1, 1, -1],
    [-1, 1, 1, 1, 1, 1, 1, 1, 1, -1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, -1, -1, -1, -1, 1, 1, 1],
    [1, 1, -1, -1, -1, -1, -1, -1, 1, 1],
    [1, 1, -1, -1, -1, -1, -1, -1, 1, 1],
    [1, 1, -1, -1, -1, -1, -1, -1, 1, 1]
])


# Transformar a matriz 2D em um vetor 1D
matriz_1d = matriz_A.reshape(-1)

# Calcular o produto externo
J = np.outer(matriz_1d, matriz_1d)

# Função para gerar uma matriz aleatória de spins
def create_random_lattice(x_len, y_len):
    return np.random.choice([-1, 1], size=(x_len, y_len))

# Calcula a energia de flip usando a matriz J
def flip_energy(lattice, x, y, J, x_len, y_len):
    close_friends_energy = 0

    neighbors = [
        ((x-1) % x_len, y),  # vizinho de cima
        ((x+1) % x_len, y),  # vizinho de baixo
        (x, (y+1) % y_len),  # vizinho à direita
        (x, (y-1) % y_len)   # vizinho à esquerda
    ]

    for (nx, ny) in neighbors:
        # O índice 1D para acessar a matriz J
        i = (x) * y_len + y  # índice 1D para o spin (x, y)
        j = (nx) * y_len + ny  # índice 1D para o spin vizinho (nx, ny)

        # Adiciona a energia de interação entre os spins i e j
        close_friends_energy += J[i, j] * lattice[x, y] * lattice[nx, ny]

    return 2 * close_friends_energy

# Atualiza a grade do modelo de Ising
def lattice_update(lattice, J, x_len, y_len, t):
    for i in range(x_len):
        for j in range(y_len):
            # Escolher uma célula aleatória para tentar o flip
            random_x = random.randint(0, x_len - 1)
            random_y = random.randint(0, y_len - 1)

            # Calcular a energia de flip
            E_flip = flip_energy(lattice, random_x, random_y, J, x_len, y_len)

            # Atualizar o spin com base na energia de flip
            if E_flip <= 0:
                lattice[random_x][random_y] = - lattice[random_x][random_y]
            elif random.random() <= math.exp(-E_flip / t):
                lattice[random_x][random_y] = - lattice[random_x][random_y]

    return lattice


def total_energy(lattice, J, x_len, y_len):
    energy = 0
    for x in range(x_len):
        for y in range(y_len):
            i = (x) * y_len + y
            neighbors = [
                ((x-1) % x_len, y),
                ((x+1) % x_len, y),
                (x, (y+1) % y_len),
                (x, (y-1) % y_len)
            ]
            for (nx, ny) in neighbors:
                j = (nx) * y_len + ny
                energy += -0.5 * J[i, j] * lattice[x, y] * lattice[nx, ny]
    return energy

# Função para exibir a matriz
def plot_lattice(lattice):
    plt.clf()  # Limpar a figura
    plt.pcolor(lattice, cmap='binary', edgecolors='black')
    plt.gca().invert_yaxis()
    plt.pause(0.1)  # Pausar para mostrar a atualização


#Inicializar a grade de spins aleatórios
lattice = create_random_lattice(x_len, y_len)

#Plot inicial
plt.figure(figsize=(6, 6))
plot_lattice(lattice)
energy = 0

# Atualizar a matriz até atingir um estado de menor energia

iteration = 0
while (energy > -200 or iteration < iterations):
    lattice = lattice_update(lattice, J, x_len, y_len, t)
    iteration += 1

    #Calcular e exibir a energia total a cada iteração
    energy = total_energy(lattice, J, x_len, y_len)
    print(f"Iteração = {iteration}, Energia = {energy}")


#Exibir a matriz sendo atualizada a cada iteração
    plot_lattice(lattice)

plt.show()