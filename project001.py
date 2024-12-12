users = [['rene', 'rene@gmail.com', 'rene1234'], ['samuel', 'samuel@gmail.com', 'samuel456'], ['jose', 'jose@gmail.com', 'jose44477'],['pedro','pedro@gmail.com','pedro123'],['pedro2','pedro2@gmail.com','pedro123']]
events =[['aaa','ai','pedro2@gmail.com',['joao pessoa','10'],['1','2','2024','12','03'],['batman','batman@gmail.com'],['pikachu','pikachu@gmail.com']],['kkk','ai','pedro2@gmail.com',['joao pessoa','20'],['1','2','2024','15','54'],['Jotaro Kujo', 'jojo@gmail.com']],['kkk','ai','pedro2@gmail.com',['joao pessoa','10'],['1','2','2024','00','00']]]
cidadesDisp = ['RIO BRANCO(AC)','MACEIO(AL)','MACAPA(AP)','MANAUS(AM)','SALVADOR(BA)','FORTALEZA(CE)','BRASILIA(DF)','VITORIA(ES)','GOIANIA(GO)','SAO LUIS(MA)','CUIABA(MT)','CAMPO GRANDE(MS)','BELO HORIZONTE(MG)','BELEM(PA)','JOAO PESSOA(PB)','CURITIBA(PR)','RECIFE(PE)','TERESINA(PI)','RIO DE JANEIRO(RJ)','NATAL(RN)','PORTO ALEGRE(RS)','PORTO VELHO(RO)','BOA VISTA(RR)','FLORIANOPOLIS(SC)','SAO PAULO(SP)','ARACAJU(SE)','PALMAS(TO)']

def calculadora_fin():
  while(True):
      receit=float(input('DIGITE A RECEITA DO SEU EVENTO:'))
      gastos=float(input('DIGITE QUANTO VOCE GASTOU PARA CRIAR O EVENTO:'))
      lucroTotal=receit-gastos
      if (lucroTotal >= 0):
          print(f'O SEU LUCRO FOI {lucroTotal}')
      else:
          print(f'INFELIZMENTE VOCE TEVE UM PREJUIZO DE {lucroTotal * -1}')

      porc=input('DESEJA VER A PORCENTAGEM DE GASTOS?').lower().strip()
      porcentagem=(gastos/receit)*100
      if(porc=='sim'):
          print(f'ESSA FOI A PORCENTAGEM DE GASTOS {porcentagem} %')
      porcentagem2=input('DESEJA VER EM FORMA DE PORCENTAGEM OS SEUS LUCROS?').lower().strip()
      porcentagemLu=(lucroTotal/receit)*100
      if(porcentagem2=='sim'):
          print(f'ESSA FOI A PORCENTAGEM DE LUCROS {porcentagemLu} %')

      exit=input('DESEJA CONTINUAR NA CALCULADORA?').lower().strip()
      if(exit!='sim'):
          break

def dados_d_evento(email):
    lupa = email
    existe = False
    evento = 0
    valor = 0
    for i in range(0, len(events)):
        if (lupa == events[i][2]):
            print('NUMERO DO EVENTO', i + 1, 'º NOME DO EVENTO: ', events[i][0],'\nHORÁRIO: ',events[i][4][3],'H:',events[i][4][4],'MIN', '\n''LOCAL:', events[i][3][0],
                  '\n''PREÇO:',
                  events[i][3][1], 'R$' '\n''DATA:', events[i][4][0], '/', events[i][4][1], '/', events[i][4][2])
            print('PESSOAS INSCRITAS NOS EVENTOS: ')
            for j in range(5, len(events[i])):
                print(f'NOME: {events[i][j][0]}')
                print(f'EMAIL: {events[i][j][1]}')
                print('------------------------------')
            valor = (float(events[i][3][1]) * (len(events[i]) - 5))
            print(f'NUMERO DE PARTICIPANTES: {len(events[i]) - 5} ')
            print(f'VALOR ARRECADADO: {valor}R$')
            print('EVENTO ENCONTRADO COM SUCESSO!')
            print('------------------------------')
            existe = True
            evento = events[i][2]
    if (not existe):
        print('EVENTO INVALIDO, CONFIRA O NOME DO SEU EVENTO NOVAMENTE!')
    else:
        return evento
