import json
import os
import subprocess

try:
  with open("./fixtures/package.json") as f:
    data = json.load(f)
  command = data["scripts"]["start"]
  os.system(command)
except IOError:
    print("At this folder package.json not found, please call from root.")
