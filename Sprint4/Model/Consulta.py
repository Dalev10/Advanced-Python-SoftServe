from Model.Mascota import Mascota
import datetime

# @Author: Alejandro Vergara

class Consulta():
    """
    Clase que representa una consulta veterinaria. Contiene información sobre la fecha de la consulta,
    la mascota que fue atendida, el motivo de la consulta y el diagnóstico realizado.
    """
    _fecha: datetime.date
    _mascota: Mascota
    _motivo: str
    _diagnostico: str

    def __init__(self, fecha: datetime.date = datetime.date.today(), mascota: Mascota = None, motivo: str = "", diagnostico: str = "") -> None:
        self._fecha = fecha
        self._mascota = mascota
        self._motivo = motivo
        self._diagnostico = diagnostico

    # Properties para acceder a los atributos de la clase
    # Se utilizan para encapsular los atributos y permitir su acceso y modificación a través de métodos
    @property
    def fecha(self) -> datetime.date:
        return self._fecha

    @property
    def mascota(self) -> Mascota:
        return self._mascota

    @property
    def motivo(self) -> str:
        return self._motivo

    @property
    def diagnostico(self) -> str:
        return self._diagnostico
    

    # Setters para modificar los atributos de la clase
    # Se utilizan para encapsular los atributos y permitir su modificación a través de métodos
    @fecha.setter
    def fecha(self, fecha: datetime.date) -> None:
        self._fecha = fecha

    @mascota.setter
    def mascota(self, mascota: Mascota) -> None:
        self._mascota = mascota

    @motivo.setter
    def motivo(self, motivo: str) -> None:
        self._motivo = motivo

    @diagnostico.setter
    def diagnostico(self, diagnostico: str) -> None:
        self._diagnostico = diagnostico

    def __str__(self) -> str:  
        """
        Método para mostrar la información de la consulta veterinaria.
        """
        return f"Fecha: {self.fecha}\n Mascota: {self.mascota}\n Motivo: {self.motivo}\n Diagnóstico: {self.diagnostico}"