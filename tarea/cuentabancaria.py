from abc import ABC, abstractmethod

class CuentaBancaria(ABC):
    def __init__( self, titular, cbu, saldo_inicial=0):
        self.titular = titular
        self._cbu = cbu 
        self._saldo = 0
        self.saldo = saldo_inicial # validacion 

    @property
    def cbu(self):
        return self._cbu

    @property
    def saldo(self):
        return self._saldo


    @saldo.setter
    def saldo(self, valor):
        if valor < 0:
            raise ValueError("El saldo no puede ser menor a 0 (cero)")
        self._saldo = valor


    def depositar (self, monto):
        if monto > 0:
            self.saldo += monto
        else:
            print("El monto que vas a depositar tiene que ser mayor a 0 (cero)")

    def __str__(self):
        return f"[{self.__class__.__name__}] Titular: {self.titular} | CBU: {self.cbu} | Saldo: ${self.saldo}"
                
    @abstractmethod
    def extraer (self, monto):
        pass
