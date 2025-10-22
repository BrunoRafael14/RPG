class Mapa():
    def __init__(self, localizacao:str):
        self.__localizacao = localizacao

    def informar_localizacao(self):
        print(f"Você está atualmente em: {self.__localizacao}")

    def mover(self, nova_localizacao:str):
        self.__localizacao = nova_localizacao
        print(f"Você se moveu para: {self.__localizacao}")