def verificar_email_eventos(gmail,events):
    existe = False
    for i in range(0, len(events)):
        for j in range(5, len(events[i])):
            if (events[i][j][1] == gmail):
                existe = True
                break
    return existe
def buscar_eventos_f_l(email):
        lupa = email
        existe = False
        evento = 0
        for i in range(0,len(events)):
            if(lupa == events[i][2]):
                 print('NUMERO DO EVENTO',i+1,'º NOME DO EVENTO: ', events[i][0], '\nHORARIO: ',events[i][4][3],'H:',events[i][4][4],'MIN','\n''LOCAL:',events[i][3][0], '\n''PREÇO:',
                          events[i][3][1],'R$' '\n''DATA:',events[i][4][0],'/',events[i][4][1],'/',events[i][4][2])
                 print('PESSOAS INSCRITAS NOS EVENTOS: ')
                 for j in range(5,len(events[i])):
                     print(f'NOME: {events[i][j][0]}')
                     print(f'EMAIL: {events[i][j][1]}')
                 print('EVENTO ENCONTRADO COM SUCESSO!')
                 print('------------------------------')
                 existe = True
                 evento = events[i][2]
        if (not existe):
            print('EVENTO INVALIDO, CONFIRA O NOME DO SEU EVENTO NOVAMENTE!')
        else:
            return evento

def apagar_evento(gmail):
    for i in range(len(events)):
        if (gmail == events[i][2]):
            print('NUMERO DO EVENTO', i + 1, 'º NOME DO EVENTO: ', events[i][0],'\nHORARIO: ',events[i][4][3],'H:',events[i][4][4],'MIN', '\n''LOCAL:', events[i][3][0],
                  '\n''PREÇO:',
                  events[i][3][1], 'R$''\n''DATA: ', events[i][4][0], '/', events[i][4][1], '/', events[i][4][2])
            print('------------------------------')
            print('EVENTO ENCONTRADO COM SUCESSO!')
            resposta = input('DIGITE O NUMERO DO EVENTO QUE DESEJA APAGAR OU OUTRA TECLA PARA CANCELAR: ').upper().strip()
            if (resposta.isnumeric()):
                resposta = int(resposta) - 1
                if (resposta >= 0 and resposta < len(events) and events[resposta][0].upper() == events[i][0].upper()):
                    confirma = input('TEM CERTEZA QUE DESEJA APAGAR O EVENTO?: ').upper().strip()
                    if (confirma == 'SIM'):
                        events.pop(resposta)
                        print('EVENTO APAGADO COM SUCESSO')
                        return True
                else:
                    print('OPERAÇÃO CANCELADA, O EVENTO NÃO FOI DELETADO')
    print('NÃO HÁ MAIS EVENTOS CADASTRADOS POR ESSE USUÁRIO')
    return False

def inscricao_eventos(nome,gmail,nome_e):
    for i in range(len(events)):
        if(nome_e.upper() == events[i][0].upper()):
            for j in range(5, len(events[i])):
                if (events[i][j][1] == gmail):
                    print('USUÁRIO JÁ CADASTRADO NESSE EVENTO!')
                    break
    resposta = input('EM QUAL EVENTO DESEJA SE CADASTRAR (DIGITE O NUMERO PARA CONCLUIR CADASTRO'
                     ' OU OUTRA TECLA PARA CANCELAR)?').upper().strip()
    if(resposta.isnumeric()):
        resposta = int(resposta) - 1
        if(resposta >= 0 and resposta < len(events) and events[resposta][0].upper() == nome_e.upper()):
            events[resposta].append([nome, gmail])
            print('CADASTRO REALIZADO COM SUCESSO')
            return True
    return False

