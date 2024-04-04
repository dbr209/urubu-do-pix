from sys import exit
from os import system as os_system
from platform import system as plataform_system

import user
import transacao

conta = user.Conta()

def menu():

    clear_screen()

    while True:

        destino = int(input('''[ 1 ] Cadastrar Conta\n[ 2 ] Login\n[ 3 ] Sair\n\nDigite o número referente a sua ação: '''))

        if destino == 1:
           clear_screen()
           conta.criar_conta()
        elif destino == 2:
            login = conta.login()
            if login != 0:
                return interface(login)
        elif destino == 3:
            break
        else:
            print('Entrada Inválida')

def interface(info):

    banco = transacao.Banco(info[0], info[1], info[2])

    while True:

        clear_screen()

        print('='*19, 'INFO', '='*19)
        print(f'Conta: {banco.name}')
        print(f'Saldo: {banco.saldo}')

        banco.historico()
        
        escolha = str(input('[ 1 ] Retirar Valor\n[ 2 ] Sair\n\nInforme o que deseja fazer: ' if banco.infos != None else '[ 1 ] Investir Valor\n[ 2 ] Sair\n\nInforme o que deseja fazer: ')) 
        if escolha == '1':
            if banco.infos == None:
                banco.investir()
            elif banco.infos != None:
                banco.retirar_valor()
        elif escolha == '2':
            return menu()
        else:
            clear_screen()
            print('Entrada Inválida\n')

def clear_screen():
    if plataform_system() == 'Windows':
        os_system('cls') or None
    else:
        os_system('clear')


menu()
