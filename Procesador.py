from Proceso import Proceso


class Procesador:
    
    nombre = ""

    def __init__(self, nombre):
        self.nombre = nombre


    def ejecutar_proceso(self,proceso,Tiempo_total):
        Tiempo_ejecucion = 0
        tiempo_ejecucionT =  proceso.tiempo_ejecucion
        cantidad = proceso.cantidad_rafagas # aca asigna la cantidad de rafagas que ejecutara 
        while  cantidad > 0 and Tiempo_ejecucion < tiempo_ejecucionT: #podria ser para para FCFS 
          Tiempo_ejecucion += 1 
          proceso.tiempo_ejecutado += 1
          Tiempo_total += 1
          print(f"TIEMPO TOTAL {Tiempo_total}")
          cantidad = proceso.cantidad_rafagas
          print(f"{proceso.nombre} está ejecutando durante: {Tiempo_ejecucion} cantidad rafagas:  {  proceso.cantidad_rafagas} tiempo que lleva ejecutado {proceso.tiempo_ejecutado}")
          
          if Tiempo_ejecucion == tiempo_ejecucionT:
           proceso.cantidad_rafagas -= 1 #aca le quita una si es la ultima ejecucion que hara 
        return Tiempo_total
   
    def buscar(self,lista_procesos,tiempo): 
        indice = 0
        encontrado = False
        tiempoC = lista_procesos[indice].tiempo_ejecucion
        proceso = lista_procesos[indice]
        while(encontrado == False and indice < len(lista_procesos)):
          if (lista_procesos[indice].tiempo_ingreso == tiempo )and (tiempoC > lista_procesos[indice].tiempo_ejecucion ):       
                proceso = lista_procesos[indice]
                tiempoC = proceso.tiempo_ingreso

                encontrado = True
                print(f"{proceso.nombre}")
          indice += 1
         
        return (proceso)
    
    def buscar_llego(self,lista_procesos,tiempo): 
     indice = 0
     encontrado = False
     tiempoC = lista_procesos[indice].tiempo_ejecucion
     proceso = lista_procesos[indice]
     while(encontrado == False and indice < len(lista_procesos)):
       if (lista_procesos[indice].tiempo_ingreso == tiempo ):       
             proceso = lista_procesos[indice]
             tiempoC = proceso.tiempo_ingreso
             encontrado = True 
       indice += 1
      
     return (proceso)

    def buscar_prioridad(self,lista_procesos,tiempo,prioridad): 
         indice = 0
         encontrado = False
         tiempoC = lista_procesos[indice].tiempo_ejecucion
         proceso = lista_procesos[indice]
         while(encontrado == False and indice < len(lista_procesos)):
              if (lista_procesos[indice].tiempo_ingreso == tiempo and proceso.prioridad > prioridad ):       
                proceso = lista_procesos[indice]
                tiempoC = proceso.tiempo_ingreso
                prioridad = proceso.prioridad
                encontrado = True
                print(f"{proceso.nombre}")
              indice += 1

         return (proceso)

    def ejecutar_proceso_SRT(self,lista_procesos,entrada_salida,lista_salida,Tiempo_cambio,Tiempo_total):
        tiempo = 1 # el tiempo tiene que aumentar siempre 
        lista_ejecicion = []# para guardar los tiempos de ejecucion de cada proceso
        # buscar la manera de 
        indice = 0 #  el indice va a ser para movernos dentro de la lista 
        tiempo_cambio = Tiempo_cambio
        while (indice <= len(lista_procesos)):
            lista_ejecicion.append(0)
            indice += 1 

        indice = 0
        while ((lista_procesos)): 
            while(tiempo_cambio>0): 
                tiempo_cambio -= 1
            proceso = self.buscar(lista_procesos,tiempo)
            print(f"{proceso.nombre} esta ejecutando  {proceso.cantidad_rafagas}")
            print(f"indice {indice} tiempo {tiempo}")
         
            if (lista_ejecicion[indice] < proceso.tiempo_ejecucion): 
                proceso.tiempo_ejecutado += 1
                Tiempo_total += 1
                lista_ejecicion[indice] += 1
            if (lista_ejecicion[indice] == proceso.tiempo_ejecucion): 
                Tiempo_total = entrada_salida.ejecutar_entrada_salida(proceso,Tiempo_total)
                lista_ejecicion[indice] = 0 
                proceso.cantidad_rafagas -= 1
                
            if (proceso.cantidad_rafagas == 0): 
             proceso.Tiempo_finalizacion = Tiempo_total
             lista_salida.append(proceso) 
             lista_procesos.remove(proceso)
             lista_ejecicion.remove(lista_ejecicion[indice])
      
            

            indice += 1 
            tiempo += 1
            print(f"indice {indice} tiempo {tiempo}")
         
            if (indice >= len(lista_procesos)): 
                indice = 0 
                tiempo = 1
            tiempo_cambio = Tiempo_cambio

    def ejecutar_proceso_SJF(self,lista_procesos,entrada_salida,lista_salida,Tiempo_cambio,Tiempo_total):
     tiempo_cambio = Tiempo_cambio
     tiempo = 1 # el tiempo tiene que aumentar siempre 
     lista_ejecucion = [] # para guardar los tiempos de ejecucion de cada proceso
     indice = 0 #  el indice va a ser para movernos dentro de la lista 
     while (indice <= len(lista_procesos)): # necesitamos si o si que tenga la cantidad de procesos que tiene la lista de procesos 
            lista_ejecucion.append(0)
            indice += 1 

     indice = 0
     while ((lista_procesos)): 
         while (tiempo_cambio>0): # nos permite simular el tiempo que le lleva al SO cambiar de proceso
            tiempo_cambio -= 1
         proceso = self.buscar_llego(lista_procesos,tiempo)
         print(f"{proceso.nombre} esta ejecutando  {proceso.cantidad_rafagas}")

         print(f"indice {indice} tiempo {tiempo} lista_procesos {len(lista_procesos)}")
         while (lista_ejecucion[indice] < proceso.tiempo_ejecucion): 
             proceso.tiempo_ejecutado += 1
             Tiempo_total += 1 
             lista_ejecucion[indice] += 1

         if (lista_ejecucion[indice]== proceso.tiempo_ejecucion): 
             Tiempo_total = entrada_salida.ejecutar_entrada_salida(proceso,Tiempo_total)
             lista_ejecucion[indice]= 0 
             proceso.cantidad_rafagas -= 1

         if (proceso.cantidad_rafagas == 0): 
             proceso.Tiempo_finalizacion = Tiempo_total
             lista_salida.append(proceso) 
             lista_procesos.remove(proceso)
             lista_ejecucion.remove(lista_ejecucion[indice])
      
         indice += 1 
         tiempo += 1
          
         if (indice > len(lista_procesos)): 
             indice = 0 
             tiempo = 1
         tiempo_cambio = Tiempo_cambio
    
    def ejecutar_poceso_RR(self,lista_procesos,quantum,entrada_salida,lista_salida,Tiempo_cambio,Tiempo_total): 
     indiceQ = 0
     lista_ejecucion = [] # para guardar los tiempos de ejecucion de cada proceso
     tiempo_cambio = Tiempo_cambio
     indice = 0 #  el indice va a ser para movernos dentro de la lista 
     while (indice <= len(lista_procesos)): # necesitamos si o si que tenga la cantidad de procesos que tiene la lista de procesos 
            lista_ejecucion.append(0)
            indice += 1 
     indice = 0
     while ( len(lista_procesos)): 
         while (tiempo_cambio>0): # nos permite simular el tiempo que le lleva al SO cambiar de proceso
            tiempo_cambio -= 1
    
         proceso =  lista_procesos[indice]

         while (lista_ejecucion[indice] < proceso.tiempo_ejecucion )and(indiceQ<quantum): 
             proceso.tiempo_ejecutado += 1
             Tiempo_total += 1 
             lista_ejecucion[indice] += 1
             print(f" {proceso.nombre} tiempo ejecutado {proceso.tiempo_ejecutado} lista de ejecucion {lista_ejecucion[indice]} {indice} ")
             indiceQ += 1
          
             
 
         if (lista_ejecucion[indice] == proceso.tiempo_ejecucion): 
             Tiempo_total = entrada_salida.ejecutar_entrada_salida(proceso,Tiempo_total) 
             proceso.cantidad_rafagas -= 1 # hay que separar el tiempo de ejecucion con la lista de ejecucion 
             lista_ejecucion[indice] = 0 
         if (proceso.cantidad_rafagas == 0): 
             proceso.Tiempo_finalizacion = Tiempo_total # almaceno el tiempo en el que finaliza cierto proceso
             lista_salida.append(proceso) 
             lista_procesos.remove(proceso)
             lista_ejecucion.remove(indice)
 
         indice += 1 
         indiceQ = 0 
         if (indice == len(lista_procesos)): 
             indice = 0
         tiempo_cambio = Tiempo_cambio

    
    def ejecutar_prio_aprop(self,lista_procesos,entrada_salida,lista_salida,Tiempo_cambio,Tiempo_total): 
        indice = 0 
        tiempo = 1 
        prioridad = 3
        lista_tiempo = []
        tiempo_cambio = Tiempo_cambio
        while (indice <= len(lista_procesos)): # necesitamos si o si que tenga la cantidad de procesos que tiene la lista de procesos 
            lista_tiempo.append(0)
            indice += 1 

        indice = 0
        while ((lista_procesos)):

            proceso = self.buscar_prioridad(lista_procesos,tiempo,prioridad) 
            while (tiempo_cambio>0): # nos permite simular el tiempo que le lleva al SO cambiar de proceso
             tiempo_cambio -= 1
    
            if (lista_tiempo[indice] < proceso.tiempo_ejecucion): 
                lista_tiempo[indice] += 1 
                proceso.tiempo_ejecutado += 1
                Tiempo_total += 1
                print(f"proceso {proceso.nombre} leva ejecutando tiempo de ejecucion {proceso.tiempo_ejecutado}")
        
            if (lista_tiempo[indice] == proceso.tiempo_ejecucion):
                Tiempo_total = entrada_salida.ejecutar_entrada_salida(proceso,Tiempo_total)
                proceso.cantidad_rafagas -= 1 
                lista_tiempo[indice] = 0
            
        
            if (proceso.cantidad_rafagas == 0): 
                proceso.Tiempo_finalizacion = Tiempo_total
                lista_salida.append(proceso)
                lista_procesos.remove(proceso)
                lista_tiempo.remove(lista_tiempo[indice])

            indice += 1 
            tiempo += 1 
            if (indice == len(lista_procesos)): 
                indice = 0 
                tiempo = 1  
            tiempo_cambio = Tiempo_cambio
    
    def ejecutar_prio_no_apro(self,lista_procesos,entrada_salida,lista_salida,Tiempo_cambio,Tiempo_total): 
        indice = 0 
        tiempo = 1 
        prioridad = 0
        lista_tiempo = []
        tiempo_cambio = Tiempo_cambio
        while (indice <= len(lista_procesos)): # necesitamos si o si que tenga la cantidad de procesos que tiene la lista de procesos 
            lista_tiempo.append(0)
            indice += 1 

        indice = 0

        while ((lista_procesos)):

            proceso = self.buscar_prioridad(lista_procesos,tiempo,prioridad) #busca el de mayor prioridad en el momento dado 
            while (tiempo_cambio>0): # nos permite simular el tiempo que le lleva al SO cambiar de proceso
              tiempo_cambio -= 1

            while (lista_tiempo[indice] < proceso.tiempo_ejecucion): 
                lista_tiempo[indice] += 1 
                Tiempo_total += 1 
                proceso.tiempo_ejecutado += 1
                print(f"proceso {proceso.nombre} lleva ejecutando tiempo de ejecucion {proceso.tiempo_ejecutado}")
        
            if (lista_tiempo[indice] == proceso.tiempo_ejecucion):
                Tiempo_total = entrada_salida.ejecutar_entrada_salida(proceso,Tiempo_total)
                proceso.cantidad_rafagas -= 1 
                lista_tiempo[indice] = 0
                
        
            if (proceso.cantidad_rafagas == 0): 
                proceso.Tiempo_finalizacion = Tiempo_total  # almaceno el tiempo en el que finaliza cierto proceso
                lista_salida.append(proceso) 
                lista_procesos.remove(proceso)
                lista_tiempo.remove( lista_tiempo[indice])

            indice += 1 
            tiempo += 1 
            print(f"indice {indice} tiempo {tiempo}")
            if (indice == len(lista_procesos)): 
                indice = 0 
                tiempo = 1  
            tiempo_cambio = Tiempo_cambio