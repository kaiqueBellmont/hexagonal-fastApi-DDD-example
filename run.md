## How to Run the Project:

#### First create a .env file in `configurator/` with [this](app/configurator/.env-example) example.

### In the Docker (Recomended):
**you need to have Docker installed. If you don't have it, you can download it by clicking [here](https://www.docker.com/)**

#### To run:
_(At the Root of the Project)_


```
docker compose up --build
```
**_This will start the database and backend containers. Don't worry because the tables will be created automatically._**

### Using:
**You can check here the [Postman Collection](WYD.postman_collection.json)**

_Just import it in postman APP_


### To Stop:
```
docker compose down -v
```

ps: 
_Some Docker version will need a `-` between comands, like:_

```
docker-compose (...)
```

### Or you can do this manually:

## Running locally:

- 1: Create a local Database (Check [here](app/configurator/.env-example) the data to be used)


- 2: Check your `/configurator/.env` file (The entire application uses this file) Use [this](app/configurator/.env-example) example


- **Make sure your db is running and its URL looks like this: `postgresql://user:password@db:5434/wyd_db`**


- ps: **_you need to have [postgres](https://www.postgresql.org/download/) installed_**

- 3: Create a venv:

```
python -m venv venv
```
```
venv\Scripts\activate
```
```python 
pip install -r requirements.txt
```

- 3: use the command (at the root):
```python 
 uvicorn app.adapters.entrypoints.application:app --reload --host 0.0.0.0 --port 8000
```

**To finish, you just `CTR + C` in the terminal**
