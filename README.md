# aspect_extractor
This project is in collaboration with the University of Paris for aspect extractor.

## Installation

Make sure you have [python 3 and pip ](https://www.python.org/downloads/) up and running on your machine.

### 1. Virtual environment
Create virtual environment by typing the folowing command

```bash
python3 -m venv env  
```
activate the environment by typing :
```bash
source ./env/bin/activate
```

### 2. Install dependencies
Type de following command to install all dependencies.

```bash
pip3 install -r requirements.txt
```

### 3. Install Spacy language
After installing dependencies, you'll need to downlaod Spacy language model (english one) by tytping the following commands :

```bash
pip3 install -U pip setuptools wheel
python3 -m spacy download en_core_web_sm
```
## Starting project
While environment running, go to the root of the project and type the following command :
```bash
python3 app.py
```
The flask server should start-up.
When the server is up and running, click [here](http://localhost:8000/)
