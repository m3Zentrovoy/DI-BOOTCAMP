import requests
import json
import os
dir_path = os.path.dirname(os.path.realpath(__file__))

jokes = {
  "categories": [],
  "created_at": "2020-01-05 13:42:29.569033",
  "icon_url": "https://api.chucknorris.io/img/avatar/chuck-norris.png",
  "id": "Sn270vPpQIy3vHYTUirFSg",
  "updated_at": "2020-01-05 13:42:29.569033",
  "url": "https://api.chucknorris.io/jokes/Sn270vPpQIy3vHYTUirFSg",
  "value": "Chuck Norris can give a Ninntendo Gameboy a sex-change and create a Gamegirl."
}


responce = requests.get("https://api.chucknorris.io/jokes/random")
print(responce.text)


data = json.load(responce.text)

with open(f"{dir_path}/jokes.json", "w", encoding="utf - 8") as f:
    json.dump(data, f, indent=2, skipkeys= True)

print(data["value"])