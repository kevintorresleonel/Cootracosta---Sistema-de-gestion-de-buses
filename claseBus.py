import numpy as np

class Bus:
      
    def __init__(self,numeroIdentificacion,placa,conductor):
        self.numeroIdentificacion = numeroIdentificacion
        self.placa = placa
        self.conductor = conductor
        self.filas = 4
        self.columnas = 10
        self.letras = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J")
        self.puestos = np.full((self.filas,self.columnas), "Disponible",object)

    def CambiarPuestos(self):
        for i in range(len(self.puestos)):
            for j in range(len(self.letras)):
                if self.puestos[i][j] != "Ocupado":
                    puesto = i+1
                    self.puestos[i][j] = self.letras[j], puesto
        return self.puestos
    
    def ModificarPuesto(self, fila, columna):
        if self.puestos[fila][columna] != "Ocupado":
            self.puestos[fila][columna] = "Ocupado"
            print("Puesto vendido con éxito")
            return True
        else:
            print("Puesto ocupado")
            return False 
    
    def puestosDisponibles(self):
        asientosVendidos=0
        for fila in range(0, self.filas):
            for columna in range(0, self.columnas):
                if self.puestos[fila][columna] != "Ocupado": 
                    asientosVendidos+=1
        return asientosVendidos

    def CambiarNúmeroIdentificación(self, nuevoNumeroIdentificación):
        setattr(self, "numeroIdentificacion", nuevoNumeroIdentificación)

    def CambiarPlacaDelBus(self, nuevaPlaca):
        setattr(self, "placa", nuevaPlaca)

    def CambiarConductorDelBus(self, nombreNuevo):
        nombreNuevo = nombreNuevo.title()
        setattr(self, "conductor", nombreNuevo) 