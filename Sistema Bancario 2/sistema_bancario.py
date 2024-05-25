import os
from time import sleep
entrar_conta = ''
Clientes = list()
pessoa = dict()
def Titulo(texto):
    print(' '*10,'--'*30)
    print(texto.center(80,' ').upper())    
    print(' '*10,'--'*30)
    print()
def Entrar(NumeroC, lst):
    for i, v in enumerate(lst):
        if lst[i]['Numero_conta'] == NumeroC:
            print('Conta localizada')
            return 'Conta localizada'
            break
    else:
        print('Conta não localizada!')
        return 'Conta não locaizada'
def Criar_conta(dicionario):
    from random import randint
    pessoa['Nome'] = str(input('Informe seu nome: '))
    pessoa['Contato'] = int(input('Informe seu numero de telefone: '))
    pessoa['Numero_conta'] = randint(10000,99999)
    pessoa['Saldo'] = 0
    print()
    print('>Conta criada com SUCESSO!<')
    print(f'Numero da sua conta: {pessoa["Numero_conta"]}')
def Deposito(ValorD,saldo):
    saldo = saldo + ValorD
    print('Deposito feito com sucesso! ')
    return saldo
def Saque(Saldo):
    ValorS = int(input('Informe o valor do saque: '))
    if Saldo < ValorS:
        print('Ops! Seu saldo esta a baixo do valor desejado para saque.')
    elif ValorS > 500:
        print('Ops! Você só pode sacar um valor até R$500')
    else:
        Saldo = Saldo - ValorS
        return Saldo


while True:
    Titulo('Sistema bancario')
    print()
    print('[1]ENTRAR\n[2]CRIAR CONTA\n[3]SAIR')
    op = int(input('  =>'))
    if op == 1:
        Numero_conta = int(input('Informe o numero da conta: '))
        entrar_conta = Entrar(NumeroC = Numero_conta,lst = Clientes)
        if entrar_conta == 'Conta localizada':
            os.system('cls')
            print('ENTRANDO...'.center(60,' '))
            sleep(2)
            os.system('cls')
            break
        else:
            limpartela = input('PRECIONE ENTER PARA VOLTAR...')
            os.system('cls')
    elif op == 2:
        
        Criar_conta(pessoa)
        Clientes.append(pessoa.copy())
        print(Clientes)
        pessoa.clear()
        limpartela = input('PRECIONE ENTER PARA VOLTAR...')
        os.system('cls')
    elif op == 3:
        break
    else:
        print('ERRO! opição invalida, tente novamente.')
if entrar_conta == 'Conta localizada':
    for i, v in enumerate(Clientes):
        if Clientes[i]['Numero_conta'] == Numero_conta:
            print(f'Olá {Clientes[i]['Nome']}')
    while True:
        print()
        print('-'*10)
        print('MENU'.center(10,' '))
        print('-'*10)
        print('[1]DEPOSITO\n[2]SAQUE\n[3]SALDO\n[4]EXTRATO\n[5]SAIR')
        op = int(input('  =>'))
        if op == 1:
            valor_deposito = int(input('Valor do deposito:'))
            #Vai procurar o saldo o cliente para depositar um valor
            for i, v in enumerate(Clientes):
                if Clientes[i]['Numero_conta'] == Numero_conta:
                    Clientes[i]['Saldo'] = Deposito(ValorD=valor_deposito,saldo = Clientes[i]['Saldo'])
            limpartela = input('PRECIONE ENTER PARA VOLTAR...')
            os.system('cls')
            print(Clientes)
        elif op == 2:
            #Vai procurar o saldo do cliente para sacar um valor
            for i, v in enumerate(Clientes):
                if Clientes[i]['Numero_conta'] == Numero_conta:
                    Clientes[i]['Saldo'] = Saque(Saldo =Clientes[i]['Saldo'])
            limpartela = input('PRECIONE ENTER PARA VOLTAR...')
            os.system('cls')
        elif op == 5:
            break
        elif op == 3:
            for i, v in enumerate(Clientes):
                if Clientes[i]['Numero_conta'] == Numero_conta:
                    print(f'Ola {Clientes[i]['Nome']}, Seu saldo atual é de: \n\nR${Clientes[i]['Saldo']}')
            limpartela = input('PRECIONE ENTER PARA VOLTAR...')
            os.system('cls')
        elif op == 4:
            print('Sem extrato!')
print('Operação encerrada com sucesso! \nNosso sistema sempre com você!')

#Esse codigo esta dando alguns erros, já estou trabalhando nisso para melhorar!