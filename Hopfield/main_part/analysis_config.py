
#* ARQUIVO COM AS CONFIGURAÇÕES E CAMINHOS DE PASTAS PARA O CÓDIGO PRINCIPAL DE ANÁLISE (analysis_core.py)

#^ Caminho para pastas dos grupos do 1 e do 8
folder_8 = "main_part/patterns_8_mindif"
folder_1 = "main_part/patterns_1_maxdif"

#^ Caminho para pastas com ruídos do número 1
folder_110 = "main_part/noisy_1_10percent"
folder_120 = "main_part/noisy_1_20percent"
folder_130 = "main_part/noisy_1_30percent"

#^ Caminho para pastas com ruídos do número 8
folder_810 = "main_part/noisy_8_10percent"
folder_820 = "main_part/noisy_8_20percent"
folder_830 = "main_part/noisy_8_30percent"

#^ Caminho para os arquivos originais dos números 8 e 1
default_8 = "main_part/patterns_bank/n8.txt"
default_1 = "main_part/patterns_bank/n1.txt"

#^ Configuração do experimento
pattern_counts = 6  # Quantidades de padrões a testar
num_trials = 20  # Número de execuções para cada quantidade
configs_g1 = [num_trials,folder_1, pattern_counts]
configs_g8 = [num_trials,folder_8,pattern_counts]