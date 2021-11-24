functionDirectory = {}

isGlobal = True

currentFunction = ''
functionIDs = []
functionTypes = []
functionKinds = []
parametersTables = []
variablesTables = []

parameterIDsStack = []
variableIDsStack = []
variableSizesStack = []
variableTypesCountStack = []
variableTypesCounter = -1
typesStack = []

def checkMemory(memory):
    for i in range(15):
        if (len(memory[i]) > 1000):
            print('ERROR: Stack overflow!')
            exit()

def buildTables(memory):
    global isGlobal
    parameters = {}
    while(len(parameterIDsStack) > 0):
        if parameterIDsStack[-1] in parameters:
            print('ERROR: Variable name < ', parameterIDsStack[-1], ' > already exists!')
            exit()
        else:
            parameters[parameterIDsStack.pop()] = typesStack.pop(len(typesStack) - len(parameterIDsStack) - len(variableTypesCountStack))
    parametersTable = []
    for parameterName, parameterType in parameters.items():
        if (parameterType == 'int'):
            parametersTable.append([parameterName, parameterType, 4000 + len(memory[3])])
            memory[3][4000 + len(memory[3])] = None
        elif (parameterType == 'float'):
            parametersTable.append([parameterName, parameterType, 5000 + len(memory[4])])
            memory[4][5000 + len(memory[4])] = None
        elif (parameterType == 'char'):
            parametersTable.append([parameterName, parameterType, 6000 + len(memory[5])])
            memory[5][6000 + len(memory[5])] = None
        checkMemory(memory)
    
    variables = {}
    while(len(variableTypesCountStack) > 0):
        for i in range(variableTypesCountStack[-1]):
            if variableIDsStack[-1] in variables or variableIDsStack[-1] in parameters:
                print('ERROR: Variable name < ', variableIDsStack[-1], ' > already exists!')
                exit()
            else:
                variables[variableIDsStack.pop()] = typesStack[-len(variableTypesCountStack)]
        typesStack.pop(-len(variableTypesCountStack))
        variableTypesCountStack.pop()
    variablesTable = []
    if (isGlobal):
        for variableName, variableType in variables.items():
            variableSize = 1
            if (variableSizesStack[-1] != None):
                variableSize = variableSizesStack[-1]
            if (variableType == 'int'):
                variablesTable.append([variableName, variableType, 1000 + len(memory[0]), variableSizesStack.pop()])
                for i in range(variableSize):
                    memory[0][1000 + len(memory[0])] = None
            elif (variableType == 'float'):
                variablesTable.append([variableName, variableType, 2000 + len(memory[1]), variableSizesStack.pop()])
                for i in range(variableSize):
                    memory[1][2000 + len(memory[1])] = None
            elif (variableType == 'char'):
                variablesTable.append([variableName, variableType, 3000 + len(memory[2]), variableSizesStack.pop()])
                for i in range(variableSize):
                    memory[2][3000 + len(memory[2])] = None
            checkMemory(memory)
    else:
        for variableName, variableType in variables.items():
            variableSize = 1
            if (variableSizesStack[-1] != None):
                variableSize = variableSizesStack[-1]
            if (variableType == 'int'):
                variablesTable.append([variableName, variableType, 4000 + len(memory[3]), variableSizesStack.pop()])
                for i in range(variableSize):
                    memory[3][4000 + len(memory[3])] = None
            elif (variableType == 'float'):
                variablesTable.append([variableName, variableType, 5000 + len(memory[4]), variableSizesStack.pop()])
                for i in range(variableSize):
                    memory[4][5000 + len(memory[4])] = None
            elif (variableType == 'char'):
                variablesTable.append([variableName, variableType, 6000 + len(memory[5]), variableSizesStack.pop()])
                for i in range(variableSize):
                    memory[5][6000 + len(memory[5])] = None
            checkMemory(memory)
    
    parametersTables.append(parametersTable)
    variablesTables.append(variablesTable)
    if typesStack:
        functionTypes.append(typesStack.pop())
    else:
        functionTypes.append('void')

    variableIDsStack.clear()
    variableTypesCountStack.clear()
    variableTypesCounter = -1
    parameterIDsStack.clear()
    typesStack.clear()

def storeFunction(address):
    print(functionIDs[-1])
    if(functionIDs[-1] in functionDirectory):
        print('ERROR: Function name already exists!')
        exit()
    else:
        functionDirectory[functionIDs[-1]] = [functionTypes[-1], functionKinds[-1], address, parametersTables[-1], variablesTables[-1]]

def getVariableData(variable):
    if (currentFunction in functionDirectory):
        currentVariablesTable = functionDirectory[currentFunction]
        for parameterName, parameterType, parameterAdress in currentVariablesTable[3]:
            if (parameterName == variable):
                return [parameterType, parameterAdress]
        for variableName, variableType, variableAdress, variableSize in currentVariablesTable[4]:
            if (variableName == variable):
                return [variableType, variableAdress, variableSize]
        currentVariablesTable = functionDirectory[functionIDs[0]]
        for variableName, variableType, variableAdress, variableSize in currentVariablesTable[4]:
            if (variableName == variable):
                return [variableType, variableAdress, variableSize]
    print('ERROR: Variable < ', variable, ' > not found!')
    exit()

def findVariable(variable):
    if (currentFunction in functionDirectory):
        currentVariablesTable = functionDirectory[currentFunction]
        for variableName, variableType in currentVariablesTable[2]:
            if (variableName == variable):
                print('ERROR: Variable < ', variable, ' > already exists!')
                exit()
        currentVariablesTable = functionDirectory[functionIDs[0]]
        for variableName, variableType in currentVariablesTable[2]:
            if (variableName == variable):
                print('ERROR: Variable < ', variable, ' > already exists!')
                exit()

def printFunctionDirectory():
    for name, data in functionDirectory.items():
        print('Name: ', name)
        print('Type: ', data[0])
        print('Kind: ', data[1])
        print('Quadruple: ', data[2])
        print('Parameters:')
        for parameterName, parameterType, parameterAddress in data[3]:
            print('\tName: ', parameterName, ' (', parameterType, ') -> ', parameterAddress)
        print('Variables:')
        for variableName, variableType, variableAddress, variableSize in data[4]:
            if (variableSize == None):
                print('\tName: ', variableName, ' (', variableType, ') -> ', variableAddress)
            else:
                print('\tName: ', variableName, '[', variableSize, '] (', variableType, ') -> ', variableAddress)
        print('------------------------')

def resetFunctionDirectory():
    global isGlobal
    isGlobal = True
    functionDirectory.clear()
    functionIDs.clear()
    functionTypes.clear()
    functionKinds.clear()
    parametersTables.clear()
    variablesTables.clear()
    parameterIDsStack.clear()
    variableIDsStack.clear()
    variableTypesCountStack.clear()
    variableTypesCounter = -1
    typesStack.clear()
