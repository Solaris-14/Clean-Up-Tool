# Directory Cleaner
A lightweight python-based directory cleaner that runs as a CLI and can be used for messy folders like Downloads or more. 
---
## Features
- **Automatic File Organization**: The CLI automatically sorts and moves your files based on predefined categories such as **Music**, **Documents**, or **Archives**.
- **Extension Filtering**: You can sort for specific extensions like `.png` or `.bat` by using the `-ext` argument.
- **Custom Directory Target** - By default, the program sorts the directory it is located in, but you can set a custom directory by supplying a file path using `-dir`.
- **Safe Execution**: Ensures that folders are created only when moving files, and for categories that have been identified.

## Pre-requisites
- Python 3.7 or higher

## Usage
Simply run the script from your terminal:
```bash
python main.py [OPTIONS]
```
## Licensing
This project is open source, under the MIT license.


