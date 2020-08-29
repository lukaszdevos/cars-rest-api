import requests, json
from django.core.exceptions import ValidationError

def car_validator(request_post_car_make, request_post_car_model):
    url = 'https://vpic.nhtsa.dot.gov/api/vehicles/getmodelsformake/'+request_post_car_make+'?format=json'
    r = requests.get(url)
    response_dict_model_name = json.loads((r.text))
    results_for_model_name = response_dict_model_name['Results']
    model_name = []
    for i in results_for_model_name:
        model_name.append(i['Model_Name'])
    if request_post_car_model in model_name:
        return True
    else:
        return False

def exists(request_post_car_make, request_post_car_model):
    if request_post_car_make and request_post_car_model:
        return True
    else:
        return False


