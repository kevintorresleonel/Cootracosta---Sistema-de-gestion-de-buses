import numpy as np
from datetime import date

class Pasajero:

    def __init__ (self,nombre,fechaNacimiento,cedula,ciudadOrigen,ciduadDestino,horaDeSalida,puestosAComprar,efectivo):
        self.nombre = nombre
        self.fechaNacimiento = fechaNacimiento
        self.cedula = cedula 
        self.ciudadOrigen  = ciudadOrigen
        self.ciduadDestino = ciduadDestino
        self.horaDeSalida = horaDeSalida
        self.puestosAComprar = puestosAComprar
        self.efectivo = efectivo
        puestosEscogidos = []
        self.puestosEscogidos = puestosEscogidos
