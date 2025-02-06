import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import tempfile
import unittest
import json
from tree_sys.config import load_config

class TestConfigModule(unittest.TestCase):
    def setUp(self):
        # Se crea un directorio temporal para los archivos de prueba
        self.temp_dir = tempfile.mkdtemp()

    def tearDown(self):
        # Se eliminan los archivos y el directorio temporal
        for filename in os.listdir(self.temp_dir):
            file_path = os.path.join(self.temp_dir, filename)
            os.remove(file_path)
        os.rmdir(self.temp_dir)

    def test_load_valid_config(self):
        """Verifica que se cargue correctamente un archivo JSON de configuración válido."""
        # Creamos un archivo de configuración válido
        config_data = {
            "tree_file": "estructura.txt",
            "output_dir": "output_structure"
        }
        config_path = os.path.join(self.temp_dir, "config_valid.json")
        with open(config_path, "w", encoding="utf-8") as f:
            json.dump(config_data, f)
        
        # Cargamos la configuración
        loaded_config = load_config(config_path)
        self.assertIsInstance(loaded_config, dict)
        self.assertEqual(loaded_config.get("tree_file"), "estructura.txt")
        self.assertEqual(loaded_config.get("output_dir"), "output_structure")

    def test_config_file_not_found(self):
        """Verifica que se lance FileNotFoundError cuando el archivo de configuración no existe."""
        config_path = os.path.join(self.temp_dir, "non_existent_config.json")
        with self.assertRaises(FileNotFoundError):
            load_config(config_path)

    def test_invalid_json_config(self):
        """Verifica que se lance json.JSONDecodeError cuando el contenido del archivo no es JSON válido."""
        config_path = os.path.join(self.temp_dir, "config_invalid.json")
        # Escribimos contenido inválido
        with open(config_path, "w", encoding="utf-8") as f:
            f.write("Este no es un JSON válido")
        
        with self.assertRaises(json.JSONDecodeError):
            load_config(config_path)

if __name__ == '__main__':
    unittest.main()
