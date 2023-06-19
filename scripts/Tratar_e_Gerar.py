import pandas as pd
from time import sleep
import os
import config

#Função de tratamento-------------------------------
def fTratamento(caminhoArquivo, comprimentoLinha: int, df: pd.DataFrame, NomedoArquivoSaida): #devo passar como paramretro uma string com o caminho do arquivo e comprimento ideal da linha
    logErro = {'numLinha':[],'Qtde':[],'Tipo':[]}
    
    #carrega a lista de arquivos que deve ignotar os TABs
    dfIgnorarTabs = pd.read_csv(r'scripts\\ignorarTabs.csv')

    with open(caminhoArquivo, 'r') as dw:
        arquivo = dw.readlines()

    tamIdeal = comprimentoLinha

    verificador = 0
    linhaToda = ''
    cont = 0
    for linha in arquivo:
        cont += 1

        linha = linha.replace('"',' ') #Remove aspas de cada linha
        
        #Confere se o arquivo está na lista IgnotarTABs
        localizar = str(caminhoArquivo).find('_')
        if localizar > -1:
            arquivoAtual = caminhoArquivo[:localizar]
            arquivoAtual = arquivoAtual[-5:]
            # Confere se o arquivo atual não está contido dentro dos valores
            #do dfIgnorarTabs
            if not arquivoAtual in dfIgnorarTabs.values:
                if linha.count('\t') > 0: #Verificar se tem TAB na linha
                    #Adicionando informações ao log de erros encontrados
                    logErro['numLinha'].append(str(f'{cont:<8}'))
                    qtdeTAB = linha.count('\t')
                    logErro['Qtde'].append(str(f'{qtdeTAB:<4}'))
                    logErro['Tipo'].append('TAB')
                    linha = linha.replace('\t', ' ') #removendo todos os tabs da linha atual

        if len(linha) < tamIdeal:
            if verificador==0: #Se = 0, primeira linha com problema
                #Adicionando informações ao log de erros encontrados
                logErro['numLinha'].append(str(f'{cont:<8}'))
                logErro['Qtde'].append(str(f'{1:<4}'))
                logErro['Tipo'].append('QUEBRA')

                parteLinha = linha.replace('\n',' ')  #Verificar se preciso adicionar espaços a cada quebra de linha
                verificador += 1
            else:
                linhaToda = parteLinha + linha.replace('\n', ' ') 
                if len(linhaToda) == tamIdeal:
                    dfNovaLinha = pd.DataFrame({'linhas': [str(linhaToda).replace('\n', '').strip() ]}) #adicionando linha única para poder concatenar com o dfDados
                    df = pd.concat([df, dfNovaLinha], ignore_index=True)
                    verificador = 0
                else:
                    parteLinha = linhaToda
        else:
            verificador = 0
            dfNovaLinha = pd.DataFrame({'linhas': [str(linha).replace('\n', '') ]})
            df = pd.concat([df, dfNovaLinha], ignore_index=True)
    
    #Exportando df tratado
    df.to_csv('DW csv\\' + NomedoArquivoSaida + '.csv', sep='\t', index=False, header=False)
    
    #Verificando log de erro e exportando se houver algo
    if len(logErro['numLinha']) != 0:
        df = pd.DataFrame(logErro)
        df.to_csv('Erros\\' + NomedoArquivoSaida + ' logErro' + '.csv', sep='#', index=False, header=True)

def fVerificarOpcao(opc):
    if opc == 'S':
        print('Saindo...')
        sleep(2)
        exit()
    elif opc == 'C':
        fAbrirConfig()
        return False
    else:
        return True


def fAbrirConfig():
    while True:
        print('''
    Escolha uma opção:
    1 - Adicionar/Remover arquivos que devo ignorar TABs
    2 - Adicionar/Remover arquivos que devo ignorar
    3 - Sair e executar programa''')
    
        opc = input()
        if opc == '1':
            config.fIgnorarTabs()
        elif opc =='2':
            config.fIgnorar()
        elif opc == '3':
            print('Saindo...')
            sleep(1)
            break
        else:
            print('Opção inválida')



#------------Programa principal----------------------
dfDados = pd.DataFrame(columns=['linhas'])

#Listas para guardar o CNPJ das CC
cnpjs = ['009114091000160', '008029092000144', '008811523000120', '046245693000183']
nomeCC = ['E20', 'N53', 'S46', 'T08'] #Esse dicionário deve seguir a mesma ordem da lista cnpjs

#Dicionário com o nome e conprimento padrão das linhas
comprimentoIdeal = {
    'DW101':716, 'DW102':211, 'DW103':69, 'DW104':54, 'DW105':56, 'DW106':537, 'DW110':1186, 'DW111':261, 'DW113':246, 'DW114':246, 'DW115':59, 'DW116':66,
    'DW117':387, 'DW118':158, 'DW119':124, 'DW120':282, 'DW121':1266, 'DW122':60, 'DW123':93, 'DW124':113, 'DW125':63, 'DW126':63, 'DW127':486, 'DW128':72,
    'DW129':64, 'DW130':0, 'DW140':1025, 'DW141':688, 'DW142':68, 'DW143':505, 'DW144':68, 'DW145':83, 'DW146':83, 'DW147':68, 'DW148':68, 'DW149':68, 'DW150':0,
    'DW151':0, 'DW152':68, 'DW153':68, 'DW154':68, 'DW155':68, 'DW156':611, 'DW157':0, 'DW158':68, 'DW159':126, 'DW160':68, 'DW161':48, 'DW162':51, 'DW163':279,
    'DW164':68, 'DW165':68, 'DW166':68, 'DW167':68, 'DW168':83, 'DW201':218, 'DW202':292, 'DW203': 603, 'DW204': 145, 'DW205': 269, 'DW206':286, 'DW207':914, 
    'DW208':811, 'DW209':387, 'DW210':253, 'DW211':147, 'DW220':1027, 'DW221':1405, 'DW222':0, 'DW223':848
}

