from utils import *
from player import Player

driver = Player('chromedriver.exe')

driver.inicializar()

tabela = driver.get_tabela()

print_tabela(tabela)

#solucionar(tabela)

