import os
from models.entities.player import Player
from tools.funcionalidades_codigo import definindo_classe
import time

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

print("Ótimo! Vamos começar a aventura! \nCaregando...")
time.sleep(2)
os.system('cls' if os.name == 'nt' else 'clear')

print("A aventura começou!")