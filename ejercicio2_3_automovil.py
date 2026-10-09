from enum import Enum


class TipoCombustible(Enum):
    GASOLINA = 1
    BIOETANOL = 2
    DIESEL = 3
    BIODIESEL = 4
    GAS_NATURAL = 5


class TipoAutomovil(Enum):
    CARRO_DE_CIUDAD = 1
    SUBCOMPACTO = 2
    COMPACTO = 3
    FAMILIAR = 4
    EJECUTIVO = 5
    SUV = 6


class Color(Enum):
    BLANCO = 1
    NEGRO = 2
    ROJO = 3
    NARANJA = 4
    AMARILLO = 5
    VERDE = 6
    AZUL = 7
    VIOLETA = 8


class Automovil:

    def __init__(self, marca, modelo, motor, tipo_combustible, tipo_automovil,
                 numero_puertas, cantidad_asientos, velocidad_maxima, color):
        self.marca = marca
        self.modelo = modelo
        self.motor = motor
        self.tipo_combustible = tipo_combustible
        self.tipo_automovil = tipo_automovil
        self.numero_puertas = numero_puertas
        self.cantidad_asientos = cantidad_asientos
        self.velocidad_maxima = velocidad_maxima
        self.color = color
        self.velocidad_actual = 0

    def get_marca(self):
        return self.marca

    def get_modelo(self):
        return self.modelo

    def get_motor(self):
        return self.motor

    def get_tipo_combustible(self):
        return self.tipo_combustible

    def get_tipo_automovil(self):
        return self.tipo_automovil

    def get_numero_puertas(self):
        return self.numero_puertas

    def get_cantidad_asientos(self):
        return self.cantidad_asientos

    def get_velocidad_maxima(self):
        return self.velocidad_maxima

    def get_color(self):
        return self.color

    def get_velocidad_actual(self):
        return self.velocidad_actual

    def set_marca(self, marca):
        self.marca = marca

    def set_modelo(self, modelo):
        self.modelo = modelo

    def set_motor(self, motor):
        self.motor = motor

    def set_tipo_combustible(self, tipo_combustible):
        self.tipo_combustible = tipo_combustible

    def set_tipo_automovil(self, tipo_automovil):
        self.tipo_automovil = tipo_automovil

    def set_numero_puertas(self, numero_puertas):
        self.numero_puertas = numero_puertas

    def set_cantidad_asientos(self, cantidad_asientos):
        self.cantidad_asientos = cantidad_asientos

    def set_velocidad_maxima(self, velocidad_maxima):
        self.velocidad_maxima = velocidad_maxima

    def set_color(self, color):
        self.color = color

    def set_velocidad_actual(self, velocidad_actual):
        self.velocidad_actual = velocidad_actual

    def acelerar(self, incremento):
        if self.velocidad_actual + incremento <= self.velocidad_maxima:
            self.velocidad_actual = self.velocidad_actual + incremento
        else:
            print("No se puede acelerar mas alla de la velocidad maxima del automovil.")

    def desacelerar(self, decremento):
        if self.velocidad_actual - decremento >= 0:
            self.velocidad_actual = self.velocidad_actual - decremento
        else:
            print("No se puede desacelerar a una velocidad negativa.")

    def frenar(self):
        self.velocidad_actual = 0

    def calcular_tiempo_llegada(self, distancia):
        if self.velocidad_actual == 0:
            print("El automovil esta detenido, no se puede calcular el tiempo.")
            return None
        return distancia / self.velocidad_actual

    def imprimir(self):
        print("Marca =", self.marca)
        print("Modelo =", self.modelo)
        print("Motor =", self.motor)
        print("Tipo de combustible =", self.tipo_combustible.name)
        print("Tipo de automovil =", self.tipo_automovil.name)
        print("Numero de puertas =", self.numero_puertas)
        print("Cantidad de asientos =", self.cantidad_asientos)
        print("Velocidad maxima =", self.velocidad_maxima)
        print("Color =", self.color.name)


auto1 = Automovil("Ford", 2018, 3, TipoCombustible.DIESEL, TipoAutomovil.EJECUTIVO,
                  5, 6, 250, Color.NEGRO)
auto1.imprimir()

auto1.set_velocidad_actual(100)
print("Velocidad actual =", auto1.get_velocidad_actual())

auto1.acelerar(20)
print("Velocidad actual =", auto1.get_velocidad_actual())

auto1.desacelerar(50)
print("Velocidad actual =", auto1.get_velocidad_actual())
print("Tiempo estimado para 300 km =", auto1.calcular_tiempo_llegada(300), "horas")

auto1.frenar()
print("Velocidad actual =", auto1.get_velocidad_actual())

auto1.desacelerar(20)
