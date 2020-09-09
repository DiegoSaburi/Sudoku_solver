from utils import *
from player import Player

driver = Player('chromedriver.exe')

driver.inicializar()

celulas = driver.get_celulas_selecionaveis()
coords = driver.get_celula_coords(celulas[0])

print(coords)