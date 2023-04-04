from utils import *
from player import Player
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = Player('chromedriver.exe', chrome_options=chrome_options)

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