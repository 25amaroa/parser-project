## Project Description
Parser project for Principles of Programming Languages

## Authors
Angela Amaro, Sophie Blick, Seth Keenen, Seth Ek, Kody McNamara


## Project requirments
A device capable of running Python atm

## How to get started
```bash
# Create your Python virtual environment
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
```bash
# Generate your grammar files
antlr -Dlanguage=Python3 -visitor -no-listener grammar/pythonGrammar.g4
```
```bash
# Run the program
python3 pythonDriver.py
```
## Project Demo
