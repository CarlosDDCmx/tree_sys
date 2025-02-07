# Tree Sys

[Español](/README.md) | [English](/Docs/README_en.md) |

A simple script to generate a whole structure from a tree in a plain text file.

## Table of Contents

- [Features](#features)
- [Technologies Used](#used-technologies)
- [Installation](#installation)
- [Usage](#usage)
- [Contact](#contact)

## Features

- **Parsing Tree Structures from Text:**
  The project includes a specialized module to read a text file containing a tree structure representation.  Delimiter characters can be used to identify levels and convert the structure into a JSON format (list of dictionaries).

- **Generation of Files and Directories:**
  Based on the parsed structure, the corresponding module automatically creates folders and files in the file system.

- **Configuration via a JSON File:**
  A configuration module is incorporated, allowing you to define key variables (such as the path to the text file containing the tree and the root path where the new files and folders will be generated) using a JSON file. This eliminates the need to directly modify the source code.

- **Error Handling and Logging:**
  The project implements error handling using `try/except` blocks and utilizes the `logging` module to record events, errors, and the execution flow.

- **Export structure to JSON:**
  It contains a module to export the resulting structure to a JSON file.

## Used Technologies

Originally developed in Python 3.11.5 with base libraries.

## Installation

Cloning the project should be sufficient.

Clone the repository:
   ```
   git clone https://github.com/CarlosDDCmx/tree_sys.git
   ```

## Usage

Create a config.json file in the root of the project and add the values for **tree_file** to indicate the file from which the tree will be read, and **output_dir** will be the root from which all files and folders will be generated.

An example file is as follows:

```
├── My project/
│   └── Files/
│       ├── text1.txt
│       ├── text2.txt
│       ├── information.md
│       └── simple_code.py
└── README.md
```

## Contact

- Carlos D. Díaz Cano
- e-mail: carlosd.dc.mx@gmail.com
- [Mi GitHub] (https://github.com/CarlosDDCmx)