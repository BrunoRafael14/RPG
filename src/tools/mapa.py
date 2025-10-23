class Mapa():
    def __init__(self, localizacao:str):
        self.__localizacao = localizacao

    def informar_localizacao(self):
        print(f"Você está atualmente em: {self.__localizacao}")

    def mover(self):
        from tools.utils import menu_mover
        import json
        import os
        resposta = "s"

        with open('data/savegame.json', 'r', encoding='utf-8') as file:
            save_data = json.load(file)
            x = save_data["save01"]["localização"]["X"]
            y = save_data["save01"]["localização"]["Y"]

        while True: 
            X, Y = menu_mover()

            x += X
            y += Y
            save_data["save01"]["localização"]["X"] = x
            save_data["save01"]["localização"]["Y"] = y

            self.__localizacao = {"X": x, "Y": y}
            print(f"Você se moveu para: {self.__localizacao}")
            return save_data


