from utils import *
from player import Player

driver = Player('chromedriver.exe')

driver.inicializar()

tabela = driver.get_tabela()

print_tabela(tabela)
print("Solucionando tabela....")
solucionar(tabela)
print("Sudoku solucionado! Solução encontrada:")
print_tabela(tabela)

celulas_selecionaveis = driver.get_celulas_selecionaveis()

for celula in celulas_selecionaveis:
    linha,coluna = driver.get_celula_coords(celula)
    driver.send_solucao(celula,tabela[linha][coluna])