def buscar_eventos():
    existe = False
    evento = 0
    while(True):
        lupa = input('DIGITE O NOME DO EVENTO QUE DESEJA BUSCAR (DIGITE 0 PARA CANCELAR A OPERAÇÃO):')
        if(lupa=='0'):
            return '0'
        for i in range(0,len(events)):
            if(lupa == events[i][0]):
             print('NUMERO DO EVENTO ',i+1,'º NOME DO EVENTO: ',events[i][0],
                    '\nLOCAL: ',events[i][3][0],
                    '\nPREÇO: R$',events[i][3][1],
                    '\nDATA: ',events[i][4][0],'/',events[i][4][1],'/',events[i][4][2],
                    '\nHORARIO: ',events[i][4][3],'H:',events[i][4][4],'MIN')
             print('------------------------------')
             print('EVENTO ENCONTRADO COM SUCESSO!')

             existe = True
             evento = events[i][0]
        if(not existe):
            print('EVENTO INVALIDO, CONFIRA O NOME DO SEU EVENTO NOVAMENTE!')
        else:
          return evento
def cadastrar_eventos(gmail):
    titulo = input('DIGITE O NOME DO EVENTO QUE DESEJA CRIAR: ')
    descricao = input('INSIRA A DESCRIÇAO NO SEU EVENTO: ')

    while (True):
        print('-------------------------------------------------------')
        dia = input('DIGITE O DIA QUE DESEJA REALIZAR O EVENTO: ')
        mes = input('DIGITE O MES QUE DESEJA REALIZAR O EVENTO: ')
        ano = input('DIGITE O ANO QUE DESEJA REALIZAR O EVENTO: ')
        if(dia.isnumeric() and mes.isnumeric() and ano.isnumeric()):
            dia = int(dia)
            mes = int(mes)
            ano = int(ano)

            anoBissexto = False
            if (ano % 100 == 0):
                if (ano % 400 == 0):
                    anoBissexto = True
            elif (ano % 4 == 4):
                anoBissexto = True
            if (ano >= 2024):
                if (dia >= 1 and dia <= 28 and mes >= 1 and mes <= 12):
                    print('DATA VALIDA')
                    break
                elif (dia == 29 and mes == 2 and anoBissexto):
                    print('DATA VALIDA')
                    break
                elif (dia >= 29 and dia <= 30 and mes != 2):
                    print('DATA VALIDA')
                    break
                elif (dia == 31 and (
                        mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12)):
                    print('DATA VALIDA')
                    break
                else:
                    print('DATA INVÁLIDA, VERIFIQUE-A E TENTE NOVAMENTE')
            else:
                print('ANO INVALIDO, INSIRA A DATA CORRETAMENTE!')
        else:
            print('DATA INVÁLIDA, VERIFIQUE-A E TENTE NOVAMENTE')
    while (True):
        hora=input('DIGITE O HORARIO QUE IRA ACONTECE O EVENTO: ')
        minuto=input('DIGITE O MINUTOS: ')
        if (hora.isnumeric() and minuto.isnumeric()):
            hora = int(hora)
            minuto = int(minuto)
            if(hora >= 0 and hora <=24 and minuto >= 0 and minuto <= 60):
                print('HORARIO VALIDO')
                break
            else:
                print('HORARIO INVALIDO !')
        else:
            print('HORARIO INVALIDO !')
    while (True):
        cdd = input('INFORME A CIDADE E O ESTADO QUE DESEJA REALIZAR O EVENTO (EX.: JOAO PESSOA(PB): ').upper().strip()
        if (cdd in cidadesDisp):
            print('CIDADE VALIDADA COM SUCESSO!')
            break
        else:
            print('CIDADE INVÁLIDA, CONFIRA SE NAO DIGITOU ALGO ERRADO')

    while (True):
        valorInscricao = float(input('INSIRA O VALOR DA INSCRIÇAO DO SEU EVENTO: '))
        if (valorInscricao >= 0):
            print('VALOR VALIDO')
            break
        else:
            print('VALOR INVALIDO, PORFAVOR DIGITE UM VALOR VALIDO!')
    events.append([titulo, descricao, gmail, [ cdd, valorInscricao], [dia, mes, ano,hora,minuto]])


