import csv
arquivo = open('BaseDeDadosGatos.csv','w')

#funções 
#1 Cadastrar felino
def CadastrarFelino():
    dados_csv = []
    print('inciando cadastro')
    print('Colocar (-) nos campos que não se sabe')
    nome=input('digite o nome do novo Felino: ')
    sexo=input('digete o sexo do gato (m/f): ')
    idade=int(input('idade do gato: '))
    raca=input('digite a raça do gato: ')
    cor=input('digite a cor do gato: ')
    castrado=input('digite se o gato é castrado (s/n): ')
    Fiv=input('digite se o cato é vacinado contra FIV+ (s/n): ')
    Felv=input('digite se o cato é vacinado contra FELV+ (s/n): ')
    DataResgate=input('digite a data do resgate (dia/mes/ano): ')
    adotado=input('digite se o gato é adotado (s/n): ')
    larTemp=input('digite se o gato esta hospedado (s/n): ')
    dataAdocaoHospedagem=input('digite a data da adoção ou hospedagem (dia/mes/ano): ')
    Tutor=input('digite o nome do tutor: ')
    contato=input('digite o número do tutor: ')
    ultimaVacina=input('digite a data da ultima vacina (dia/mes/ano): ')
    ultimaVermi=input('digite a data da ultima Desvermifugação (dia/mes/ano): ')
    ultimoAntipulgas=input('digite a data do ultimo AntiPulgas (dia/mes/ano): ')
    infoExtra=input('digite qualquer informaçao extra aqui (se tiver): ')

    dados_csv.append([nome, sexo,idade,raca,cor,castrado,Fiv,Felv,DataResgate,adotado,larTemp,dataAdocaoHospedagem,Tutor,contato,ultimaVacina,ultimaVermi,ultimoAntipulgas,infoExtra])
    
    arquivo=csv.writer(dados_csv)


#2 Alterar status do felino
def AlterarStatus():
    resposta=input('digite o nome do gato que deseja alterar: ')


#3 Consultar informações sobre o felino
def ConsultarInfo():
    resposta=input('digite o nome do gato que deseja consultar: ')


#4 Apresentar estatísticas gerais
def Estatisticas():
    pass

#5 Filtragem de dados
def filtro():
    pass

#6 Salvar
def salvar(arquivo):
    arquivo.close()
    print('arquivo salvo com sucesso!')
#main
encerrar=False

#menu
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
        CadastrarFelino()
    elif resposta=='2':
        pass
    elif resposta=='3':
        pass
    elif resposta=='4':
        pass
    elif resposta=='5':
        pass
    elif resposta=='6':
        salvar(arquivo)
    elif resposta=='7':
        salvar(arquivo)
        encerrar=True
        print('encerrando programa...')
    else:
        print('ERRO! por favor digite a ação conforme o menu')

