# advertising-locations-backend

Web API wrapper for the module - backend part

### [Module](https://github.com/digital-fracture/advertising-locations)
#### [Documentation](https://digital-fracture.github.io/advertising-locations)

### [Website](https://card-mu-lyart.vercel.app/)

### [Folder with notebooks and other sources](https://drive.google.com/drive/folders/1_mlXCOj2t3n2GSYQgjePXLy0It9COIET?usp=sharing)


## Run by yourself

### Python package is available at [PyPI](https://pypi.org/project/advertising-locations)

### Pipenv

```shell
git clone https://github.com/digital-fracture/advertising-locations-backend
cd advertising-locations-backend
pipenv install
pipenv run uvicorn main:app
```

### Pure python 3.11

Windows (PowerShell) (not tested):
```powershell
git clone https://github.com/digital-fracture/advertising-locations-backend.git
cd advertising-locations-backend
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn main:app
```

Linux / MacOS:
```shell
git clone https://github.com/digital-fracture/advertising-locations-backend.git
cd advertising-locations-backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app
```

## Stack

- [python 3.11](https://python.org) - programming language
- [advertising-locations](https://pypi.org/project/advertising-locations) - ML processor
- [FastAPI](https://pypi.org/project/fastapi) - web server engine
- And more
