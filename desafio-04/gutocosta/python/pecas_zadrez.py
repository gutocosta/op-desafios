'''
    Programa xadrez
'''


def main():
    '''
    Main Function
    '''
    tabuleiro = []
    linha = 1
    coluna = 1
    while linha < 9:
        while coluna < 9:
            print('Digite o valor da peça na coluna',coluna,',linha:',linha)
            peca = input()
            tabuleiro[coluna][linha] = tabuleiro.append(peca)
            coluna = coluna + 1
    linha = linha + 1
    
    print(tabuleiro)

if __name__ == "__main__":
    main()
