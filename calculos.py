def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)

# Testando a função
print(fatorial(5))  # Saída: 120
print(fatorial(0))  # Saída: 1




def ordenar_lista(lista):
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] > lista[j]:
                lista[i], lista[j] = lista[j], lista[i]
    return lista

# Testando a função
print(ordenar_lista([34, 2, 25, 6, 12]))  # Saída: [2, 6, 12, 25, 34]
print(ordenar_lista([5, 3, 8, 1, 2]))    # Saída: [1, 2, 3, 5, 8]
