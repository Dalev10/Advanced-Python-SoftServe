
# 🐾 Amigos Peludos - Sistema de Gestión Veterinaria

**Autor:** Diego Alejandro Vergara Ruiz  
**Versión:** 1.0  
**Lenguaje:** Python 3.11 

---

## 📋 Descripción del Proyecto

**Amigos Peludos** es una aplicación de consola diseñada para gestionar los datos de una clínica veterinaria ficticia. El sistema permite registrar, consultar y visualizar información relacionada con mascotas, consultas médicas y sus historiales, facilitando una gestión eficiente desde una interfaz sencilla basada en texto.

---

## 🧱 Arquitectura del Software

Este sistema ha sido desarrollado siguiendo el patrón de diseño **MVC (Modelo-Vista-Controlador)**:

- **Modelo (Model):** Contiene las clases que representan las entidades del sistema como `Mascota`, `Consulta`, `Duenio` e `Historial`.
- **Vista (View):** Se encarga de la interacción con el usuario por medio de menús de consola.
- **Controlador (Controller):** Coordina las acciones entre la vista y el modelo, manejando la lógica del programa.

Además, se aplica el principio de **responsabilidad única**, asegurando que cada clase y método tenga una única función bien definida. Esto mejora la mantenibilidad, escalabilidad y comprensión del código.

---

## 🧠 Principales Características

- Registro de nuevas mascotas.
- Registro de consultas médicas por fecha, motivo y diagnóstico.
- Gestión de historiales de consulta por mascota.
- Validación de existencia de mascotas antes de registrar datos.
- Normalización de nombres para búsquedas robustas (insensibles a mayúsculas, tildes, etc.).

---

## 🛠 Tecnologías Utilizadas

- **Python 3.11**
- Programación Orientada a Objetos (OOP)
- Estructura modular por paquetes y clases

---

## ▶️ Cómo Ejecutar

1. Clona el repositorio en tu máquina local.
2. Asegúrate de tener Python 3 instalado.
3. Ejecuta el archivo principal:

```bash
python main.py
