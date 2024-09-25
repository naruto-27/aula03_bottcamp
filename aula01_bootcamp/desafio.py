nome_usuario = input("Digite seu nome: ")
salario_usuario = float(input("Digite seu salário: "))
bonus_usuario = float(input("Digite seu bonus: "))

valor_do_bonus = 1000 + salario_usuario * bonus_usuario

print(f"O usuario {nome_usuario} possui o bonos de {valor_do_bonus}")

