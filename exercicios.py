quantidade = 40
preco = 20

if quantidade > 0 and preco > 0:
    print("valores validos")
else:
    print("valores invalidos")


idade = 25
email = "usuario@email.com"

if not 18 <= 65 :
    print("Idade fora do intervalo permitido")
elif "@" not in email or "." not in email :
    print('Email invalido')
else:
    print("Dados de usuário válidos")


temperatura = int(input("Digite uma temperatura: "))

if temperatura < 18:
    print("Baixa")
elif 18 <= temperatura <= 26:
    print("Normal")
else:
    print("Alta")








