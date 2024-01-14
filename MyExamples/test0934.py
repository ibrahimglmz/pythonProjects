import json

with open("person.json") as f:
    data = json.load(f)
    print(data["name"])
    print(data["languages"][0])
