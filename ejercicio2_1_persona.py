class Persona:

    def __init__(self, nombre, apellidos, numero_documento, anio_nacimiento):
        self.nombre = nombre
        self.apellidos = apellidos
        self.numero_documento = numero_documento
        self.anio_nacimiento = anio_nacimiento

    def imprimir(self):
        print("Nombre =", self.nombre)
        print("Apellidos =", self.apellidos)
        print("Numero de documento de identidad =", self.numero_documento)
        print("Año de nacimiento =", self.anio_nacimiento)
        print()


p1 = Persona("Pedro", "Pérez", "1053121010", 1998)
p2 = Persona("Luis", "León", "1053223344", 2001)

p1.imprimir()
p2.imprimir()
