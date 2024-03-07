# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

def multiplicador(*args):
    total = 1
    for numero in args:
        total *= numero
    return total

numeros = multiplicador(10,2,3,4,5)
print(numeros)


# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.

import random

def par(numero_inteiro):
    resultado = (numero_inteiro % 2) == 0
    if resultado is True:
        print(f'O numero { numero_inteiro } e par')
    else:
        print(f'O numero { numero_inteiro } e impar')
    # return resultado

numero = random.randint(0,9999)
par(numero)