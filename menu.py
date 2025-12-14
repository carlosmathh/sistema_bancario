from main import *

conta_carlos = CurrentAccount('0001-9', 12345, 100, 500)

cliente_carlos = Client('Carlos', 23, conta_carlos)

banco_nubank = Bank([cliente_carlos],[conta_carlos])

def deposit():
    value = float(input('Qual valor deseja sacar? '))
    banco_nubank.deposit_bank(cliente_carlos, value)
    return f'Seu saldo agora é: {conta_carlos.balance}'

def withdraw():
    print(f'Saldo: {conta_carlos.balance} limite de crédito: {conta_carlos.credit_limit}')
    value = float(input('Qual valor deseja sacar? '))
    banco_nubank.withdraw_bank(cliente_carlos, value)
    return f'Seu saldo {conta_carlos.balance}'

def exit_():
    print('Obrigado e volte sempre ;)')
    exit()


options = {
    'D': deposit,
    'S': withdraw,
    'X': exit_
}


while True:
    choise = input('Depositar(D) | Sacar(S) | Sair(X) ').upper()

    action = options.get(choise)

    if action:
        try:
            action()
        except ValueError as e:
            print(f'Error: {e}')
    else:
        print('Opção inválida')
