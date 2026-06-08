import requests
from datetime import datetime

url = "https://lichess.org/api/tournament"
response = requests.get(url)
data = response.json()
tournament_count = 0

for t in data['created'][:10]:
    tournament_count += 1
    start_time = datetime.fromtimestamp(t['startsAt'] / 1000) 
    print(f"number: {tournament_count}, \n ID: {t['id']}, \n Name: {t['fullName']}, \n  Starts at: {start_time}")
