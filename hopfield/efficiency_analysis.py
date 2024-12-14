import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from utils_mc import load_patterns, cria_j, load_noisy_pattern
from core_mc import lattice_update, total_energy, j_combinado
from config_mc import x_len, y_len, iterations,noisy_pattern_file,folder_1,folder_8

#código para gerar gráficos e avaliar eficiência

def get_selected_patterns(all_patterns, count):
    """
    Retorna os primeiros `count` padrões da lista de padrões,
    ou todos os padrões disponíveis se count >= len(all_patterns).
    """
    if count >= len(all_patterns):
        print(f"Aviso: Apenas {len(all_patterns)} padrões disponíveis. Usando todos.")
        return [all_patterns]  # Usa todos os padrões disponíveis
    else:
        # Seleciona os primeiros `count` padrões
        return [all_patterns[:count]]  # Retorna uma lista com uma única seleção
    


def calculate_efficiency(lattice, selected_patterns, js, iterations):
    """
    Calcula a eficiência para uma combinação de padrões.
    """
    combined_j = j_combinado(lattice, selected_patterns, js)
    
    # Calcula as energias dos padrões e a menor energia
    pattern_energies = [total_energy(lattice, js[i], x_len, y_len) for i in range(len(selected_patterns))]
    min_energy = min(pattern_energies)  # Menor energia dos padrões salvos

    # Atualiza o lattice e calcula as energias finais
    final_energies = []
    for _ in range(iterations):
        lattice = lattice_update(lattice, combined_j, x_len, y_len, t=None)
        final_energy = total_energy(lattice, combined_j, x_len, y_len)
        final_energies.append(final_energy)

    # Calcula a energia média final e a eficiência (módulo da diferença)
    avg_final_energy = np.mean(final_energies)
    efficiency = abs(avg_final_energy - min_energy)
    return efficiency


def evaluate_single_trial(all_patterns, count, iterations,noisy):
    """
    Avalia a eficiência para um único trial com um dado número de padrões (count).
    """
    selected_combinations = get_selected_patterns(all_patterns, count)
    trial_efficiencies = []

    for combination in selected_combinations:
        js = [cria_j(pattern) for pattern in combination]
        lattice = load_noisy_pattern(noisy)
        efficiency = calculate_efficiency(lattice, combination, js, iterations)
        trial_efficiencies.append(efficiency)

    # Retorna a média das eficiências para todas as combinações
    return np.mean(trial_efficiencies)


def evaluate_efficiency(pattern_counts, noisy, pat, num_trials=5):
    """
    Avalia a eficiência para diferentes quantidades de padrões, executando múltiplos trials.
    """
    all_patterns = load_patterns(pat)  # Carrega todos os padrões
    results = []

    for count in pattern_counts:
        trial_accuracies = [
            evaluate_single_trial(all_patterns, count, iterations, noisy) for _ in range(num_trials)
        ]
        avg_accuracy = np.mean(trial_accuracies)
        results.append(avg_accuracy)

    return results


def plot_results(pattern_counts, results1, results8):
    """Plota os resultados da avaliação para 1 e 8 padrões salvos com o mesmo intervalo no eixo y."""
    plt.figure(figsize=(14, 6))

    # Determinar o intervalo comum para o eixo y
    all_results = results1 + results8
    y_min = min(all_results)
    y_max = max(all_results)
    y_margin = 0.1 * (y_max - y_min)  # Adiciona uma margem de 10%
    y_range = (y_min - y_margin, y_max + y_margin)

    # Gráfico 1 - Resultados para folder_1
    plt.subplot(1, 2, 1)
    plt.plot(pattern_counts, results1, marker='o', label="Eficiência do reconhecimento (1)")
    plt.title("Eficiência para 1 Padrão")
    plt.xlabel("Número de Padrões Salvos")
    plt.ylabel("Eficiência (delta médio de energia)")
    plt.ylim(y_range)  # Define o intervalo no eixo y
    plt.gca().xaxis.set_major_locator(MaxNLocator(integer=True))
    plt.grid()
    plt.legend()

    # Gráfico 2 - Resultados para folder_8
    plt.subplot(1, 2, 2)
    plt.plot(pattern_counts, results8, marker='o', label="Eficiência do reconhecimento (8)")
    plt.title("Eficiência para 8 Padrões")
    plt.xlabel("Número de Padrões Salvos")
    plt.ylabel("Eficiência (delta médio de energia)")
    plt.ylim(y_range)  # Define o mesmo intervalo no eixo y
    plt.gca().xaxis.set_major_locator(MaxNLocator(integer=True))
    plt.grid()
    plt.legend()

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    # Configuração do experimento
    pattern_counts = [1, 2, 3, 4]  # Quantidades de padrões a testar
    num_trials = 10  # Número de execuções para cada quantidade

    # Avaliar eficiência
    results1 = evaluate_efficiency(pattern_counts,noisy_pattern_file, folder_1, num_trials)
    results8 = evaluate_efficiency(pattern_counts,noisy_pattern_file, folder_8, num_trials)

    # Exibir os resultados
    print("Resultados 1:", results1)
    print("Resultados 8:", results8)

    # Plotar os resultados
    plot_results(pattern_counts, results1,results8)
    
    
