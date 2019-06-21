import requests
from time import sleep
from bs4 import BeautifulSoup
from csv import writer

with open("friends_season1.csv", "w") as csv_file:
  csv_writer = writer(csv_file)
  csv_writer.writerow(["character", "line"])

for i in range(1, 25):
  if i < 10:
    response = requests.get(f"https://fangj.github.io/friends/season/010{i}.html")
  else:
    response = requests.get (f"https://fangj.github.io/friends/season/01{i}.html")

  soup = BeautifulSoup(response.text, "html.parser")
  lines = soup.find_all("p")[2:-1]

  with open("friends_season1.csv", "a") as csv_file:
    csv_writer = writer(csv_file)
    for line in lines:
      splitted = line.get_text().split(":")
      if len(splitted) > 1 and splitted[0][0] != "[": 
        character = splitted[0]
        line = splitted[1][1:-1]
        csv_writer.writerow([character, line])
  sleep(2)