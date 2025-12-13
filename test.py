from main import *

conta_carlos = ContaCorrente('0001-9', 123456, 100, 500)

cliente_carlos = Cliente('Carlos', 23, conta_carlos)

banco_pan = Banco([cliente_carlos],[conta_carlos])

print(banco_pan.withdraw_bank(cliente_carlos, 100))
