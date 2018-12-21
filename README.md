[![Build Status](https://travis-ci.org/nesh-dev/unsullied-DRF.svg?branch=develop)](https://travis-ci.org/nesh-dev/unsullied-DRF)

# Unsullied TODO list
This repository contains Api endpoints for Unsullied TODO list.Unsullied TODO list is a django REST api that performs simple CRUD operations on a TODO list.The application allows users to add to a list of things they want to do,Edit existing things they want to do, Delete some of the task they had listed to do and mark done the things they have done on the list.

### The minimum required endpoint are
| Endpoint | Description |
| --- | --- |
| POST/Add to the list | This endpoint adds a new task to the TODO list |
|GET/List all tasks | This endpoint lists all tasks in the TODO list|
|GET/List single task | This endpoint lists a single task in the TODO list |
|UPDATE/Edit existing task | This endpoint edits an existing task in the TODO list |
|DELETE/Drop an existing task | This endpoint deletes and existing task from the TODO list |

### How to run the application
- Download the application
```
   Open the terminal
   git clone https://github.com/nesh-dev/unsullied-DRF.git
```
- configure the application and dependancies
```
  cd unsullied-DRF
  python3 -m venv venv
  source venv/bin/activate
  pip install -r requirements.txt
  python manage.py makemigrations
  python manage.py migrate
  ```
- Run the application
```
   python manage.py runserver
```
### How to run the tests
- Download the application
```
   Open the terminal
   git clone https://github.com/nesh-dev/unsullied-DRF.git
```
- configure the application and dependancies
```
  cd unsullied-DRF
  python3 -m venv venv
  source venv/bin/activate
  pip install -r requirements.txt
  python manage.py makemigrations
  python manage.py migrate
  ```
- Run the application
```
   python manage.py tests
```

### Team Members
[Kwanj](https://pages.github.com/kwanj-k).
[Nesh](https://pages.github.com/nesh-dev).
[Sly](https://pages.github.com/sylviawanjiku).
[Kelvin](https://pages.github.com/kelvinwm).
[Allan](https://pages.github.com/Allan690).
[Sammy](https://pages.github.com/mbugwasami).
