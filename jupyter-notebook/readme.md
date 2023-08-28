# Run Jupiter locally:

## create venv

```
cd ./data-exploration
python -m venv venv
```

## restart vscode

```
code -r .
```

## work with venv

- activate:

```bash
# unix
source venv/bin/activate

# windows
venv\Scripts\activate
```

- deactivate:

```
deactivate
```

## install jupyter and ipykernel

```
pip install jupyter
pip install ipykernel
```

## Create new kernel

```bash
# example
python -m ipykernel install --user --name=myproject
```

## start jupyter

```
jupyter notebook
```

## Select kernel for project

- Open the VSCODE search bar: cmd+shift+p
- Type in & choose: c

## Requirements

```
pip freeze > requirements.txt
pip install -r requirements.txt
```

# Run Jupiter with Docker: