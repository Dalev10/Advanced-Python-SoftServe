from Model.Consulta import Consulta
from Model.Mascota import Mascota

# @Author: Alejandro Vergara

class Historial():
    """
    Clase que representa el historial de consultas de una mascota. Contiene una lista de consultas
    y la mascota a la que pertenecen.
    """
    consultas_por_mascota: list[Consulta]
    mascota: Mascota

    def __init__(self, mascota: Mascota = None) -> None:
        self.consultas_por_mascota = []
        self.mascota = mascota

    def __str__(self) -> str:
        return f"Historial de {self.mascota.nombre}:\n" + "\n".join(str(consulta) for consulta in self.consultas_por_mascota)