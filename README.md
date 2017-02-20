 ---------------------------------------------
## LEM
Luizalabs Employee Manager

### Tools
Python, Django Web Framework and Tastypie

### My first system in Python
I enyoed that opportuniy about learning Python. I remembered ruby on rails :)

### Services:
	- GET /api/v1/department/?format=json
	- DELETE /api/v1/department/{id}/
	- POST /api/v1/department/
	- GET /api/v1/department/{id}/
	- GET /api/v1/employee/?format=json
	- DELETE /api/v1/employee/{id}/
	- POST /api/v1/deparemployeetment/
	- GET /api/v1/employee/{id}.
    - GET /admin
	- GET /admin/auth/group
    - GET /admin/auth/user
    - GET /admin/employees/department
    - GET /admin/employees/employee

### Samples API
	- curl -X POST -H "Content-Type: application/json" -d '{"name":"Architecture"}' http://localhost:8000/api/v1/department/
	- curl -X GET http://localhost:8000/api/v1/department/Architecture/
	- curl -X GET http://localhost:8000/api/v1/department/
	- curl -X DELETE http://localhost:8000/api/v1/department/Architecture/
	- curl -X GET http://localhost:8000/api/v1/employee/
	- curl -X GET http://localhost:8000/api/v1/employee/9793ca81-e813-497a-944d-1f01220a18bc/ 
	- curl -X DELETE http://localhost:8000/api/v1/employee/9793ca81-e813-497a-944d-1f01220a18bc/
	- curl -X POST -H "Content-Type: application/json" -d '{"name":"Leandro", "email":"leandro.miserani@magazineluiza.com.br","department":{"name": "Architecture"}}' http://localhost:8000/api/v1/employee/

### Repository
```sh
$ 
```
### Health Check API
	- healthcheck/

### Start application
```sh
$ git clone https://github.com/lemiserani/employee.git 
$ cd employee

$ pip3.4 install -U -r requirements.txt

$ python3.4 manage.py makemigrations
$ python3.4 manage.py migrate
$ python3.4 manage.py createsuperuser
$ python3.4 manage.py runserver
```

### Test - Coverage
```sh
$ cd employee
$ python3.4 -m coverage  run manage.py
$ python3.4 manage.py test
```
---------------------------------------------

[doc]:https://www.python.org/
[doc]:https://www.djangoproject.com/
[doc]:http://django-tastypie.readthedocs.io
[doc]:https://pypi.python.org/pypi/django-health-check
[doc]:http://django-testing-docs.readthedocs.io/en/latest/coverage.html
