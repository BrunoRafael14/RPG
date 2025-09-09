import json
import os
import time
from models.entities.player import Player


#Função para definir a classe do personagem
classes = {1:"Guerreiro", 2:"Mago", 3:"Arqueiro"}

def definindo_classe(number_class):
    class_player = classes[number_class]
    if class_player not in classes[number_class]:
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
            return player
        else:
            os.system('cls' if os.name == 'nt' else 'clear')


#Funções para salvar e carregar infos do game
def save_game(player):
    player_infos = {"save01":{
        "nome": player.nome,
        "level": player.level,
        "classe": player.classe,
        "hp": player.hp,
        "hp_max": player.hp_max,
        "dano": player.dano
    }} 
    with open("data/savegame.json", "w", encoding="utf-8") as save:
        json.dump(player_infos, save, ensure_ascii=False, indent=4)

def load_game() -> dict:
    with open("data/savegame.json", "r", encoding="utf-8") as load:
        load = json.load(load)
        return load



#Função do Menu inicial do jogo
def menu():
    print("1- Novo Jogo \n2- Continuar\n3- Sair\n")
    menu_opcao = int(input(""))
    os.system('cls' if os.name == 'nt' else 'clear')


    if menu_opcao == 1:
        player = player_create()
        save_game(player)
        print("Ótimo! Vamos começar a aventura! \nCaregando...")
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        print("A aventura começou!")

    elif menu_opcao == 2:
        load = load_game()
        print("Carregando jogo...")
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"Bem vindo de volta {load["save01"]["nome"]}")
        pass
    else:
        exit()


# Menu de Batalha
def menu_batalha():
    while True:
        respostas = [1, 2, 3]
        print("1- Atacar \n2- Itens \n3- Trocar Arma")
        resposta = int(input())
        if resposta in respostas:
            break
        else:
            print("Ação Inválida")
            time.sleep(1)


