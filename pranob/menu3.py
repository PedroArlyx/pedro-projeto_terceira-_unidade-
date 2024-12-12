def calculadora_financeira():
    while(True):
        while (True):
            receit = input('DIGITE A RECEITA DO SEU EVENTO: ').replace(',', '.')
            if (receit.replace('.', '').isnumeric()):
                receit = float(receit)
                if (receit >= 0):
                    print('VALOR VALIDO')
                    break
                else:
                    print('VALOR INVALIDO, PORFAVOR DIGITE UM VALOR VALIDO!')
            else:
              print('VALOR INVALIDO, PORFAVOR DIGITE UM VALOR VALIDO!')

        while (True):
            gastos = input('DIGITE QUANTO VOCE GASTOU PARA CRIAR O EVENTO: ').replace(',', '.')
            if (gastos.replace('.', '').isnumeric()):
                gastos = float(gastos)
                if (gastos >= 0):
                    print('VALOR VALIDO')
                    break
                else:
                    print('VALOR INVALIDO, PORFAVOR DIGITE UM VALOR VALIDO!')
            else:
              print('VALOR INVALIDO, PORFAVOR DIGITE UM VALOR VALIDO!')

        lucroTotal=receit-gastos
        if (lucroTotal >= 0):
            print(f'O SEU LUCRO FOI {lucroTotal}')
        else:
            print(f'INFELIZMENTE VOCE TEVE UM PREJUIZO DE {lucroTotal * -1}')

        porc=input('DESEJA VER A PORCENTAGEM DE GASTOS?').lower().strip()
        if(porc=='sim'):
            porcentagem = (gastos / receit) * 100
            print(f'ESSA FOI A PORCENTAGEM DE GASTOS {porcentagem} %')
        porcentagem2=input('DESEJA VER EM FORMA DE PORCENTAGEM OS SEUS LUCROS?').lower().strip()
        if(porcentagem2=='sim'):
            porcentagemLu = (lucroTotal / receit) * 100
            print(f'ESSA FOI A PORCENTAGEM DE LUCROS {porcentagemLu} %')

        exit=input('DESEJA CONTINUAR NA CALCULADORA? ("SIM" PARA CONTINUAR, OUTRA TECLA PARA SAIR)').lower().strip()
        if(exit!='sim'):
            break

def dados_dos_eventos(email, events):
    lupa = email
    existe = False
    evento = 0
    valor = 0
    for i in range(0, len(events)):
        if (lupa == events[i][2]):
            print('NUMERO DO EVENTO', i + 1, 'º NOME DO EVENTO: ', events[i][0], '\n''LOCAL:', events[i][3][0],
                  '\n''PREÇO:',
                  events[i][3][1], 'R$' '\n''DATA:', events[i][4][0], '/', events[i][4][1], '/', events[i][4][2],
                  '\nHORÁRIO: ',events[i][4][3],'H',events[i][4][4],'MIN')
            print('PESSOAS INSCRITAS NOS EVENTOS: ')
            for j in range(5, len(events[i])):
                print(f'NOME: {events[i][j][0]}')
                print(f'EMAIL: {events[i][j][1]}')
                print('------------------------------')
            valor = (float(events[i][3][1]) * (len(events[i]) - 5))
            print(f'NUMERO DE PARTICIPANTES: {len(events[i]) - 5} ')
            print(f'VALOR ARRECADADO: R$ {valor}')
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
def buscar_eventos_f_l(email, events):
    lupa = email
    existe = False
    evento = 0
    for i in range(0,len(events)):
        if(lupa == events[i][2]):
             print('NUMERO DO EVENTO',i+1,'º NOME DO EVENTO: ', events[i][0], '\n''LOCAL:',events[i][3][0], '\n''PREÇO: R$ ',
                      events[i][3][1],'\n''DATA:',events[i][4][0],'/',events[i][4][1],'/',events[i][4][2],
                   '\nHORÁRIO: ',events[i][4][3],'H',events[i][4][4],'MIN')
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

def apagar_evento(gmail, events):
    for i in range(len(events)):
        if (gmail == events[i][2]):
            print('NUMERO DO EVENTO', i + 1, 'º NOME DO EVENTO: ', events[i][0], '\n''LOCAL:', events[i][3][0],
                  '\n''PREÇO:',
                  events[i][3][1], 'R$''\n''DATA: ', events[i][4][0], '/', events[i][4][1], '/', events[i][4][2],
                  '\nHORÁRIO: ',events[i][4][3],'H',events[i][4][4],'MIN')
            print('------------------------------')
            print('EVENTO ENCONTRADO COM SUCESSO!')
            resposta = input('DIGITE O NUMERO DO EVENTO QUE DESEJA APAGAR PARA CONFIRMAR OU OUTRA TECLA PARA CANCELAR E IR PARA O PRÓXIMO EVENTO: ').upper().strip()
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
def buscar_eventos_f(email, events):
    existe = False
    evento = 0
    while(True):
        lupa = email
        for i in range(0,len(events)):
            if(lupa == events[i][2]):
             print('NUMERO DO EVENTO',i+1,'º NOME DO EVENTO: ',events[i][0], '\n''LOCAL:',events[i][3][0], '\n''PREÇO:',
                      events[i][3][1],'R$''\n''DATA: ',events[i][4][0],'/',events[i][4][1],'/',events[i][4][2],
                   '\nHORÁRIO: ',events[i][4][3],'H',events[i][4][4],'MIN')
             print('------------------------------')
             print('EVENTO ENCONTRADO COM SUCESSO!')

             existe = True
             email = events[i][2]
        if(not existe):
            print('EVENTO INVALIDO, CONFIRA O EMAIL DO RESPONSAVEL PELO EVENTO NOVAMENTE!')
        else:
         return evento