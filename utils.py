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