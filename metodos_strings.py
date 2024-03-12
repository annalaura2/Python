
curso = "pYTHOn"

# maiúscula 
print(curso.upper())
# minúscula 
print(curso.lower())
# título 
print(curso.title())

# eliminando espaços em branco 

nome = "     anna     "

#strip - remove todos os espaços em branco 
print(nome.strip())

#lstrip - remove os espaços em branco da esquerda 
print(nome.lstrip())

#rstrip - remove os espaços em branco da direita
print(nome.rstrip())

# junções e centralização 

variavel = "peixe"
#centralização - nela você passa dois argumentos, o primeiro é o número de caracteres
# que você deseja ocupar
# o segundo é opcional e representa o caractere que você deseja que ocupe o espaço 
# se nenhum for informado, fica vazio
print(variavel.center(10, "#")) 

# junção
print(".".join(variavel))

