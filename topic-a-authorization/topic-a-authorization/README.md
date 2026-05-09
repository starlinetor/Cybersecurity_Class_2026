# Cybersecurity and National Defense -- Technical Project

## Topic A -- Authorization Policy Engine

---

## Group Members
- Edoardo Arturo Cancelli -- s335716
- Francesca Malagodi -- s336645

---

## Project Description
This project implements a simple Attribute-Based-Access-Control (ABAC) Policy-based access control authorization engine. 

### Authorization pipeline
1. The main file loads the json file as raw data utilizing the provided loader module
2. The main file parses the raw json to the verify json module 
    1. Checks if the raw data is the correct data type (eg : subjects.json should be a dict)
    2. The file checks if the main keys in the data are present (eg : a subject should have a role and a clearance)
    3. The data is stored in a more particle datatype (eg : subjects are stored as a dict with they id as a key)
    4. An exception is raised if the file is wrongly formatted (only keys are checked datatype are assumed correct)
3. The main file sends the parsed data to the verification policy engine
4. The engine iterates on the request stack analyzing each one
5. For each request the engine Searches the first matching policy
    1. For each policy the engine iterates on the TEST_LIST
    2. The TEST_LIST is a list of functions that test for a specific policy argument, the tests are handled by the tests.py module
6. Once all policies are tested or a matching one is found the engine writes the report on the request
7. Requests are combined for the final report that is dumped in the output.json file

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