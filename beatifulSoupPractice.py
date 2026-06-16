import requests
from bs4 import BeautifulSoup

url = "https://dictionary.cambridge.org/dictionary/english/test"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/114.0 Safari/537.36"
}

response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, 'html.parser')

dailyWordWrap = soup.find('p', class_='fs36 lmt-5 feature-w-big wotd-hw')
dailyWord = dailyWordWrap.find('a')
# print(dailyWord['href'])
# print(wordOfDay)
# print(theMeaning.text)
theMeaningUrl = dailyWord['href']

respOfTheMeaning = requests.get("https://dictionary.cambridge.org/" + theMeaningUrl, headers=headers)
meaningSoup = BeautifulSoup(respOfTheMeaning.text, 'html.parser')
wordMeaning = meaningSoup.find('div', class_='def ddef_d db').text.strip()
wordExample = meaningSoup.find('span', class_="eg deg").text.strip()
print(f'Word of the day in the dictionary is: \n {dailyWord.text} \n the meaning is: \n {wordMeaning} \n the example: \n {wordExample} ')