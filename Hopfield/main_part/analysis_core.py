import numpy as np

from hopfield_utils import load_patterns, generate_j
from hopfield_core import lattice_update, total_energy, j_combiner
from hopfield_config import x_len, y_len, iterations
from analysis_utils import get_default_energy, get_selected_patterns,plot_convergence,plot_energy_achieved
from analysis_config import folder_810, folder_820, folder_830, folder_110, folder_120, folder_130, configs_g1, configs_g8

#* ARQUIVO PRINCIPAL DE ANÁLISE DO COMPORTAMENTO DA REDE NEURAL DO TIPO HOPFIELD

#^ Repete "times" vezes a rodada de convergência para cada combinação de grupo e ruído
def repeat_convergence(times, noisy_patterns, selected_patterns, js, group):
    min_energies = []
    iteration_energies = np.zeros((times, iterations))
    default_energies_sum = 0
    default_energies_list = []  # Lista para armazenar as energias do padrão original
    
    for r in range(times):
        print(f'Round {r + 1}')
        lattice = noisy_patterns[r % len(noisy_patterns)]
        j_combinated = j_combiner(lattice, selected_patterns, js)
        default_energy = get_default_energy(j_combinated, group)
        default_energies_sum += default_energy
        default_energies_list.append(default_energy)  
        # Rodada de convergência
        for iteration in range(iterations):
            lattice = lattice_update(lattice, j_combinated, x_len, y_len, t=None)
            iteration_energies[r, iteration] = total_energy(lattice, j_combinated)
        min_energies.append(iteration_energies[r, -1])
        
    # Cálculo da média e variância da energia original
    default_energy_avg = default_energies_sum / times
    default_energy_var = np.var(default_energies_list)
    # Cálculo da média e variância da energia original
    iteration_energy_avg = np.mean(iteration_energies, axis=0)
    iteration_energy_var = np.var(iteration_energies, axis=0)

    return min_energies, iteration_energy_avg, iteration_energy_var, default_energy_avg, default_energy_var

#^ Função que faz a rede neural funcionar e retorna dados de energia para cada quantidade n de padrões armazenados
def analyze(group, configs, noisy_versions):
    max_patterns = configs[0]
    group_patterns = configs[1]
    times = configs[2]
    energy_averages = []
    energy_stdev = []
    og_energy = []
    og_energy_var = []
    # Repete tudo para n variando de 1 (só o padrão mestre salvo) a 6 (todos os padrões do grupo salvos)
    for num_patterns in range(1, max_patterns + 1):
        noisy_patterns = load_patterns(noisy_versions)
        all_patterns = load_patterns(group_patterns)
        selected_patterns = get_selected_patterns(all_patterns, num_patterns)
        js = [generate_j(pattern) for pattern in selected_patterns]
        
        (
            min_energies, 
            iteration_energy_avg, 
            iteration_energy_var, 
            default_energy_avg,
            default_energy_var
        ) = repeat_convergence(times, noisy_patterns, selected_patterns, js, group)

        # Cálculo da média e desvio padrão da energia atingida e a energia original
        energy_averages.append(np.mean(min_energies))
        energy_stdev.append(np.std(min_energies))
        og_energy.append(default_energy_avg)
        og_energy_var.append(default_energy_var)
        
        # Plotar a convergência com variância da energia base
        plot_convergence(group, iteration_energy_avg, iteration_energy_var, default_energy_avg, default_energy_var, iterations, num_patterns)
    
    return energy_averages, energy_stdev, og_energy


if __name__ == "__main__":

#^ Analisar desempenho do grupo 8
    #? -> 10% de ruído
    avg_energy810, stdev_energy810, e810 = analyze(8, configs_g8, folder_810)
    plot_energy_achieved(avg_energy810, stdev_energy810, e810, "8", "10%")
    #? -> 20% de ruído
    avg_energy820, stdev_energy820, e820 = analyze(8, configs_g8, folder_820)
    plot_energy_achieved(avg_energy820, stdev_energy820, e820, "8", "20%")
    #? -> 30% de ruído
    avg_energy830, stdev_energy830, e830 = analyze(8, configs_g8, folder_830)
    plot_energy_achieved(avg_energy830, stdev_energy830, e830, "8", "30%")

#^ Analisar desempenho do grupo 1
    #? -> 10% de ruído
    avg_energy110, stdev_energy110, e110 = analyze(1, configs_g1, folder_110)
    plot_energy_achieved(avg_energy110, stdev_energy110, e110, "1", "10%")
    #? -> 20% de ruído
    avg_energy120, stdev_energy120, e120 = analyze(1, configs_g1, folder_120)
    plot_energy_achieved(avg_energy120, stdev_energy120, e120, "1", "20%")
    #? -> 30% de ruído
    avg_energy130, stdev_energy130, e130 = analyze(1, configs_g1, folder_130)
    plot_energy_achieved(avg_energy130, stdev_energy130, e130, "1", "30%")
