import os
import numpy as np
import matplotlib.pyplot as plt

def read_binary_matrix(file_path):
    """Lê uma matriz binária de um arquivo .txt."""
    with open(file_path, 'r') as file:
        lines = file.readlines()
        matrix = [list(map(int, line.strip().split())) for line in lines]
    return np.array(matrix)

def plot_matrices(matrices, title="Cópias do nº 8 com ruído de 20%"):
    """Exibe as matrizes binárias graficamente."""
    num_matrices = len(matrices)
    cols = 5  # número de colunas para o grid de plotagem
    rows = (num_matrices + cols - 1) // cols  # calcular número de linhas
    
    fig, axes = plt.subplots(rows, cols, figsize=(15, 3 * rows))
    fig.suptitle(title, fontsize=16, fontweight='bold', y=1.00)  # Adiciona título no topo
    
    axes = axes.flatten()  # Garante que os eixos sejam indexáveis em 1D
    
    for i, matrix in enumerate(matrices):
        axes[i].imshow(matrix, cmap='binary')
        axes[i].axis('off')
        
    # Desliga os eixos extras se houver
    for i in range(len(matrices), len(axes)):
        axes[i].axis('off')
    
    plt.tight_layout()
    plt.subplots_adjust(top=0.9)  # Ajusta espaço para o título no topo
    plt.show()

def main():
    folder_path = "hopfield/noisy_8_20percent"
    
    # Obtém os 10 primeiros arquivos .txt na pasta
    txt_files = [f for f in os.listdir(folder_path) if f.endswith('.txt')]
    txt_files = sorted(txt_files)[:10]  # Garante ordem e limita a 10 arquivos

    matrices = []

    for txt_file in txt_files:
        file_path = os.path.join(folder_path, txt_file)
        try:
            matrix = read_binary_matrix(file_path)
            matrices.append(matrix)
        except Exception as e:
            print(f"Erro ao ler o arquivo {txt_file}: {e}")

    if matrices:
        plot_matrices(matrices)
    else:
        print("Nenhuma matriz válida foi encontrada.")

if __name__ == "__main__":
    main()
