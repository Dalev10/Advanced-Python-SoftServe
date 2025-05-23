from Model.Mascota import Mascota
from Model.Duenio import Duenio
from Controller.Utilidades_text import normalizar


# @Author: Alejandro Vergara

class GestorMascota():
    """
    Clase que gestiona el registro y la obtención de la información de cada mascota.
    """
    mascotas: list[Mascota]

    def __init__(self) -> None:
        self.mascotas = []

    def registrar_mascota(self) -> None:

        """
        Método para registrar una nueva mascota. Se piden los datos de la mascota y de su dueño,
        creando los objetos correspondientes para agregarlos posteriormente a la lista de mascotas.
        """

        #Se instancian los objetos de Mascota y Duenio
        nueva_mascota = Mascota()
        duenio = Duenio()
        #Se piden los datos de la mascota
        nombre = str(input("Ingrese el nombre de la mascota: "))
        nueva_mascota.nombre = nombre
        especie = str(input("Ingrese la especie de la mascota: "))
        nueva_mascota.especie = especie
        raza = str(input("Ingrese la raza de la mascota: "))
        nueva_mascota.raza = raza
        edad = int(input("Ingrese la edad de la mascota: "))
        nueva_mascota.edad = edad
        #Se piden los datos del dueño de la mascota
        print("DATOS DEL DUEÑO DE LA MASCOTA".center(50, "*"))
        duenio_nombre = str(input("Ingrese el nombre del dueño de la mascota: "))
        duenio.nombre = duenio_nombre
        direccion = str(input("Ingrese la dirección del dueño de la mascota: "))
        duenio.direccion = direccion
        telefono = str(input("Ingrese el teléfono del dueño de la mascota: "))
        duenio.telefono = telefono
        #Se asigna el dueño a la mascota
        nueva_mascota.duenio = duenio
        #Se agrega la mascota a la lista de mascotas   
        self.mascotas.append(nueva_mascota)


    def buscar_mascota_por_nombre(self, nombre: str) -> Mascota | None:
        """
        Busca una mascota por su nombre.
        """
        nombre_normalizado = normalizar(nombre)
        for mascota in self.mascotas:
            if normalizar(mascota.nombre) == nombre_normalizado:
                return mascota
        return None
    

    def validar_mascota_consulta(self, nombre: str) -> Mascota:
        """
        Valida si la mascota existe. Si no, se registra una nueva.
        Retorna la instancia de la mascota.
        """
        mascota = self.buscar_mascota_por_nombre(nombre)
        if mascota is None:
            print("Mascota no encontrada. Se registrará una nueva.")
            self.registrar_mascota()
            mascota = self.buscar_mascota_por_nombre(nombre)
        return mascota


    def mostrar_mascotas(self) -> None:
        """
        Método para mostrar todas las mascotas registradas, utilizando sus representaciones __str__.
        """
        if not self.mascotas:
            print("No hay mascotas registradas.")
            return
    
        print("LISTADO DE MASCOTAS REGISTRADAS".center(60, "="))
        for i, mascota in enumerate(self.mascotas, start=1):
            print(f"\nMascota #{i}".center(60, "-"))
            print(mascota) 
