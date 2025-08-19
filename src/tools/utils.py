import json
import os
import time
from models.entities.player import Player

#Função do Menu inicial do jogo
def menu():
    print("1- Novo Jogo \n2- Continuar\n3- Sair\n")
    menu = int(input(""))
    os.system('cls' if os.name == 'nt' else 'clear')
    if menu == 1:
        player_create()
        print("Ótimo! Vamos começar a aventura! \nCaregando...")
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
    elif menu == 2:
        print("Carregando jogo...")
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        pass
    else:
        exit()
    return menu

#Função para definir a classe do personagem
classes = {1:"Guerreiro", 2:"Mago", 3:"Arqueiro"}

def definindo_classe(class_player):
    class_player = classes[class_player]
    if class_player not in classes:
        print("Classe desconhecida")

    with open('data/classes.json', 'r') as busca_class:
        busca_class = json.load(busca_class)
        class_player_info = busca_class[class_player]
    return class_player, class_player_info

#Função para criar o personagem
def player_create():
    while True:
        print("Olá jogador! Bem-vindo ao The Game. \nVamos começar montando seu personagem.")
        nome_player = input("Nome do personagem: ")
        os.system('cls' if os.name == 'nt' else 'clear')
        class_player = int(input("Classe do personagem: \n1-Guerreiro\n2-Mago\n3-Arqueiro\n "))
        os.system('cls' if os.name == 'nt' else 'clear')
        class_player, class_player_info = definindo_classe(class_player)

        player = Player(nome_player, 1, class_player, class_player_info['hp_max'], class_player_info['dano'])

        print(f"{player.nome}, {player.classe} de nível {player.level}, com {player.hp_max} de HP e {player.dano} de dano.")
        resposta = input("Continuar ? (s/n): ").lower()
        if resposta == "s" or resposta == "sim":
            os.system('cls' if os.name == 'nt' else 'clear')
            break
        else:
            os.system('cls' if os.name == 'nt' else 'clear')


