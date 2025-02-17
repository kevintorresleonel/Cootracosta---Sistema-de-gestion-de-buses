import numpy as np

class Ruta:

    def __init__(self,ciudadOrigen,ciudadDestino,horaDeSalida:int,pasajePorPersona,numeroIdentificacionDelBus):
        self.ciudadOrigen = ciudadOrigen
        self.ciudadDestino= ciudadDestino
        self.horaDeSalida = horaDeSalida
        self.pasajePorPersona = pasajePorPersona
        self.numeroIdentificacionDelBus = numeroIdentificacionDelBus
        
    def MostrarRutas(self):
        for i in range(len(self.viajes)):
            for j in range(1):
                print("Ciudad origen: ",self.viajes[i][j],"| Ciudad destino: ", self.viajes[i][j+ 1], "| Hora de salida: ",self.viajes[i][j+2], "| Pasaje por persona: ",self.viajes[i][j+3], "| Número de identificación Interna del bus de esta ruta: ",self.viajes[i][j+4])

    def CambiarNumeroIdentificacionDelBus(self, numeroIdentificacioNuevo):
        setattr(self, "numeroIdentificacionDelBus", numeroIdentificacioNuevo)
    
    def ConseguirPasjePorPersona(self):
        getattr(self, "pasajePorPersona")