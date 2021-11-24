import json

while True:
    try:
        path_to_file = input('>> ')
        if (path_to_file[len(path_to_file)-5:] != '.json'):
            print('ERROR: JSON file expected!')
            continue
        with open(path_to_file) as json_file:
            data = json.load(json_file)
    except IOError:
        print('ERROR: File does not exist!')
        continue
    
    functionDirectory = data['functionDirectory']
    semanticCube = data['semanticCube']
    memory = data['memory']
    quadruples = data['quadruples']
    print(functionDirectory)
    print()
    print(semanticCube)
    print()
    print(memory)
    print()
    print(quadruples)