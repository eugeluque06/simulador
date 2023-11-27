class Entrada_salida:

    
    def __init__(self, nombre):
        self.nombre = nombre

    def ejecutar_entrada_salida(self,proceso,Tiempo_total):
        tiempo_ES = 0 
        tiempo_esT = proceso.tiempo_E_S
        cantidad = proceso.cantidad_rafagas_E_S
        while cantidad > 0 and tiempo_ES  < tiempo_esT: 
          tiempo_ES += 1 
          Tiempo_total += 1

          proceso.tiempo_ejecutado += 1
          print(f"proceso {proceso.nombre}ejecuta E/S de {proceso.nombre} durante {tiempo_ES} tiempo total {Tiempo_total}")
          if (tiempo_ES == tiempo_esT):
            proceso.cantidad_rafagas_E_S -= 1 
        return Tiempo_total 