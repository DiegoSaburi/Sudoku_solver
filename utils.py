def print_tabela (tabela):

    for linha in range(len(tabela)):
        if (linha % 3 == 0 and linha != 0):
            print("----------------")
        
        for coluna in range(len(tabela[0])):
            if (coluna % 3 == 0 and coluna != 0):
                print(" | ", end = "")

                if (coluna == 8):
                    print(table[linha][coluna] + "", end = "")