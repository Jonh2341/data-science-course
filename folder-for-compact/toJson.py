import requests
import json
import pandas as pd

url = "https://lichess.org/api/tournament"
response = requests.get(url)
data = response.json()

# we get only data in list 'created'
created = data['created']

# save to json
with open('tournaments.json', 'w', encoding='utf-8') as file:
    json.dump(created, file, ensure_ascii=False, indent=4)

# read json
with open('tournaments.json', 'r', encoding='utf-8') as file:
    tournaments_json = json.load(file)

# print(created[:3])
df = pd.DataFrame(tournaments_json)

print(df.head())

max_players_row = df.loc[df['nbPlayers'].idxmax()]
print(f'tournament with the biggest amount of players for now is: {max_players_row['fullName'], {max_players_row['nbPlayers']}, {max_players_row['id']}}')