def listar_eventos():
    listar=input('VOCE DESEJA VER TODOS OS EVENTOS(SIM OU NAO)?: ').upper()
    if(listar=='SIM'):
        for i in range(0, len(events)):
                print('NUMERO DO EVENTO', i + 1, 'º NOME DO EVENTO:', events[i][0], '\n''LOCAL:', events[i][3][0],
                      '\n''PREÇO:',
                      events[i][3][1], 'R$''\n''DATA:', events[i][4][0], '/', events[i][4][1], '/', events[i][4][2],'\nHORÁRIO: ',events[i][4][3],'H:',events[i][4][4],'MIN')
                print('------------------------------')
def login_eventos(lista, email):
    ind =-1
    for i in range(len(lista)):
        if (lista[i][2] == email):
            ind = i
            break
    if (ind != -1):
        print('---------------------------')
        print('LOGIN EFETUADO COM SUCESSO')
        print('---------------------------')
        return True
    else:
        return False

def verificar_nome(nome):
    if (len(nome) >= 3):
        return True
    else:
        return False

def verificar_email(email):
    if ('@gmail.com' in email or '@GMAIL.COM' in email):
        return True
    else:
        return False

def login(users, email, senha):
    ind = -1
    for i in range(len(users)):
        if (users[i][1] == email and users[i][2] == senha):
            ind = i
    if (ind != -1):
        print(f'LOGIN EFETUADO COM SUCESSO, SEJA BEM VINDO(A) {users[ind][0].upper()}')
        return users[ind]
    else:
        return ['', '', '']

def verificar_senha(senha1, senha2):
    if (senha1 == senha2 and len(senha1) >= 8 and len(senha2) >= 8):
        return True
    else:
        return False

def verificar_user_existente(email, usuarios):
    existe = False
    for user in usuarios:
        if (user[1] == email):
            existe = True
            break
    return existe
