import json

path_to_file = input('>> ')

with open(path_to_file) as json_file:
    data = json.load(json_file)
    print(type(data))
    print(data)