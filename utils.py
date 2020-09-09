def print_tabela (tabela):

    for linha in range(len(tabela)):
        if (linha % 3 == 0 and linha != 0):
            print("----------------")
        
        for coluna in range(len(tabela[0])):
            if (coluna % 3 == 0 and coluna != 0):
                print(" | ", end = "")

                if (coluna == 8):
                    print(table[linha][coluna])
                else:
                    print(table[linha][coluna] + "", end = "")

def encontrar_vazios (tabela):
    ''' encontrará as células a serem preenchidas '''

    for linha in range(len(tabela)):
        for coluna in range(len(tabela[0])):
            if (tabela[linha][coluna] == 0):
                return (linha,coluna)
def check_solucao(tabela, solucao, posicao : set ):
    '''
    checará se o numero "solucao" na posição "posicao"
    sendo que posicao = (linha,coluna)
    infringiu alguma regra do jogo"
    retorna: True ou False
    '''
    #Checando existencia de numero repetido na coluna
    for coluna in range(len(tabela[0])):
        if(tabela[posicao[0]][coluna] == solucao and posicao[0] != coluna):
            return False

    #Checando existencia de numero repetido na linha
    for linha in range(len(tabela)):
        if(tabela[linha][posicao[1]] == solucao and posicao[1] != linha):
            return False
    
    #checando existencia de numero repetido no quadrado
    quad_x = posicao[1]//3
    quad_y = posicao[0]//3

    for linha in range(quad_x * 3, quad_y * 3 + 3):
        for coluna in range(quad_x * 3, quad_y * 3 + 3):
            if (tabela[linha][coluna] == solucao and (linha,coluna) != posicao):
                return False
    
    return True
