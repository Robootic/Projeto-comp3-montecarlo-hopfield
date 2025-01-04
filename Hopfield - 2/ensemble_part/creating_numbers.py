import os
import matplotlib.patches as patches
import numpy as np
import matplotlib.pyplot as plt

# Função para gerar os dígitos em matrizes 8x8
def generate_8x8(digit):
    # Criar uma matriz de 8x8 preenchida com -1 (vazio)
    matrix = np.full((8, 8), -1, dtype=int)
    
    # Ajuste de cada dígito (baseado na imagem de referência)
    if digit == 0:
        matrix[2:7, 1:3] = 1  # Lado esquerdo
        matrix[2:7, 5:7] = 1  # Lado direito
        matrix[1, 2:6] = 1  # Parte superior
        matrix[7, 2:6] = 1  # Parte inferior
    elif digit == 1:
        matrix[1:6, 4] = 1  # Linha central
        matrix[1, 3:5] = 1  # Parte superior
    elif digit == 2:
        matrix[1, 2:6] = 1  # Parte superior
        matrix[2, 5] = 1    # Curva superior direita
        matrix[3, 3:6] = 1  # Meio
        matrix[4, 2] = 1    # Curva inferior esquerda
        matrix[5, 2:6] = 1  # Parte inferior
    elif digit == 3:
        matrix[1, 2:6] = 1  # Parte superior
        matrix[2:4, 5] = 1  # Linha direita superior
        matrix[3, 3:6] = 1  # Meio
        matrix[4:6, 5] = 1  # Linha direita inferior
        matrix[5, 2:6] = 1  # Parte inferior
    elif digit == 4:
        matrix[1:4, 5] = 1  # Linha direita
        matrix[3, 2:6] = 1  # Meio
        matrix[1:6, 3] = 1  # Coluna central
    elif digit == 5:
        matrix[1, 2:6] = 1  # Parte superior
        matrix[1:3, 2] = 1  # Lado esquerdo superior
        matrix[3, 2:6] = 1  # Meio
        matrix[4:6, 5] = 1  # Lado direito inferior
        matrix[5, 2:6] = 1  # Parte inferior
    elif digit == 6:
        matrix[1, 2:6] = 1  # Parte superior
        matrix[1:6, 2] = 1  # Lado esquerdo
        matrix[3, 2:6] = 1  # Meio
        matrix[4:6, 5] = 1  # Lado direito inferior
        matrix[5, 2:6] = 1  # Parte inferior
    elif digit == 7:
        matrix[1, 2:6] = 1  # Parte superior
        matrix[2:6, 5] = 1  # Lado direito
    elif digit == 8:
        matrix[1, 2:6] = 1  # Parte superior
        matrix[3, 2:6] = 1  # Meio
        matrix[5, 2:6] = 1  # Parte inferior
        matrix[1:6, 2] = 1  # Lado esquerdo
        matrix[1:6, 5] = 1  # Lado direito
    elif digit == 9:
        matrix[1, 2:6] = 1  # Parte superior
        matrix[1:4, 2] = 1  # Lado esquerdo superior
        matrix[1:6, 5] = 1  # Lado direito
        matrix[3, 2:6] = 1  # Meio
        matrix[5, 2:6] = 1  # Parte inferior
    return matrix

