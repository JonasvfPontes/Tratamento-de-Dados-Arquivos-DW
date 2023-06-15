import pandas as pd

def fIgnorarTabs():
    dfLista = pd.read_csv(r'scripts\\ignorarTabs.csv')   
    while True:
        opc = input('''
        O que deseja fazer agora?
        1 - Ver lista atual
        2 - Adicionar item à lista
        3 - Excluir item da lista
        4 - Sair
        ''')
        if opc.upper() == "VOLTAR":
            break
        if opc =='1':
            print(dfLista)
        
        elif opc =='2':
            print('Digite "Fim" a qualquer momento')
            print('='*50)
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
        elif opc == '3':
            print('Digite "Fim" a qualquer momento')
            print('='*50)
            while True:
                i = input('Digite o número da linha que deseja excluir: ')
                if i.upper() == 'FIM':
                    
                    dfLista.to_csv(r'scripts\\ignorarTabs.csv', index=False)
                    break
                elif i.isnumeric():
                    dfLista = dfLista.drop(index=int(i))
                    print('Feito')
                else:
                    print('Não entendi esse valor, tente novamente')

        
        elif opc == '4':
            break


def fIgnorar():
    path = input('Digite o novo caminho de busca\n')

fIgnorarTabs()
        