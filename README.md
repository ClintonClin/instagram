# Instagram clone
This is an application that enables users to log in, upload photos, view the photos in their profile, search other users, follow them.
 They will be able to view their photos as well as like and comment on them.   

#### Web clone of the Instagram app
#### By [Clinton Okerio](https://github.com/ClintonClin)

## Description
Instagram is a simple clone of the actual Instagram website. A user is able to create an account and then sign in. 
Once signed in, the user can upload photos, follow other users and comment on their photos.

## Set Up and Installations

### Prerequisites
1. Django
2. Python3.6
3. [Postgres](https://www.postgresql.org/download/)
4. Virtual environment.

### Clone the Repo
Run the following command on the terminal:
`git clone git@github.com:ClintonClin/instagram.git`

### Activate virtual environment
Activate virtual environment.
```
python3.6 -m venv --without-pip virtual && source virtual/bin/activate. 
```

### Install dependancies
Install dependancies that will create an environment for the app to run.
`pip3 install -r requirements.txt`

### Create the Database
```
psql
name=# CREATE DATABASE (name-of-app-database);
```
### .env file
Create .env file and paste paste the following filling where appropriate:
```python
SECRET_KEY = '<Secret_key>'
DBNAME = 'name-of-app-database'
USER = '<Username>'
PASSWORD = '<password>'
DEBUG = True

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = '<your-email>'
EMAIL_HOST_PASSWORD = '<your-password>'
```
### Run initial Migration
```bash
python3.6 manage.py makemigrations _name-of-app_
python3.6 manage.py migrate
```

### Run the app
```
python3.6 manage.py runserver
```
Open the browser on `http://localhost:8000/`

## Technologies used
    - Python 3.6
    - HTML
    - Bootstrap 4
    - JavaScript
    - Heroku
    - Postgresql

### License
Copyright (c) **Clinton Okerio**

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
 