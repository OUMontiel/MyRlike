import json

'''
generateGlobalMemory()
    Crea una instancia de memoria global
'''
def generateGlobalMemory():
    globalMemory = [{}, {}, {}]
    for i in range(3):
        for j in range(1000):
            globalMemory[i][1000 * (i + 1) + j] = None
    return globalMemory

'''
generateLocalMemory()
    Crea una instancia de memoria local
'''
def generateLocalMemory():
    localMemory = [{}, {}, {}]
    for i in range(3):
        for j in range(1000):
            localMemory[i][3000 + 1000 * (i + 1) + j] = None
    return localMemory

'''
generateTemporalMemory()
    Crea una instancia de memoria de temporales
'''
def generateTemporalMemory():
    temporalMemory = [{}, {}, {}]
    for i in range(3):
        for j in range(1000):
            temporalMemory[i][6000 + 1000 * (i + 1) + j] = None
    return temporalMemory

'''
generateTemporalPointerMemory()
    Crea una instancia de memoria de temporales para pointers
'''
def generateTemporalPointerMemory():
    temporalPointerMemory = [{}, {}, {}]
    for i in range(3):
        for j in range(1000):
            temporalPointerMemory[i][9000 + 1000 * (i + 1) + j] = None
    return temporalPointerMemory

'''
generateConstantMemory()
    Crea una instancia de memoria de constantes
'''
def generateConstantMemory():
    constantMemory = [{}, {}, {}]
    for i in range(3):
        for j in range(1000):
            constantMemory[i][12000 + 1000 * (i + 1) + j] = None
    return constantMemory

'''
storeConstants()
constantMemory = instancia de memoria de constantes
memory = la memoria que proviene del compilador
    Pasa los valores de las constantes guardadas en el compilador a la memoria de la máquina virtual
'''
def storeConstants(constantMemory, memory):
    for address, content in memory[12].items():
        constantMemory[0][int(address)] = content
    for address, content in memory[13].items():
        constantMemory[1][int(address)] = content
    for address, content in memory[14].items():
        constantMemory[2][int(address)] = content
    return constantMemory

