import csv
import msvcrt
arquivo_csv=('BaseDeDadosGatos.csv')

#funções 

#CARREGADOR
def carregador(arquivo_csv):
    geral = []
    with open('BaseDeDadosGatos.csv', 'r', newline='') as arquivo_csv:
        leitor = csv.reader(arquivo_csv)
        for linha in leitor:
            geral.append(linha)
    return geral

#1 Cadastrar felino
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
    Fiv=input('digite se o gato possui FIV+ (s/n): ')
    Felv=input('digite se o gato possui FELV+ (s/n): ')
    DataResgate=input('digite a data do resgate (dia/mês/ano): ')
    adotado=input('digite se o gato é adotado (s/n): ')
    larTemp=input('digite se o gato esta hospedado (s/n): ')
    dataAdocaoHospedagem=input('digite a data da adoção ou hospedagem (dia/mês/ano): ')
    Tutor=input('digite o nome do tutor: ')
    contato=input('digite o número do tutor: ')
    ultimaVacina=input('digite a data da ultima vacina (dia/mês/ano): ')
    ultimaVermi=input('digite a data da ultima Desvermifugação (dia/mês/ano): ')
    ultimoAntipulgas=input('digite a data do ultimo AntiPulgas (dia/mês/ano): ')
    infoExtra=input('digite qualquer informaçao extra aqui (se tiver): ')
    dadosCadastro=[nome,sexo,idade,raca,cor,castrado,Fiv,Felv,DataResgate,adotado,larTemp,dataAdocaoHospedagem,Tutor,contato,ultimaVacina,ultimaVermi,ultimoAntipulgas,infoExtra]

    return dadosCadastro
    
#2 Alterar status do felino
def AlterarStatus(geral):
    #essa parte escolhe o gato conforme o número selecionado pelo user
    print('Lista de Bixinhos Cadastrados')
    selecionando=True
    while selecionando !=False:
        cont=1
        for x in range(len(geral)):
            print(cont,'-',geral[x][0])
            cont=cont+1
        print('Voltar ao Menu -> 0')
        resposta=int(input('digite o número do felino que deseja alterar: '))
        if resposta==0:
            selecionando=False
            print('Retornando ao MENU...')
        else:
            indice=resposta-1
            print('---------------------------------------------------------')

            editando=True
            while editando!=False:
                #printa todos os campos atuais e seu número para alterar
                cont=1
                print('Informações sobre',geral[indice][0])
                for y in range(len(geral[indice])): 
                    if cont==1: #ainda não sei de um jeito melhor mas colquei uma mensagem para cada cont como o nome de um campo
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
                    print(campo,':',geral[indice][y],'->',cont)
                    cont=cont+1
                print('Voltar a Seleção -> 0')
                resposta=int(input('digite o número da informação que deseja alterar(->): '))
                if resposta==0:
                    editando=False
                else:
                    coluna=resposta-1
                    infovelha=geral[indice][coluna]
                    novaInfo=input('digite a nova informação:  ')
                    geral[indice][coluna]=novaInfo
                    print('mudando',infovelha,'para',novaInfo)
                    print('Alteração realizada com Sucesso!')
                    print('---------------------------------------------------------')
    print('---------------------------------------------------------')
    return geral

#3 Consultar informações sobre o felino
def ConsultarInfo(geral):
        print('Lista de Bixinhos Cadastrados')
        cont=1
        for x in range(len(geral)):
            print(cont,'-',geral[x][0])
            cont=cont+1
        resposta=int(input('digite o número do felino que deseja consultar: '))
        indice=resposta-1
        print('---------------------------------------------------------')
        nomes_campos = {
        0: 'Nome', 1: 'Sexo', 2: 'Idade', 3: 'Raça', 4: 'Cor Predominante',
        5: 'Castrado', 6: 'Vacina FIV+', 7: 'Vacina FELV+', 8: 'Data de Resgate',
        9: 'Adotado', 10: 'Lar Temporário', 11: 'Data de Adoção/Hospedagem',
        12: 'Tutor', 13: 'Contato do Tutor', 14: 'Data da última Vacina',
        15: 'Data da Última Desvermifugação', 16: 'Data último antipulgas',
        17: 'Informações Extras'}
        for y, valor in enumerate(geral[indice]):
            campo = nomes_campos[y]
            print(f'{campo}: {valor}')
        print("Pressione qualquer tecla para continuar...")
        msvcrt.getch()
        print('---------------------------------------------------------')

