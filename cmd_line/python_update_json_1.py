import json
with open("abc1.json", "r") as jsonFile:
    data = json.load(jsonFile)

tmp = data["name"]
data["name"] = "y"
data["address"]["street"] = "15 GIP Colony Hatpukur"
data["address"]["pin"] = "12345"
print(tmp)

with open("abc1.json", "w") as jsonFile:
    json.dump(data, jsonFile)