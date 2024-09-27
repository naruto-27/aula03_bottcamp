def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)

# Testando a função
print(fatorial(5))  # Saída: 120
print(fatorial(0))  # Saída: 1


