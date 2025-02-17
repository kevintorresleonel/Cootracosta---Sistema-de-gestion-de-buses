from time import sleep
from claseBus import Bus
from claseEmpresea import Empresa
from clasePasajero import Pasajero
from claseRuta import Ruta
from datetime import datetime, date

empresaCootracosta = Empresa("Cootracosta")
print("-----------------------------------------------------")
print("-----------------------------------------------------")
print(" ~~~~~~~~~~~~~BIENVENIDO A COOTRACOSTA ~~~~~~~~~~~~~~")
print("                                 ___ ")
print("---------------------------------'  |----------------")
print("--------/| _ .---. .---. .---. .---.|----------------")
print("--------|j||||___| |___| |___| |___||----------------")
print("--------|=|||=======================|----------------")
print("--------[_|j||(O)\__________|(O)\___]----------------")
print("-----------------------------------------------------")
menú = 0
while menú == 0:
    print(" ¿Que desea hacer?")
    print("-------------------------")
    print("Menu de opciones")
    print("-------------------------")
    print("1. Registrar un nuevo Bus")
    print("2. Mostrar buses registrados ")
    print("3. Registrar nueva ruta ")
    print("4. Mostrar rutas registradas")
    print("5. Buscar ruta especifica y sus puestos disponibles.")
    print("6. Ver puestos disponibles de un bus específico.")
    print("7. Vender un puesto y ver resumen de la venta.")
    print("8. Ordenar rutas de acuerdo a la cantidad de pasajes vendidos")
    print("9. Modificar los datos de un bus ya registrado.")
    print("Salir del Programa.")
    print("------------------------------------------------------------------")
    opcion = int(input("Por favor, ingrese una de las opciones disponibles: "))
    print("------------------------------------------------------------------")
 
    if opcion == 1: 
        print("Registrar un nuevo Bus ")
        y = True
        while y :
          try:
                numeroIdentificacion= input("Ingrese el numero de indentificacion interna del bus: ")
                
                if len(numeroIdentificacion) == 4 and int(numeroIdentificacion) :
                    
                    while y:

                        placa = input("Ingrese la placa del bus: ")

                        if len(placa) == 5  and placa.isalnum():

                            while y:


                             conductor = input("Ingrese el nombre y apellido del conductor: ")
                             conductor = conductor.title()

                             if conductor.isalnum() is False and len(conductor) != 0 :
                                    
                                    empresaCootracosta.RegistrarBus(Bus(numeroIdentificacion,placa,conductor))
                                    print("")
                                    print(" ✨ Bus ingresado con éxito ✨ ")
                                    print("")
                                    y = False

                             else:
                                print("no ingrese numeros o dejes la casilla vacia ")
                                
                        else:
                            print("no ingreses mas o menos de 5 elementos o dejes la casilla vacia y la placa tiene que ser una combinacion alfanumerica")

                else:
                    print("no ingreses mas o menos de 4 elementos, tampoco letras o dejes la casilla vacia ")
          except:
            print("no ingreses letras (agregar errores anteriores en este print")

    elif opcion ==2:
        numeroBus = 0
        if len(empresaCootracosta.buses) != 0:

            while numeroBus < len(empresaCootracosta.buses):
                    print("Bus", numeroBus+1)
                    print("Num. Identificacion interna: ",empresaCootracosta.buses[numeroBus].numeroIdentificacion, "| numero de placa :",empresaCootracosta.buses[numeroBus].placa,"| nombre del conductor:",empresaCootracosta.buses[numeroBus].conductor)
                    numeroBus += 1
        else:
            print("no hay buses registrados, por favor, registra al menos uno ")

    elif opcion == 3:
    
     if len(empresaCootracosta.buses) != 0:
        print("Registrar una nueva ruta")
        h = True
        while h:
                     
                ciudadOrigen= input("Ingrese la ciudad de origen: ")
                ciudadOrigen = ciudadOrigen.title()
        
                if ciudadOrigen in empresaCootracosta.ciudadesDeOperacion :

                    while h:

                        ciudadDestino = input("Ingrese la ciudad de destino: ")
                        ciudadDestino = ciudadDestino.title()
                        if ciudadDestino in empresaCootracosta.ciudadesDeOperacion  and ciudadDestino != ciudadOrigen:
                        
                         while h:
                            try:
                                horaDeSalida = int(input("Ingrese  la hora de salida: "))
                            
                                if 0 <= horaDeSalida <= 23 and int(horaDeSalida) and  len(str(horaDeSalida)) != 0 :

                                    while h:
                                      try:
                                        pasajePorPersona = int(input("Ingrese el pasaje por persona: "))

                                        if int(pasajePorPersona) and 15000 <= pasajePorPersona <= 50000 and len(str(pasajePorPersona)) != 0:

                                            while h:
                                                 try:
                                                    numeroIdentificacion = input("Número de identificación del bus para esta ruta: ")
                                        
                                                    for buses in empresaCootracosta.buses: 

                                                     if int(numeroIdentificacion) and len(numeroIdentificacion) !=0 and buses.numeroIdentificacion == numeroIdentificacion:

                                                            empresaCootracosta.RegistrarRuta(Ruta(ciudadOrigen,ciudadDestino,horaDeSalida,pasajePorPersona,numeroIdentificacion))
                                                            print("")
                                                            print(" ✨ Ruta ingresada con éxito ✨ ")
                                                            print("")
                                                            h = False

                                                     else: 
                                                      print("no ingrese letra, tampoco dejes la casilla vacia o el numero de identificacion debe concordar con algun bus ya registrado")

                                                 except:
                                                    print(" metedo rutina")
                                        
                                        else:
                                            print("no ingrese letas, tampoco dejes la casilla vacia y el valor del pasaje se deben de encontrar entre 15000 y 50000 ")

                                      except:
                                       print("No ingreses letras")
                                else:
                                  print("no dejes la casilla vacia tanpoco ingrese letras y la hora se tiene que encontrar entre 0 y 23")
                                  
                            except:
                                print("No ingreses letras")
                               
                        else:
                            print("no ingrese numeros ,no dejes la casilla vacia,  tampoco ingrese una ciudad que no se encuentre entre las disponibles y debe ser distinta a la ciudad de origen  ")

                else:
                    print("no ingrese numeros ,no dejes la casilla vacia,  tampoco ingrese una ciudad que no se encuentre entre las disponibles")
                
     else:
        print("debe ingresar primero al menos un bus")
         
    
    elif opcion == 4:
        numeroRuta = 0
        if len(empresaCootracosta.rutas) != 0:

            while numeroRuta < len(empresaCootracosta.rutas):
                print("Ruta", numeroRuta+1)
                print("ciudad de origen:",empresaCootracosta.rutas[numeroRuta].ciudadOrigen, "| ciudad de destino: ",  empresaCootracosta.rutas[numeroRuta].ciudadDestino,"| hora de salida: ",empresaCootracosta.rutas[numeroRuta].horaDeSalida,"| precio del pasaje por persona: ",empresaCootracosta.rutas[numeroRuta].pasajePorPersona,"$")
                numeroRuta += 1

        else:
            print("no hay rutas registradas, por favor, registra al menos una ")


    elif opcion == 5 :
        hora = datetime.now()
        if len(empresaCootracosta.rutas) != 0:
            print("Mostrar una ruta especifica ")
            l = True
            while l:
    
                ciudadOrigen = input("Digite ciudad de origen: ")
                ciudadOrigen = ciudadOrigen.title()

                if len(ciudadOrigen) != 0 and  ciudadOrigen in empresaCootracosta.ciudadesDeOperacion:

                    while l:

                        ciudadDestino = input("Digite ciudad destino: ")
                        ciudadDestino = ciudadDestino.title()

                        if  len(ciudadDestino) != 0 and  ciudadDestino in empresaCootracosta.ciudadesDeOperacion and ciudadDestino != ciudadOrigen :
                            
                         rutasEncontradas = empresaCootracosta.BuscarRuta(ciudadOrigen,ciudadDestino, hora.hour)[0]
                         busesEncontrados = empresaCootracosta.BuscarRuta(ciudadOrigen,ciudadDestino, hora.hour)[1]
                         for a in range(len(rutasEncontradas)):
                            print("Primera ruta", a+1)
                            print("Ciudad de origen:",empresaCootracosta.rutas[rutasEncontradas[a]].ciudadOrigen, "Ciudad de destino:", empresaCootracosta.rutas[rutasEncontradas[a]].ciudadDestino)
                            print("Hora de salida:",empresaCootracosta.rutas[rutasEncontradas[a]].horaDeSalida)
                            print("Bus para esta ruta:")
                            print("Número de identificación:",empresaCootracosta.buses[busesEncontrados[a]].numeroIdentificacion)
                            print("Placa:",empresaCootracosta.buses[busesEncontrados[a]].placa)
                            print("Conductor:",empresaCootracosta.buses[busesEncontrados[a]].conductor)
                         l = False


                        else:
                          print("no deje la casilla vacia, no ingrese numeros, la ciudad de destino tiene que ser diferente a la de origen y se tiene que encontrar dentro de las ciudades disponibles  ")
                    
                else:
                    print("no deje la casilla vacia, no ingrese numeros o se tiene que encontrar dentro de las ciudades disponibles  ")

        else:
            print("debe tener ingresado al menos una ruta ")

                        
    elif opcion == 6:
      if len(empresaCootracosta.buses) != 0:
        
        numeroIdentificacion = input("Número de identificación del bus: ")
        for ruta in empresaCootracosta.rutas:
            if numeroIdentificacion == ruta.numeroIdentificacionDelBus:
    
                numBus = empresaCootracosta.BuscarBusYPuestoDisponbles(numeroIdentificacion)
                print(empresaCootracosta.buses[numBus].CambiarPuestos())

            else:
                print("no se encuentra ningun bus registrado con ese numero de identificacion")

      else:
        print("deben haber al menos un bus registrado")


    elif opcion == 7:
        fechadehoy = date.today()
        if len(empresaCootracosta.buses) !=0 and len(empresaCootracosta.rutas) != 0:
            fechaNacimiento = []
            j = True
            while j:

                nombrePasajero = input("Ingrese el nombre y apellido del pasajero: ")
                if nombrePasajero.isalnum() is False and len(nombrePasajero) != 0 :

                    while j:
                        añoNacimiento = int(input("Ingrese el año de nacimiento del pasajero: "))
                        if len(str(añoNacimiento)) != 0 and 1900 <= añoNacimiento <= fechadehoy.year and (fechadehoy.year - añoNacimiento) >= 18:
                            while j:

                                mesNacimiento = int(input("Ingrese el mes de nacimiento del pasajero: "))
                                if len(str(mesNacimiento)) != 0 and 1 <= mesNacimiento <= 12:
                                    
                                    while j:

                                        diaNacimiento = int(input("Ingrese el día de nacimiento del pasajero: "))
                                        if len(str(diaNacimiento)) != 0 and 1 <= diaNacimiento <= 31:

                                            fechaNacimiento.append(añoNacimiento)
                                            fechaNacimiento.append(mesNacimiento)
                                            fechaNacimiento.append(diaNacimiento)

                                            if empresaCootracosta.CalculoEdad(añoNacimiento,mesNacimiento,diaNacimiento) >= 18:
                                                while j:

                                                 cantidadPuestos = int(input("Ingrese los puestos a comprar: "))
                                                 if  len(str(cantidadPuestos)) != 0 and 1 <= cantidadPuestos <= 40:

                                                    while j:
                                                        cedulaPasajero = int(input("Ingrese la cédula del pasajero: "))
                                                        if len(str(cedulaPasajero)) != 0 and 8 <= len(str(cedulaPasajero)) <= 10:
                                                        
                                                            while j:

                                                                ciudadOrigen = input("Ingrese la ciudad de Origen: ")
                                                                ciudadOrigen = ciudadOrigen.title()

                                                                if len(ciudadOrigen) != 0 and ciudadOrigen in empresaCootracosta.ciudadesDeOperacion:

                                                                    while j:

                                                                        ciudadDestino = input("Ingrese la ciudad de Destino: ")
                                                                        ciudadDestino = ciudadDestino.title()

                                                                        if len(ciudadDestino) != 0 and ciudadDestino  in empresaCootracosta.ciudadesDeOperacion and ciudadDestino != ciudadOrigen:
                                                                        
                                                                            while j:
                                                                                    
                                                                                    hora = int(input("Ingrese la hora de salida : "))
                                                                                    if 0 <= hora <= 23 and int(hora) and  len(str(hora)) != 0 :


                                                                                        while j:
                                                                                            plata = int(input("Ingrese el dinero que paga el pasajero: "))

                                                                                            if   int(plata) and  len(str(plata)) != 0:

                                                                                            
                                                                                             empresaCootracosta.RegistrarPasajero(Pasajero(nombrePasajero,fechaNacimiento,cedulaPasajero,ciudadOrigen,ciudadDestino,hora,cantidadPuestos,plata))
                                                                                             for a in range(cantidadPuestos):
                                                                                                 while j:
                                                                                                    letras = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J")
                                                                                                    print("Puesto", (a+1))
                                                                                                    filaPuesto = input("Digite la fila del puesto a comprar: ")
                                                                                                    filaPuesto = filaPuesto.title()
                                                                                                    

                                                                                                    if len(filaPuesto) ==1 and filaPuesto in letras:
                                                                                                        

                                                                                                        while j:
                                                                                                          try:
                                                                                                            columnaPuesto = int(input("Digite la columna del puesto a comprar: "))
                                                                                                            if len(str(columnaPuesto)) == 1  and 1 <= columnaPuesto <= 4:
                                                                                                         

                                                                                                                columnaPuesto = int(columnaPuesto)
                                                                                                                letraPuesto = letras.index(filaPuesto)
                                                                                                                numeroBus = empresaCootracosta.BuscarRutaYHora(ciudadOrigen, ciudadDestino, horaDeSalida)
                                                                                                                empresaCootracosta.buses[numeroBus].CambiarPuestos()
                                                                                                                puestosEscogidos = (filaPuesto,"-",columnaPuesto)
                                                                                                                venta = empresaCootracosta.buses[numeroBus].ModificarPuesto((columnaPuesto - 1),letraPuesto)
                                                                                                                if venta:
                                                                                                                 empresaCootracosta.pasajero[0].puestosEscogidos.append(puestosEscogidos) 
                                                                                                                 
                                                                                                                
                                                                                                            
                                                                                                          except:
                                                                                                            print(" no ingrese letras ")

                                                                                                    else:
                                                                                                        print("no deje la mrda vacia y solo ponga una ñero adema tiene que ir desde la A a la J")
                                                                                             
                                                                                             sleep(2)
                                                                                             print("")
                                                                                             print("---------------------------")
                                                                                             print("Pasajero: ",empresaCootracosta.pasajero[0].nombre)
                                                                                             print("CC: ", empresaCootracosta.pasajero[0].cedula)
                                                                                             print("---------------------------")
                                                                                             print("Total: $", empresaCootracosta.pagoSinDescuento(empresaCootracosta.pasajero[0].puestosAComprar))
                                                                                             print("-   Descuento:", empresaCootracosta.evaluarDescuento(empresaCootracosta.pasajero[0].puestosAComprar),"%") 
                                                                                             print("Total a pagar:$", empresaCootracosta.sacarDescuento())
                                                                                             print("---------------------------")
                                                                                             print("Recibido: $", empresaCootracosta.pasajero[0].efectivo)
                                                                                             print("Total a devolver: $",empresaCootracosta.sacarVuelto())
                                                                                             print("---------------------------")
                                                                                             print("Cantidad de puestos:", empresaCootracosta.pasajero[0].puestosAComprar)
                                                                                             print("Puestos escogidos: ", empresaCootracosta.pasajero[0].puestosEscogidos)
                                                                                             print("Ruta escogida:", empresaCootracosta.pasajero[0].ciudadOrigen, "-", empresaCootracosta.pasajero[0].ciduadDestino)
                                                                                             print("--------------------------") 
                                                                                             empresaCootracosta.pasajero.clear()
                                                                                             j = False
                                                                                           
                                                                                            else:
                                                                                                print("no ingrese letras o no deje la casilla vacia")

                                                                                    else:
                                                                                      print("no deje la casilla vacia y la hora tiene que estar en un rango entre 0 y 23")

                                                                        else:
                                                                         print("no deje la casilla vacia o la ciudad ingresada tiene que estar entre las ciudades de operacion y no tiene que ser igual a la ciudad de origen")
 
                                                                else:
                                                                 print("no deje la casilla vacia o la ciudad ingresada tiene que estar entre las ciudades de operacion")

                                                        else:
                                                         print("no deje la casilla vacia o no sobre pase el rango entre 8 y 10")

                                                 else:
                                                  print("no deje la casilla vacia o el rango de puestos a comprar esta entre 1 y 40")

                                            else:
                                                print("tiene que ingresar un numero entre 1 y 12")
                                         
                                        else:
                                         print("no deje la casilla vacia o el rango tiene que estar entre 1 y 31 dependiendo el mes ")

                                else:
                                    print("no deje la casilla vacia o el rango tiene que estar entre 1 y 12")

                        else:
                            print("no deje la casilla vacia o el rango permitido tiene que estar entre 1900 y el año actual ademas no se le venden a menores de edad")

                else:
                    print("no deje la casilla vacia o ingrese el nombre con su apellido")

        else:
            print("tienes que registrar por lo menos un bus y una ruta ")



            

    elif opcion == 8:
        if len(empresaCootracosta.rutas) !=0:
            listaRutas = empresaCootracosta.OrdenarCiudadesPorPuestosVendidos()
            for i in range(len(listaRutas)):
                print("--------------------------------------")
                print("Ciudad de origen:", listaRutas[i][0], "- Ciudad Destino: ", listaRutas[i][1])
                print("Hora de salida: ", listaRutas[i][2])
                print("Puestos vendidos: ", listaRutas[i][3])
                print("--------------------------------------")
        else:
            print("primero debe ingresar por lo menos una ruta")

    elif opcion == 9:
        k = True
        if len(empresaCootracosta.buses)!=0:
            print("¿Que desea cambiar?")
            print("1. Número de identificación interna de un bus.")
            print("2. Placa de un bus.")
            print("3. Conductor de un bus.")
            while k:
              try:

                opcionCambio = int(input("Por favor, ingrese una de las opciones disponibles: "))
                if len(str(opcionCambio)) != 0 and 1 <= opcionCambio <= 3 :       
                        if opcionCambio == 1:
                            while k:
                                try:
                                    numeroIdentificacionViejo = input("Número de identificación del bus a cambiar: ")
                                    for bus in empresaCootracosta.buses:
                                        if len(numeroIdentificacionViejo) != 0 and numeroIdentificacionViejo == bus.numeroIdentificacion:
                                         while k:
                                           try:        
                                            nuevoNumeroIdentificación = input("Nuevo número de identifación nuevo del bus: ")
                                            if len(nuevoNumeroIdentificación) == 4:
                                                numErrores = 0
                                                for bus in empresaCootracosta.buses:

                                                    if nuevoNumeroIdentificación == bus.numeroIdentificacion:
                                                        numErrores += 1

                                                if numErrores >= 1:
                                                    print("El número de identificacion no debe estar vacío")

                                                if numErrores ==0:
                    
                                                    empresaCootracosta.CambiarNumeroIdentificacion(numeroIdentificacionViejo,nuevoNumeroIdentificación)
                                                    if len(empresaCootracosta.rutas)== 0:
                                                        print("Número de identificación cambiado.")
                                                    else:
                                                        for ruta in empresaCootracosta.rutas:
                                                            if ruta.numeroIdentificacionDelBus == numeroIdentificacionViejo:
                                                                ruta.CambiarNumeroIdentificacionDelBus(nuevoNumeroIdentificación)
                                                                print("Número de identificacion cambiado.")

                                                    k = False

                                                else:
                                                    print("numero de identificacion tiene que ser diferente de un numero de identificacion ingresado")
                                            else:
                                                print("El número de identificacion no debe estar vacio o debe ser un número de 4 dígitos")
                                           except:
                                            print("El número de identificacion no debe estar vacio.")
                                        else:
                                            print(" no exite un bus con este numero de identificacion, por favor ingrese un numero de identificacion correcta")
                                except:
                                    print("Jiovani vazques")
                        elif opcionCambio == 2:
                            while k:
                                try:
                                    placaVieja = input("Placa del bus antiguo: ")
                                    for bus in empresaCootracosta.buses:
                                        if len(placaVieja) == 5 and placaVieja == bus.placa: 

                                            while k :

                                                placaNueva = input("Placa nueva del bus: ")
                                                numErrores = 0
                                                for bus in empresaCootracosta.buses:
                                                    if len(placaNueva) != 5 or placaNueva == bus.placa :
                                                        numErrores += 1 
                                                        
                                                if numErrores >= 1:
                                                    print("La placa tiene que ser de 5 digitos o no debe ser una ingresada anteriormente")
                                                
                                                if numErrores ==0:
                                                                                                   
                                                    cambio = empresaCootracosta.CambiarPlacaDelBus(placaVieja, placaNueva)
                                                    if cambio is True:
                                                        print("Placa cambiada con éxito.")
                                                        k = False

                                                    
                                except:
                                    print("La placa no está en la lista de los buses")
                        
                        elif opcionCambio ==3:
                            while k:
                                nombreConductorAntiguo = input("Nombre antiguo del conductor: ")
                                for bus in empresaCootracosta.buses:
                                    if len(nombreConductorAntiguo) != 0 and nombreConductorAntiguo == bus.conductor: 

                                        while k :
                                                                       
                                           nombreConductorNuevo = input("Nombre nuevo del conductor: ")
                                           numErrores = 0
                                           for bus in empresaCootracosta.buses:

                                            if len(nombreConductorNuevo) == 0 or nombreConductorNuevo == bus.conductor or nombreConductorNuevo.isalnum() is True :
                                             numErrores += 1

                                           if numErrores >= 1:
                                            print("El nombre del conductor no tiene que estar vacio")   

                                           if numErrores ==0:

                                            cambio = empresaCootracosta.CambiarNombreDelConductor(nombreConductorAntiguo, nombreConductorNuevo)
                                            if cambio is True:
                                                print("Nombre cambiado correctamente.")
                                                k = False


                        else:
                            print(" ingrese una opcion entre 1 y 3")
              except:
                print("")
        else:
            print("debe ingresar por lo menos un bus")

    else:
        print("--------------------------------------")
        print("¡Gracias por utilizar el programa! :D")
        exit()