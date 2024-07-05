import csv
#funções 
#1 Cadastrar felino
def carregador():
    arquivo=open('BaseDeDadosGatos.csv','w')
    return arquivo

def CadastrarFelino():
    dadosCadastro=[]
    print('inciando cadastro...')
    print('Colocar (-) nos campos que não se sabe')
    nome=input('digite o nome do novo Felino: ')
    sexo=input('digete o sexo do gato (m/f): ')
    idade=int(input('idade do gato: '))
    raca=input('digite a raça do gato: ')
    cor=input('digite a cor do gato: ')
    castrado=input('digite se o gato é castrado (s/n): ')
    Fiv=input('digite se o cato é vacinado contra FIV+ (s/n): ')
    Felv=input('digite se o cato é vacinado contra FELV+ (s/n): ')
    DataResgate=input('digite a data do resgate (ano): ')
    adotado=input('digite se o gato é adotado (s/n): ')
    larTemp=input('digite se o gato esta hospedado (s/n): ')
    dataAdocaoHospedagem=input('digite a data da adoção ou hospedagem (ano): ')
    Tutor=input('digite o nome do tutor: ')
    contato=input('digite o número do tutor: ')
    ultimaVacina=input('digite a data da ultima vacina (ano): ')
    ultimaVermi=input('digite a data da ultima Desvermifugação (ano): ')
    ultimoAntipulgas=input('digite a data do ultimo AntiPulgas (ano): ')
    infoExtra=input('digite qualquer informaçao extra aqui (se tiver): ')
    dadosCadastro=[nome,sexo,idade,raca,cor,castrado,Fiv,Felv,DataResgate,adotado,larTemp,dataAdocaoHospedagem,Tutor,contato,ultimaVacina,ultimaVermi,ultimoAntipulgas,infoExtra]
    print(dadosCadastro)
    return dadosCadastro
    

#2 Alterar status do felino
def AlterarStatus(geral):
    #essa parte escolhe o gato conforme o número selecionado pelo user
    cont=1
    for x in range(len(geral)):
        print(cont,'-',geral[x][0])
        cont=cont+1
    resposta=int(input('digite o número do felino que deseja alterar: '))
    indice=resposta-1
    
    #printa todos os campos atuais e seu número para alterar
    cont=1
    for y in range(len(geral[indice])):
        if cont==1:
            campo='Nome'
        elif cont==2:
            campo='Sexo'
        elif cont==3:
            campo='Idade'
        elif cont==4:
            campo='Raça'
        elif cont==5:
            campo='Cor Predominante'
        elif cont==6:
            campo='Castrado'
        elif cont==7:
            campo='Vacina FIV+'
        elif cont==8:
            campo='Vacina FELV+'
        elif cont==9:
            campo='Data de Resgate' 
        elif cont==10:
            campo='Adotado' 
        elif cont==11:
            campo='Lar Temporário' 
        elif cont==12:
            campo='Data de Adoção/Hospedagem' 
        elif cont==13:
            campo='Tutor'    
        elif cont==14:
            campo='Contato do Tutor' 
        elif cont==15:
            campo='Data da última Vacina' 
        elif cont==16:
            campo='Data da Última Desvermifugação' 
        elif cont==17:
            campo='Data último antipulgas'
        elif cont==18:
            campo='Informações Extras' 
        print(campo,'-',geral[indice][y],'->',cont)
        cont=cont+1
    resposta=int(input('digite o número da informação que deseja alterar(->): '))
    coluna=resposta-1
    novaInfo=input('digite a nova informação:  ')
    geral[indice][coluna]=novaInfo
    #return geral

#3 Consultar informações sobre o felino
def ConsultarInfo(geral):
    pass


#4 Apresentar estatísticas gerais
def Estatisticas():
    pass
    #dividir por 100 
    #fazer e acessar contadores individuas com base no arquivo da base de dados

#5 Filtragem de dados
def filtro():
    pass

#6 Salvar
#def salvar(arquivo):
    #arquivo.close()
    #print('arquivo salvo com sucesso!')

#main
encerrar=False
geral=[]
#teste
geral=[
    ['vito', 'm', 1, '-', 'preto', '', '', '', '', '', '', '', '', '', '', '', '', ''],
    ['juju', 'm', 10, '-', 'branca', 's', '', '', '', '', '', '', '', '', '', '', '', '']
]
#menu
arquivo=carregador()
while encerrar!=True:
    print('MENU PRINCIPAL:')
    print('')
    print('1 - Cadastrar felino')
    print('2 - Alterar status do felino')
    print('3 - Consultar infromações sobre felino')
    print('4 - Apresentar estatísticas gerais ')
    print('5 - Filtro de dados ')
    print('6 - Salvar ')
    print('7 - Sair do programa ')
    resposta=input('o que deseja fazer? ')

    if resposta=='1':
        dadosCadastro=CadastrarFelino()
        geral.append(dadosCadastro)
    elif resposta=='2':
        AlterarStatus(geral)
    elif resposta=='3':
        ConsultarInfo()
    elif resposta=='4':
        Estatisticas()
    elif resposta=='5':
        filtro()
    #elif resposta=='6':
        #salvar()
    elif resposta=='7':
        #salvar()
        encerrar=True
        print('encerrando programa...')
    else:
        print('ERRO! por favor digite a ação conforme o menu')

for L in range(len(geral)):
    for C in range(len(geral[0])):
        print(geral[L][C], end="\t")
    print()