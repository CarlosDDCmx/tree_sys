import logging
from typing import List, Dict, Any

class TreeParser:
    """
    Módulo que se encarga de leer la estructura del árbol en texto
    y convertirla en un formato JSON (lista de diccionarios).
    """
    def __init__(self, file_path: str) -> None:
        self.file_path = file_path

    def parse(self) -> List[Dict[str, Any]]:
        """
        Lee el archivo de texto con la estructura del árbol y lo convierte
        en una lista de diccionarios.
        """
        try:
            with open(self.file_path, 'r', encoding="utf-8") as file:
                lines = file.readlines()
            structure: List[Dict[str, Any]] = []
            stack: List[Dict[str, Any]] = []
            for line in lines:
                stripped_line = line.rstrip('\n')
                level = stripped_line.count('│')  # Nivel determinado por '│'
                name = stripped_line.split('─')[-1].strip()
                logging.info(f"name: {name}")
                is_folder = '.' not in name  # Si no contiene un punto, es una carpeta

                entry: Dict[str, Any] = {
                    'name': name,
                    'level': level,
                    'is_folder': is_folder
                }

                if level == len(stack):
                    stack.append(entry)
                else:
                    stack = stack[:level]
                    stack.append(entry)

                if level == 0:
                    structure.append(entry)
                else:
                    parent = stack[level - 1]
                    if 'children' not in parent:
                        parent['children'] = []
                    parent['children'].append(entry)
                logging.info("-" * 100)
            logging.info(f"Estructura de árbol leída correctamente desde {self.file_path}")
            logging.info(f"Estructura: {structure}")
            return structure
        except FileNotFoundError:
            logging.error(f"El archivo {self.file_path} no se encuentra.")
            raise
        except Exception as e:
            logging.error(f"Error al leer o procesar el archivo {self.file_path}: {e}")
            raise
