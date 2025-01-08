import numpy as np
import matplotlib.pyplot as plt
import os
#from hopfield_utils import load_pattern

def load_pattern(file_name):
    """
    Carrega um padrão de um arquivo .txt e o retorna como uma matriz NumPy.
    """
    file_path = os.path.abspath(file_name)  # Obtém o caminho absoluto
    
    if not os.path.exists(file_path):
        print(f"Erro: O arquivo {file_path} não existe.")
        return None

    try:
        pattern = np.loadtxt(file_path)  # Carrega o arquivo como uma matriz
        return pattern
    except Exception as e:
        print(f"Erro ao carregar o arquivo {file_path}: {e}")
        return None

def add_noise(matrix, noise_percentage):
    """Adiciona ruído a uma matriz com base em uma porcentagem de elementos alterados."""
    noisy_matrix = matrix.copy()
    num_elements = matrix.size
    num_noisy_elements = int(num_elements * noise_percentage / 100)

    # Gera índices aleatórios para adicionar ruído
    indices = np.random.choice(num_elements, num_noisy_elements, replace=False)

    # Inverter os valores nos índices escolhidos (1 -> -1 ou -1 -> 1)
    flat_matrix = noisy_matrix.flatten()
    flat_matrix[indices] *= -1  
    noisy_matrix = flat_matrix.reshape(matrix.shape)

    return noisy_matrix

def save_matrix(matrix, file_path):
    """Salva uma matriz em um arquivo .txt."""
    try:
        np.savetxt(file_path, matrix, fmt="%d")
    except Exception as e:
        print(f"Erro ao salvar a matriz: {e}")
        raise

def visualize_matrices(original, noisy_matrices):
    """Visualiza a matriz original e suas versões ruidosas."""
    plt.figure(figsize=(15, 10))

    # Exibe a matriz original
    plt.subplot(2, 3, 1)
    plt.imshow(original, cmap="gray", interpolation="none")
    plt.title("Matriz Original")
    plt.colorbar()

    # Exibe as matrizes ruidosas
    for i, noisy_matrix in enumerate(noisy_matrices):
        plt.subplot(2, 3, i + 2)
        plt.imshow(noisy_matrix, cmap="gray", interpolation="none")
        plt.colorbar()

    plt.tight_layout()
    plt.show()

def generate_noisy_versions(file_path, noise_percentages, output_folder):
    """Gera e salva versões ruidosas de uma matriz."""
    # Carrega a matriz original
    original_matrix = load_pattern(file_path)

    # Cria o diretório de saída, se não existir
    os.makedirs(output_folder, exist_ok=True)

    noisy_matrices = []

    # Gera e salva cada versão ruidosa
    for i, noise in enumerate(noise_percentages):
        noisy_matrix = add_noise(original_matrix, noise)
        noisy_matrices.append(noisy_matrix)

        output_file = os.path.join(output_folder, f"noisy_8_{i + 11}_{noise}.txt")
        save_matrix(noisy_matrix, output_file)

    # Visualiza as matrizes
    #visualize_matrices(original_matrix, noisy_matrices)

# uso
if __name__ == "__main__":
    input_file = "main_part/patterns_bank/n8.txt"  # Arquivo de entrada (15x10)
    output_dir = "noisy_8_10percent"  # Pasta para salvar os números ruidosos
    noise_levels = [30, 30, 30, 30, 30,30,30,30,30,30]  # Porcentagens de ruído

    generate_noisy_versions(input_file, noise_levels, output_dir)