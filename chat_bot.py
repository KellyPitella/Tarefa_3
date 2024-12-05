import os
from datetime import datetime
import random 

def obter_resposta(texto: str,user_info: dict ) -> str:
    comando: str = texto.lower()
    # if comando in ('olá', 'boa tarde', 'bom dia'):
    #     return 'Olá tudo bem!'
    # if comando == 'como estás':
    #     return 'Estou bem, obrigado!'
    # if comando == 'como te chamas':
    #     return 'O meu nome é: Bot :)'
    # if comando == 'tempo':
    #     return 'Está um dia de sol!'
    # if comando in ('bye', 'adeus', 'tchau'):
    #     return 'Gostei de falar contigo! Até breve...'
    # if 'horas' in comando:
    #     return f'São: {datetime.now():%H:%M} horas'
    # if 'data' in comando:
    #     return f'Hoje é dia: {datetime.now():%d-%m-%Y}'

    # return f'Desculpa, não entendi a questão! {texto}'

    respostas = {
        ('olá', 'boa tarde', 'bom dia'): 'Olá tudo bem!',
        'como estás': 'Estou bem, obrigado!',
        'como te chamas': 'O meu nome é: Bot :)',
        'tempo': 'Está um dia de sol!',
        ('que horas são', 'horas'): f'São: {datetime.now():%H:%M} horas',
        ('data' , 'dia'): f'Hoje é dia: {datetime.now():%d-%m-%Y}',
        ('bye', 'adeus', 'tchau'): 'Gostei de falar contigo! Até breve...'
    }
    
    perguntas_engracadas = {
        'Se você fosse um super-herói, qual seria o seu poder?': f'Interessante, acho que eu escolheria o poder de teletransportar!',
        'Qual é o seu animal favorito e por quê?': f'Curioso, eu seria uma andorinha, assim poderia voar e conhecer muitos lugares!',
        'Se você pudesse ter qualquer habilidade, qual escolheria?': f'Boa escolha, concordo com você!',
        'Se você fosse um personagem de desenho animado, quem você seria?':f'Gostei da sua ideia, eu seria a Dory de "Procurando Nemo", sempre esquecendo tudo! O que estavamos fazendo mesmo?',
    }
    
    fatos_curiosos = [
        
        'Sabia que as abelhas podem reconhecer rostos humanos?',
        'Os golfinhos têm nomes uns para os outros!',
        'Você sabia que os polvos têm três corações?',
        'O coração de um camarão está na cabeça!',
        'O maior animal do mundo é a baleia azul, que pode medir até 30 metros!',
        'Você sabia que os flamingos nascem brancos e ficam cor-de-rosa devido à sua alimentação?',
        'O mel nunca estraga! Encontraram mel em tumbas egípcias com mais de 3000 anos e ele ainda estava comestível!',
    ]
    
    piadas = [
    'Por que o computador foi ao médico? Porque ele estava com um vírus!',
    'O que o pato disse para a pata? Vem Quá!',
    'Por que o tomate foi ao tribunal? Porque ele quis apelar!',
    'Por que o estudante levou uma escada para a escola? Porque ele queria chegar ao ensino superior!',
    'Qual é o café mais perigoso do mundo? O ex-presso!',
    'Por que a matemática é péssima em festas? Porque ela sempre fica procurando por uma solução!',
    ]
    
    if comando == 'pergunta engraçada':
        pergunta = random.choice(list(perguntas_engracadas.keys()))
        user_info['ultima_pergunta'] = pergunta
        return pergunta

    elif comando == 'fato curioso':
        return random.choice(fatos_curiosos)
    
    elif comando == 'conte-me uma piada':
        return random.choice(piadas)


    if 'ultima_pergunta' in user_info and user_info['ultima_pergunta'] in perguntas_engracadas:
        resposta_bot = perguntas_engracadas[user_info['ultima_pergunta']]
        user_info.pop('ultima_pergunta')
        return resposta_bot
    

    for chave, resposta in respostas.items():
        if isinstance(chave, tuple):
            if comando in chave:
                return resposta
        elif chave in comando:
            return resposta

    #if 'horas' in comando:
        #return f'São: {datetime.now():%H:%M} horas'

    #if 'data' in comando:
        #return f'Hoje é dia: {datetime.now():%d-%m-%Y}'

    return f'Desculpa, não entendi a questão! {texto}'


def chat() -> None:
    print('Bem-vindo ao ChatBot! \nVamos nos conhecer melhor!')
    print('Escreva "bye" para sair do chat')
    name: str = input('Bot: Como te chamas? ')
    
    user_info = {'nome': name}
    
    hobby = input('Bot: Quais são seus hobbies? ')
    user_info['hobby'] = hobby
    print(f'Bot: É um hobby muito interessante, {name}! Gostaria de tentar um dia!')

    idade = input('Bot: Quantos anos você tem? ')
    user_info['idade'] = idade
    
    print(f'Obrigado por compartilhar um pouco sobre você comigo =) \nComo te posso te ajudar hoje {name} ?')
    while True:
        user_input: str = input('Tu: ')
        resposta = obter_resposta(user_input, user_info)
        print(f'Bot: {resposta}')

        if resposta == 'Gostei de falar contigo! Até breve...':
            break

    print('Chat acabou')
    print()


def main() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')
    chat()


if __name__ == '__main__':
    main()
