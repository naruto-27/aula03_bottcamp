# Exemplo de código com múltiplos try/except dentro de um loop while
max_tentativas = 5  # Definindo um limite para evitar loop infinito
tentativa_atual = 0

while tentativa_atual < max_tentativas:
    try:
        # Bloco 1 - Tentando abrir um arquivo
        try:
            arquivo = open("dados.txt", "r")
            conteudo = arquivo.read()
            print("Arquivo lido com sucesso!")
        except FileNotFoundError:
            print("Erro: Arquivo não encontrado. Verifique o nome e caminho do arquivo.")
            break

        # Bloco 2 - Tentando converter um valor de string para inteiro
        try:
            valor = int(conteudo.strip())  # Remove espaços e converte para inteiro
            print(f"Valor lido do arquivo: {valor}")
        except ValueError:
            print("Erro: Não foi possível converter o conteúdo do arquivo para um número inteiro.")
            break

        # Bloco 3 - Tentando dividir por um valor lido do arquivo
        try:
            resultado = 100 / valor  # Cálculo arbitrário
            print(f"Resultado da divisão: {resultado}")
        except ZeroDivisionError:
            print("Erro: Divisão por zero não é permitida.")
            break

    except Exception as e:
        print(f"Erro inesperado: {e}")
        break

    finally:
        # Garantindo que o arquivo seja fechado, caso tenha sido aberto
        try:
            arquivo.close()
        except NameError:
            pass

    # Incrementa a tentativa atual
    tentativa_atual += 1

    # Condicional para encerrar o loop
    if tentativa_atual >= max_tentativas:
        print("Número máximo de tentativas atingido. Encerrando o loop.")
        break

print("Processo finalizado com sucesso.")
