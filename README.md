# Tratamento-de-Dados-Arquivos-DW
Procurando quebras de linhas e/ou TABs nos arquivos

Estávamos com problemas na exportação de dados do nosso banco de dados, 
o problema não era exatamento no bd mas sim no software que a empresa NBS criou, os arquivos
estávam vindo com muitas quebras de linha e vários TABs o que ocasionava problemas quando iamos usar
os dados dos arquivos usando tabulação para separar cada campo do banco de dados. 

Esse script irá percorrer cada linha e verificar se há quebras, isso será possível porque cara arquivo tem
o comprimento ideal de cada linha, e também irá verificar se há TABs, sendo assim irá tratar cada linha removendo 
as quebras e removendo os TABs, ao final irá gerar logs de erro detalhando o nome do arquivo, o número da linha e qual tipo de problema
há naquela linha para que eu possa enviar esses logs para o CPD e eles possam corrigir via banco de dados
