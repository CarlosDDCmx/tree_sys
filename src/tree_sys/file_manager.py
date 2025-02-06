import logging
from pathlib import Path
from typing import List, Dict, Any

def create_folder(path: Path) -> None:
    """
    Crea una carpeta en la ruta especificada.
    """
    try:
        path.mkdir(parents=True, exist_ok=True)
        logging.info(f"Carpeta creada: {path}")
    except Exception as e:
        logging.error(f"Error al crear la carpeta {path}: {e}")
        raise

def create_file(path: Path, content: str = "") -> None:
    """
    Crea un archivo en la ruta especificada y escribe el contenido.
    """
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open('w', encoding='utf-8') as file:
            file.write(content)
        logging.info(f"Archivo creado: {path}")
    except Exception as e:
        logging.error(f"Error al crear el archivo {path}: {e}")
        raise

def process_item(item: Dict[str, Any], base_path: Path) -> None:
    """
    Procesa recursivamente cada item (archivo o carpeta) de la estructura.
    """
    try:
        name: str = item["name"]
        is_folder: bool = item["is_folder"]
        current_path: Path = base_path / name

        if is_folder:
            create_folder(current_path)
            children = item.get("children", [])
            if not isinstance(children, list):
                raise ValueError("La clave 'children' debe ser una lista.")
            for child in children:
                process_item(child, current_path)
        else:
            create_file(current_path)
    except Exception as e:
        logging.error(f"Error al procesar el item {item}: {e}")
        raise

def create_structure(data: List[Dict[str, Any]], base_dir: str = ".") -> None:
    """
    Recibe la estructura (lista de diccionarios) y crea la jerarquía
    de archivos y carpetas a partir de un directorio base.
    """
    base_path: Path = Path(base_dir).resolve()
    logging.info(f"Creando estructura en: {base_path}")
    for item in data:
        process_item(item, base_path)
