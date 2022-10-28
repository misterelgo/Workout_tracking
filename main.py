import requests

APP_ID = "6f0d5b5b"
API_KEY = "ee9c92be749ce50e3eb1f779def831e9"

header = {
    "x-app-id": APP_ID,
    'x-app-key': API_KEY
}
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

GENDER = "MALE"
WEIGHT_KG = "82"
HEIGHT = "193.5"
AGE = "25"

exercise_input = input("Tell which exercise you did today?: ")

parameters = {
    'query': exercise_input,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT,
    "age": AGE,
}

response = requests.post(url=exercise_endpoint, json=parameters, headers=header)
response.raise_for_status()
result = response.json()
print(result, len(result["exercises"]))

#Making requests on sheety
projectName = "myWorkouts"
sheetName = "workouts"

sheety_API_URL = "https://api.sheety.co/10fce03195300cfd5c84ea323144da6f/"+projectName+"/"+sheetName
sheety_response = requests.get(url=sheety_API_URL)
sheety_response.raise_for_status()
sheety_result = sheety_response.json()
print(sheety_result)

