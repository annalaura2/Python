# Compressão de listas
# Filtro versão 1
numeros = {1, 30, 40, 25, 6, 8, 90, 65}
pares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)

print(f"Pares: {pares} ")

# Filtro de versão 2

numeros2 = [1, 24, 3, 6, 88, 56, 7]
par = [num for num in numeros2 if num % 2 == 0]
print(f"Pares: {par}")
        
