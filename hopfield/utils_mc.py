import os
import numpy as np

#Códigos que criam as matrizes

def load_patterns(folder_path):
    """Carrega padrões de arquivos .txt em uma pasta."""
    patterns = []
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            filepath = os.path.join(folder_path, filename)
            pattern = np.loadtxt(filepath, dtype=int)
            patterns.append(pattern)
    return patterns

def cria_j(matriz):
    """Cria a matriz J a partir de um padrão."""
    matriz_1d = matriz.reshape(-1)
    return np.outer(matriz_1d, matriz_1d)

def load_noisy_pattern(file_name):
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