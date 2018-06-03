### Instructions

* clone repository

* create virtualenv

* create .env (use .env.dist as an example)

`pip install -r requirements.txt`

`python manage.py migrate`

`python manage.py generate_data` (took 20 seconds)

`python manage.py createsuperuser`

`python manage.py runserver`

user view: http://localhost:8000/

admin panel: http://localhost:8000/admin

### Results
* categories: 1364
* products: 13806
* load time 10s

![alt text](results.png)