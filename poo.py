class CuentaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, monto):
        if monto > 0:
            self.saldo += monto
            print(f"Deposito de ${monto} realizado.")
        else:
            print("El monto debe ser mayor a 0.")
        
    def retirar(self, monto):
        if monto > self.saldo:
            print("Fondos insuficientes.")
        elif monto <= 0:
            print("El monto deber ser mayor a 0.")
        else:
            self.saldo -= monto
            print(f" Retiro de ${monto} realizado.")
    
    def mostrar_saldo(self):
        print(f"Titular: {self.titular} | Saldo actual: ${self.saldo}")

# Programa principal
print("=== Sistema Bancario ===")

cuenta1 = CuentaBancaria("Alan" , 1000000)

cuenta1.mostrar_saldo()
cuenta1.depositar(500)
cuenta1.retirar(200)
cuenta1.retirar(2000)  # prueba de error
cuenta1.mostrar_saldo()
