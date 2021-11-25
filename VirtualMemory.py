memory = [{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}]

'''
eraseLocal()
    Borra variables locales y temporales
'''
def eraseLocal():
    for i in range(3, 12):
        memory[i].clear()

'''
storeConstant()
constant = el valor de una constante que se va a guardar en memoria virutal
type = el tipo de dato de la constante
    Guarda la constante en la memoria virtual
'''
def storeConstant(constant, type):
    if (type == 'int'):
        if (len(memory[12]) == 1000):
            print('ERROR: Stack overflow!')
            exit()
        memory[12][13000 + len(memory[12])] = int(constant)
        return 13000 + len(memory[12]) - 1
    elif (type == 'float'):
        if (len(memory[13]) == 1000):
            print('ERROR: Stack overflow!')
            exit()
        memory[13][14000 + len(memory[13])] = float(constant)
        return 14000 + len(memory[13]) - 1
    elif (type == 'char'):
        if (len(memory[14]) == 1000):
            print('ERROR: Stack overflow!')
            exit()
        memory[14][15000 + len(memory[14])] = constant
        return 15000 + len(memory[14]) - 1

'''
getContent()
address = la dirección de memoria que se quiere accesar
    Regresa el contenido en la dirección especificada de la memoria virtual
'''
def getContent(address):
    if address in memory[0]:
        return memory[0][address]
    elif address in memory[1]:
        return memory[1][address]
    elif address in memory[2]:
        return memory[2][address]
    elif address in memory[3]:
        return memory[3][address]
    elif address in memory[4]:
        return memory[4][address]
    elif address in memory[5]:
        return memory[5][address]
    elif address in memory[6]:
        return memory[6][address]
    elif address in memory[7]:
        return memory[7][address]
    elif address in memory[8]:
        return memory[8][address]
    elif address in memory[9]:
        return memory[9][address]
    elif address in memory[10]:
        return memory[10][address]
    elif address in memory[11]:
        return memory[11][address]
    elif address in memory[12]:
        return memory[12][address]
    elif address in memory[13]:
        return memory[13][address]
    elif address in memory[14]:
        return memory[14][address]

'''
printMemory()
    Imprime la memoria virtual en consola
'''
def printMemory():
    for stack in memory:
        for index in stack:
            print(index, ' : ', stack[index])

'''
resetMemory():
    Reinicia la memoria virtual borrando todos sus contenidos
'''
def resetMemory():
    for i in range(15):
        memory[i].clear()