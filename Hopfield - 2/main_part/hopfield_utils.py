import os
import numpy as np

#* ARQUIVO COM FUNÇÕES AUXILIARES PARA O CÓDIGO PRINCIPAL DA REDE NEURAL (hopfield_core.py)

#^ Carrega de uma pasta padrões gravados em arquivos .txt e o retorna como uma matriz NumPy
def load_patterns(folder_path):
    patterns = []
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            filepath = os.path.join(folder_path, filename)
            pattern = np.loadtxt(filepath, dtype=int)
            patterns.append(pattern)
    return patterns

#^ Cria a matriz j a partir de um padrão.
def generate_j(matriz):
    matriz_1d = matriz.reshape(-1)
    return np.outer(matriz_1d, matriz_1d)

#^ Carrrega um padrão de um arquivo .txt e o retorna como uma matriz NumPy
def load_pattern(file_name):
    if not os.path.exists(file_name):
        print(f"Erro: O arquivo {file_name} não existe.")
        return None

    try:
        pattern = np.loadtxt(file_name)  # Carrega o arquivo como uma matriz
        return pattern
    except Exception as e:
        print(f"Erro ao carregar o arquivo {file_name}: {e}")
        return None