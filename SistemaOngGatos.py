import csv
#funções 
#1 Cadastrar felino
def carregador():
    arquivo=open('BaseDeDadosGatos.csv','w')
    return arquivo

def CadastrarFelino():
    dados_csv = []
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
    
    dados_csv.append((nome,sexo,idade,raca,cor,castrado,Fiv,Felv,DataResgate,adotado,larTemp,dataAdocaoHospedagem,Tutor,contato,ultimaVacina,ultimaVermi,ultimoAntipulgas,infoExtra))

    return dados_csv
    

#2 Alterar status do felino
def AlterarStatus(geral):
    cont=1
    for x in range(len(geral[0])):
            print(cont,'-',geral[x][0])
            cont=cont+1
    resposta=int(input('digite o número do felino que deseja alterar: '))
    indice=resposta-1
    cont=1
    for y in range(len(geral)):
            print(cont,'-',geral[indice][y])
            cont=cont+1
    resposta=int(input('digite o número da informação que deseja alterar: '))
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
geral = [
    ["Frajola", "SRD", 3, "m"],
    ["Bolinha", "Persa", 2, "f"],
    ["Rex", "Labrador", 5, "m"],
    ["Mia", "Siamesa", 1, "f"]
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
        geral.append(CadastrarFelino())
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