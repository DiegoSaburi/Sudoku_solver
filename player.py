from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from globals import *
import time

class Player (Chrome):

    def __init__(self, executable_path, port=0, options=None, service_args=None, desired_capabilities=None, service_log_path=None, chrome_options=None, keep_alive=True):
        super().__init__(executable_path=executable_path, port=port, options=options, service_args=service_args, desired_capabilities=desired_capabilities, service_log_path=service_log_path, chrome_options=chrome_options, keep_alive=keep_alive)

    def inicializar(self):
        '''
        carrega o site
        '''
        self.get(Globals.SITE_LINK)
        self.maximize_window()
        self.scroll_para_novo_jogo()
        time.sleep(0.5)
    
    def get_tabela(self):
        '''
        Vai pegar a tabela do site e colocar em uma lista de listas

        retorna tabela
        '''
        linha = []
        tabela = []
        for i in range(0,81):
            celula = self.find_element(By.ID, f'c{i}').text
            if(celula == ''):
                celula = 0
            else:
                celula = int(celula)
            linha.append(celula)
            if((i + 1) % 9 == 0):
                tabela.append(linha)
                aux = 0
                linha = []
        
        return tabela

    def get_celulas_selecionaveis(self):
        '''
        Encontrará todas as células selecionáveis na tabela
        retorna lista de webelements
        '''
        return self.find_elements(By.XPATH, Globals.CELULAS_SELECIONAVEIS_XPATH)
    
    def get_celula_coords(self, celula):
        '''
        Encontrará as coordenadas (linha,coluna) da célula
        retorna tupla de linha e coluna
        '''
        celula_id = celula.get_attribute('id')
        filtro = filter(str.isdigit, celula_id)
        coords = int("".join(filtro))
        linha = coords//9
        coluna = coords%9
        return (linha, coluna)

    def scroll_para_novo_jogo(self):
        botao_novo_jogo = self.find_element(By.ID, Globals.NOVO_JOGO_BUTTON_ID)
        self.execute_script("arguments[0].scrollIntoView(false);", botao_novo_jogo)

    def send_solucao(self, celula, solucao):
        '''
        irá selecionar o número na celula
        '''
        celula.click()
        self.find_element(By.XPATH, Globals().get_valor_da_celula_id(solucao)).click()
