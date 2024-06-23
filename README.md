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
