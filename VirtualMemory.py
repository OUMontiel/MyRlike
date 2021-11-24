memory = [{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}]

def eraseLocal():
    for i in range(3, 12):
        memory[i].clear()

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

def printMemory():
    for stack in memory:
        for index in stack:
            print(index, ' : ', stack[index])

def resetMemory():
    for i in range(12):
        memory[i].clear()