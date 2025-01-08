import os
import numpy as np
import matplotlib.pyplot as plt

from hopfield_utils import load_pattern
from hopfield_core import total_energy
from analysis_config import default_8, default_1

#* ARQUIVO COM FUNÇÕES AUXILIARES PARA O CÓDIGO PRINCIPAL DE ANÁLISE (analysis_core.py)

#^ Seleciona apenas a quantidade n de padrões de um conjunto maior 
def get_selected_patterns(all_patterns, count):
    if count > len(all_patterns):
        print(f"Aviso: Apenas {len(all_patterns)} padrões disponíveis. Usando todos.")
        return all_patterns
    else:
        return all_patterns[:count]

#^ Pega o padrão original do .txt e calcula a energia total dele na matriz de interações J  
def get_default_energy(j_combinated, group):
    og = load_pattern(default_1) if group == 1 else load_pattern(default_8)
    return total_energy(og, j_combinated)

#^ Função para verificar se um arquivo já existe e gerar um novo nome, se necessário
def save_unique_plot(filename):
    base, ext = os.path.splitext(filename)
    counter = 1
    new_filename = filename
    # Verificar se o arquivo já existe
    while os.path.exists(new_filename):
        new_filename = f"{base}_{counter}{ext}"
        counter += 1
    # Salvar a figura com o nome único
    plt.savefig(new_filename)
    print(f"Figura salva como: {new_filename}")

#^ Plota gráfico de energia mínima atingida, ao fim de 10 iterações, em relação a qtde n de padrões salvos 
def plot_energy_achieved(energy_averages, energy_stdev, og_energy, group, noise):
    plt.figure(figsize=(10, 6))
    #Energia mínima atingida média e seu desvio padrão
    x = np.arange(1, len(energy_averages) + 1)
    plt.errorbar(x, energy_averages, yerr=energy_stdev, fmt='-o', color='blue', capsize=5, label='Energia Mínima Atingida')
    #Energia do padrão original
    plt.plot(x, og_energy, '-s', label='Energia do Padrão Original', color='magenta')
    plt.xticks(np.arange(1, len(energy_averages) + 1, 1))
    lim_inf = np.min(energy_averages)
    plt.ylim(lim_inf -500, lim_inf + 3500)
    plt.xlabel('Número de Padrões Salvos')
    plt.ylabel('Energia Mínima Atingida')
    plt.title('Número mestre: ' + group + "     Reconhecimento com " + noise + " de ruído")
    plt.grid(True)
    plt.legend()
    # Salvar a imagem automaticamente
    plt.savefig(f'grupo{group}_{noise}.png')
    plt.close()
    plt.show()

#^ Plota gráfico da energia do sistema convergindo no decorrer das iterações
def plot_convergence(group, iteration_energy_average, iteration_energy_var, default_energy, default_energy_var, iterations, n):
    plt.figure(figsize=(10, 6))
    x = np.arange(1, iterations + 1)
    # Energia média do sistema
    plt.plot(x, iteration_energy_average, label='Energia Média do Sistema', color='blue')
    # Variância da energia do sistema
    plt.fill_between(
        x, 
        iteration_energy_average - np.sqrt(iteration_energy_var), 
        iteration_energy_average + np.sqrt(iteration_energy_var), 
        color='blue', alpha=0.2
    )
    # Energia do padrão original (base)
    plt.axhline(y=default_energy, color='magenta', linestyle='--', label='Energia do Padrão Original')
    # Variância da energia do padrão original
    plt.fill_between(
        x, 
        default_energy - np.sqrt(default_energy_var), 
        default_energy + np.sqrt(default_energy_var), 
        color='magenta', alpha=0.2
    )
    plt.xticks(ticks=np.arange(1, iterations + 1, 1), labels=np.arange(1, iterations + 1, 1))
    lim_inf = np.min(iteration_energy_average)
    plt.ylim(lim_inf -1000, lim_inf + 3500)
    plt.xlabel('Iterações')
    plt.ylabel('Energia')
    plt.title(f'Convergência da Energia em n = {n}')
    plt.legend()
    plt.grid(True)
    # Salvar a imagem automaticamente
    save_unique_plot(f'grupo{group}_n{n}.png')
    plt.close()
    plt.show()