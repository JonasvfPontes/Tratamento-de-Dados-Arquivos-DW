import pandas as pd
dfDados = pd.DataFrame(columns=['linhas'])

print(dfDados)
#Tratar DW110
with open('Arquivos Gerados\DW110_20230511_009114091000160.txt', 'r') as dw110:
    arquivo = dw110.readlines()
tamIdeal = 1186

verificador = 0
linhaToda = ''
cont = 0
for linha in arquivo:
    cont += 1
    linha = linha.replace('\t', ' ') #removendo todos os tabs da linha atual
    tam = len(linha)
    if len(linha) < tamIdeal:
        if verificador==0: #Se = 0, primeira linha com problema
            parteLinha = linha.replace('\n',' ')  #Verificar se preciso adicionar espaços a cada quebra de linha
            verificador += 1
        else:
            linhaToda = parteLinha + linha.replace('\n', ' ') 
            tam = len(linhaToda)
            if len(linhaToda) == tamIdeal:
                dfNovaLinha = pd.DataFrame({'linhas': [str(linhaToda).replace('\n', '').strip() ]}) #adicionando linha única para poder concatenar com o dfDados
                dfDados = pd.concat([dfDados, dfNovaLinha], ignore_index=True)
                verificador = 0
            else:
                parteLinha = linhaToda
    else:
        dfNovaLinha = pd.DataFrame({'linhas': [str(linha).replace('\n', '') ]})
        dfDados = pd.concat([dfDados, dfNovaLinha], ignore_index=True)
        

#print(dfDados.head(50))
dfDados.to_csv('teste.csv', sep='\t', index=False, header=False)
print('FIM!')