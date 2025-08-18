import json

def definindo_classe(class_player):
    if class_player == 1:
        class_player = "Guerreiro"
    elif class_player == 2:
        class_player = "Mago"
    elif class_player == 3:
        class_player = "Arqueiro"
    else:
        return "Classe desconhecida"

    with open('data/classes.json', 'r') as busca_class:
        busca_class = json.load(busca_class)
        class_player_info = busca_class[class_player]
    return class_player, class_player_info

