# lindo-crl-api
Lindo Crl Official Rest Api 

https://api.lindocrl.org/docs

## Requirements

Python 3.6+

## Installation

<div class="termy">

```console
$ pip install -r requirements.txt

```
</div>

### Run it (locally)

<div class="termy">

```console
$ uvicorn main:app --reload

INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [28720]
INFO:     Started server process [28722]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

</div>

<details markdown="1">
<summary>About the command <code>uvicorn main:app --reload</code>...</summary>

The command `uvicorn main:app` refers to:

* `main`: the file `main.py` (the Python "module").
* `app`: the object created inside of `main.py` with the line `app = FastAPI()`.
* `--reload`: make the server restart after code changes. Only do this for development.

</details>


## Deploy (continuous delivery)
- Just commit/merge to master branch to deploy app in production.
