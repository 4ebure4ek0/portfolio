import json

file = open("var1.json", "r")
str = file.read()
file.close()

tasks = json.loads(str)

print(type(tasks))