#### Installation
pip install fastapi pymongo pydantic pydantic_settings "uvicorn[standard]"

> Import cv-control.lists.json to mongodb 

#### The command ``uvicorn main:app --reload`` refers to:

- main: the file main.py (the Python "module").
- app: the object created inside of main.py with the line app = FastAPI().
- --reload: make the server restart after code changes. Only do this for development.