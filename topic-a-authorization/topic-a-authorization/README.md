# Cybersecurity and National Defense -- Technical Project

## Topic A -- Authorization Policy Engine

---

## Group Members
TODO : Write here the name, surname, and student ID of all group members.

Example:
- Edoardo Arturo Cancelli -- s335716
- Francesca Malagodi -- s234567

---

## Project Description
This project implements a simple Attribute-Based-Access-Control (ABAC) Policy-based access control authorization engine. 

### Authorization pipeline
1) 

---

# Usage
```bash
usage: main.py [-h] --input INPUT --usaoutput OUTPUT

options:
  -h, --help       show this help message and exit
  --input INPUT    Input directory
  --output OUTPUT  Output JSON file
```
---

# Example 
``` bash
(.venv) PS C:\\Users\\user_1\\OneDrive\\Documenti\\GitHub\\Cybersecurity_Class_2026\\topic-a-authorization\\topic-a-authorization>  py main.py --input input --output output\output.json
```

---

## Project Structure

- `topic-a-authorization`
    - `input/`: example input files
    - `output/`: example output files
    - `src/`: Python modules used by the program
        - `engine.py`: authorization engine module
        - `loader.py`: json loading module
        - `tests.py`: policy tests module
        - `verify_json.py`: json verifier and parser module
    - `test_input/`: edge case testing input files
    - `test_output/`: edge case testing output files
    - `Group_Projects_Technical_part.pdf`: Project instructions      
    - `main.py`: main program
    - `README.md`: read me file

---

## Python Version
Python 3.12.6 (tested on windows 11)

---

## Required Libraries
This project uses only the following standard libraries : 
- `argparse` : argument parsing
- `pathlib` : linux - mac - windows compatible pathing
- `json` : json handling
- `typing` : type hints

---

## Creating a Virtual Environment
A virtual environment is recommended in order to install the project libraries in an isolated way.

### Linux / macOS
```bash
python -m venv .venv
source .venv/bin/activate
```

### Windows
```bash
python -m venv .venv
.venv\Scripts\activate
```