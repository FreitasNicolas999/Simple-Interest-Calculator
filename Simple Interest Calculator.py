def calcular_juros_simples(capital_inicial, taxa_juros, tempo):
    valor_futuro = capital_inicial * (1 + (taxa_juros / 100) * tempo)
    return valor_futuro

# Leitura dos dados
capital_inicial = float(input("Digite o capital inicial: R$ "))
taxa_juros = float(input("Digite a taxa de juros (em %): "))
tempo = float(input("Digite o tempo (em anos): "))

valor_futuro = calcular_juros_simples(capital_inicial, taxa_juros, tempo)
print(f"O valor futuro da aplicação é: R$ {valor_futuro:.2f}")