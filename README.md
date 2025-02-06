# Tree Sys

[Español](/README.md) | [English](docs/README_en.md) |

Una pequeño programa para generar todos los archivos y carpetas a partir de un árbol hecho en texto plano.

## Tabla de Contenidos

- [Características](#características)
- [Tecnologías Usadas](#tecnologías-usadas)
- [Instalación](#instalación)
- [Uso](#uso)
- [Contacto](#contacto)

## Características

- **Parseo de Estructuras de Árbol desde Texto:**  
  El proyecto incluye un módulo especializado para leer un archivo de texto con la representación de una estructura de árbol. Se puede utilizar caracteres delimitadores para identificar niveles y convertir la estructura en un formato JSON (lista de diccionarios).

- **Generación de Archivos y Directorios:**  
  A partir de la estructura parseada, el módulo correspondiente crea de forma automática carpetas y archivos en el sistema de archivos.

- **Configuración a través de un Archivo JSON:**  
  Se incorpora un módulo de configuración que permite definir variables clave (como la ruta del archivo de texto con el árbol y la ruta raíz donde se generarán los nuevos archivos y carpetas) mediante un archivo JSON. Así no es necesario modificar directamente el código fuente.

- **Manejo de Errores y Logging:**  
  El proyecto implementa manejo de errores mediante bloques `try/except` y utiliza el módulo `logging` para registrar eventos, errores y el flujo de ejecución.


## Tecnologías Usadas

Desarrollado originalmente en Python 3.11.5 con librerías base.

## Instalación

Debería bastar con clonar el proyecto

Clona el repositorio:
   ```
   git clone https://github.com/CarlosDDCmx/tree_sys.git
   ```

## Uso

Crea un archivo config.json en la raíz del proyecto y agrega los valores de **tree_file** para indicar el archivo del cual se leerá el árbol y **output_dir** será en la raíz desde donde se generarán todos los archivos y carpetas.

Un ejemplo de archivo es el siguiente:

```
├── Mi proyecto/
│   └── Archivos/          
│       ├── texto1.txt       
│       ├── texto2.txt       
│       ├── información.md    
│       └── codigo_simple.py
└── README.md
```


## Contacto

Carlos D. Díaz Cano
Correo: carlosd.dc.mx@gmail.com
[Mi GitHub] (https://github.com/CarlosDDCmx)

