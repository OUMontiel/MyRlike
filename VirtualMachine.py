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
virtualMemory = la memoria de la máquina virtual
    Ejectuta el cuádruplo de asignación
'''
def runAssignment(quadruple, virtualMemory):
    right_operand = getContent(quadruple[1], virtualMemory)
    if (right_operand == None):
        print('ERROR: Variables have not been assigned!')
        exit()
    setContent(right_operand, quadruple[3], virtualMemory)

'''
runExpression()
quadruple = cuádruplo de una expresión que se correrá
virtualMemory = la memoria de la máquina virtual
    Ejectuta el cuádruplo de la expresión
'''
def runExpression(quadruple, virtualMemory):
    left_type = getType(quadruple[1])
    right_type = getType(quadruple[2])
    left_operand = getContent(quadruple[1], virtualMemory)
    right_operand = getContent(quadruple[2], virtualMemory)
    if (left_operand == None or right_operand == None):
        print('ERROR: Variables have not been assigned!')
        exit()
    value = calculateExpression(quadruple[0], left_operand, right_operand, left_type, right_type)
    setContent(value, quadruple[3], virtualMemory)

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
        return left_operand + right_operand
    elif (operator == '-'):
        return left_operand - right_operand
    elif (operator == '*'):
        return left_operand * right_operand
    elif (operator == '/'):
        if (left_type == 'int' and right_type == 'int'):
            return left_operand // right_operand
        else:
            return left_operand / right_operand
    elif (operator == '%'):
        return left_operand % right_operand

def runProgram(functionDirectory, semanticCube, memory, quadruples):
    globalMemory = generateGlobalMemory()
    localMemory = [generateLocalMemory()]
    temporalMemory = [generateTemporalMemory()]
    temporalPointerMemory = [generateTemporalPointerMemory()]
    constantMemory = generateConstantMemory()
    storeConstants(constantMemory, memory)
    virtualMemory = [globalMemory, localMemory, temporalMemory, temporalPointerMemory, constantMemory]

    quadruplePointer = 0
    while True:
        quadruple = quadruples[quadruplePointer]
        if (quadruple[0] == '='):
            runAssignment(quadruple, virtualMemory)
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
            runExpression(quadruple, virtualMemory)
            quadruplePointer += 1

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
    