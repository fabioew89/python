perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '1', '1', '1', '3', '4', '5'],
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

for ask in perguntas:
    print(f'Pergunta:',ask['Pergunta'],)
    
    for i, option in enumerate(ask['Opções']):
        print(f'{i}) ->', option)

    answer = input('Escolha uma opcao: ')
    answer_int = None
    options_count = len(ask['Opções'])

    if answer.isdigit():
        answer_int = int(answer)

    if answer_int is not None:
        if answer_int >= 0 and answer_int < options_count:
            if option[answer_int] == int(ask['Resposta']):
                print(options_count, type(options_count))
