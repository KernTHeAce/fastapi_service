# Test Task FastAPI service

### Requirements:

- Pythons version: 3.8.*

### Links
- [INSTALLATION](#installation)
- [RUNNING](#running)
- [USEFUL COMMANDS](#useful-commands)


# [Installation](#links)

For Linux
```bash
python3 -m venv venv
source venv/bin/activate
python install -r requirements.txt
```

# [Running](#links)

```bash
python -m uvicorn src.server.__main__:app --reload 
```
`--reload`: make the server restart after code changes

# Useful Commands

## Running tests

```bash
pytest tests
```

## Running black for code formatting

```bash
black . --line-length 120
```

## Running isort for sorting imports

```bash
isort . --line-length 120
```

## Running pylint for code analysing

```bash
pylint src
pylint tests
```
