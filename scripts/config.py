import pandas as pd
import os

def fIgnorarTabs():
    #Carregar lista
    #verificar se a lista existe, senão, criar
    if os.path.isfile('scripts\\ignorarTabs.csv'):
        dfLista = pd.read_csv(r'scripts\\ignorarTabs.csv')
    else:
        dfLista = pd.DataFrame({'Arquivos':[]})

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
                    if not os.path.exists('scripts'): #Confere se pasta já existe
                        os.makedirs('scripts') #Cria a pasta caso não exista

                    dfLista.to_csv(r'scripts\\ignorarTabs.csv', index=False)
                    break
                elif i.isnumeric():
                    try:
                        dfLista = dfLista.drop(index=int(i))
                        print('Feito')
                    except KeyError:
                        print('='*50)
                        print('Opção inválida, digite o valor da linha que deseja excluir')
                        print('='*50)
                else:
                    print('Não entendi esse valor, tente novamente')

        elif opc == '4':
            break


def fIgnorar():
     #verificar se a lista existe, senão, criar
    if os.path.isfile('scripts\\ignorarDW.csv'):
        dfLista = pd.read_csv(r'scripts\\ignorarDW.csv')
    else:
        dfLista = pd.DataFrame({'Arquivos':[]})

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
                    dfLista.to_csv(r'scripts\\ignorarDW.csv', index=False)
                    break
                novosArquivos.append('DW' + arquivo)
        elif opc == '3':
            print('Digite "Fim" a qualquer momento')
            print('='*50)
            while True:
                i = input('Digite o número da linha que deseja excluir: ')
                if i.upper() == 'FIM':
                    if not os.path.exists('scripts'): #Confere se pasta já existe
                        os.makedirs('scripts') #Cria a pasta caso não exista

                    dfLista.to_csv(r'scripts\\ignorarDW.csv', index=False)
                    break
                elif i.isnumeric():
                    try:
                        dfLista = dfLista.drop(index=int(i))
                        print('Feito')
                    except KeyError:
                        print('='*50)
                        print('Digite o número da linha que deseja excluir')
                        print('='*50)
                else:
                    print('Não entendi esse valor, tente novamente')

        elif opc == '4':
            return dfLista
            break
        