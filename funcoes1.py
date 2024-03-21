#def exibir_msg(nome):
  #  print(f"olá, {nome}")

salario = 200
def salario_bonus(bonus):
    global salario
    salario += bonus
    return salario


#nome = "Anna Laura"
#exibir_msg(nome)
    

salario_com_b = salario_bonus(500)
print(salario_com_b)