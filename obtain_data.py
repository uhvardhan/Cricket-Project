from bs4 import BeautifulSoup
import requests

url = "https://www.espncricinfo.com/series/indian-premier-league-2024-1410320/gujarat-titans-vs-delhi-capitals-32nd-match-1426270/full-scorecard"
page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")

print(soup.get_text())
# elements = soup.find_all("__next", class_="ds-text-tight-xs")

# print(elements)