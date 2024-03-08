# Verificar se um número é primo

numero = int(input("Informe o número: "))

primo = True

if numero > 1:
    for i in range(2, numero):
        if (numero % i) == 0:
            primo = False
            break
else:
    primo = False

if primo: 
    print(numero, "é primo")
else:
    print(numero, "não é primo")