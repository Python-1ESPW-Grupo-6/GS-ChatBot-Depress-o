import random

ultima_pergunta = [1]

def chatbot(resposta):
    respostas_prontas = {
        "oi": ["Olá, sou o ChatBot!"],
        "como você está?": ["Estou bem, obrigado!", "Ótimo!", "Mais ou menos."],
        "qual é o seu nome?": ["Meu nome é ChatBot.", "Pode me chamar de ChatBot."],
        "o que você faz?": ["Eu sou um chatbot simples, programado em Python, para te ajudar!", "Minha função é te ajudar!"],
        "não estou bem!": ["Tente relaxar, leia um livro ou escute uma musica relaxante!", "Tente assistir um programa de tv animador!", 
                           "Ligue para alguma pessoa próxima, um amigo ou algum parente!"]
    }

    # Verifica se a pergunta está nas respostas prontas
    if resposta.lower() == "gostaria de outra dica." and "não estou bem!" in ultima_pergunta:
        return random.choice(respostas_prontas["não estou bem!"])
    elif resposta.lower() in respostas_prontas:
        return random.choice(respostas_prontas[resposta.lower()])
    else:
        return "Desculpe, não entendi sua pergunta."
    
def pergunta(resposta):
    del ultima_pergunta[0]
    ultima_pergunta.append(resposta)
    

# Exemplo de uso
while True:
    pergunta_usuario = input("Você: ")
    print('')

    if pergunta_usuario.lower() == 'sair':
        print("Até mais!")
        break

    resposta_chatbot = chatbot(pergunta_usuario)
    pergunta(pergunta_usuario)
    print("ChatBot:", resposta_chatbot)
    print('')