def calcular_fibonacci(num):
    """Calcula a sequência de Fibonacci até o número fornecido."""
    sequencia = [0, 1]
    while sequencia[-1] < num:
        sequencia.append(sequencia[-1] + sequencia[-2])
    return sequencia

def verificar_fibonacci(num):
    """Verifica se um número pertence à sequência de Fibonacci."""
    sequencia = calcular_fibonacci(num)
    if num in sequencia:
        return True, sequencia
    return False, sequencia

numero = int(input("Digite um número para verificar: "))

pertence, sequencia_gerada = verificar_fibonacci(numero)

# Exibi o resultado

print("Sequência de Fibonacci gerada:", sequencia_gerada)
if pertence:
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} NÃO pertence à sequência de Fibonacci.")
