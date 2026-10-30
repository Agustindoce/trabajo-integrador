from .cuentabancaria import CuentaBancaria

class CuentaCheque(CuentaBancaria):
    def __init__(self, titular, cbu, saldo_inicial=0, costo_emision=50):
        super().__init__(titular, cbu, saldo_inicial)
        self.costo_emision = costo_emision

    def extraer(self, monto):
        if (monto + self.costo_emision) <= self.saldo:
            self.saldo -= (monto + self.costo_emision)
        else:
            print("Fondos insuficientes para cubrir el monto y la comision.")