print('\n')
print('='*50 + '\nDigite "S" a qualquer momento para sair ou "C" para abrir as configurações\n' + '='*50 + '\n')

#Verificando opções do usuário
verificador1 = False
verificador2 = False
verificador3 = False
verificador4 = False
while True:
    if not verificador1:
        dataExportacao = input('Digite a data de exportação do arquivo DW [Ex 20230510]: ').strip().upper()
        verificador1 = fVerificarOpcao(dataExportacao)
        if verificador1 and verificador2 and verificador3 and verificador4:
            break
    
    if not verificador2:
        nomeArquivoInicio = input('Digite o nome do primeiro arquivo que quer tratar [Ex: DW110]: ').upper()
        verificador2 = fVerificarOpcao(nomeArquivoInicio)
        if verificador1 and verificador2 and verificador3 and verificador4:
            break

    if not verificador3:
        nomeArquivoFim = input('Digite o nome do último arquivo que quer tratar [Ex: DW114]: ').upper()
        verificador3 = fVerificarOpcao(nomeArquivoFim)
        if verificador1 and verificador2 and verificador3 and verificador4:
            break

    if not verificador4:
        opc = input('Qual CC quer tratar?\n1 - E20\n2 - N53\n3 - S46\n4 - T08\n5 - Todos\n').upper()
        verificador4 = fVerificarOpcao(opc)
        if verificador1 and verificador2 and verificador3 and verificador4:
            break

print('\n' + '='*50)
print('Aguarde, estou trabalhando nos arquivos .txt')


#Loop para tratamento de cada arquivo
numInicio = int(str(f'{nomeArquivoInicio[-3:]}'))
numFim = int(str(f'{nomeArquivoFim[-3:]}'))


if numFim < numInicio: #a ordem é o que diz se o for vai trabalhar com acrescimo ou decrescimo
    ordem =-1
else:
    ordem =1


if int(opc) > len(cnpjs): #Verifica a opção das CCs escolhidas pelo usuário
    for i in range(numInicio, numFim + ordem, ordem):
        for cnpj in cnpjs:
            #Cria o caminho do arquivo para ser aplicado a função de tratamento
            pathArquivo = str('Arquivos Gerados\DW' + str(i) + '_' + dataExportacao + '_' + cnpj + '.txt') #Nome dos arquivos DWs padrão → DW110_20230511_009114091000160
            if os.path.isfile(pathArquivo): #Verificando se o arquivo existe
                fTratamento(pathArquivo, comprimentoIdeal['DW' + str(i)], dfDados, 'DW' + str(i) + '-' + nomeCC[cnpjs.index(cnpj) ])
else:
    for i in range(numInicio, numFim + ordem, ordem) :
            pathArquivo = str('Arquivos Gerados\DW' + str(i) + '_' + dataExportacao + '_' + cnpjs[int(opc)-1] + '.txt') #Nome dos arquivos DWs padrão → DW110_20230511_009114091000160
            if os.path.isfile(pathArquivo):
                fTratamento(pathArquivo, comprimentoIdeal['DW' + str(i)], dfDados, 'DW' + str(i) + '-' + nomeCC[int(opc)-1])

#Juntar arquivos por layout para eu poder usar esse único arquivo
#como padrão quando carregar no banco de dados
print('Unificando arquivos por layout...')
sleep(1)

'''
Padrão de saída dos arquivos
DW101-E20.csv
DW101-N53.csv
'''
#Percorre cada arquivos dentro da pasta DW csv e junta 
#se for o mesmo layout DW csv\DW101-E20.csv

#dfs = []  # Lista para armazenar os DataFrames
for elemento in comprimentoIdeal.keys():
    dfConsolidado = pd.DataFrame()
    dfs = []  # Cria/Esvazia lista para armazenar os DataFrames
    for cc in nomeCC:
        arquivoDw = 'DW csv\\' + elemento + '-' + cc + '.csv'
        if os.path.isfile(arquivoDw):
            try:
                dfAtual = pd.read_csv(arquivoDw,sep='\t', encoding='utf-8', header=None)
                dfAtual['CC'] = cc #Adiciona a CC de origem aos dados
                dfs.append(dfAtual)  # Adiciona o DataFrame à lista

            except pd.errors.EmptyDataError:
                print('Arquivo ' + arquivoDw + ' vazio')
            dfAtual = pd.DataFrame()

    if len(dfs) > 0:
        dfConsolidado = pd.concat(dfs)  # Concatena os DataFrames da lista
        dfConsolidado.to_csv('DW csv\\' + elemento + '.csv',sep='\t', index=False, header=False)

print('Sucesso!')
print('Saindo...')
sleep(2)
