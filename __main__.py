from Procesador import Procesador
from Controlador import Controlador
from Entrada_salida import Entrada_salida 
from Proceso import Proceso


def  ingresar_procesos(contenido):
    contenido_aux = contenido.split("\n")
    lista_procesos = []
    for linea in contenido_aux:
        atributos_proceso = linea.split(',')
        # print(atributos_proceso)           
        nombre = atributos_proceso[0].strip()
        tiempo_ejecucion = int(atributos_proceso[1].strip())
        tiempo_ingreso = int(atributos_proceso[2].strip())
        tiempo_e_s = int(atributos_proceso[3].strip())
        cantidad_rafagas = int(atributos_proceso[4].strip())
        cantidad_rafagas_e_s = int(atributos_proceso[5].strip())
        tiempo_ejecutado = int(atributos_proceso[6].strip())
        prioridad = int(atributos_proceso[7].strip())
        proceso = Proceso(nombre,tiempo_ejecucion,tiempo_ingreso,tiempo_e_s,cantidad_rafagas,cantidad_rafagas_e_s,tiempo_ejecutado,prioridad)
        lista_procesos.append(proceso)
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
    
    Archivo = input("Ingresa el nombre del archivo: ")
    contenido = ""
    try:
        with open(Archivo, "r") as archivo:
            contenido = archivo.read()

    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{Archivo}'.")
    except Exception as e:
        print(f"Error inesperado: {e}")

    lista = ingresar_procesos(contenido)
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
    