import json

# Caminho do arquivo JSON (altere conforme a estrutura de pastas)
caminho_arquivo =  r"C:\Users\anderson.teles\Desktop\Faturamento Mensal\Sistema-de-Faturamento\assets\docs\faturamento.json"

# Abre o arquivo JSON e carrega os dados
with open(caminho_arquivo, 'r') as arquivo:
    faturamento = json.load(arquivo)

# Filtra os dias com faturamento maior que 0
faturamento_valido = [dia["valor"] for dia in faturamento if dia["valor"] > 0]

# Calcula o menor e maior faturamento
menor_valor = min(faturamento_valido)
maior_valor = max(faturamento_valido)

# Calcula a média mensal
media_mensal = sum(faturamento_valido) / len(faturamento_valido)

# Conta os dias com faturamento acima da média
dias_acima_da_media = sum(1 for valor in faturamento_valido if valor > media_mensal)

# Exibe os resultados
print(f"Menor valor de faturamento: R${menor_valor:.2f}")
print(f"Maior valor de faturamento: R${maior_valor:.2f}")
print(f"Número de dias com faturamento acima da média: {dias_acima_da_media}")
