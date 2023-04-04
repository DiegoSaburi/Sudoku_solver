class Globals():
    SITE_LINK = 'https://www.geniol.com.br/logica/sudoku/'
    CELULAS_SELECIONAVEIS_XPATH = '//td[@class = "cell user"]'
    NOVO_JOGO_BUTTON_ID = 'btn-toolbar-newgame'
    _VALOR_DA_CELULA_ID = f'//td[@data-value = "valor"]'

    @classmethod
    def get_valor_da_celula_id(self, valor):
        return self._VALOR_DA_CELULA_ID.replace("valor", str(valor))