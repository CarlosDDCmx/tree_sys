import logging
import re
from typing import List, Dict, Any

class TreeParser:
    """
    Módulo que se encarga de leer la estructura del árbol en texto
    y convertirla en una lista de diccionarios.
    """
    def __init__(self, file_path: str) -> None:
        self.file_path = file_path

    def parse(self) -> List[Dict[str, Any]]:
        try:
            with open(self.file_path, 'r', encoding="utf-8") as file:
                lines = file.readlines()
            
            structure: List[Dict[str, Any]] = []
            stack = []  # Almacenará tuplas: (indent, nodo)

            for line in lines:
                stripped_line = line.rstrip('\n')
                # Se obtiene el prefijo (caracteres iniciales, que pueden ser espacios o símbolos)
                match = re.match(r'^([\s├│└]+)', stripped_line)
                if match:
                    prefix = match.group(1)
                    indent = len(prefix)
                else:
                    indent = 0

                # Se extrae el nombre:
                # Si existe el separador "──", se asume que el nombre es la parte final.
                if '──' in stripped_line:
                    name = stripped_line.split('──')[-1].strip()
                else:
                    name = stripped_line.strip()

                logging.info("Detectado: '%s' con indentación %d", name, indent)

                # Determinar si es carpeta (si el nombre termina en '/')
                is_folder = name.endswith('/')
                # Creamos el nodo, sin asignar aún el nivel
                node: Dict[str, Any] = {
                    'name': name,
                    'is_folder': is_folder
                }

                # Determinar el nivel del nodo basado en la pila
                if not stack:
                    # Primer nodo (raíz)
                    node['level'] = 0
                    stack.append((indent, node))
                    structure.append(node)
                else:
                    # Si el indent actual es mayor que el tope de la pila, es hijo directo
                    if indent > stack[-1][0]:
                        node['level'] = stack[-1][1]['level'] + 1
                        stack.append((indent, node))
                    else:
                        # Se desapilan nodos hasta encontrar un indent menor que el actual
                        while stack and indent <= stack[-1][0]:
                            stack.pop()
                        if stack:
                            node['level'] = stack[-1][1]['level'] + 1
                        else:
                            node['level'] = 0
                        stack.append((indent, node))
                    
                    # Ubicar el padre: es el nodo cuyo nivel es (nivel_actual - 1)
                    parent = None
                    for _, candidate in reversed(stack[:-1]):
                        if candidate['level'] == node['level'] - 1:
                            parent = candidate
                            break
                    if parent:
                        if 'children' not in parent:
                            parent['children'] = []
                        parent['children'].append(node)
                    else:
                        # Si no se encuentra padre, se asume que es nodo raíz
                        structure.append(node)
            
            logging.info("Estructura final: %s", structure)
            return structure

        except Exception as e:
            logging.error("Error al procesar el archivo %s: %s", self.file_path, e)
            raise
