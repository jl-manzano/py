from CuentaCorriente import CuentaCorriente

def main():
    cc1 = CuentaCorriente("12345678A", 1000, "Juan")
    cc2 = CuentaCorriente("87654321B", 500)

    print(cc1)
    print(cc2)

    if cc1.withdraw(200):
        print("Withdrawal successful")
    else:
        print("Insufficient funds")

    if cc2.deposit(500): 
        print("Deposit successful")
    
    if cc2.withdraw(300):
        print("Withdrawal successful")
    else:
        print("Insufficient funds")
    
    if cc2.deposit(500):
        print("Deposit successful")
    
    if cc1 == cc2:
        print("The accounts are the same")
    else:
        print("The accounts are different")
    
    if cc1 < cc2:
        print("Account 1 has less balance than Account 2")
    else:
        print("Account 1 has more or equal balance than Account 2")
        
if __name__ == "__main__":
    main()