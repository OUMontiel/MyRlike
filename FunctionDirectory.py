functionDirectory = {}

currentFunction = ''
functionIDs = []
functionTypes = []
functionKinds = []
variablesTable = []

variableIDsStack = []
variableTypesCountStack = []
variableTypesCounter = -1
parameterIDsStack = []
typesStack = []

def buildTable():
    variables = {}
    while(len(variableTypesCountStack) > 0):
        for i in range(0, variableTypesCountStack.pop(0)):
            if variableIDsStack[0] in variables:
                print("ERROR")
                exit()
            else:
                variables[variableIDsStack.pop(0)] = typesStack[-1]
        typesStack.pop()
    
    while(len(parameterIDsStack) > 0):
        if parameterIDsStack[0] in variables:
            print("ERROR: Variable name already exists!")
            exit()
        else:
            variables[parameterIDsStack.pop(0)] = typesStack.pop()

    variablesTable.append(variables)
    if typesStack:
        functionTypes.append(typesStack.pop())
    else:
        functionTypes.append('void')

    variableIDsStack.clear()
    variableTypesCountStack.clear()
    variableTypesCounter = -1
    parameterIDsStack.clear()
    typesStack.clear()

def storeFunction():
    print(functionIDs[-1])
    if(functionIDs[-1] in functionDirectory):
        print('ERROR: Function name already exists!')
        exit()
    else:
        functionDirectory[functionIDs[-1]] = [functionTypes[-1], functionKinds[-1], variablesTable[-1]]

def printFunctionDirectory():
    for name, data in functionDirectory.items():
        print('Name: ', name)
        print('Type: ', data[0])
        print('Kind: ', data[1])
        print('Variables:')
        for variableName, variableType in data[2].items():
            print('\tName: ', variableName, ' (', variableType, ')')
        print('------------------------')

def getVariableType(variable):
    if (currentFunction in functionDirectory):
        currentVariablesTable = functionDirectory[currentFunction]
        for variableName, variableType in currentVariablesTable[2].items():
            if (variableName == variable):
                return variableType
        currentVariablesTable = functionDirectory[functionIDs[0]]
        for variableName, variableType in currentVariablesTable[2].items():
            if (variableName == variable):
                return variableType
    print('ERROR: Variable < ', variable, ' > not found!')
    exit()

def findVariable(variable):
    if (currentFunction in functionDirectory):
        currentVariablesTable = functionDirectory[currentFunction]
        for variableName, variableType in currentVariablesTable[2].items():
            if (variableName == variable):
                print('ERROR: Variable < ', variable, ' > already exists!')
                exit()
        currentVariablesTable = functionDirectory[functionIDs[0]]
        for variableName, variableType in currentVariablesTable[2].items():
            if (variableName == variable):
                print('ERROR: Variable < ', variable, ' > already exists!')
                exit()

def resetFunctionDirectory():
    functionDirectory.clear()
    functionIDs.clear()
    functionTypes.clear()
    functionKinds.clear()
    variablesTable.clear()
    variableIDsStack.clear()
    variableTypesCountStack.clear()
    variableTypesCounter = -1
    parameterIDsStack.clear()
    typesStack.clear()
