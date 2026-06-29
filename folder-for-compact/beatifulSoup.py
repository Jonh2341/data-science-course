import requests
from bs4 import BeautifulSoup
import json

url = 'https://lichess.org/tournament/TVLlxNb7'
responce = requests.get(url)

soup = BeautifulSoup(responce.text, 'html.parser')

players_script = soup.find("script", {'id': 'page-init-data'})

data = json.loads(players_script.string)
competitots = data['data']['standing']['players']

pairs = [competitots[i:i+2] for i in range(0, len(competitots), 2)]

# for c in competitots[:10]:
#     print(c['name'], c['rating'], c['score'])

for pair in pairs[:5]:
    for c in pair:
        print(c['name'], c['rating'], c['score'])

    print('---------')