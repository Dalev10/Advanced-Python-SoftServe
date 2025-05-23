from Controller.GestorConsulta import GestorConsulta
from Controller.GestorMascota import GestorMascota

def menu_principal() -> None:
    """
    Función para mostrar el menú principal y gestionar las opciones del usuario.
    """
    gestor_mascota = GestorMascota()
    gestor_consulta = GestorConsulta(gestor_mascota)

    while True:
        print("Menu Principal".upper().center(50, "*"))
        print("1. Registrar Mascota")
        print("2. Mostrar Mascotas")
        print("3. Registrar Consulta")
        print("4. Mostrar Historial de Consultas")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            print("Registro de Mascota".upper().center(50, "*"))
            gestor_mascota.registrar_mascota()
            print("Mascota registrada con éxito.")
        elif opcion == "2":
            print("Mascotas".upper().center(50, "*"))
            gestor_mascota.mostrar_mascotas()
        elif opcion == "3":
            print("Registro de Consulta".upper().center(50, "*"))
            gestor_consulta.registrar_consulta()
        elif opcion == "4":
            print("Historial de Consultas".upper().center(50, "*"))
            gestor_consulta.mostrar_historial()
        elif opcion == "5":
            break
        else:
            print("Opción no válida. Intente nuevamente.")