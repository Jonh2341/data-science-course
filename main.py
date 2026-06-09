import requests
import csv
from datetime import datetime

url = "https://lichess.org/api/tournament"
response = requests.get(url)
data = response.json()
tournament_count = 0

with open('tournaments.csv', 'w', newline='', encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(['Number', 'ID', 'Name', 'StartsAt'])

    for i, t in enumerate(data['created'][:10], start=1):
        # tournament_count += 1
        start_time = datetime.fromtimestamp(t['startsAt'] / 1000) 
        writer.writerow([i, t['id'], t['fullName'], start_time])
    