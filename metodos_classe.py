# append - adicionar valores
print("\nAppend")
lista = []
print(lista)
lista.append("laura")
print(lista)
lista.append([40,50, 60])
print(f"\nadicionei: {lista}")

# clear - limpar lista
print("\nClear:")
lista.clear()
print(f"lista atualizada: {lista}")

# copy - copiar lista 
print("\nCopy:")
lista = [1, 2, 3]
l2 = lista.copy
print(lista)
print(l2)