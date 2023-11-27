from Procesador import Procesador
from Controlador import Controlador
from Entrada_salida import Entrada_salida 
from Proceso import Proceso


def  ingresar_procesos(lista_procesos,Prioridad):
    seguir = True
    while (seguir): 
        nombre = input("ingrese por favor el nombre del proceso: ")
        tiempo_ingreso = int(input("ingrese por favor el tiempo de ingreso: "))
        tiempo_ejecucion = int(input("ingrese por favor el tiempo de ejecucion del proceso: "))
        cantidad_rafagas = int(input("ingrese por favor la cantidad rafagas: "))
        tiempo_E_S = int(input("ingrese por favor el tiempo de entrada/salida: "))
        cantidad_rafagas_E_S = int(input("ingrese por favor la cantidad de entrada salidas que tendra: "))
        prioridad = 0
        if (Prioridad == True ): 
            prioridad = int(input("ingrese por favor la prioridad que tendra: "))
        proceso = Proceso( nombre, tiempo_ejecucion, tiempo_ingreso, tiempo_E_S, cantidad_rafagas, cantidad_rafagas_E_S,0, prioridad)
        lista_procesos.append(proceso) 
        respuesta = input("desea seguir agregando procesos?")
        if (respuesta == "no"): 
            seguir = False
        else: 
            seguir = True
    return (lista_procesos)

class main(): 
    print("BIENVENIDO AL SIMULADOR DE PROCESADOR")
    apropiativa = False
    prioridad = False
    quantum = 0
    Aceptar_procesos =  int(input("ingrese por favor el tiempo de aceptacion de los procesos: "))
    tiempo_cambio =  int(input("ingrese por favor el tiempo de cambio de los procesos: "))
    termino_proceso =  int(input("ingrese por favor el tiempo de termino  de los procesos: "))
    politica = input("ingrese la politica a utilizar(recuerde que debe de ser en mayusculas):")
    if (politica == "RR"): 
        quantum =  int(input ("ingrese por favor el quantum a utilizar:"))
    else: 
        if (politica == "PRIORIDAD"): 
            preemtiva = input ("ingrese si la politica es preemtiva:")
            if (preemtiva == "SI"): 
                apropiativa = True
            else: 
                apropiativa = False
    lista = []
    while (Aceptar_procesos > 0): 
        Aceptar_procesos -= 1
    print(f'prioridad {prioridad}')
    lista = ingresar_procesos(lista,prioridad)
    controlador = Controlador()
    procesador = Procesador("")
    entrada_salida = Entrada_salida("")
    lista_salida = []
    Tiempo_total = 0
    switch_dict = {
        'FCFS':controlador.ejecutar_procesos_FCFS(lista,procesador,entrada_salida,lista_salida,tiempo_cambio,Tiempo_total),
        'RR': controlador. ejecutar_procesos_RR(lista,procesador,entrada_salida,quantum,lista_salida,tiempo_cambio,Tiempo_total),
        'SRT': controlador.ejecutar_procesos_SRT(lista,procesador,entrada_salida,lista_salida,tiempo_cambio,Tiempo_total),
        'SJF': controlador.ejecutar_procesos_SJF(lista,procesador,entrada_salida,lista_salida,tiempo_cambio,Tiempo_total),
        'PRIORIDAD': controlador.ejecutar_procesos_Prioridad(lista,procesador,entrada_salida,apropiativa,lista_salida,tiempo_cambio,Tiempo_total)
}
    
    switch_dict[politica]
    indice = 0
    while (indice < len(lista_salida)): 
      proceso = lista_salida[indice]
      proceso.Tiempo_finalizacion += termino_proceso
      print(f"proceso {proceso.nombre} tiempo ejecucion: {proceso.tiempo_ejecutado} tiempo finalizacion  {proceso.Tiempo_finalizacion }")
     
      indice += 1
    