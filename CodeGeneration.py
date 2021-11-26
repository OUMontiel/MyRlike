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

'''
checkMemory()
memory = la memoria virtual
    Revisa que no se haya acabado la memoria
'''
def checkMemory(memory):
    for i in range(15):
        if (len(memory[i]) > 1000):
            print('ERROR: Stack overflow!')
            exit()

'''
generateQuadruple()
possibleOperators = los operadores que pueden ir en este cuádruplo
memory = la memoria virtual
    Genera un cuádruplo de una expresión
'''
def generateQuadruple(possibleOperators, memory):
    if (len(operators) > 0 and operators[-1] in possibleOperators):
        print(operands)
        print(types)
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
            # Genera variable temporal
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

'''
generateAssignment()
    Genera un cuádruplo de una asignación
'''
def generateAssignment():
    print(operators)
    if (len(operators) > 0 and operators[-1] == '='):
        right_operand = operands.pop()
        right_type = types.pop()
        left_operand = operands.pop()
        left_type = types.pop()
        operator = operators.pop()

        quadruples.append([operator, right_operand, None, left_operand])

'''
generateReturn()
    Genera un cuádruplo de un retorno
'''
def generateReturn(functionName, functionType):
    return_operand = operands.pop()
    return_type = types.pop()

    if (return_type != functionType):
        print('ERROR: Return type does not match function type!')
        exit()
    else:
        quadruples.append(['return', functionName, None, return_operand])

'''
generateInput()
    Genera un cuádruplo de una lectura
'''
def generateInput():
    while(len(operators) > 0 and operators[-1] == 'read'):
        read_operand = operands.pop()
        types.pop()
        read_operator = operators.pop()

        quadruples.append([read_operator, None, None, read_operand])

'''
generatOutput()
    Genera un cuádruplo de una escritura
'''
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
'''
condicionPoint1()
    Primer punto neurálgico de estatuto condicional if
'''
def condicionPoint1():
    condition_operand = operands.pop()
    types.pop()

    jumps.append(len(quadruples))
    quadruples.append(['gotof', condition_operand, None, None])

'''
condicionPoint2()
    Segundo punto neurálgico de estatuto condicional if
'''
def condicionPoint2():
    gotof_index = jumps.pop()

    quadruples[gotof_index][3] = len(quadruples)

'''
condicionPoint3()
    Tercer punto neurálgico de estatuto condicional if
'''
def condicionPoint3():
    gotof_index = jumps.pop()

    jumps.append(len(quadruples))
    quadruples.append(['goto', None, None, None])
    quadruples[gotof_index][3] = len(quadruples)

'''
condicionPoint4()
    Cuarto punto neurálgico de estatuto condicional if
'''
def condicionPoint4():
    goto_index = jumps.pop()

    quadruples[goto_index][3] = len(quadruples)

'''
whilePoint1()
    Primer punto neurálgico de estatuto condicional while
'''
def whilePoint1():
    jumps.append(len(quadruples))

'''
whilePoint2()
    Segundo punto neurálgico de estatuto condicional while
'''
def whilePoint2():
    condition_operand = operands.pop()
    types.pop()

    jumps.append(len(quadruples))
    quadruples.append(['gotof', condition_operand, None, None])

'''
whilePoint3()
    Tercer punto neurálgico de estatuto condicional while
'''
def whilePoint3():
    gotof_index = jumps.pop()
    return_index = jumps.pop()

    quadruples.append(['goto', None, None, return_index])
    quadruples[gotof_index][3] = len(quadruples)

'''
forPoint1()
    Primer punto neurálgico de estatuto condicional for
'''
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

'''
forPoint2()
    Segundo punto neurálgico de estatuto condicional for
'''
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

'''
forPoint3()
    Tercer punto neurálgico de estatuto condicional for
'''
def forPoint3(counter):
    quadruples.append(['+', controlVariables[-1], counter, controlVariables[-1]])
    controlVariables.pop()
    end_index = jumps.pop()
    return_index = jumps.pop()
    quadruples.append(['goto', None, None, return_index])
    quadruples[end_index][3] = len(quadruples)

'''
funcionPoint1()
    Primer punto neurálgico de estatuto modular
'''
def funcionPoint1(functionName, functionDirectory):
    if (functionName in functionDirectory):
        quadruples.append(['era', functionName, None, None])
        functionNames.append(functionName)
        functionParametersTables.append(functionDirectory[functionName][4])
        functionParameterIndex.append(0)
    else:
        print('ERROR: Function < ', functionName, ' > does not exist!')
        exit()

'''
funcionPoint2()
    Segundo punto neurálgico de estatuto modular
'''
def funcionPoint2():
    parameter_type = functionParametersTables[-1][functionParameterIndex[-1]][1]
    parameter_address = functionParametersTables[-1][functionParameterIndex[-1]][2]
    variable_name = operands.pop()
    variable_type = types.pop()

    if (variable_type != parameter_type):
        print('ERROR: Parameter type does not match function signature!')
        exit()
    else:
        functionParameterIndex[-1] = functionParameterIndex[-1] + 1
        quadruples.append(['param', variable_name, None, parameter_address])

'''
funcionPoint3()
    Tercer punto neurálgico de estatuto modular
'''
def funcionPoint3(functionDirectory, memory):
    quadruples.append(['gosub', functionNames[-1], None, None])
    functionType = functionDirectory[functionNames[-1]][0]
    if (functionType != 'void'):
        # Genera variable temporal
        if (functionType == 'int'):
            results.append(7000 + len(memory[6]))
            memory[6][7000 + len(memory[6])] = None
        elif (functionType == 'float'):
            results.append(8000 + len(memory[7]))
            memory[7][8000 + len(memory[7])] = None
        elif (functionType == 'char'):
            results.append(9000 + len(memory[8]))
            memory[8][9000 + len(memory[8])] = None
        checkMemory(memory)
        resultsTypes.append(functionType)
        quadruples.append(['=', functionNames.pop(), None, results[-1]])
        operands.append(results[-1])
        types.append(resultsTypes[-1])

'''
arregloPoint1()
    Primer punto neurálgico de arreglos
'''
def arregloPoint1(arrayType, arrayAddress, arrayData, memory):
    quadruples.append(['ver', arrayData[0], arrayData[1], arrayData[2]])
    # Genera memoria de apuntador
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

'''
printQuadruples()
    Imprime en consola los cuádruplos y sus índices
'''
def printQuadruples():
    for i in range(len(quadruples)):
        print(f'{str(i):>4}', ': ', quadruples[i])

'''
resetCodeGeneration()
    Reinicia todas las estructuras de datos para un nuevo programa
'''
def resetCodeGeneration():
    quadruples.clear()
    operators.clear()
    operands.clear()
    types.clear()
    jumps.clear()
    results.clear()
    resultsTypes.clear()
    controlVariables.clear()
