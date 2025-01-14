texto = input("Digite a string que deseja inverter: ")

# Inverte a string
string_invertida = ""
for char in texto:
    string_invertida = char + string_invertida

# Exibi o resultado
print(f"String original: {texto}")
print(f"String invertida: {string_invertida}")
