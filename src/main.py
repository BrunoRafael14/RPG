import os
from tools.utils import definindo_classe, menu, save_game, menu_batalha, menu_mover, load_position, load_game
import time
from tools.create import gerar_inimigo, player_create
from tools.mapa import Mapa

menu()

mapa = Mapa(load_position())
mapa.informar_localizacao()
infos = mapa.mover()
mapa.informar_localizacao()
save_game(infos)