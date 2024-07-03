import csv
arquivo = open('BaseDeDadosGatos.csv','w')


#funções 
#1 Cadastrar felino
def CadastrarFelino():
    pass

#2 Alterar status do felino
def AlterarStatus():
    pass

#3 Consultar informações sobre o felino
def ConsultarInfo():
    pass

#4 Apresentar estatísticas gerais
def Estatisticas():
    pass

#5 Filtragem de dados
def filtro():
    pass

#6 Salvar
def salvar():
    pass

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
        salvar()
    elif resposta=='7':
        salvar()
        encerrar=True
        print('encerrando programa...')
    else:
        print('ERRO! por favor digite a ação conforme o menu')

