The code is executed on intelliJ. For VSCode environment might differ.
Use below library versions to run this project 

uvicorn>=0.16.0,<0.18.0
requests>=2.24.0,<2.32.0
fastapi>=0.104.0
pydantic==2.10.6
pydantic-settings==2.8.1
numpy>=1.26.0,<2.0.0

Name: pydantic
Version: 2.10.6


Name: pydantic-settings
Version: 2.8.1


Name: PyYAML
Version: 6.0

Replace your .whl with existing one to run your code.

You must decide whether you want to stay on FastAPI < 1.0.0 (older and stable, but pydantic v1), or move to FastAPI 0.104.0+ (pydantic v2 support).
