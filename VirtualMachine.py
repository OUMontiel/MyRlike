import json

def generateGlobalMemory():
    globalMemory = [{}, {}, {}]
    for i in range(3):
        for j in range(1000):
            globalMemory[i][1000 * (i + 1) + j] = None
    return globalMemory

def generateLocalMemory():
    localMemory = [{}, {}, {}]
    for i in range(3):
        for j in range(1000):
            localMemory[i][3000 + 1000 * (i + 1) + j] = None
    return localMemory

def generateTemporalMemory():
    temporalMemory = [{}, {}, {}]
    for i in range(3):
        for j in range(1000):
            temporalMemory[i][6000 + 1000 * (i + 1) + j] = None
    return temporalMemory

def generateTemporalPointerMemory():
    temporalPointerMemory = [{}, {}, {}]
    for i in range(3):
        for j in range(1000):
            temporalPointerMemory[i][9000 + 1000 * (i + 1) + j] = None
    return temporalPointerMemory

def generateConstantMemory():
    constantMemory = [{}, {}, {}]
    for i in range(3):
        for j in range(1000):
            constantMemory[i][12000 + 1000 * (i + 1) + j] = None
    return constantMemory

def storeConstants(constantMemory, memory):
    for address, content in memory[12].items():
        constantMemory[0][int(address)] = content
    for address, content in memory[13].items():
        constantMemory[1][int(address)] = content
    for address, content in memory[14].items():
        constantMemory[2][int(address)] = content
    return constantMemory

def runProgram(functionDirectory, semanticCube, memory, quadruples):
    globalMemory = generateGlobalMemory()
    constantMemory = generateConstantMemory()
    storeConstants(constantMemory, memory)

    quadruplePointer = 0
    while True:
        quadruple = quadruples[quadruplePointer]
        if (quadruple[0] == '='):
            print(quadruple[0])
            quadruplePointer += 1
        elif (quadruple[0] == 'return'):
            print(quadruple[0])
            quadruplePointer += 1
        elif (quadruple[0] == 'read'):
            print(quadruple[0])
            quadruplePointer += 1
        elif (quadruple[0] == 'write'):
            print(quadruple[0])
            quadruplePointer += 1
        elif (quadruple[0] == 'write'):
            print(quadruple[0])
            quadruplePointer += 1
        elif (quadruple[0] == 'gotof'):
            print(quadruple[0])
            quadruplePointer += 1
        elif (quadruple[0] == 'goto'):
            print(quadruple[0])
            quadruplePointer += 1
        elif (quadruple[0] == 'era'):
            print(quadruple[0])
            quadruplePointer += 1
        elif (quadruple[0] == 'param'):
            print(quadruple[0])
            quadruplePointer += 1
        elif (quadruple[0] == 'gosub'):
            print(quadruple[0])
            quadruplePointer += 1
        elif (quadruple[0] == 'ver'):
            print(quadruple[0])
            quadruplePointer += 1
        elif (quadruple[0] == 'endfunc'):
            print(quadruple[0])
            quadruplePointer += 1
        elif (quadruple[0] == 'end'):
            print(quadruple[0])
            quadruplePointer += 1
            break
        else:
            print(quadruple[0])
            quadruplePointer += 1

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
    for i in range(len(quadruples)):
        print(f'{str(i):>4}', ': ', quadruples[i])
    runProgram(functionDirectory, semanticCube, memory, quadruples)
    