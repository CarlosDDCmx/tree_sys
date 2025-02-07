import json
import logging
from typing import List, Dict, Any

def save_structure_to_json(structure: List[Dict[str, Any]], output_file: str) -> None:
    """
    Guarda la estructura parseada en un archivo JSON.

    :param structure: Lista de diccionarios que representa la estructura del árbol.
    :param output_file: Ruta del archivo JSON donde se guardará la estructura.
    """
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(structure, f, ensure_ascii=False, indent=4)
        logging.info("Estructura guardada correctamente en %s", output_file)
    except Exception as e:
        logging.error("Error al guardar la estructura en %s: %s", output_file, e)
        raise