import numpy as np
import matplotlib.pyplot as plt
from core_mc import lattice_update, total_energy, j_combinado
from utils_mc import load_patterns, cria_j, load_noisy_pattern
from config_mc import x_len, y_len, iterations, pattern_folder,noisy_pattern_file

#Código de visualização e reconhecimento de padrão

def plot_lattice(lattice):
    """Exibe a matriz."""
    plt.clf()
    plt.pcolor(lattice, cmap='binary', edgecolors='black')
    plt.gca().invert_yaxis()
    plt.pause(0.1)

if __name__ == "__main__":
    # Carrega os padrões dos números 0,2,5,7,9 da pasta
    patterns = load_patterns(pattern_folder)
    js = [cria_j(pattern) for pattern in patterns]

    # Carrega o padrão do 3 de um arquivo .txt para tentá-lo convergí-lo para um dos padrões salvos
    lattice = load_noisy_pattern(noisy_pattern_file)
    if lattice is None:  # Verifica se houve erro ao carregar o arquivo
        raise ValueError(f"Erro ao carregar o arquivo {noisy_pattern_file}. Verifique se ele existe e está formatado corretamente.")

    # Verifica se o tamanho do lattice está correto
    if lattice.shape != (x_len, y_len):
        raise ValueError(f"Tamanho do lattice no arquivo ({lattice.shape}) não corresponde ao esperado ({x_len}, {y_len}).")
    
    # Cria um J combinado a partir dos padrões dos números salvos e do núm
    new_j = j_combinado(lattice, patterns, js)
    
    # Plot inicial
    plt.figure(figsize=(6, 6))
    plot_lattice(lattice)

    # Atualizar a matriz até atingir um estado de menor energia
    for iteration in range(iterations):
        lattice = lattice_update(lattice, new_j, x_len, y_len, t=None)
        energy = total_energy(lattice, new_j, x_len, y_len)
        print(f"Iteração = {iteration}, Energia = {energy}")
        plot_lattice(lattice)

    plt.show()