# Números pares e ímpares de uma lista 
inicio = int(input("Informe o ínico do intervalo: "))
fim = int(input("Informe o final do intervalo: "))

pares = 0
impares = 0

for num in range(inicio, fim + 1):
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1

print("Pares: ", pares)
print("Ímpares: ", impares)