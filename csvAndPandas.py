import requests
import csv
import pandas as pd
from datetime import datetime

url = "https://lichess.org/api/tournament"
response = requests.get(url)
data = response.json()
# tournament_count = 0

with open('tournaments.csv', 'w', newline='', encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(['Number', 'ID', 'Name', 'StartsAt'])
    data_list = []

    for i, t in enumerate(data['created'][:10], start=1):
        # tournament_count += 1
        start_time = datetime.fromtimestamp(t['startsAt'] / 1000) 
        earned_data = {"Number": i, "Link": 'https://lichess.org/tournament/' + t['id'], "Name": t['fullName'], "StartsAt": start_time}
        data_list.append(earned_data)
        # writer.writerow([i, t['id'], t['fullName'], start_time])

    df = pd.DataFrame(data_list)
    df.to_csv('tournaments_pandas.csv', index=False, encoding='utf-8')

# reader = pd.read_csv('tournaments.csv')
reader_pandas = pd.read_csv('tournaments_pandas.csv')
# print(reader)
print(reader_pandas)

# analysis
print(df.head())
print(df.info())
print(df.describe())
print(f'Blitz tournaments: {df[df['Name'].str.contains('Blitz')]}')
print(f'Bullet tournaments: {df[df['Name'].str.contains('Bullet')]}')
print(df.sort_values(by='StartsAt'))
