from enum import Enum


class TipoCuenta(Enum):
    AHORROS = 1
    CORRIENTE = 2


class CuentaBancaria:

    def __init__(self, nombres_titular, apellidos_titular, numero_cuenta, tipo_cuenta):
        self.nombres_titular = nombres_titular
        self.apellidos_titular = apellidos_titular
        self.numero_cuenta = numero_cuenta
        self.tipo_cuenta = tipo_cuenta
        self.saldo = 0

    def imprimir(self):
        print("Titular =", self.nombres_titular, self.apellidos_titular)
        print("Numero de cuenta =", self.numero_cuenta)
        print("Tipo de cuenta =", self.tipo_cuenta.name)
        print("Saldo =", self.saldo)

    def consultar_saldo(self):
        return self.saldo

    def consignar(self, valor):
        self.saldo = self.saldo + valor

    def retirar(self, valor):
        if valor > self.saldo:
            print("No se puede retirar, el valor supera el saldo de la cuenta.")
        else:
            self.saldo = self.saldo - valor


cuenta1 = CuentaBancaria("Carlos", "Gómez", 123456, TipoCuenta.AHORROS)
cuenta1.imprimir()

cuenta1.consignar(500000)
print("Saldo despues de consignar =", cuenta1.consultar_saldo())

cuenta1.retirar(200000)
print("Saldo despues de retirar =", cuenta1.consultar_saldo())

cuenta1.retirar(1000000)
print("Saldo final =", cuenta1.consultar_saldo())
