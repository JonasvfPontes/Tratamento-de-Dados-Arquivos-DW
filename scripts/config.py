import pandas as pd

def fIgnorarTabs():
    dfLista = pd.read_csv(r'scripts\\ignorarTabs.csv')   
    while True:
        opc = input('''
        O que deseja fazer agora?
        1 - Ver lista atual
        2 - Adicionar item à lista
        3 - Sair
        ''')
        if opc.upper() == "VOLTAR":
            break
        if opc =='1':
            print(dfLista)
        elif opc == '3':
            break
        elif opc =='2':
            print('Digite "Fim" a qualquer momento:')
            novosArquivos = []            
            while True:
                arquivo = input('Nome do Arquivo [Ex. DW000 ou 000]: ')
                if arquivo.upper() =="FIM":
                    #Adicionar dicionário ao dfLista
                    if len(dfLista) != 0 :
                        lista = dfLista['Arquivos'].to_list()
                        for valor in novosArquivos:
                            lista.append(valor)
                    else:
                        lista = novosArquivos
                    dfTodos = pd.DataFrame({'Arquivos': lista})
                    dfLista= dfTodos
                    dfLista.to_csv(r'scripts\\ignorarTabs.csv', index=False)
                    break
                novosArquivos.append('DW' + arquivo)
                


def fIgnorar():
    path = input('Digite o novo caminho de busca\n')

fIgnorarTabs()
        