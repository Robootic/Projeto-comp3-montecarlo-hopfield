import numpy as np
import pandas as pd
import os

#Código para analisar semelhança dos números

# Função para calcular a porcentagem de similaridade entre duas matrizes binárias
def calculate_similarity(matrix_a, matrix_b):
    """
    Calcula a fração de similaridade entre duas matrizes binárias.
    """
    if matrix_a.shape != matrix_b.shape:
        raise ValueError("As matrizes precisam ter o mesmo tamanho para comparação.")

    total_elements = matrix_a.size
    matching_elements = np.sum(matrix_a == matrix_b)
    similarity_percentage = (matching_elements / total_elements)

    return similarity_percentage

# Função para gerar uma tabela de similaridade
def generate_similarity_table(matrices):
    """
    Gera uma tabela com a fração de similaridade entre as matrizes fornecidas.
    """
    num_matrices = len(matrices)
    similarity_table = np.zeros((num_matrices, num_matrices))

    for i in range(num_matrices):
        for j in range(num_matrices):
            similarity_table[i, j] = calculate_similarity(matrices[i], matrices[j])

    # Converter para DataFrame para melhor visualização
    similarity_df = pd.DataFrame(similarity_table, 
                                  columns=[f"Matrix {i}" for i in range(num_matrices)],
                                  index=[f"Matrix {i}" for i in range(num_matrices)])
    similarity_df = similarity_df.round(decimals=3)
    return similarity_df


if __name__ == "__main__":
    # Carregar matrizes binárias a partir de arquivos .txt na pasta "patterns_bank"
    folder_path = "hopfield/patterns_bank"
    matrices = []

    for file_name in sorted(os.listdir(folder_path)):
        if file_name.endswith(".txt"):
            file_path = os.path.join(folder_path, file_name)
            matrix = np.loadtxt(file_path, dtype=int)
            matrices.append(matrix)

    # Gerar a tabela de similaridade
    similarity_df = generate_similarity_table(matrices)
    print("Tabela de Similaridade:")
    print(similarity_df)