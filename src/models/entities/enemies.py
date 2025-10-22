class Enemies():
    def __init__(self, especie:str, hp_max:int, level:int, dano:int):
        self.especie = especie
        self.hp = hp_max
        self.level = level
        self.hp_max = hp_max + ((level * 15) - 15)
        self.dano = dano * level