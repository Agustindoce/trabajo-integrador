from .cuentabancaria import CuentaBancaria

class CuentaAhorro(CuentaBancaria):
    def extraer(self, monto):
        if monto <= self.saldo:
            self.saldo -= monto
        else:
            print("Fondos insuficientes en Cuenta Ahorro.")

    def aplicar_interes(self):
        self.saldo += self.saldo * 0.001