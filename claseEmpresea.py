import numpy as np
from claseBus import Bus
from claseRuta import Ruta
from clasePasajero import Pasajero
from datetime import date

class Empresa:
    
    def __init__(self, nombre:str):
        self.nombre = nombre
        self.buses = []
        self.rutas = []
        self.pasajero = []
        self.ciudadesDeOperacion = ("Santa Marta","Barranquilla","Monteria","Riohacha","Sincelejo","Valledupar","Cartagena")

    def RegistrarBus(self, i:Bus):
        busAgregado = False
        self.buses.append(i)
        busAgregado = True
        return busAgregado

    def MostrarBuses(self):
        pass

    def RegistrarRuta(self, ruta:Ruta):
        rutaAgregada = False
        self.rutas.append(ruta)
        rutaAgregada= True
        return rutaAgregada

    def BuscarRuta(self, ciudadOrigen, ciudadDestino, horaDeBusqueda):
        numRuta = []
        numBus = []
        for ruta in self.rutas:
            if ruta.ciudadOrigen == ciudadOrigen and ruta.ciudadDestino == ciudadDestino and ruta.horaDeSalida > horaDeBusqueda:
                #print(ruta.ciudadOrigen, "-", ruta.ciudadDestino, "-", ruta.horaDeSalida,"-",ruta.pasajePorPersona)
                for i in range(len(self.buses)):
                    if ruta.numeroIdentificacionDelBus == self.buses[i].numeroIdentificacion:
                        #print("Bus para esta ruta:")
                        #print(self.buses[i].numeroIdentificacion,"-",self.buses[i].placa,"-",self.buses[i].conductor)
                        #print("Cantidad de puestos disponibles para esta ruta:",self.buses[i].puestosDisponibles()
                        numBus.append(int(i))
                        numRuta.append(self.rutas.index(ruta))
        return numRuta, numBus
    
    def BuscarBusYPuestoDisponbles(self, numeroIdentificacion):
        numBus = 0
        for i in self.buses:
            if i.numeroIdentificacion == numeroIdentificacion:
                numBus = self.buses.index(i)
        return numBus

    def RegistrarPasajero(self, pasajero:Pasajero):
        pasajeroAgregado = False
        self.pasajero.append(pasajero)
        pasajeroAgregado = True
        return pasajeroAgregado

    def conseguirPasajeDeLaRuta(self, ciudadOrigen, ciudadDestino, horaDeSalida):
        pasajeRuta = 0
        for ruta in self.rutas:
            if ruta.ciudadOrigen == ciudadOrigen and ruta.ciudadDestino == ciudadDestino and ruta.horaDeSalida == horaDeSalida:
                pasajeRuta = ruta.ConseguirPasjePorPersona()
        return pasajeRuta

    def sacarDescuento(self):
        totalDinero = 0
        pasaje = self.conseguirPasajeDeLaRuta(self.pasajero[0].ciudadOrigen, self.pasajero[0].ciudadDestino, self.pasajero[0].horaDeSalida)
        puestosAComprar = self.pasajero[0].puestosAComprar
        if puestosAComprar >= 3:
            for pasaje in range(1, puestosAComprar + 1):
                if pasaje >= 3:
                    descuento = 0.5 * pasaje
                    totalDinero += descuento 
                else:
                    totalDinero += pasaje
        else:
            totalDinero = puestosAComprar * pasaje
        return totalDinero

    def sacarVuelto(self):
        vuelto = self.pasajero[0].efectivo - self.sacarDescuento()
        if vuelto < 0:
            vuelto = 0
        return vuelto

    def evaluarDescuento(self, cantidadPuestos):
        cantidadPuestos = cantidadPuestos
        totalPago = self.sacarDescuento()
        pasaje = self.conseguirPasajeDeLaRuta(self.pasajero[0].ciudadOrigen, self.pasajero[0].ciudadDestino, self.pasajero[0].horaDeSalida)
        totalDescuento = (100*totalPago)/(cantidadPuestos*pasaje)
        DescuentoAplicado = round((100 - totalDescuento),2)
        return DescuentoAplicado

    def pagoSinDescuento(self, cantidadPuestos):
        pasaje = self.conseguirPasajeDeLaRuta(self.pasajero[0].ciudadOrigen, self.pasajero[0].ciudadDestino, self.pasajero[0].horaDeSalida)
        pago = pasaje * cantidadPuestos
        return pago

    def BuscarRutaYHora(self, ciudadOrigen, ciudadDestino, horaDeSalida):
        numeroBus = 0
        for ruta in self.rutas:
            if ruta.ciudadOrigen == ciudadOrigen and ruta.ciudadDestino == ciudadDestino and ruta.horaDeSalida == horaDeSalida:
                for i in range(len(self.buses)):
                    if ruta.numeroIdentificacionDelBus == self.buses[i].numeroIdentificacion:
                        numeroBus = i
        return numeroBus

    def ObtenerCantidadDePuestoVendidosPorRuta(self):
        listaRutas = []
        for ruta in self.rutas:
            for i in range(len(self.buses)):
                if ruta.numeroIdentificacionDelBus == self.buses[i].numeroIdentificacion:
                    puestosOcupados = 40 - self.buses[i].puestosDisponibles()
                    listaRutas.append([ruta.ciudadOrigen,ruta.ciudadDestino,ruta.horaDeSalida,puestosOcupados])
        return listaRutas

    def OrdenarCiudadesPorPuestosVendidos(self):
        listasRutas = self.ObtenerCantidadDePuestoVendidosPorRuta()
        cantidadRutas = len(listasRutas)
        for i in range(0, cantidadRutas):
            for j in range(0, cantidadRutas - 1):
                    if listasRutas[j][3] > listasRutas[j+1][3]:
                        temporal = listasRutas[j]
                        listasRutas[j] = listasRutas[j+1]
                        listasRutas[j+1] = temporal
        return listasRutas

    def CambiarNumeroIdentificacion(self, numeroIdentificacion, nuevoNumeroIdentifiacion):
        for buses in self.buses:
            if  buses.numeroIdentificacion == numeroIdentificacion:
                buses.CambiarNúmeroIdentificación(nuevoNumeroIdentifiacion)

    def CambiarPlacaDelBus(self, placaVieja, placaNueva):
        cambio = False
        for buses in self.buses:
            if buses.placa == placaVieja:
                buses.CambiarPlacaDelBus(placaNueva)
                cambio = True
        return cambio

    def CambiarNombreDelConductor(self, nombreAntiguo, nombreNuevo):
        cambio = False
        for buses in self.buses:
            if buses.conductor == nombreAntiguo:
                buses.CambiarConductorDelBus(nombreNuevo)
                cambio = True
        return cambio

    def es_bisiesto(self,añoNacimiento) -> bool:
        year = añoNacimiento
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

    def obtener_dias_del_mes(self,añoNacimiento,mesNacimiento) -> int:
        month = mesNacimiento
        if month in [4, 6, 9, 11]:
            return 30
    # Febrero depende de si es o no bisiesto
        if month  == 2:
            if self.es_bisiesto(añoNacimiento):
                return 29
            else:
                return 28
        else:
            return 31

    def CalculoEdad(self,añoNacimiento,mesNacimiento,diaNacimiento):

        fechaDeHoy = date.today() 
        limiteDias = self.obtener_dias_del_mes(añoNacimiento,mesNacimiento)
        edad = None
        restar = 0
        if ((añoNacimiento >= 1900 and añoNacimiento <= fechaDeHoy.year) and (mesNacimiento >= 1 and mesNacimiento <= 12) 
            and (diaNacimiento>=1 and diaNacimiento <= limiteDias)):
            diferenciaDeAños = fechaDeHoy.year - añoNacimiento
            diferenciaDeMeses = fechaDeHoy.month - mesNacimiento
            diferenciaDeDías = fechaDeHoy.day - diaNacimiento
            if diferenciaDeMeses < 0 or (diferenciaDeMeses==0 and diferenciaDeDías < 0):
                restar = 1
            edad = diferenciaDeAños - restar
            return edad
        else:
            return edad 



            