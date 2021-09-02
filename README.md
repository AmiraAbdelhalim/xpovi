# xpovi


answering a questionnaire or more to get a business plan.


## Tech

- Django rest-framework
- PostgreSQL

## Installation


create virtual environment and activate it

```sh
virtualenv <env-name>
source <env-name>/bin/activate
```

install requirements

```sh
pip install -r requirements.txt
```

migrate db

```sh
./manage.py makemigrations
./manage.py migrate
```

create super user

```sh
./manage.py createsuperuser
```

run server

```sh
./manage.py runserver
```
login to the admin page `127.0.0.1:8000/admin` to create questionnaire questions.

## endpoints

- get access token to login
- get refresh token
- get section 1 question
- get section 2 question
- get trial number for logged in user
- submit new questionnaire
- update submissions answers