# Função para gerar os dígitos em matrizes 15x10
def generate_10x15(digit):
    # Criar uma matriz de 15x10 preenchida com -1 (vazio)
    matrix = np.full((15, 10), -1, dtype=int)
    
    # Desenho de cada número baseado na imagem fornecida
    if digit == 0:
        matrix[[0,14],2:8] = 1
        matrix[[1,13],1:9] = 1
        matrix[2, [0, 1, 2, 7, 8, 9]] = 1
        matrix[12, [0, 1, 2, 7, 8, 9]] = 1
        matrix[3:12, [0,1,8,9]] = 1
    elif digit == 1:
        matrix[13,2:8] = 1
        matrix[14,2:8] = 1
        matrix[0:13, 4:6] = 1
        matrix[1,3] = 1
        matrix[2:4,2:4] = 1
    elif digit == 2:
        matrix[14,0:15] = 1
        matrix[13,0:15] = 1
        matrix[12,1:4] = 1
        matrix[11,2:5] = 1
        matrix[10,3:6] = 1
        matrix[9,4:7] = 1
        matrix[8,5:8] = 1
        matrix[7,6:9] = 1
        matrix[6,7:10] = 1
        matrix[4:6, 8:10] = 1
        matrix[3,[0,1,8,9]] = 1
        matrix[2,[0,1,2,7,8,9]] = 1
        matrix[1,1:9] = 1
        matrix[0,2:8] = 1
    elif digit == 3:
        matrix[8,7:10] = 1
        matrix[9,8:10] = 1
        matrix[10,8:10] = 1
        matrix[11,[0,1,8,9]] = 1
        matrix[12,[0,1,2,7,8,9]] = 1
        matrix[13,1:9] = 1
        matrix[14,2:8] = 1
        matrix[6:8,3:9] = 1
        matrix[5,7:10] = 1
        matrix[4,8:10] = 1
        matrix[3,[0,1,8,9]] = 1
        matrix[2,[0,1,2,7,8,9]] = 1
        matrix[1,1:9] = 1
        matrix[0,2:8] = 1      
    elif digit == 4:
       matrix[0:15,8:10] = 1
       matrix[0:7,0:2] = 1
       matrix[7:9,0:8] = 1
    elif digit == 5:
        matrix[0:2, 0:10] = 1  # Parte superior
        matrix[2:7, 0:2] = 1  # Lado esquerdo superior
        matrix[7:9, 0:10] = 1  # Linha do meio
        matrix[9:13, 8:10] = 1  # Lado direito inferior
        matrix[13:15, 0:10] = 1  # Parte inferior
    elif digit == 6:
        matrix[3,[0,1,8,9]] = 1
        matrix[2,[0,1,2,7,8,9]] = 1
        matrix[1,1:9] = 1
        matrix[0,2:8] = 1
        matrix[9,[0,1,8,9]] = 1
        matrix[10,[0,1,8,9]] = 1  
        matrix[11,[0,1,8,9]] = 1
        matrix[12,[0,1,2,7,8,9]] = 1
        matrix[13,1:9] = 1
        matrix[14,2:8] = 1 #topo e base
        matrix[4:9,0:2] = 1 
        matrix[6:8,2:8] = 1
        matrix[8,7:10] = 1
        matrix[7,8] = 1
    elif digit == 7:
        matrix[0:2, 0:10] = 1  # Parte superior
        matrix[2:4,8:10] = 1
        matrix[4:6,7:9] = 1
        matrix[6:8,6:8] = 1
        matrix[8:15, 5:7] = 1
    elif digit == 8:
        matrix[9,[0,1,8,9]] = 1
        matrix[10,[0,1,8,9]] = 1
        matrix[11,[0,1,8,9]] = 1
        matrix[12,[0,1,2,7,8,9]] = 1
        matrix[13,1:9] = 1
        matrix[14,2:8] = 1
        matrix[8,[0,1,2,7,8,9]] = 1
        matrix[5,[0,1,2,7,8,9]] = 1
        matrix[6:8,1:9] = 1
        matrix[4,[0,1,8,9]] = 1
        matrix[3,[0,1,8,9]] = 1
        matrix[2,[0,1,2,7,8,9]] = 1
        matrix[1,1:9] = 1
        matrix[0,2:8] = 1 
    elif digit == 9:
        matrix[9,8:10] = 1
        matrix[10,8:10] = 1
        matrix[11,[0,1,8,9]] = 1
        matrix[12,[0,1,2,7,8,9]] = 1
        matrix[13,1:9] = 1
        matrix[14,2:8] = 1

        matrix[8,2:10] = 1
        matrix[7,1:10] = 1
        matrix[6,[0,1,2,7,8,9]] = 1
        matrix[5,[0,1,8,9]] = 1
        matrix[4,[0,1,8,9]] = 1
        matrix[3,[0,1,8,9]] = 1
        matrix[2,[0,1,2,7,8,9]] = 1
        matrix[1,1:9] = 1
        matrix[0,2:8] = 1 
    
    return matrix


# Pasta onde os arquivos serão salvos
output_folder = "10x15 - numeros"
os.makedirs(output_folder, exist_ok=True)  # Criar a pasta se ela não existir

# Gerar e salvar os novos dígitos em arquivos .txt e mostrar visualizações
for digit in range(10):
    #adjusted_matrix = generate_8x8(digit)
    adjusted_matrix = generate_10x15(digit)
    file_path = os.path.join(output_folder, f"digit_15x10_{digit}.txt")
    np.savetxt(file_path, adjusted_matrix, fmt='%d')
    
    plt.figure(figsize=(2, 2))
    plt.imshow(adjusted_matrix, cmap='gray_r', interpolation='nearest')
    plt.title(f"Digit {digit} (15x10)")
    plt.axis('off')
    plt.show()
    
    
   
