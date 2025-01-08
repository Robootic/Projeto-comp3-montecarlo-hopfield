import matplotlib.pyplot as plt
from hopfield_core import lattice_update, total_energy, j_combiner
from hopfield_utils import load_patterns, generate_j, load_pattern
from hopfield_config import x_len, y_len, iterations, pattern_folder,noisy_pattern_file

#* ARQUIVO COM AMOSTRA DE FUNCIONALIDADE DO CÓDIGO PRINCIPAL DA REDE NEURAL (hopfield_core.py) - contém visualização

#^ Exibe a matriz graficamente
def plot_lattice(lattice):
    """Exibe a matriz."""
    plt.clf()
    plt.pcolor(lattice, cmap='binary', edgecolors='black')
    plt.gca().invert_yaxis()
    plt.pause(0.1)

if __name__ == "__main__":
    #^ Carrega os padrões dos números 2,3,7,8 da pasta
    patterns = load_patterns(pattern_folder)
    js = [generate_j(pattern) for pattern in patterns]

    #^ Carrega o padrão do 2 com 35% de ruído para tentar convergi-lo para um dos padrões salvos
    lattice = load_pattern(noisy_pattern_file)
    if lattice is None:  # Verifica se houve erro ao carregar o arquivo
        raise ValueError(f"Erro ao carregar o arquivo {noisy_pattern_file}. Verifique se ele existe e está formatado corretamente.")
    # Verifica se o tamanho do lattice está correto
    if lattice.shape != (x_len, y_len):
        raise ValueError(f"Tamanho do lattice no arquivo ({lattice.shape}) não corresponde ao esperado ({x_len}, {y_len}).")
    
    #^ Cria um J combinado a partir dos padrões dos números salvos e do número ruidoso
    new_j = j_combiner(lattice, patterns, js)
    
    #^ Plot inicial
    plt.figure(figsize=(6, 6))
    plot_lattice(lattice)

    #^ Atualiza a matriz até atingir um estado de menor energia
    for iteration in range(iterations):
        lattice = lattice_update(lattice, new_j, x_len, y_len, t=None)
        energy = total_energy(lattice, new_j)
        print(f"Iteração = {iteration}, Energia = {energy}")
        plot_lattice(lattice)

    plt.show()