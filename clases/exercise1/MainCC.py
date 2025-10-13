# Importamos CuentaCorriente
from CuentaCorriente import CuentaCorriente

# Función principal
def main():
    # Creamos dos cuentas
    cc1 = CuentaCorriente("12345678A", 1000, "Juan")
    cc2 = CuentaCorriente("87654321B", 500)

    # Mostramos cuentas
    print(cc1)
    print(cc2)

    # Probamos extracción
    if cc1.withdraw(200):
        print("Withdrawal successful")
    else:
        print("Insufficient funds")

    # Ingreso en cc2
    if cc2.deposit(500): 
        print("Deposit successful")
    
    # Extracción en cc2
    if cc2.withdraw(300):
        print("Withdrawal successful")
    else:
        print("Insufficient funds")
    
    # Otro ingreso
    if cc2.deposit(500):
        print("Deposit successful")
    
    # Comparamos si son la misma cuenta
    if cc1 == cc2:
        print("The accounts are the same")
    else:
        print("The accounts are different")
    
    # Comparamos saldos
    if cc1 < cc2:
        print("Account 1 has less balance than Account 2")
    else:
        print("Account 1 has more or equal balance than Account 2")

    # Ordenamos cuentas por saldo
    ccs = [cc1, cc2]
    ccs.sort()
    print("Accounts sorted by balance:")
    for cc in ccs:
        print(cc)