# openweather-demo-python

## Context
This project is created to learn the API of OpenWeather and Python programming language.

## Prerequisites
Create database and table using script in folder `sql`  

## Install dependencies
### Use virtual environment
python -m venv venv

### Activate virtual environment
venv\Scripts\activate

### Install dependencies
pip install -r requirements.txt

### Deactive virtual environment
deactivate

## How to run project
python main.py

## How to test
Import Postman collection script in folder `postman`  

## Dependency
Python 3.x  
FastAPI Framework  (Web framework)  
Pydantic (for configuration)  
SQL Alchemy (ORM library)  
MySQL Client (Driver)  
AIOHTTP (for calling external API)  

## Others
### List all installed dependencies and export to text file (you can also use pipreqs)
pip freeze > requirements.txt

### Remove dependencies
pip uninstall -r requirements.txt

### Remove all dependencies
pip uninstall -r requirements.txt -y

## List outdated packages
pip list --outdated

## Upgrade package
pip install -U fastapi

## Check missing dependencies
python -m pip check

