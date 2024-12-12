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

def login(users, email, senha):
    ind = -1
    for i in range(len(users)):
        if (users[i][1] == email and users[i][2] == senha):
            ind = i
    if (ind != -1):
        print(f'LOGIN EFETUADO COM SUCESSO, SEJA BEM VINDO(A) {users[ind][0].upper()}')
        return users[ind]
    else:
        return False