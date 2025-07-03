import os
from datetime import datetime

# 6.1º 
# if len(sys.argv) < 2:
#     print("É necessário escrever uma mensagem para o chatbot")
#     exit()
# message = sys.argv[1]
# if "Olá" in message or "olá" in message:
#     print("Olá! Como posso ajudar?")
# elif "Adeus" in message or "adeus" in message:
#     print("Adeus! Até à próxima.")
# else:
#     print("Desculpa, não entendi.")

# 6.2
def obter_resposta(texto: str) -> str:
    comando = texto.lower()

    # Interações originais
    if comando in ('olá', 'boa tarde', 'bom dia'):
        return 'Olá tudo bem!'
    if comando == 'como estás':
        return 'Estou bem, obrigado!'
    if comando == 'como te chamas?':
        return 'O meu nome é Bot :)'
    if comando == 'tempo':
        return 'Está um dia de sol!'
    if comando in ('bye', 'adeus', 'tchau'):
        return 'Gostei de falar contigo! Até breve...'
    if 'horas' in comando:
        return f'São: {datetime.now():%H:%M} horas'
    if 'data' in comando:
        return f'Hoje é dia: {datetime.now():%d-%m-%Y}'

    # 6.2º - Novas interações 
    if 'obrigado' in comando or 'obrigada' in comando:
        return 'De nada! Sempre às ordens.'
    if 'onde estás' in comando:
        return 'Estou aqui no teu terminal!'
    if 'o que sabes fazer' in comando:
        return 'Sei responder a perguntas simples e conversar contigo!'
    if 'piada' in comando:
        return 'Porque é que o computador foi ao médico? Porque tinha um vírus!'
    if 'gostas de mim' in comando:
        return 'Claro que gosto! És muito simpático.'
    if 'qual é a capital de portugal' in comando:
        return 'A capital de Portugal é Lisboa.'
    if 'qual o teu filme favorito' in comando:
        return 'Gosto muito de Wall-E!'
    if 'qual é o sentido da vida' in comando:
        return '42. ;)'
    if 'tens sentimentos' in comando:
        return 'Ainda não... mas estou a aprender!'
    if 'programar' in comando:
        return 'Programar é transformar ideias em código. Muito fixe!'

    return f'Desculpa, não entendi a questão: {texto}'


def chat() -> None:
    print('Bem-vindo ao ChatBot!')
    print('Escreva "bye" para sair do chat.')
    nome = input('Bot: Como te chamas? ')
    print(f'Bot: Olá, {nome}! Como te posso ajudar?')

    while True:
        user_input = input('Tu: ')
        resposta = obter_resposta(user_input)
        print(f'Bot: {resposta}')
        if resposta == 'Gostei de falar contigo! Até breve...':
            break

    print('Chat acabou. Obrigado pela conversa!')


def main() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')
    chat()


if __name__ == '__main__':
    main()
