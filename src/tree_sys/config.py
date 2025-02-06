import json
import logging
from typing import Any, Dict

def load_config(config_file: str) -> Dict[str, Any]:
    """
    Lee la configuración desde un archivo JSON y la devuelve como un diccionario.
    
    Se esperan, al menos, las siguientes claves:
      - "tree_file": ruta del archivo de texto con la estructura del árbol.
      - "output_dir": ruta raíz donde se guardarán los nuevos archivos y carpetas.
    
    :param config_file: Ruta al archivo de configuración en formato JSON.
    :return: Diccionario con la configuración.
    :raises: FileNotFoundError si no se encuentra el archivo.
             json.JSONDecodeError si hay un error al decodificar el JSON.
    """
    try:
        with open(config_file, 'r', encoding="utf-8") as f:
            config = json.load(f)
        logging.info("Configuración cargada correctamente desde %s", config_file)
        return config
    except FileNotFoundError as e:
        logging.error("No se encontró el archivo de configuración: %s", config_file)
        raise e
    except json.JSONDecodeError as e:
        logging.error("Error al decodificar el JSON en %s: %s", config_file, e)
        raise e
