perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

qtd_acertos = 0

for ask in perguntas:
    print('Pergunta: ',ask['Pergunta'])

    opcoes = ask['Opções']
    for i, opcao in enumerate(opcoes):
        print(f'{i})', opcao)

    escolha = input('Escolha uma opcao: ')
    escolha_int = None
    acertou = None
    qtd_opcoes = len(opcoes)

    if escolha.isdigit():
        escolha_int = int(escolha)

    if escolha_int is not None:
        if escolha_int >= 0 and escolha_int < qtd_opcoes:
            if opcoes[escolha_int] == ask['Resposta']:
                acertou = True
    
    if acertou:
        qtd_acertos += 1
        print('acertou 🤌')
    else:
        print('Errou!!! 🚫')
print('Voce acertou', qtd_acertos)
print('de', len(qtd_acertos),'perguntas')
