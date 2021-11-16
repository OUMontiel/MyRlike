from enum import Enum

class Types(Enum):
    INT = 0
    FLOAT = 1
    CHAR = 2

class Operators(Enum):
    OR = 0
    AND = 1
    EQ = 2
    NE = 3
    LT = 4
    LE = 5
    GT = 6
    GE = 7
    PLUS = 8
    MINUS = 9
    MULTIPLY = 10
    DIVIDE = 11
    MODULO = 12

typeNames = ['int', 'float', 'char']
operatorNames = ['||', '&&', '==', '!=', '<', '<=', '>', '>=', '+', '-', '*', '/', '%']

'''
semanticCube = [[
                 [Types.INT, Types.INT, Types.INT, Types.INT, Types.INT, Types.INT, Types.INT, Types.INT, Types.INT, Types.INT, Types.INT, Types.INT, Types.INT],
                 [Types.INT, Types.INT, Types.INT, Types.INT, Types.INT, Types.INT, Types.INT, Types.INT, Types.FLOAT, Types.FLOAT, Types.FLOAT, Types.FLOAT, 'error'],
                 [Types.INT, Types.INT, Types.INT, Types.INT, Types.INT, Types.INT, Types.INT, Types.INT, Types.CHAR, Types.CHAR, Types.CHAR, Types.CHAR, Types.CHAR],
                ],
                [
                 [Types.INT, Types.INT, Types.INT, Types.INT, Types.INT, Types.INT, Types.INT, Types.INT, Types.FLOAT, Types.FLOAT, Types.FLOAT, Types.FLOAT, 'error'],
                 [Types.INT, Types.INT, Types.INT, Types.INT, Types.INT, Types.INT, Types.INT, Types.INT, Types.FLOAT, Types.FLOAT, Types.FLOAT, Types.FLOAT, 'error'],
                 [Types.INT, Types.INT, Types.INT, Types.INT, Types.INT, Types.INT, Types.INT, Types.INT, 'error', 'error', 'error', 'error', 'error'],
                ],
                [
                 [Types.INT, Types.INT, Types.INT, Types.INT, Types.INT, Types.INT, Types.INT, Types.INT, Types.CHAR, Types.CHAR, Types.CHAR, Types.CHAR, Types.CHAR],
                 [Types.INT, Types.INT, Types.INT, Types.INT, Types.INT, Types.INT, Types.INT, Types.INT, 'error', 'error', 'error', 'error', 'error'],
                 [Types.INT, Types.INT, Types.INT, Types.INT, Types.INT, Types.INT, Types.INT, Types.INT, Types.CHAR, Types.CHAR, Types.CHAR, Types.CHAR, Types.CHAR]
                ]]
'''
semanticCube = [[
                 ['int', 'int', 'int', 'int', 'int', 'int', 'int', 'int', 'int', 'int', 'int', 'int', 'int'],
                 ['int', 'int', 'int', 'int', 'int', 'int', 'int', 'int', 'float', 'float', 'float', 'float', 'error'],
                 ['int', 'int', 'int', 'int', 'int', 'int', 'int', 'int', 'char', 'char', 'char', 'char', 'char'],
                ],
                [
                 ['int', 'int', 'int', 'int', 'int', 'int', 'int', 'int', 'float', 'float', 'float', 'float', 'error'],
                 ['int', 'int', 'int', 'int', 'int', 'int', 'int', 'int', 'float', 'float', 'float', 'float', 'error'],
                 ['int', 'int', 'int', 'int', 'int', 'int', 'int', 'int', 'error', 'error', 'error', 'error', 'error'],
                ],
                [
                 ['int', 'int', 'int', 'int', 'int', 'int', 'int', 'int', 'char', 'char', 'char', 'char', 'char'],
                 ['int', 'int', 'int', 'int', 'int', 'int', 'int', 'int', 'error', 'error', 'error', 'error', 'error'],
                 ['int', 'int', 'int', 'int', 'int', 'int', 'int', 'int', 'char', 'char', 'char', 'char', 'char']
                ]]

def printDivider():
    print('|', end = '')
    for i in range(14):
        print('-------|', end = '')
    print()

def printSemanticCube():
    for type1 in Types:
        print('|---------------------------------------------------------------------------------------------------------------|')
        print('|                                                     ', end = '')
        print(type1.name, end = '\t')
        print('                                                |')
        print('|---------------------------------------------------------------------------------------------------------------|')

        print('|', end = '\t')
        for operator in Operators:
            print('| ', operatorNames[operator.value], end = '\t')
        print('|')
        printDivider()

        for type2 in Types:
            print('|', type2.name, end = '\t'),
            for operator in Operators:
                if semanticCube[type1.value][type2.value][operator.value] == 'int':
                    print('| INT', end = '\t')
                elif semanticCube[type1.value][type2.value][operator.value] == 'float':
                    print('| FLOAT', end = '\t')
                elif semanticCube[type1.value][type2.value][operator.value] == 'char':
                    print('| CHAR', end = '\t')
                else:
                    print('| error', end = '\t')
            print('|')
            printDivider()
        print()
