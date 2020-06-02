# REMS (Real estate management system)

A full stack project which uses django for the backdend and postgres as the database and javascript for the frontend. It is used to manage property listings online.

### Installation
REMS requires python , postgres ,django .

So first install postgres and setup a postgres username and password
then create a database named rems


```sh
$ sudo apt-get install python-psycopg2
$ sudo apt-get install libpq-dev
```
Clone the repo and setup a virtual env if you want to
```sh
$ pip install django psycopg2 pillow
$ python manage.py migrate
$ python manage.py createsuperuser
$ python manage.py runserver
```

