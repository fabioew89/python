# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.

# import random

# def duplo(x):
#     return x * 2

# def triplo(x):
#     return x * 3

# def quadroplo(x):
#     return x * 4

# numero_random = random.randint(0,9)

# duplo = duplo(numero_random)


# print(f'Meu numero e { numero_random } e seu duplo e { duplo }')

def criar_operador(operador):
    def operando(numero):
        return operador * numero
    return operando
    ...

duplicar = criar_operador(2)
triplicar = criar_operador(3)
quadruplicar = criar_operador(4)

print(duplicar(10))
print(triplicar(10))
print(quadruplicar(10))
