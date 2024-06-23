# Catalog Prizes REST API

This is a REST API exercise built with Flask.

## Requirements
Packages:
- pipenv
- pyenv (to install the python according version)
- bash

## First time
Create a new `.env` file, use the `.env.example` to do so
```bash
$ cp .env.example .env
```

Install then all the dependencies with using pipenv
```bash
pipenv install --dev
```

## Usage
Start the local server
```bash
make serve
```

## Testing
Execute the available tests
```bash
make test
```

or simply list the available python tests
```bash
make list-test
```

## Notes
There are many improvements that can be applied:
- swagger doc
- instead of having multiple `try catch` create custom exceptions to handle query parameters validation
- more in depth tests
- versioning with a separate file and not hardcoded in pyproject.toml
- add as a function parameter the database instead of hardcode it inside the function
- add logger
