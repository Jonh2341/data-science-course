import requests
import json
import pandas as pd
from datetime import datetime
from bs4 import BeautifulSoup

# requests
url = "https://lichess.org/api/tournament"
responce = requests.get(url)
data = responce.json()

# write json
with open("lichessTournaments.json", 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
    
# read json
with open("lichessTournaments.json", "r", encoding='utf-8') as f:
    tournaments_json = json.load(f)

# types of tournaments
created_tournaments = tournaments_json['created']
finished_tournaments = tournaments_json['finished']
started_tournaments = tournaments_json['started']

user_prompt = input('In what tournaments you are interested in? (created, finished, started): ')

if user_prompt == 'created':
    df = pd.DataFrame(created_tournaments)
elif user_prompt == 'finished':
    df = pd.DataFrame(finished_tournaments)
elif user_prompt == 'started':
    df = pd.DataFrame(started_tournaments)
else:
    print('error')

# link is made here
df['link'] = 'https://lichess.org/tournament/' + df['id']
# time is converted here
df['startsAt'] = df['startsAt'].apply(lambda x: datetime.fromtimestamp(x / 1000))

# first 30 tournaments are printed
print(df[['link', 'fullName', 'nbPlayers', 'startsAt']][:30])

user_prompt2 = input('Do you want to find the tournament with the biggest amount of competitors? (yes, no): ')

# tournament with the biggest amount of players
if user_prompt2 == 'yes':
    max_players_t = df.loc[df['nbPlayers'].idxmax()]
    print(f'tournament with the biggest amount of players for now is: \n {max_players_t['fullName']} \n {max_players_t['nbPlayers']} \n {max_players_t['link']} \n {max_players_t['startsAt']}')

user_prompt3 = input("Do you want to find something in particular tournament? (yes, no): ")

def find_Specific_Tournament_By_Id(df, tournament_id):
    res = df[df['id'] == tournament_id]
    if not res.empty:
        t = res.iloc[0]
        return {
            "name": t['fullName'],
            "players": t['nbPlayers'],
            "link": t['link'],
            "startsAt": t['startsAt']
        }
    else:
        return None

if user_prompt3 == 'yes':
    user_prompt4 = input('Enter the id of the tournament below (for instance: 4TObh84E): ')
    result = find_Specific_Tournament_By_Id(df, user_prompt4)
    
    if result:
        print(f'Name: {result['name']}')
        print(f'Players: {result['players']}')
        print(f'Link: {result['link']}')
        print(f'StartsAt: {result['startsAt']}')
    else:
        print('Tournament not found.')