import requests
from datetime import datetime

# PART 1: getting data from the API nutritionix
#------------------------------------------------------------------------------------------------------
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


# PART 2: get the data returned by nutritionix into sheety
#----------------------------------------------------------------------------------------------------
#Making requests on sheety
projectName = "myWorkouts"
sheetName = "workouts"
bearer_headers = {
"Authorization": "Bearer IBOjg2kf5C4ct72NrCmtSjcGAjnchIcv"
}
sheety_API_URL = "https://api.sheety.co/10fce03195300cfd5c84ea323144da6f/"+projectName+"/"+sheetName
sheety_response = requests.get(url=sheety_API_URL, headers=bearer_headers)
sheety_response.raise_for_status()
sheety_result = sheety_response.json()
print(sheety_result)

#Post request on sheety

# Parsing the date and time
today = datetime.now()
the_date = today.strftime("%d/%m/%Y")
the_time = today.strftime("%H:%M:%S")

# posting workouts into sheety API
for workout in result["exercises"]:
    workout_date = the_date
    workout_time = the_time
    exercise_name = workout["name"]
    duration = workout["duration_min"]
    calories = workout["nf_calories"]
    tag_id = workout["tag_id"]

    data = {
        'workout':
                        {
                        'date': workout_date,
                        'time': workout_time,
                        'exercise': exercise_name,
                        'duration': duration,
                        'calories': calories,
                        'id': tag_id
                        }
    }
    sheety_post_response = requests.post(url=sheety_API_URL, json=data, headers=bearer_headers)
    print("response.status_code =", sheety_post_response.status_code)