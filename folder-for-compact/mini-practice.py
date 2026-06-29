import requests
import json
# from bs4 import BeautifulSoup

def get_tournament_rating(url):
    responce = requests.get(url)

    data = responce.json()

    standing = data['standing']

    with open('hourlyBlitz.json', 'w', encoding='utf-8') as f:
        json.dump(standing, f, ensure_ascii=False, indent=4)

    with open('hourlyBlitz.json', 'r', encoding='utf-8') as f:
        standing_players = json.load(f)

    for p in standing_players['players']:
        print(f'player: {p['name']} \n rank: {p['rank']} \n rating: {p['rating']} \n score: {p['score']}')

get_tournament_rating('https://lichess.org/api/tournament/4qaG8GDL')
