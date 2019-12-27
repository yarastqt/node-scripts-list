import json

try:
  with open("./fixtures/package.json") as file:
    data = json.load(file)
  print(data["name"])
except IOError:
    print("At this folder package.json not found, please call from root.")
