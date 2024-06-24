# Catalog Prizes REST API

This is a REST API exercise built with Flask.

## Requirements
Packages:
- pipenv
- pyenv (to install the python according version, python 3.12, see [Pipfile](./Pipfile))
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

Refer to the [OpenAPI doc](./swagger.yaml), open it with the [Swagger Editor](https://editor.swagger.io)

## Testing
Execute the available tests
```bash
make test
```

or simply list the available python tests
```bash
make list-test
```

Testing the endpoint with curl:
```bash
# expected total to be one and prize to be id 3 and OK 200 status
$ curl -X GET http://127.0.0.1:5000/api/catalog/1/prizes\?id\=3\&description\=ancient
```

```bash
#  page and per_page must be provided toghethere or not provided and status 400
$ curl -X GET http://127.0.0.1:5000/api/catalog/1/prizes\?page\=3
```

```bash
#  page and per_page must be provided toghethere or not provided and status 400
$ curl -X GET http://127.0.0.1:5000/api/catalog/1/prizes\?per_page\=3
```

```bash
# page and per_page must be integer and status 400
$ curl -X GET http://127.0.0.1:5000/api/catalog/1/prizes\?page\=3\&per_page\=e
```

```bash
# expected total to be 1 and an OK 200 status
$ curl -X GET http://127.0.0.1:5000/api/catalog/1/prizes\?page\=3\&per_page\=3
```

```bash
# expected total to be 2 and an OK 200 status
$ curl -X GET http://127.0.0.1:5000/api/catalog/1/prizes\?page\=1\&per_page\=2
```

```bash
# expected total to be 1 and an OK 200 status
$ curl -X GET http://127.0.0.1:5000/api/catalog/1/prizes\?page\=2\&per_page\=2
```

## Notes
There are many improvements that can be applied:
- instead of having multiple `try catch` create custom exceptions to handle query parameters validation
- more in depth tests
- versioning with a separate file and not hardcoded in pyproject.toml
- add as a function parameter the database instead of hardcode it inside the function
- add logger
