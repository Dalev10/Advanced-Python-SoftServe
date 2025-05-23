from Model.Duenio import Duenio

#@Author: Alejandro Vergara

class Mascota():
    """
    Clase que representa una mascota. Contiene información sobre su nombre, especie, raza, edad y dueño.
    """
    _nombre: str
    _especie: str
    _raza: str
    _edad: int
    _duenio: Duenio

    def __init__(self, nombre: str = "", especie: str = "", raza: str = "", edad: int = 0, duenio: Duenio = None) -> None:
        """
        Inicializa una nueva instancia de la clase Mascota.
        """
        self._nombre = nombre
        self._especie = especie
        self._raza = raza
        self._edad = edad
        self._duenio = duenio

    # Properties para acceder a los atributos de la clase
    # Se utilizan para encapsular los atributos y permitir su acceso y modificación a través de métodos
    @property
    def nombre(self) -> str:
        return self._nombre

    @property
    def especie(self) -> str:
        return self._especie

    @property
    def raza(self) -> str:
        return self._raza

    @property
    def edad(self) -> int:
        return self._edad

    @property
    def duenio(self) -> Duenio:
        return self._duenio

    # Setters para modificar los atributos de la clase
    # Se utilizan para encapsular los atributos y permitir su modificación a través de métodos
    @nombre.setter
    def nombre(self, nombre: str) -> None:
        self._nombre = nombre

    @especie.setter
    def especie(self, especie: str) -> None:
        self._especie = especie

    @raza.setter
    def raza(self, raza: str) -> None:
        self._raza = raza

    @edad.setter
    def edad(self, edad: int) -> None:
        self._edad = edad

    @duenio.setter
    def duenio(self, duenio: Duenio) -> None:
        self._duenio = duenio

    def __str__(self) -> str:
        """
        Representa la información de la mascota como una cadena.
        """
        return f"\nNombre: {self.nombre}\n Especie: {self.especie}\n Raza: {self.raza}\n Edad: {self.edad}\n Dueño: {self.duenio}"
