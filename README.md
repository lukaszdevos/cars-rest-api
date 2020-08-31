# **Cars API**
:wrench: :wrench: :wrench:

Simply REST API on Django Rest Framework with postgresql

a basic cars makes and models database interacting with external [API](https://vpic.nhtsa.dot.gov/api/)

## Endpoints 

- :arrow_left: GET ``` /cars ``` returns list of all cars presented in database.
- :arrow_right: POST ``` /cars ``` interacting with external [API](https://vpic.nhtsa.dot.gov/api/) after POST request and check car make and model name if requested car exists in external [API](https://vpic.nhtsa.dot.gov/api/) is saved in database, if not returns an error. In case when requsted car is in database returned record from database. 
- :arrow_right: POST ``` /rate ``` rate choosen car from 1 to 5 .
- :arrow_left: GET ``` /popular ``` return top rated cars based on number of votes.

## .env config 
:lock: :lock: :lock:
1. Create file .env in /netguru_task/netguru_task/.env
2. Copy variables from .env_example to .env
3. Setup your variables

## Run project
:whale: :whale: :whale: 
1. Run with docker-compose
```
docker-compose up
```
- for tun test in docker
``` 
docker-compose run netguru_task bash -c "python manage.py test"
```


:house: :house: :house:
2. Run localy, without docker
```
pip install -r requirements.txt
```
```
python manage.py makemigrations && python manage.py migrate
```
```
python manage.py runserver
```
- for run test
```
python manage.py test
```



## License :copyright:
[MIT](https://choosealicense.com/licenses/mit/)