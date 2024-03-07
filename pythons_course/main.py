"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""

import os

lista = []

while True:
  print('Escolha uma opcao')
  opcao = input('[i]nserir, [l]istar, [a]pagar, [s]air: ')

  if opcao == 'i':
    os.system('clear')
    valor = input('Valor: ')
    lista.append(valor)
    
  elif opcao == 'l':
    os.system('clear')
    if len(lista) == 0:
      print('Nao nada na lista!!')

    for i, valor in enumerate(lista):
      print(i, valor)

  elif opcao == 'a':
    indice_str = input('Informe um indice para apagar: ')

    try:
      indice = int(indice_str)
      del(lista[indice])
      
    except ValueError:
        print('Por favor digite número int.')
    except IndexError:
        print('Índice não existe na lista')
    except Exception:
        print('Erro desconhecido')

  elif opcao == 's':
    break
  
  else:
    print('Por favor, escolha i, a ou l.')