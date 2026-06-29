import requests
import json
import pandas as pd

userlichess = input('name of the lichess user: ').rstrip()

def is_lichessuser_playing(user):
    url = f'https://lichess.org/api/user/{userlichess}'

    responce = requests.get(url)
    data = responce.json()

    with open('lichessuser.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    with open('lichessuser.json', 'r', encoding='utf-8') as f:
        lichessUser_json = json.load(f)
    
    try: 
        if lichessUser_json['playing']:
            print(f'currently playing: {lichessUser_json['playing']}')
        else:
            print('error')
    except KeyError:
        print(f"{user} is not playing currently.")

    question = input(f'do you want basic info about {user}? (yes, no): ')

    if question == 'yes':
        user_info = data['perfs']
        df = pd.DataFrame(user_info)
        print(df.head())
    elif question == 'no':
        print('ok.')
    else:
        print('error')

is_lichessuser_playing(userlichess)




