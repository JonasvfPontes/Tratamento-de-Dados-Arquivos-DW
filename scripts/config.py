import pandas as pd
def fIgnorar():
    path = input('Digite o novo caminho de busca\n')


def fIgnorarTabs():
    dfLista = pd.read_csv(r'scripts\ignorarTabs.csv')
    print('Digite "Voltar" para voltar ao menu anterior:')
   
    while True:
        opc = input('''
        O que deseja fazer agora?
        1 - Ver lista atual
        2 - Adicionar item à lista
        ''')
        if opc.upper() == "VOLTAR":
            break
        if opc =='1':
            print(dfLista)
        elif opc =='2':
            print('Digite "Fim" a qualquer momento:')
            while True:
                novosArquivos =[]
                arquivo = input('Nome do Arquivo: ')
                if arquivo.upper() =="FIM":
                    #Adicionar dicionário ao dfLista
                    dfNovosArquivos = pd.DataFrame(novosArquivos)
                    dfConcatenado = pd.concat(dfLista, dfNovosArquivos, ignore_index=True)
                    dfConcatenado.to_csv(r'scripts\ignorarTabs.csv')
                    break
                novosArquivos.append(arquivo)
                


        