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

def generateQuadruple(possibleOperators):
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
            results.append('t' + str(len(results) + 1))
            resultsTypes.append(result_type)
            quadruples.append([operator, left_operand, right_operand, results[-1]])
            #print(quadruples)
            return [results[-1], resultsTypes[-1]]

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
        #print(quadruples)

def generateReturn(current_function_type):
    return_operand = operands.pop()
    return_type = types.pop()

    if (return_type != current_function_type):
        print('ERROR: Return type does not match function type!')
        exit()
    else:
        quadruples.append(['return', None, None, return_operand])
        #print(quadruples)

def generateInput():
    while(len(operators) > 0 and operators[-1] == 'read'):
        read_operand = operands.pop()
        read_operator = operators.pop()

        quadruples.append([read_operator, None, None, read_operand])
        #print(quadruples)

def generateOutput():
    while(len(operators) > 0 and operators[-1] == 'write'):
        write_operand = operands.pop()
        types.pop()
        write_operator = operators.pop()

        quadruples.append([write_operator, None, None, write_operand])
        #print(quadruples)

def condicionPoint1():
    condition_operand = operands.pop()
    types.pop()

    jumps.append(len(quadruples))
    quadruples.append(['gotof', condition_operand, None, None])
    #print(quadruples)
    #print(jumps)

def condicionPoint2():
    gotof_index = jumps.pop()

    quadruples[gotof_index][3] = len(quadruples)
    #print(quadruples)
    #print(jumps)

def condicionPoint3():
    gotof_index = jumps.pop()

    jumps.append(len(quadruples))
    quadruples.append(['goto', None, None, None])
    quadruples[gotof_index][3] = len(quadruples)
    #print(quadruples)
    #print(jumps)

def condicionPoint4():
    goto_index = jumps.pop()

    quadruples[goto_index][3] = len(quadruples)
    #print(quadruples)
    #print(jumps)

def whilePoint1():
    jumps.append(len(quadruples))
    #print(quadruples)
    #print(jumps)

def whilePoint2():
    condition_operand = operands.pop()
    types.pop()

    jumps.append(len(quadruples))
    quadruples.append(['gotof', condition_operand, None, None])
    #print(quadruples)
    #print(jumps)

def whilePoint3():
    gotof_index = jumps.pop()
    return_index = jumps.pop()

    quadruples.append(['goto', None, None, return_index])
    quadruples[gotof_index][3] = len(quadruples)
    #print(quadruples)
    #print(jumps)

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

def forPoint2():
    if (types[-1] != 'int'):
        print('ERROR: \'For\' expression is not of type integer!')
        exit()
    
    exp_operand = operands.pop()
    types.pop()
    results.append('t' + str(len(results) + 1))
    resultsTypes.append('int')

    jumps.append(len(quadruples))
    quadruples.append(['<', controlVariables[-1], exp_operand, results[-1]])
    jumps.append(len(quadruples))
    quadruples.append(['gotof', results[-1], None, None])

def forPoint3():
    quadruples.append(['+', controlVariables[-1], '1', controlVariables[-1]])
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
