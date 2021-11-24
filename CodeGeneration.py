import SemanticCube

quadruples = []

operators = []
operands = []
types = []
jumps = []

results = []
resultsTypes = []
controlVariables = []

functionNames = []
functionParametersTables = []
functionParameterIndex = []

extraOperator = ''

def checkMemory(memory):
    for i in range(15):
        if (len(memory[i]) > 1000):
            print('ERROR: Stack overflow!')
            exit()

def generateQuadruple(possibleOperators, memory):
    if (len(operators) > 0 and operators[-1] in possibleOperators):
        right_operand = operands.pop()
        right_type = types.pop()
        left_operand = operands.pop()
        left_type = types.pop()
        operator = operators.pop()

        result_type = SemanticCube.semanticCube[SemanticCube.typeNames.index(left_type)][SemanticCube.typeNames.index(right_type)][SemanticCube.operatorNames.index(operator)]
        if (result_type == 'error'):
            print('ERROR: Types mismatch!')
            exit()
        else:
            if (result_type == 'int'):
                results.append(7000 + len(memory[6]))
                memory[6][7000 + len(memory[6])] = None
            elif (result_type == 'float'):
                results.append(8000 + len(memory[7]))
                memory[7][8000 + len(memory[7])] = None
            elif (result_type == 'char'):
                results.append(9000 + len(memory[8]))
                memory[8][9000 + len(memory[8])] = None
            checkMemory(memory)
            resultsTypes.append(result_type)
            quadruples.append([operator, left_operand, right_operand, results[-1]])
            operands.append(results[-1])
            types.append(resultsTypes[-1])

def generateAssignment():
    if (len(operators) > 0 and operators[-1] == '='):
        right_operand = operands.pop()
        right_type = types.pop()
        left_operand = operands.pop()
        left_type = types.pop()
        operator = operators.pop()

        '''
        if (left_type != right_type):
            print('ERROR: Types mismatch!')
            exit()
        else:
        '''
        quadruples.append([operator, right_operand, None, left_operand])

def generateReturn(current_function_type):
    return_operand = operands.pop()
    return_type = types.pop()

    if (return_type != current_function_type):
        print('ERROR: Return type does not match function type!')
        exit()
    else:
        quadruples.append(['return', None, None, return_operand])

def generateInput():
    while(len(operators) > 0 and operators[-1] == 'read'):
        read_operand = operands.pop()
        read_operator = operators.pop()

        quadruples.append([read_operator, None, None, read_operand])

def generateOutput():
    while(len(operators) > 0 and operators[-1] == 'write'):
        write_operand = operands.pop()
        write_size = 1
        write_type = types.pop()
        write_operator = operators.pop()

        if (write_type == 'string'):
            write_size = operands.pop()
            quadruples.append([write_operator, write_size, None, write_operand])
        else:
            quadruples.append([write_operator, None, None, write_operand])

def condicionPoint1():
    condition_operand = operands.pop()
    types.pop()

    jumps.append(len(quadruples))
    quadruples.append(['gotof', condition_operand, None, None])

def condicionPoint2():
    gotof_index = jumps.pop()

    quadruples[gotof_index][3] = len(quadruples)

def condicionPoint3():
    gotof_index = jumps.pop()

    jumps.append(len(quadruples))
    quadruples.append(['goto', None, None, None])
    quadruples[gotof_index][3] = len(quadruples)

def condicionPoint4():
    goto_index = jumps.pop()

    quadruples[goto_index][3] = len(quadruples)

def whilePoint1():
    jumps.append(len(quadruples))

def whilePoint2():
    condition_operand = operands.pop()
    types.pop()

    jumps.append(len(quadruples))
    quadruples.append(['gotof', condition_operand, None, None])

def whilePoint3():
    gotof_index = jumps.pop()
    return_index = jumps.pop()

    quadruples.append(['goto', None, None, return_index])
    quadruples[gotof_index][3] = len(quadruples)

def forPoint1():
    if (types[-1] != 'int'):
        print('ERROR: \'For\' expression is not of type integer!')
        exit()
    
    exp_operand = operands.pop()
    types.pop()
    control_operand = operands.pop()
    types.pop()

    controlVariables.append(control_operand)
    quadruples.append(['=', exp_operand, None, controlVariables[-1]])

def forPoint2(memory):
    if (types[-1] != 'int'):
        print('ERROR: \'For\' expression is not of type integer!')
        exit()
    
    exp_operand = operands.pop()
    types.pop()
    results.append(7000 + len(memory[6]))
    memory[6][7000 + len(memory[6])] = None
    checkMemory(memory)
    resultsTypes.append('int')

    jumps.append(len(quadruples))
    quadruples.append(['<', controlVariables[-1], exp_operand, results[-1]])
    jumps.append(len(quadruples))
    quadruples.append(['gotof', results[-1], None, None])

def forPoint3():
    quadruples.append(['+', controlVariables[-1], '1', controlVariables[-1]])
    controlVariables.pop()
    end_index = jumps.pop()
    return_index = jumps.pop()
    quadruples.append(['goto', None, None, return_index])
    quadruples[end_index][3] = len(quadruples)

def funcionPoint1(functionName, functionDirectory):
    if (functionName in functionDirectory):
        quadruples.append(['era', functionName, None, None])
        functionNames.append(functionName)
        functionParametersTables.append(functionDirectory[functionName][3])
        functionParameterIndex.append(0)
    else:
        print('ERROR: Function < ', functionName, ' > does not exist!')
        exit()

def funcionPoint2():
    parameter_name = operands.pop()
    parameter_type = types.pop()

    if (parameter_type != functionParametersTables[-1][functionParameterIndex[-1]][1]):
        print('ERROR: Parameter type does not match function signature!')
        exit()
    else:
        functionParameterIndex[-1] = functionParameterIndex[-1] + 1
        quadruples.append(['param', parameter_name, None, 'param' + str(functionParameterIndex[-1])])

def funcionPoint3():
    quadruples.append(['gosub', functionNames.pop(), None, None])

def arregloPoint1(arrayType, arrayAddress, arrayData, memory):
    quadruples.append(['ver', arrayData[0], arrayData[1], arrayData[2]])
    if (arrayType == 'int'):
        results.append(10000 + len(memory[9]))
        memory[9][10000 + len(memory[9])] = None
    elif (arrayType == 'float'):
        results.append(11000 + len(memory[10]))
        memory[10][11000 + len(memory[10])] = None
    elif (arrayType == 'char'):
        results.append(12000 + len(memory[11]))
        memory[11][12000 + len(memory[11])] = None
    checkMemory(memory)
    resultsTypes.append(arrayType)
    quadruples.append(['+', arrayData[0], arrayAddress, results[-1]])
    operands.append(results[-1])
    types.append(resultsTypes[-1])

def printQuadruples():
    for i in range(len(quadruples)):
        print(f'{str(i):>4}', ': ', quadruples[i])

def resetCodeGeneration():
    quadruples.clear()
    operators.clear()
    operands.clear()
    types.clear()
    jumps.clear()
    results.clear()
    resultsTypes.clear()
    controlVariables.clear()
