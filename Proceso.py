class Proceso:
       
    nombre = ""
    tiempo_ejecucion = "" #tiempo que tiene que ejecutar las rafagas
    tiempo_ingreso = "" #tiempo en el que ingreso el 
    tiempo_E_S = "" 
    cantidad_rafagas = 0 
    cantidad_rafagas_E_S =  0
    tiempo_ejecutado =  0 #tiempo que lleva ejecutando 
    prioridad = 0
    Tiempo_finalizacion = 0
    def __init__(self, nombre, tiempo_ejecucion, tiempo_ingreso, tiempo_E_S, cantidad_rafagas, cantidad_rafagas_E_S, tiempo_ejecutado, prioridad):
        self.nombre = nombre
        self.tiempo_ejecucion = tiempo_ejecucion #tiempo que tiene que ejecutar las rafagas
        self.tiempo_ingreso = tiempo_ingreso #tiempo en el que ingreso el 
        self.tiempo_E_S = tiempo_E_S 
        self.cantidad_rafagas = cantidad_rafagas 
        self.cantidad_rafagas_E_S = cantidad_rafagas_E_S 
        self.tiempo_ejecutado = tiempo_ejecutado #tiempo que lleva ejecutando 
        self.prioridad = prioridad
        """ el tiempo ejecutado se va a ir editando a medida que va corriendo el proceso
            por lo tanto es un dato que no ingresa en el comienzo del proceso sino se va 
            a ir cargando en el momento en el que corre y va almacenando en esa variable
        """