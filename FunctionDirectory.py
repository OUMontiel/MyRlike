functionDirectory = {}

currentFunction = ''
functionIDs = []
functionTypes = []
functionKinds = []
parametersTables = []
variablesTables = []

parameterIDsStack = []
variableIDsStack = []
variableTypesCountStack = []
variableTypesCounter = -1
typesStack = []

def buildTables():
    parameters = {}
    while(len(parameterIDsStack) > 0):
        if parameterIDsStack[-1] in parameters:
            print('ERROR: Variable name < ', parameterIDsStack[-1], ' > already exists!')
            exit()
        else:
            parameters[parameterIDsStack.pop()] = typesStack.pop(len(typesStack) - len(parameterIDsStack) - len(variableTypesCountStack))
    parametersTable = []
    for parameterName, parameterType in parameters.items():
        parametersTable.append([parameterName, parameterType])
    
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
    for variableName, variableType in variables.items():
        variablesTable.append([variableName, variableType])
    
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

def printFunctionDirectory():
    for name, data in functionDirectory.items():
        print('Name: ', name)
        print('Type: ', data[0])
        print('Kind: ', data[1])
        print('Quadruple: ', data[2])
        print('Parameters:')
        for parameterName, parameterType in data[3]:
            print('\tName: ', parameterName, ' (', parameterType, ')')
        print('Variables:')
        for variableName, variableType in data[4]:
            print('\tName: ', variableName, ' (', variableType, ')')
        print('------------------------')

def getVariableType(variable):
    if (currentFunction in functionDirectory):
        currentVariablesTable = functionDirectory[currentFunction]
        for parameterName, parameterType in currentVariablesTable[3]:
            if (parameterName == variable):
                return parameterType
        for variableName, variableType in currentVariablesTable[4]:
            if (variableName == variable):
                return variableType
        currentVariablesTable = functionDirectory[functionIDs[0]]
        for variableName, variableType in currentVariablesTable[4]:
            if (variableName == variable):
                return variableType
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

def resetFunctionDirectory():
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
