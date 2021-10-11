functionDirectory = {}

functionIDsStack = []
functionTypesStack = []
variableTablesStack = []

variableIDsStack = []
variableTypesCountStack = []
variableTypesCounter = -1
parameterIDsStack = []
typesStack = []

def storeFunction(id, type, kind, table):
    print(id, type, kind, table)
    functionDirectory[id] = [type, kind, table]

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
            print("ERROR")
            exit()
        else:
            variables[parameterIDsStack.pop(0)] = typesStack.pop()

    variableTablesStack.append(variables)
    if typesStack:
        functionTypesStack.append(typesStack.pop())
    else:
        functionTypesStack.append('void')

    variableIDsStack.clear()
    variableTypesCountStack.clear()
    variableTypesCounter = -1
    parameterIDsStack.clear()
    typesStack.clear()

def buildFunctionDirectory():
    functionDirectory[functionIDsStack.pop()] = [functionTypesStack.pop(0), 'program', variableTablesStack.pop(0)]
    while len(functionIDsStack) > 0:
        functionDirectory[functionIDsStack.pop()] = [functionTypesStack.pop(0), 'function', variableTablesStack.pop(0)]

def printFunctionDirectory():
    for name, data in functionDirectory.items():
        print('----------------')
        print('Name: ', name)
        print('Type: ', data[0])
        print('Kind: ', data[1])
        print('Variables:')
        for variableName, variableType in data[2].items():
            print('\tName: ', variableName, ' (', variableType, ')')
