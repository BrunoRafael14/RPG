import random
import os
from models.entities.enemies import Enemies
from models.entities.player import Player



def gerar_inimigo():
    especies = ["Goblin", "Esqueleto Possuido", "Urso Raivoso", "Dragão"]
    especie = random.choice(especies)
    enemie = Enemies(especie, 100, random.randint(1, 10), 20)
    print(f"Apareceu um {enemie.especie} de nível {enemie.level} com {enemie.hp_max} de HP e {enemie.dano} de dano!")


#Função para criar o personagem
def player_create():
    from tools.utils import definindo_classe

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