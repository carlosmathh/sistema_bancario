from main import *

conta_carlos = CurrentAccount('0001-9', 123456, 100, 500)

cliente_carlos = Client('Carlos', 23, conta_carlos)

banco_pan = Bank([cliente_carlos],[conta_carlos])

print(banco_pan.withdraw_bank(cliente_carlos, 100))