op = -1
while (op != 0):
    print('-----------------------------------')
    print('  SEJA BEM-VINDO AO GADELHAEVENTS  ')
    print('-----------------------------------')
    print('1-CRIAR CONTA NA PLATAFORMA ')
    print('2-EFETUAR LOGIN')
    print('0-SAIR DO PROGRAMA')

    print('-----------------------------------')
    opcoes = ['0','1','2']
    op = input('DIGITE A OPÇAO DESEJADA: ').strip()
    while(op not in opcoes):
        op = input('DIGITE UMA OPÇÃO VÁLIDA: ').strip()
    op = int(op)
    print('-----------------------------------')
    if (op == 1):
        nome1 = input('PORFAVOR, INSIRA SEU NOME COMPLETO: ').upper().strip()
        while (not verificar_nome(nome1)):
            print('NOME SO PODE TER 3 OU MAIS CARACTERES ')
            print('--------------------------------------')
            nome1 = input('PORFAVOR, INSIRA SEU NOME NOVAMENTE: ')
        email = input('DIGITE SEU EMAIL PRINCIPAL: ').strip()
        while (not verificar_email(email)):
            print('EMAIL INVALIDO!!')
            print('------------------------')
            email = input('PORFAVOR, INSIRA SEU EMAIL VALIDO: ').strip()
            while (verificar_user_existente(email, users)):
                print('------------------------------------')
                print('ESSE EMAIL JA ESTA SENDO UTILIZADO ')
                print('------------------------------------')
                email = input('PORFAVOR, INSIRA SEU EMAIL NOVAMENTE: ').strip()
        senha = input('DIGITE SUA SENHA COM 8 OU MAIS CARACTERES: ')
        senha2 = input('PORFAVOR, CONFIRME SUA SENHA: ')
        while (not verificar_senha(senha, senha2)):
            print('DESTA VEZ, DIGITE SENHAS QUE SEJAM IGUAIS E TENHAM 8 OU MAIS CARACTERES ')
            print('----------------------------------------------------------')
            senha = input('DIGITE SUA SENHA: ')
            senha2 = input('CONFIRME SUA SENHA: ')

        users.append([nome1, email, senha])

    elif(op == 2):
        email = input('DIGITE SEU EMAIL CADASTRADO: ')
        senha = input('DIGITE SUA SENHA: ')
        userAtual = login(users, email, senha)
        while (userAtual == ['','','']):
            print('ERRO!!! A SENHA OU O EMAIL ESTAO INCORRETOS')
            print('-----------------------------------')
            email = input('DIGITE SEU EMAIL: ')
            senha = input('DIGITE SUA SENHA: ')
            userAtual = login(users, email, senha)

        ope = -1
        while (ope != 0):
            print('---------------------------------------------------')
            print(f' OLA {userAtual[0].upper()}, O QUE VOCE GOSTARIA DE REALIZAR HOJE ')
            print('---------------------------------------------------')
            print('1-PARTICIPAR DE UM EVENTO')
            print('2-CRIAR UM EVENTO')
            print('3-MENU DE CRIADOR')
            print('4-VER LISTA DE EVENTOS')
            print('0-ENCERRAR SESSÃO')
            print('---------------------------------------------------')

            opcoes = ['0', '1', '2', '3', '4']
            ope = input('DIGITE A OPÇAO DESEJADA: ').strip()
            while (ope not in opcoes):
                ope = input('DIGITE UMA OPÇÃO VÁLIDA: ').strip()
            ope = int(ope)
            print('--------------------------------------------------')
            if(ope == 1):
                nome_e=buscar_eventos()
                nome = userAtual[0]
                gmail = userAtual[1]
                while (nome_e!='0' and not inscricao_eventos(nome,gmail,nome_e)):
                    nome_e = buscar_eventos()

            if (ope == 2):
                gmail = userAtual[1].strip()
                cadastrar_eventos(gmail)

            if (ope == 3):
                email = userAtual[1]
                if (not login_eventos(events, email)):
                    print('ERRO!!! VOCÊ NAO TEM NENHUM EVENTO CADASTRADO')
                    print('-------------------------------------------------------')
                    opi = 0
                else:
                    opi = -1
                while (opi != 0):
                    print(f'  OLA {userAtual[0].upper()} O QUE DESEJA FAZER HOJE: ')
                    print('1-REMOVER EVENTO')
                    print('2-LISTAR PARTICIPANTES DO EVENTO')
                    print('3-LISTAR DADOS DOS EVENTOS')
                    print('4-CALCULAR FINANÇAS')
                    print('0-VOLTAR PARA O MENU PRINCIPAL')

                    print('---------------------------------------------------')

                    opcoes = ['0', '1', '2', '3', '4']
                    opi = input('DIGITE A OPÇAO DESEJADA: ').strip()
                    while (opi not in opcoes):
                        opi = input('DIGITE UMA OPÇÃO VÁLIDA: ').strip()
                    opi = int(opi)
                    print('--------------------------------------------------')
                    if (opi == 1):
                        print('EVENTOS CADASTRADOS COM SEU GMAIL: ')
                        apagar_evento(userAtual[1])
                    if(opi == 2 ):
                        gmail = buscar_eventos_f_l(userAtual[1])
                    if(opi == 3 ):
                        gmail = dados_d_evento(userAtual[1])
                    if(opi==4):
                        gmail=calculadora_fin()
                    if(opi==0):
                        break

            if (ope == 4):
                listar_eventos()
    if(op == 0):
        print('PROGRAMA FECHADO')