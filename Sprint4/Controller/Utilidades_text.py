import unicodedata

# @Author: Alejandro Vergara

def normalizar(texto: str) -> str:
        """
        Elimina tildes y convierte el texto a minúsculas sin acentos.
        """
        texto = texto.strip().lower()  # Elimina espacios y pasa a minúsculas
        texto = unicodedata.normalize('NFD', texto)  # Descompone los acentos
        texto = ''.join(c for c in texto if unicodedata.category(c) != 'Mn')  # Elimina marcas de acento
        return texto