'''
getContent()
address = dirección de memoria
virtualMemory = la memoria de la máquina virtual
    Regresa el valor que se encuentra dentro de la dirección en la máquina virtual
'''
def getContent(address, virtualMemory):
    if (address >= 1000 and address <= 3999):
        return virtualMemory[0][(address // 1000 + 2) % 3][address]
    elif (address >= 4000 and address <= 6999):
        return virtualMemory[1][-1][(address // 1000 + 2) % 3][address]
    elif (address >= 7000 and address <= 9999):
        return virtualMemory[2][-1][(address // 1000 + 2) % 3][address]
    elif (address >= 10000 and address <= 12999):
        return virtualMemory[3][-1][(address // 1000 + 2) % 3][address]
    elif (address >= 13000 and address <= 15999):
        return virtualMemory[4][(address // 1000 + 2) % 3][address]

'''
setContent()
value = valor que se desea guardar
address = dirección de memoria
virtualMemory = la memoria de la máquina virtual
    Se guarda el valor dentro de la dirección en la máquina virtual
'''
def setContent(value, address, virtualMemory):
    if (address >= 1000 and address <= 3999):
        virtualMemory[0][(address // 1000 + 2) % 3][address] = value
    elif (address >= 4000 and address <= 6999):
        virtualMemory[1][-1][(address // 1000 + 2) % 3][address] = value
    elif (address >= 7000 and address <= 9999):
        virtualMemory[2][-1][(address // 1000 + 2) % 3][address] = value
    elif (address >= 10000 and address <= 12999):
        virtualMemory[3][-1][(address // 1000 + 2) % 3][address] = value
    elif (address >= 13000 and address <= 15999):
        virtualMemory[4][(address // 1000 + 2) % 3][address] = value

'''
getType()
address = dirección de memoria
    Regresa el tipo de dato basado en la dirección de memoria
'''
def getType(address):
    if (address // 1000 % 3 == 1):
        return 'int'
    elif (address // 1000 % 3 == 2):
        return 'float'
    else:
        return 'char'

'''
runAssignment()
quadruple = cuádruplo de asignación que se correrá
quadruplePointer = contador que apunta al cuádruplo actual
virtualMemory = la memoria de la máquina virtual
returnTable = diccionario con valor de retorno de cada función
    Ejectuta el cuádruplo de asignación
'''
def runAssignment(quadruple, quadruplePointer, virtualMemory, returnTable):
    # Si el contenido a asignar es el nombre de una función, regresar su valor de retorno
    if (quadruple[1] in returnTable):
        setContent(returnTable[quadruple[1]], quadruple[3], virtualMemory)
    else:
        right_operand = getContent(quadruple[1], virtualMemory)
        address = quadruple[3]
        # Si la dirección de memoria es de tipo apuntador, accesar la dirección de su valor
        if (quadruple[1] >= 10000 and quadruple[1] <= 12999):
            right_operand = getContent(right_operand, virtualMemory)
        # Si la dirección de memoria es de tipo apuntador, accesar la dirección de su valor
        if (quadruple[3] >= 10000 and quadruple[3] <= 12999):
            address = getContent(address, virtualMemory)

        if (right_operand == None):
            print('ERROR: Variables have not been assigned!')
            exit()
        setContent(right_operand, address, virtualMemory)
    return quadruplePointer + 1

'''
runReturn()
quadruple = cuádruplo de asignación que se correrá
virtualMemory = la memoria de la máquina virtual
functionDirectory = directorio de funcionamiento generado por el compilador
returnTable = diccionario con valor de retorno de cada función
    Ejectuta el cuádruplo de retorno
'''
def runReturn(quadruple, virtualMemory, functionDirectory, returnTable):
    returnTable[quadruple[1]] = getContent(quadruple[3], virtualMemory)
    return functionDirectory[quadruple[1]][3]

'''
runRead()
quadruple = cuádruplo de asignación que se correrá
quadruplePointer = contador que apunta al cuádruplo actual
virtualMemory = la memoria de la máquina virtual
    Ejectuta el cuádruplo de lectura
'''
def runRead(quadruple, quadruplePointer, virtualMemory):
    varType = getType(quadruple[3])
    var = input()
    if (varType == 'int'):
        try:
            int(var)
            setContent(var, quadruple[3], virtualMemory)
        except ValueError:
            print('ERROR: Input value is not the correct type!')
            exit()
    elif (varType == 'float'):
        try:
            float(var)
            setContent(var, quadruple[3], virtualMemory)
        except ValueError:
            print('ERROR: Input value is not the correct type!')
            exit()
    elif (varType == 'char'):
        if (len(var) == 1):
            setContent(var, quadruple[3], virtualMemory)
        else:
            print('ERROR: Input value is not the correct type!')
            exit()
    return quadruplePointer + 1

'''
runWrite()
quadruple = cuádruplo de asignación que se correrá
quadruplePointer = contador que apunta al cuádruplo actual
virtualMemory = la memoria de la máquina virtual
    Ejectuta el cuádruplo de escritura
'''
def runWrite(quadruple, quadruplePointer, virtualMemory):
    if (quadruple[1] == None):
        if (quadruple[3] >= 10000 and quadruple[3] <= 12999):
            print(getContent(getContent(quadruple[3], virtualMemory), virtualMemory))
        else:
            print(getContent(quadruple[3], virtualMemory))
    else:
        address = quadruple[3]
        string = ''
        for i in range(quadruple[1]):
            string += getContent(address + i, virtualMemory)
        print(string)
    return quadruplePointer + 1

'''
runGotof()
quadruple = cuádruplo de asignación que se correrá
quadruplePointer = contador que apunta al cuádruplo actual
virtualMemory = la memoria de la máquina virtual
    Ejectuta el cuádruplo de GOTOF
'''
def runGotof(quadruple, quadruplePointer, virtualMemory):
    if (getContent(quadruple[1], virtualMemory) == 0):
        return quadruple[3]
    else:
        return quadruplePointer + 1

'''
runGoto()
quadruple = cuádruplo de asignación que se correrá
    Ejectuta el cuádruplo de GOTO
'''
def runGoto(quadruple):
    return quadruple[3]

'''
runEra()
quadruplePointer = contador que apunta al cuádruplo actual
virtualMemory = la memoria de la máquina virtual
    Ejectuta el cuádruplo de ERA
'''
def runEra(quadruplePointer, virtualMemory):
    virtualMemory[1].append(generateLocalMemory())
    virtualMemory[2].append(generateLocalMemory())
    virtualMemory[3].append(generateLocalMemory())
    return quadruplePointer + 1

'''
runParam()
quadruple = cuádruplo de asignación que se correrá
quadruplePointer = contador que apunta al cuádruplo actual
virtualMemory = la memoria de la máquina virtual
    Ejectuta el cuádruplo de PARAM
'''
def runParam(quadruple, quadruplePointer, virtualMemory):
    setContent(getContent(quadruple[1], virtualMemory), quadruple[3], virtualMemory)
    return quadruplePointer + 1

'''
runGosub()
quadruple = cuádruplo de asignación que se correrá
quadruplePointer = contador que apunta al cuádruplo actual
pointerStack = pila de apuntadores cuyo valor final contiene el índice del cuádruplo al que se tiene que regresar
functionDirectory = directorio de funcionamiento generado por el compilador
    Ejectuta el cuádruplo de GOSUB
'''
def runGosub(quadruple, quadruplePointer, pointerStack, functionDirectory):
    pointerStack.append(quadruplePointer + 1)
    return functionDirectory[quadruple[1]][2]

'''
runVer()
quadruple = cuádruplo de asignación que se correrá
quadruplePointer = contador que apunta al cuádruplo actual
virtualMemory = la memoria de la máquina virtual
    Ejectuta el cuádruplo de VER
'''
def runVer(quadruple, quadruplePointer, virtualMemory):
    variable = getContent(quadruple[1], virtualMemory)
    lowerLimit = getContent(quadruple[2], virtualMemory)
    upperLimit = getContent(quadruple[3], virtualMemory)
    if (variable < lowerLimit or variable >= upperLimit):
        print('ERROR: Value < ', variable, ' > is not within the limits of the array!')
        exit()
    return quadruplePointer + 1

'''
runEndfunc()
virtualMemory = la memoria de la máquina virtual
pointerStack = pila de apuntadores cuyo valor final contiene el índice del cuádruplo al que se tiene que regresar
    Ejectuta el cuádruplo de ENDFUNC
'''
def runEndfunc(virtualMemory, pointerStack):
    virtualMemory[1].pop()
    virtualMemory[2].pop()
    virtualMemory[3].pop()
    return pointerStack.pop()

'''
runExpression()
quadruple = cuádruplo de una expresión que se correrá
quadruplePointer = contador que apunta al cuádruplo actual
virtualMemory = la memoria de la máquina virtual
    Ejectuta el cuádruplo de la expresión
'''
def runExpression(quadruple, quadruplePointer, virtualMemory):
    left_type = getType(quadruple[1])
    right_type = getType(quadruple[2])
    left_operand = getContent(quadruple[1], virtualMemory)
    right_operand = getContent(quadruple[2], virtualMemory)
    if (left_operand == None or right_operand == None):
        print('ERROR: Variables have not been assigned!')
        exit()
    if (quadruple[1] >= 10000 and quadruple[1] <= 12999):
        left_operand = getContent(left_operand, virtualMemory)
    if (quadruple[2] >= 10000 and quadruple[2] <= 12999):
        right_operand = getContent(right_operand, virtualMemory)
    value = calculateExpression(quadruple[0], left_operand, right_operand, left_type, right_type)
    setContent(value, quadruple[3], virtualMemory)
    return quadruplePointer + 1

'''
calculateExpression()
operator = operador de la expresión
left_operand = operando izquiero de la expresión
right_operand = operando derecho de la expresión
left_type = tipo de dato del operando izquierdo
right_type = tipo de dato del operando derecho
    Calcula la expresión y regresa el valor resultante
'''
def calculateExpression(operator, left_operand, right_operand, left_type, right_type):
    # Obtener valores ASCII de valores tipo 'char'
    if (left_type == 'char'):
        if (left_operand[0] == '+'):
            left_operand = ord(left_operand[1:])
        if (left_operand[0] == '-'):
            left_operand = (-1) * ord(left_operand[1:])
        else:
            left_operand = ord(left_operand)
    if (right_type == 'char'):
        right_operand = ord(right_operand)

    if (operator == '||'):
        return 1 if left_operand or right_operand else 0
    elif (operator == '&&'):
        return 1 if left_operand and right_operand else 0
    elif (operator == '=='):
        return 1 if left_operand == right_operand else 0
    elif (operator == '!='):
        return 1 if left_operand != right_operand else 0
    elif (operator == '<'):
        return 1 if left_operand < right_operand else 0
    elif (operator == '<='):
        return 1 if left_operand <= right_operand else 0
    elif (operator == '>'):
        return 1 if left_operand > right_operand else 0
    elif (operator == '>='):
        return 1 if left_operand >= right_operand else 0
    elif (operator == '+'):
        if (left_type == 'char' or right_type == 'char'):
            return chr(left_operand + right_operand)
        else:
            return left_operand + right_operand
    elif (operator == '-'):
        if (left_type == 'char' or right_type == 'char'):
            return chr(left_operand - right_operand)
        else:
            return left_operand - right_operand
    elif (operator == '*'):
        if (left_type == 'char' or right_type == 'char'):
            return chr(left_operand * right_operand)
        else:
            return left_operand * right_operand
    elif (operator == '/'):
        if (left_type == 'char' or right_type == 'char'):
            return chr(left_operand // right_operand)
        elif (left_type == 'int' and right_type == 'int'):
            return left_operand // right_operand
        else:
            return left_operand / right_operand
    elif (operator == '%'):
        if (left_type == 'char' or right_type == 'char'):
            return chr(left_operand % right_operand)
        else:
            return left_operand % right_operand

'''
runProgram()
functionDirectory = directorio de funcionamiento generado por el compilador
semanticCube = la tabla de consideraciones semánticas
memory = la memoria que proviene del compilador
quadruples = la lista de cuádruplos generados por el compilador
    Corre el programa ejecutando los cuádruplos
'''
def runProgram(functionDirectory, semanticCube, memory, quadruples):
    globalMemory = generateGlobalMemory()
    localMemory = [generateLocalMemory()]
    temporalMemory = [generateTemporalMemory()]
    temporalPointerMemory = [generateTemporalPointerMemory()]
    constantMemory = generateConstantMemory()
    storeConstants(constantMemory, memory)
    virtualMemory = [globalMemory, localMemory, temporalMemory, temporalPointerMemory, constantMemory]
    pointerStack = []
    returnTable = {}

    quadruplePointer = 0
    while True:
        quadruple = quadruples[quadruplePointer]
        #print(quadruple)
        if (quadruple[0] == '='):
            quadruplePointer = runAssignment(quadruple, quadruplePointer, virtualMemory, returnTable)
        elif (quadruple[0] == 'return'):
            quadruplePointer = runReturn(quadruple, virtualMemory, functionDirectory, returnTable)
        elif (quadruple[0] == 'read'):
            quadruplePointer = runRead(quadruple, quadruplePointer, virtualMemory)
        elif (quadruple[0] == 'write'):
            quadruplePointer = runWrite(quadruple, quadruplePointer, virtualMemory)
        elif (quadruple[0] == 'gotof'):
            quadruplePointer = runGotof(quadruple, quadruplePointer, virtualMemory)
        elif (quadruple[0] == 'goto'):
            quadruplePointer = runGoto(quadruple)
        elif (quadruple[0] == 'era'):
            quadruplePointer = runEra(quadruplePointer, virtualMemory)
        elif (quadruple[0] == 'param'):
            quadruplePointer = runParam(quadruple, quadruplePointer, virtualMemory)
        elif (quadruple[0] == 'gosub'):
            quadruplePointer = runGosub(quadruple, quadruplePointer, pointerStack, functionDirectory)
        elif (quadruple[0] == 'ver'):
            quadruplePointer = runVer(quadruple, quadruplePointer, virtualMemory)
        elif (quadruple[0] == 'endfunc'):
            quadruplePointer = runEndfunc(virtualMemory, pointerStack)
        elif (quadruple[0] == 'end'):
            break
        else:
            quadruplePointer = runExpression(quadruple, quadruplePointer, virtualMemory)

# Ejecutar el programa de un archivo introducido por el usuario
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
    #for i in range(len(quadruples)):
    #    print(f'{str(i):>4}', ': ', quadruples[i])
    runProgram(functionDirectory, semanticCube, memory, quadruples)
    