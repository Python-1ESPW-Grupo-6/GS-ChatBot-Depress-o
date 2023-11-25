import random
from datetime import datetime
import os

ultima_pergunta = [1]

timestamp = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
nova_atualização = f'Não se sentiu bem: {timestamp}\n'
nome_arquivo = 'relatório.txt'

def erro():
    print('-'*30)
    print('Opção não encontrada, tente novamente!')
    print('-'*30)

def chatbot(resposta):
    respostas_prontas = {
        "oi": ["Olá, sou o ChatBot!"],
        "como você está?": ["Estou bem, obrigado!", "Ótimo!", "Mais ou menos."],
        "qual é o seu nome?": ["Meu nome é SereniBOT.", "Pode me chamar de SereniBOT."],
        "o que você faz?": ["Eu sou um chatbot simples, programado em Python, para te ajudar!", "Minha função é te ajudar!"],
        "não estou bem!": ["Tente relaxar, leia um livro ou escute uma musica relaxante!", "Tente assistir um programa de tv animador!", 
                           "Ligue para alguma pessoa próxima, um amigo ou algum parente!"]
    }

    if resposta.lower() == "não estou bem!":
        if os.path.exists(nome_arquivo):
            with open(nome_arquivo, 'a') as arquivo:
                arquivo.write(nova_atualização)
        else:
            with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
                arquivo.write(nova_atualização)


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
    
while True:
    try:
        menu = int(input('''Bem vindo ao SereniBOT?
    [1] Iniciar Chat
    [2] Ver relatório
    [3] Sair do programa\nSeleciona a opção desejada: '''))
        print('')
        
        match menu:

            case 1:
                while True:
                    pergunta_usuario = input("Você: ")
                    print('')

                    if pergunta_usuario.lower() == 'voltar para o menu.':
                        print("Até mais!")
                        print('')
                        break

                    resposta_chatbot = chatbot(pergunta_usuario)
                    pergunta(pergunta_usuario)
                    print("ChatBot:", resposta_chatbot)
                    print('')
            
            case 2:
                if os.path.exists(nome_arquivo):
                    with open(nome_arquivo, 'r') as arquivo:
                        for linha in arquivo:
                            print(linha)
                else:
                    print('Não há dados ainda!')
                    print('')

            case 3:
                print('Finalizando Programa...')
                break

            case _:
                erro()

    except ValueError:
        erro()