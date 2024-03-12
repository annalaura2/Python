frutas = ["laranja", "maca", "banana"]
cores = []
letras = list("python")
numeros = list(range(10))
carro = ["onix", "true", 32400]

print(frutas)
print(cores)
print(letras)
print(numeros)
print(carro)

# acesso direto 
print("\nAcesso direto")
print(frutas[0])
print(frutas[0:2])

# índice negativo 

print("\nÍndice negativo")
print(frutas[-1])
print(frutas[-3])

# Fatiamento 

print("\nFatiamento")
print(frutas[0:2])
print(frutas[::])
print(frutas[::-1])
print(frutas[0:2])

# Iterando 

print("\nIteração")
for fruta in frutas: 
    print(fruta)

# FUnção enumerate 
print("\nFunção enumerate")
for indice, fruta in enumerate(frutas):
    print(f"{indice} : {fruta}")