#4 Apresentar estatísticas gerais
def Estatisticas(geral):
    print('Estatístiscas Gerais')
    MachoCont=0
    FemeaCont=0
    NCont=0
    #machos e femeas
    for x in range(len(geral)):
        if geral[x][1]=='m' or geral[x][1]=='M':
            MachoCont=MachoCont+1
        elif geral[x][1]=='f' or geral[x][1]=='F':
            FemeaCont=FemeaCont+1
        else:
            NCont=NCont+1
    total=len(geral)
    #porcentagens M/F
    Pmacho=MachoCont/total*100
    Pfemea=FemeaCont/total*100
    Pn=NCont/total*100
    if NCont>0: #essa parte mostra se tiver cadastro incorreto
        print('a porcentagem de Gatos Machos é',round(Pmacho),'%')
        print('a porcentagem de Gatas Fêmeas é',round(Pfemea),'%')
        print('existe uma porcentagem de',Pn,'dos felinos que não estão cadastrados corretamente entre Macho ou Fêmea(M/F)')
    else:
        print('a porcentagem de Gatos Machos é',round(Pmacho),'%')
        print('a porcentagem de Gatas Fêmeas é',round(Pfemea),'%')
    print()
    #adoção
    contAdo=0
    contnaoAdo=0
    for x in range(len(geral)):
        if geral[x][9]=='s' or geral[x][9]=='S':
            contAdo=contAdo+1
        elif geral[x][9]=='n' or geral[x][9]=='N':
            contnaoAdo=contnaoAdo+1
        else: #se não tiver nada ou - contará como não adotado
             contnaoAdo=contnaoAdo+1
    Pado=contAdo/total*100
    PnAdo=contnaoAdo/total*100
    print('a porcentagem de Gatos Adotados é',round(Pado),'%')
    print('a porcentagem de Gatos Não Adotados é',round(PnAdo),'%')
    print()
    #Doenças
    contLimpo=0
    contFiv=0
    contFelv=0
    contAmbas=0
    for x in range(len(geral)):
        if (geral[x][6]=='n' or geral[x][6]=='n') and (geral[x][7]=='n' or geral[x][7]=='N'):
            contLimpo=contLimpo+1
        elif (geral[x][6]=='s' or geral[x][6]=='S') and (geral[x][7]=='s' or geral[x][7]=='S'):
            contAmbas=contAmbas+1
        elif (geral[x][6]=='s' or geral[x][6]=='S'):
            contFiv=contFiv+1
        elif (geral[x][7]=='s' or geral[x][7]=='S'):
            contFelv=contFelv+1
    Plimpo=contLimpo/total*100
    Pfiv=contFiv/total*100
    Pfelv=contFelv/total*100
    Pambas=contAmbas/total*100
    print('a Porcentagem de gatos que não apresenta nem FIV+ nem FELV+ é',round(Plimpo),'%')
    print('a Porcentagem de gatos que apresenta Apenas FIV+ é',round(Pfiv),'%')
    print('a Porcentagem de gatos que apresenta Apenas FELV+ é',round(Pfelv),'%')
    print('a Porcentagem de gatos que apresenta Ambas FIV+ e FELV+ é',round(Pambas),'%')
    print("Pressione qualquer tecla para continuar...")
    msvcrt.getch()
    print('---------------------------------------------------------')

