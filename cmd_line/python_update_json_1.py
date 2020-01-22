import json
with open("abc1.json", "r") as jsonFile:
    data = json.load(jsonFile)

tmp = data["name"]
data["name"] = "y"
print(tmp)

with open("abc1.json", "w") as jsonFile:
    json.dump(data, jsonFile)