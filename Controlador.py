
from Procesador import Procesador
from Entrada_salida import Entrada_salida 
from Proceso import Proceso

class Controlador: # el controlador lo que hara es despachar cada proceso 

    tiempo_ejecucion = 0
    Archivo = ""
    Aceptar_procesos = 0
    tiempo_cambio = 0
    termino_proceso = 0
    procesador = Procesador('procesador')
    entrada_salida = Entrada_salida('entrada_salida')

    def __init__(self): 
      
        self.procesador = Procesador("procesador")
        self.entrada_salida = Entrada_salida("entrada_salida")
    
    def hay_proceso_con_rafa_mas_corta(self,lista_procesos,tiempo_limite):
        indice = 0
        while  indice < len(lista_procesos):
            proceso = lista_procesos[indice]
            if proceso.tiempo_ejecucion < tiempo_limite:
               chequear = False  # Si se encuentra un proceso con ráfaga más corta, devuelve false
            else: 
                chequear = True  # Si no encuentra un proceso con ráfaga más corta, devuelve true
            indice += 1
        return chequear

    def ordenar_FCFS(self, lista_procesos, lista_procesos_ordenados):   #debe recibir la lista de procesos para ordenarlos por orden de llegada 
        lista_procesos_ordenados = sorted(lista_procesos, key=lambda x: x.tiempo_ingreso)
        lista_procesos = lista_procesos_ordenados

    def ordenar_prioridades(self,lista_procesos): # politica prioridades
        lista_procesos_ordenados = sorted(lista_procesos, key=lambda x: x.prioridad)
      
    
    def ordenar_SRT(self, lista_procesos,lista_procesos_ordenados):   #debe recibir la lista de procesos para ordenarlos por orden de llegada 
        indice = 0
        lista_procesos_ordenados = sorted(lista_procesos, key=lambda x: x.tiempo_ejecucion)   
    
            
        while  indice < len(lista_procesos_ordenados):
            proceso = lista_procesos_ordenados[indice]
            print(f"nombre PROCESO : {proceso.nombre}") 
            indice += 1    


    def ejecutar_procesos_FCFS(self,lista_procesos,procesador,entrada_salida,lista_salida,Tiempo_cambio,Tiempo_total): 
      indice = 0
      tiempo_cambio = Tiempo_cambio
      while  indice < len(lista_procesos):
        while (tiempo_cambio>0): # nos permite simular el tiempo que le lleva al SO cambiar de proceso
            tiempo_cambio -= 1
        proceso = lista_procesos[indice]
        Tiempo_total = procesador.ejecutar_proceso(proceso,Tiempo_total) 
        if proceso.cantidad_rafagas_E_S > 0 : 
         Tiempo_total = entrada_salida.ejecutar_entrada_salida(proceso,Tiempo_total)
        indice +=1
        if indice == len(lista_procesos):
           indice = 0 
        if proceso.cantidad_rafagas == 0: 
            proceso.Tiempo_finalizacion = Tiempo_total
            print(f" sacando procesos que terminaron {proceso.nombre} esta ejecutando  {proceso.cantidad_rafagas}")
            lista_salida.append(proceso) 
            lista_procesos.remove(proceso)
        tiempo_cambio = Tiempo_cambio


    def ejecutar_procesos_SRT(self,lista_procesos,procesador,entrada_salida,lista_salida,Tiempo_cambio,Tiempo_total): #implementar el corte con una variable 
        procesador.ejecutar_proceso_SRT(lista_procesos,entrada_salida,lista_salida,Tiempo_cambio,Tiempo_total)
        
    def ejecutar_procesos_SJF(self,lista_procesos,procesador,entrada_salida,lista_salida,Tiempo_cambio,Tiempo_total): #implementar el corte con una variable 
        procesador.ejecutar_proceso_SJF(lista_procesos,entrada_salida,lista_salida,Tiempo_cambio,Tiempo_total)
        

    def ejecutar_procesos_RR(self,lista_procesos,procesador,entrada_salida,quantum,lista_salida,Tiempo_cambio,Tiempo_total):
        indice = 0
        while (indice < len(lista_procesos)): 
            proceso = lista_procesos[indice]
            print(f"Nombre {proceso.nombre} tiempo ejecucion {proceso.tiempo_ejecucion} cantidad rafagas {proceso.cantidad_rafagas}")
            indice += 1

        procesador.ejecutar_poceso_RR(lista_procesos,quantum,entrada_salida,lista_salida,Tiempo_cambio,Tiempo_total)

    def ejecutar_procesos_Prioridad(self,lista_procesos,procesador,entrada_salida,apropiativa,lista_salida,Tiempo_cambio,Tiempo_total):
        if (apropiativa == True):
            procesador.ejecutar_prio_aprop(lista_procesos,entrada_salida,lista_salida,Tiempo_cambio,Tiempo_total)
        else: 
            procesador.ejecutar_prio_no_apro(lista_procesos,entrada_salida,lista_salida,Tiempo_cambio,Tiempo_total)


    