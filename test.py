from datetime import datetime
workout_exercise = {
    'tag_id': 317,
    'user_input': 'run',
    'duration_min': 31.08,
    'met': 9.8,
    'nf_calories': 416.26,
    'photo': {'highres': 'https://d2xdmhkmkbyw75.cloudfront.net/exercise/317_highres.jpg',
              'thumb': 'https://d2xdmhkmkbyw75.cloudfront.net/exercise/317_thumb.jpg', 'is_user_uploaded': False},
    'compendium_code': 12050,
    'name': 'running',
    'description': None,
    'benefits': None
}

print(workout_exercise["tag_id"])

today = datetime.now()
print(today)
the_date = today.strftime("%d/%m/%Y")
the_time = today.strftime("%H:%M:%S")
print(the_time)
print(the_date)

exercie = [
	{'tag_id': 317, 'user_input': 'run', 'duration_min': 31.08, 'met': 9.8, 'nf_calories': 416.26, 'photo': {'highres': 'https://d2xdmhkmkbyw75.cloudfront.net/exercise/317_highres.jpg', 'thumb': 'https://d2xdmhkmkbyw75.cloudfront.net/exercise/317_thumb.jpg', 'is_user_uploaded': False}, 'compendium_code': 12050, 'name': 'running', 'description': None, 'benefits': None},
	{'tag_id': 5, 'user_input': 'cycled', 'duration_min': 20, 'met': 10, 'nf_calories': 273.33, 'photo': {'highres': 'https://d2xdmhkmkbyw75.cloudfront.net/exercise/5_highres.jpg', 'thumb': 'https://d2xdmhkmkbyw75.cloudfront.net/exercise/5_thumb.jpg', 'is_user_uploaded': False}, 'compendium_code': 1040, 'name': 'road cycling', 'description': None, 'benefits': None}
	]

for workout in exercie:
    print(workout)