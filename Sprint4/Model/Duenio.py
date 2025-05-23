#@Author: Alejandro Vergara

class Duenio():
    """
    Clase que representa a un dueño de mascota. Contiene información sobre su nombre, dirección y teléfono.
    """
    _nombre: str
    _direccion: str
    _telefono: int

    def __init__(self, nombre: str = "", direccion: str = "", telefono: int = 0) -> None:
        self._nombre = nombre
        self._direccion = direccion
        self._telefono = telefono

    # Properties para acceder a los atributos de la clase
    # Se utilizan para encapsular los atributos y permitir su acceso y modificación a través de métodos
    @property
    def nombre(self) -> str:
        return self._nombre
    
    @property
    def direccion(self) -> str:
        return self._direccion
    
    @property
    def telefono(self) -> int:
        return self._telefono

    # Setters para modificar los atributos de la clase
    # Se utilizan para encapsular los atributos y permitir su modificación a través de métodos
    @nombre.setter
    def nombre(self, nombre: str) -> None:
        self._nombre = nombre

    @direccion.setter
    def direccion(self, direccion: str) -> None:
        self._direccion = direccion

    @telefono.setter
    def telefono(self, telefono: int) -> None:
        self._telefono = telefono

    def __str__(self) -> str:
        """
        Método para mostrar la información del dueño de la mascota.
        """
        return f"\nNombre: {self.nombre}\n Dirección: {self.direccion}\n Teléfono: {self.telefono}"