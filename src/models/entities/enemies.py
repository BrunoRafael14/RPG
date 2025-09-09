class Enemies():
    def __init__(self, especie, hp_max, level, dano):
        self.especie = especie
        self.hp = hp_max
        self.level = level
        self.hp_max = hp_max + ((level * 15) - 15)
        self.dano = dano * level