#5 Filtragem de dados
def filtro(geral):
    encerrar=False
    #if resposta==1
    while encerrar!=True:
        print('MENU do filtro')
        print()
        print('Opções de filtragem')
        print('1 - Filtrar por Data Resgate')
        print('2 - Filtrar por Data Adoção')
        print('0 - Voltar ao Menu Principal')

        resposta=int(input('digite a opção que deseja: '))
        print('---------------------------------------------------------')
        
        if resposta==1:
            #parametros do filtro de resgate
            AnoInicio=int(input('digite o ano de inicio que deseja filtrar os resgates: '))
            AnoFim=int(input('digite o ano de limite que deseja filtrar os resgates: '))
            
            cont=0
            opcoesFelinos = [] #irá armazenar os bixinhos validos
            
            print(f'Lista de Bixinhos Resgatados entre {AnoInicio} e {AnoFim}:')
            for i in range(len(geral)):
                ano_resgate = int(geral[i][8][-4:]) 
                if ano_resgate >= AnoInicio and ano_resgate <= AnoFim:
                    print(f'{cont} - {geral[i][0]}')
                    opcoesFelinos.append(i)  
                    cont += 1
            if cont == 0:
                print('Nenhum Felino encontrado no intervalo de tempo especificado.')
                continue
            #escolha do gato
            resposta= int(input('Digite o número do animal que deseja consultar: '))
            #validação
            if resposta < 0 or resposta >= len(opcoesFelinos):
                print('Opção inválida.')
                continue
            #resultado
            indice=opcoesFelinos[resposta]
            nomes_campos = {
            0: 'Nome', 1: 'Sexo', 2: 'Idade', 3: 'Raça', 4: 'Cor Predominante',
            5: 'Castrado', 6: 'Vacina FIV+', 7: 'Vacina FELV+', 8: 'Data de Resgate',
            9: 'Adotado', 10: 'Lar Temporário', 11: 'Data de Adoção/Hospedagem',
            12: 'Tutor', 13: 'Contato do Tutor', 14: 'Data da última Vacina',
            15: 'Data da Última Desvermifugação', 16: 'Data último antipulgas',
            17: 'Informações Extras'}
            for y, valor in enumerate(geral[indice]):
                campo = nomes_campos[y]
                print(f'{campo}: {valor}')
            print("Pressione qualquer tecla para continuar...")
            msvcrt.getch()
            print('---------------------------------------------------------')

        elif resposta==2:
            #parametros do filtro de adoção
            AnoInicio=int(input('digite o ano de inicio que deseja filtrar as adoções: '))
            AnoFim=int(input('digite o ano de limite que deseja filtrar os adoções: '))
            
            cont=0
            opcoesFelinos = [] #irá armazenar os bixinhos validos
            
            print(f'Lista de Bixinhos Resgatados entre {AnoInicio} e {AnoFim}:')
            for i in range(len(geral)):
                ano_adocao = int(geral[i][11][-4:]) 
                adotado = geral[i][9].lower()
                if adotado == 's' and ano_adocao >= AnoInicio and ano_adocao <= AnoFim:
                    print(f'{cont} - {geral[i][0]}')
                    opcoesFelinos.append(i)  # Guardando o índice do animal para referência posterior
                    cont += 1
            if cont == 0:
                print('Nenhum animal encontrado no intervalo de tempo especificado ou que tenha sido adotado.')
                continue
            #escolha do gato
            resposta= int(input('Digite o número do animal que deseja consultar: '))
            #validação
            if resposta < 0 or resposta >= len(opcoesFelinos):
                print('Opção inválida.')
                continue
            #resultado
            indice=opcoesFelinos[resposta]
            nomes_campos = {
            0: 'Nome', 1: 'Sexo', 2: 'Idade', 3: 'Raça', 4: 'Cor Predominante',
            5: 'Castrado', 6: 'Vacina FIV+', 7: 'Vacina FELV+', 8: 'Data de Resgate',
            9: 'Adotado', 10: 'Lar Temporário', 11: 'Data de Adoção/Hospedagem',
            12: 'Tutor', 13: 'Contato do Tutor', 14: 'Data da última Vacina',
            15: 'Data da Última Desvermifugação', 16: 'Data último antipulgas',
            17: 'Informações Extras'}
            for y, valor in enumerate(geral[indice]):
                campo = nomes_campos[y]
                print(f'{campo}: {valor}')
            print("Pressione qualquer tecla para continuar...")
            msvcrt.getch()
            print('---------------------------------------------------------')

        elif resposta==0:
            encerrar=True
        else:
            print('Erro! por favor digite o um número conforme as opções')
            print()

#6 Salvar
def salvar(geral,arquivo_csv):
    with open('BaseDeDadosGatos.csv', 'w', newline='') as arquivo_csv:
        escritor = csv.writer(arquivo_csv)  
        for linha in geral:
            escritor.writerow(linha)
    arquivo_csv.close()

#main
encerrar=False
geral=carregador(arquivo_csv)

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
    resposta=input('O que deseja fazer? ')
    print('---------------------------------------------------------')

    if resposta=='1':
        dadosCadastro=CadastrarFelino()
        geral.append(dadosCadastro)
    elif resposta=='2':
        AlterarStatus(geral)
    elif resposta=='3':
        ConsultarInfo(geral)
    elif resposta=='4':
        Estatisticas(geral)
    elif resposta=='5':
        filtro(geral)
    elif resposta=='6':
        salvar(geral,arquivo_csv)
        print('Informações salvas com sucesso!')
    elif resposta=='7':
        salvar(geral,arquivo_csv)
        encerrar=True
        print('Informações salvas com sucesso!')
        print('Encerrando o Programa...')
    else:
        print('ERRO! por favor digite a ação conforme o menu')
