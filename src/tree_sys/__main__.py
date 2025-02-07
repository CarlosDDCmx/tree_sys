import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import logging
from tree_sys.tree_parser import TreeParser
from tree_sys.file_manager import create_structure
from tree_sys.config import load_config
from tree_sys.export import save_structure_to_json

# Configuración básica del logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def main() -> None:
    # Se asume que el archivo de configuración se llama 'config.json' y se encuentra en la raíz del proyecto.
    config_file = "config.json"
    
    try:
        config = load_config(config_file)
    except Exception as e:
        logging.critical("No se pudo cargar la configuración: %s", e)
        return

    tree_file = config.get("tree_file")
    output_dir = config.get("output_dir")
    json_out = config.get("json_out")
    
    if not tree_file or not output_dir:
        logging.critical("La configuración debe contener 'tree_file' y 'output_dir'.")
        return
    
    if not json_out:
        json_out = "estructure.json"
    
    parser = TreeParser(tree_file)
    
    try:
        structure = parser.parse()
        # Se guarda la estructura en un archivo JSON adicionalmente a crear la jerarquía.
        save_structure_to_json(structure, json_out)
        create_structure(structure, base_dir=output_dir)
    except Exception as e:
        logging.critical("Error en el procesamiento: %s", e)

if __name__ == "__main__":
    main()
