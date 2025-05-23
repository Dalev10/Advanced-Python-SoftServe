from Model.Consulta import Consulta
from Model.Historial import Historial
from Controller.GestorMascota import *
from Controller.Utilidades_text import normalizar
from datetime import date

# @Author: Alejandro Vergara

class GestorConsulta():

    consultas: list[Consulta]
    historiales: dict[str, Historial]
    gestor_mascota: GestorMascota

    def __init__(self, gestor_mascota: GestorMascota) -> None:
        """
        Constructor de la clase GestorConsulta. Inicializa la lista de consultas y el historial de la mascota.
        """
        self.consultas = []
        self.historiales = {}
        self.gestor_mascota = gestor_mascota


    def registrar_consulta(self) -> None:
        """
        Método para registrar una nueva consulta. Se piden los datos de la consulta y se crea un objeto
        Consulta que se agrega a la lista de consultas y al historial de la mascota.
        """
        #Se instancian los objetos de Consulta
        nueva_consulta = Consulta()
        #Se piden los datos de la consulta
        fecha = date.fromisoformat(input("Ingrese la fecha de la consulta (YYYY-MM-DD): ")) #Formato de fecha
        nueva_consulta.fecha = fecha
        nombre_mascota = str(input("Ingrese el nombre de la mascota: "))
        mascota = self.gestor_mascota.validar_mascota_consulta(nombre_mascota)
        nueva_consulta.mascota = mascota
        motivo = str(input("Ingrese el motivo de la consulta: "))
        nueva_consulta.motivo = motivo
        diagnostico = str(input("Ingrese el diagnóstico: "))
        nueva_consulta.diagnostico = diagnostico

        #Se agrega la consulta a la lista de consultas y al historial de la mascota
        self.consultas.append(nueva_consulta)

        clave = normalizar(mascota.nombre)
        if clave not in self.historiales:
            self.historiales[clave] = Historial(mascota)
        self.historiales[clave].consultas_por_mascota.append(nueva_consulta)

        print(f"Consulta registrada para la mascota {mascota.nombre}.")


    def mostrar_historial(self) -> None:
        """
        Método para mostrar el historial de consultas de una mascota. 
        Se pide el nombre de la mascota y se muestra su historial.
        """
        nombre = input("Ingrese el nombre de la mascota: ")
        clave = normalizar(nombre)

        if clave in self.historiales:
            print(self.historiales[clave])
        else:
            print("No hay historial para esta mascota.")



