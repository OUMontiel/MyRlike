import ply.lex as lex
import ply.yacc as yacc
import sys
import FunctionDirectory
import SemanticCube
import CodeGeneration
import VirtualMemory

tokens = [
    'PROGRAM',
    'MAIN',
    'VARS',
    'FUNCTION',
    'RETURN',
    'READ',
    'WRITE',
    'IF',
    'THEN',
    'ELSE',
    'WHILE',
    'DO',
    'FOR',
    'TO',
    'TYPEFLOAT',
    'TYPEINT',
    'TYPECHAR',
    'TYPEVOID',
    'ID',
    'INT',
    'FLOAT',
    'CHAR',
    'STRING',
    'SEMICOLON',
    'COLON',
    'COMMA',
    'OPENCURLY',
    'CLOSECURLY',
    'OPENBOX',
    'CLOSEBOX',
    'OPENPAR',
    'CLOSEPAR',
    'IS',
    'OR',
    'AND',
    'EQ',
    'NE',
    'LT',
    'LE',
    'GT',
    'GE',
    'PLUS',
    'MINUS',
    'MULTIPLY',
    'DIVIDE',
    'MODULO',
]

reserved = {
    'Program': 'PROGRAM',
    'main': 'MAIN',
    'VARS': 'VARS',
    'function' : 'FUNCTION',
    'return': 'RETURN',
    'read': 'READ',
    'write': 'WRITE',
    'if': 'IF',
    'then': 'THEN',
    'else': 'ELSE',
    'while': 'WHILE',
    'do': 'DO',
    'for': 'FOR',
    'to': 'TO',
    'float': 'TYPEFLOAT',
    'int': 'TYPEINT',
    'char': 'TYPECHAR',
    'void': 'TYPEVOID'
}

t_SEMICOLON = r'\;'
t_COLON = r'\:'
t_COMMA = r'\,'
t_OPENCURLY = r'\{'
t_CLOSECURLY = r'\}'
t_OPENBOX = r'\['
t_CLOSEBOX = r'\]'
t_OPENPAR = r'\('
t_CLOSEPAR = r'\)'

t_IS = r'\='
t_OR = r'\|\|'
t_AND = r'\&\&'
t_EQ = r'\=\='
t_NE = r'\!\='
t_LT = r'\<'
t_LE = r'\<\='
t_GT = r'\>'
t_GE = r'\>\='
t_PLUS = r'\+'
t_MINUS = r'\-'
t_MULTIPLY = r'\*'
t_DIVIDE = r'\/'
t_MODULO = r'\%'

t_ignore = r' '

def t_PROGRAM(t):
    r'Program'
    return t

def t_MAIN(t):
    r'main'
    return t

def t_VARS(t):
    r'VARS'
    return t

def t_FUNCTION(t):
    r'function'
    return t

def t_RETURN(t):
    r'return'
    return t

def t_READ(t):
    r'read'
    return t

def t_WRITE(t):
    r'write'
    return t

def t_IF(t):
    r'if'
    return t

def t_THEN(t):
    r'then'
    return t

def t_ELSE(t):
    r'else'
    return t

def t_WHILE(t):
    r'while'
    return t

def t_DO(t):
    r'do'
    return t

def t_FOR(t):
    r'for'
    return t

def t_TO(t):
    r'to'
    return t

def t_TYPEFLOAT(t):
    r'float'
    return t

def t_TYPEINT(t):
    r'int'
    return t

def t_TYPECHAR(t):
    r'char'
    return t

def t_TYPEVOID(t):
    r'void'
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = 'ID'
    return t

def t_FLOAT(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_CHAR(t):
    r'\'([^\\\']|(\\\')|(\\\\))?\''
    t.value = str(t.value)
    return t

def t_STRING(t):
    r'\"([^\\\"]|(\\\")|(\\\\))*\"'
    t.value = str(t.value)
    return t

def t_error(t):
    print('LEXER ERROR: ', t.value)
    t.lexer.skip(1)

lexer = lex.lex()

def p_programa(p):
    '''
    programa : PROGRAM programa_punto1 programa1 programa2 main OPENPAR CLOSEPAR OPENCURLY programa3 CLOSECURLY
    '''
    print('programa')
    CodeGeneration.quadruples.append(['end', None, None, None])

def p_programa1(p):
    '''
    programa1 : ID SEMICOLON vars
              | ID SEMICOLON
    '''
    print('programa1')
    FunctionDirectory.buildTables(VirtualMemory.memory)
    FunctionDirectory.variableTypesCountStack.clear()
    FunctionDirectory.variableTypesCounter = -1
    FunctionDirectory.functionIDs.append(p[1])
    FunctionDirectory.functionKinds.append('program')
    FunctionDirectory.storeFunction(len(CodeGeneration.quadruples))
    FunctionDirectory.isGlobal = False

def p_programa2(p):
    '''
    programa2 : funciones
              | epsilon
    '''
    print('programa2')

def p_programa3(p):
    '''
    programa3 : estatutos
              | epsilon
    '''
    print('programa3')

def p_programa_punto1(p):
    '''
    programa_punto1 : epsilon
    '''
    print('programa_punto1')
    CodeGeneration.quadruples.append(['goto', 'main', None, None])

def p_main(p):
    '''
    main : MAIN
    '''
    print('main')
    print(FunctionDirectory.functionIDs[0])
    FunctionDirectory.currentFunction = FunctionDirectory.functionIDs[0]
    CodeGeneration.quadruples[0][3] = len(CodeGeneration.quadruples)

def p_vars(p):
    '''
    vars : VARS vars1
    '''
    print('vars')

def p_vars1(p):
    '''
    vars1 : tipo COLON vars2
    '''
    print('vars1')

def p_vars2(p):
    '''
    vars2 : ID vars3
    '''
    print('vars2')
    FunctionDirectory.variableIDsStack.append(p[1])
    FunctionDirectory.variableTypesCountStack[FunctionDirectory.variableTypesCounter] += 1

def p_vars3(p):
    '''
    vars3 : OPENBOX INT CLOSEBOX vars4
          | vars4
    '''
    print('vars3')
    if (p[1] == '['):
        FunctionDirectory.variableSizesStack.append(p[2])
    else:
        FunctionDirectory.variableSizesStack.append(None)

def p_vars4(p):
    '''
    vars4 : SEMICOLON vars5
          | COMMA vars2
    '''
    print('vars4')

def p_vars5(p):
    '''
    vars5 : vars1
          | epsilon
    '''
    print('vars5')
    FunctionDirectory.variableTypesCounter += 1
    FunctionDirectory.variableTypesCountStack.append(0)

def p_lista_ids(p):
    '''
    lista_ids : lista_ids1 lista_ids2
              | ID lista_ids2
    '''
    print('lista_ids')
    if (p[1] != None):
        variableData = FunctionDirectory.getVariableData(p[1])
        CodeGeneration.operands.append(variableData[1])
        CodeGeneration.operators.append('read')

def p_lista_ids1(p):
    '''
    lista_ids1 : ID OPENBOX exp CLOSEBOX
    '''
    print('lista_ids1')
    if (CodeGeneration.types.pop() != 'int'):
        print('ERROR: Array size has to be of type integer!')
        exit()
    variableData = FunctionDirectory.getVariableData(p[1])
    if (variableData[2] == None):
        print('ERROR: Variable < ', p[1], ' > is not an array!')
        exit()
    arrayData = [CodeGeneration.operands.pop(), VirtualMemory.storeConstant('0', 'int'), VirtualMemory.storeConstant(str(variableData[2]), 'int')]
    CodeGeneration.arregloPoint1(variableData[0], VirtualMemory.storeConstant(variableData[1], 'int'), arrayData, VirtualMemory.memory)

def p_lista_ids2(p):
    '''
    lista_ids2 : COMMA lista_ids
               | epsilon
    '''
    print('lista_ids2')

def p_tipo(p):
    '''
    tipo : TYPEFLOAT
         | TYPEINT
         | TYPECHAR
    '''
    print('tipo')
    FunctionDirectory.typesStack.append(p[1])

def p_tipo_void(p):
    '''
    tipo_void : TYPEVOID
    '''
    print('tipo_void')
    FunctionDirectory.typesStack.append(p[1])

def p_funciones(p):
    '''
    funciones : FUNCTION funciones1
              | epsilon
    '''
    print('funciones')

def p_funciones1(p):
    '''
    funciones1 : tipo funciones2 funciones3
               | tipo_void funciones2 funciones3
    '''
    print('funciones1')

def p_funciones2(p):
    '''
    funciones2 : ID OPENPAR
    '''
    print('funciones2')
    FunctionDirectory.functionIDs.append(p[1])

def p_funciones3(p):
    '''
    funciones3 : parameters funciones4
               | funciones4
    '''
    print('funciones3')

def p_funciones4(p):
    '''
    funciones4 : CLOSEPAR funciones5
    '''
    print('funciones4')

def p_funciones5(p):
    '''
    funciones5 : vars funciones_punto1 OPENCURLY funciones6
               | funciones_punto1 OPENCURLY funciones6
    '''
    print('funciones5')

def p_funciones6(p):
    '''
    funciones6 : estatutos funciones6
               | CLOSECURLY funciones_punto2 funciones
    '''
    print('funciones6')

def p_funciones_punto1(p):
    '''
    funciones_punto1 : epsilon
    '''
    print('funciones_punto1')
    FunctionDirectory.buildTables(VirtualMemory.memory)
    FunctionDirectory.variableTypesCountStack.clear()
    FunctionDirectory.variableTypesCounter = -1
    FunctionDirectory.functionKinds.append('function')
    FunctionDirectory.storeFunction(len(CodeGeneration.quadruples))
    FunctionDirectory.currentFunction = FunctionDirectory.functionIDs[-1]

def p_funciones_punto2(p):
    '''
    funciones_punto2 : epsilon
    '''
    print('funciones_punto2')
    CodeGeneration.quadruples.append(['endfunc', None, None, None])
    CodeGeneration.results.clear()
    CodeGeneration.resultsTypes.clear()
    VirtualMemory.memory[3].clear()
    VirtualMemory.memory[4].clear()
    VirtualMemory.memory[5].clear()

def p_parameters(p):
    '''
    parameters : tipo ID parameters1
    '''
    print('parameters')
    FunctionDirectory.parameterIDsStack.append(p[2])

def p_parameters1(p):
    '''
    parameters1 : COMMA parameters
                | epsilon
    '''
    print('parameters1')

def p_estatutos(p):
    '''
    estatutos : asignacion estatutos1
              | llamada estatutos1
              | retorno estatutos1
              | lectura estatutos1
              | escritura estatutos1
              | condicion estatutos1
              | while estatutos1
              | for estatutos1
              | est_exp estatutos1
    '''
    print('estatutos')

def p_estatutos1(p):
    '''
    estatutos1 : estatutos
               | epsilon
    '''
    print('estatutos1')
    
def p_asignacion(p):
    '''
    asignacion : asignacion1 expresion SEMICOLON
    '''
    print('asignacion')
    CodeGeneration.generateAssignment()

def p_asignacion1(p):
    '''
    asignacion1 : ID OPENBOX exp CLOSEBOX IS
                | ID IS
    '''
    print('asignacion1')
    if (len(p) > 3):
        if (CodeGeneration.types.pop() != 'int'):
            print('ERROR: Array size has to be of type integer!')
            exit()
        variableData = FunctionDirectory.getVariableData(p[1])
        if (variableData[2] == None):
            print('ERROR: Variable < ', p[1], ' > is not an array!')
            exit()
        arrayData = [CodeGeneration.operands.pop(), VirtualMemory.storeConstant('0', 'int'), VirtualMemory.storeConstant(str(variableData[2]), 'int')]
        CodeGeneration.arregloPoint1(variableData[0], VirtualMemory.storeConstant(variableData[1], 'int'), arrayData, VirtualMemory.memory)
        CodeGeneration.operators.append(p[5])
    else:
        variableData = FunctionDirectory.getVariableData(p[1])
        CodeGeneration.operands.append(variableData[1])
        CodeGeneration.types.append(variableData[0])
        CodeGeneration.operators.append(p[2])

def p_llamada(p):
    '''
    llamada : funcion SEMICOLON
    '''
    print('llamada')

def p_funcion(p):
    '''
    funcion : funcion_punto1 OPENPAR funcion1 funcion_punto3
    '''
    print('funcion')

def p_funcion1(p):
    '''
    funcion1 : exp funcion_punto2 funcion2
             | CLOSEPAR
    '''
    print('funcion1')

def p_funcion2(p):
    '''
    funcion2 : COMMA funcion1
             | CLOSEPAR
    '''
    print('funcion2')

def p_funcion_punto1(p):
    '''
    funcion_punto1 : ID
    '''
    print('funcion_punto1')
    CodeGeneration.funcionPoint1(p[1], FunctionDirectory.functionDirectory)

def p_funcion_punto2(p):
    '''
    funcion_punto2 : epsilon
    '''
    print('funcion_punto2')
    CodeGeneration.funcionPoint2()

def p_funcion_punto3(p):
    '''
    funcion_punto3 : epsilon
    '''
    print('funcion_punto3')
    CodeGeneration.funcionPoint3(FunctionDirectory.functionDirectory, VirtualMemory.memory)

def p_retorno(p):
    '''
    retorno : RETURN OPENPAR exp CLOSEPAR SEMICOLON
    '''
    print('retorno')
    CodeGeneration.generateReturn(FunctionDirectory.functionTypes[FunctionDirectory.functionIDs.index(FunctionDirectory.currentFunction)])

def p_lectura(p):
    '''
    lectura : READ OPENPAR lista_ids CLOSEPAR SEMICOLON
    '''
    print('lectura')
    CodeGeneration.generateInput()

def p_escritura(p):
    '''
    escritura : WRITE OPENPAR escritura1 CLOSEPAR SEMICOLON
    '''
    print('escritura')

def p_escritura1(p):
    '''
    escritura1 : escritura_string escritura2
               | escritura_expresion escritura2
    '''
    print('escritura1')

def p_escritura2(p):
    '''
    escritura2 : COMMA escritura1
               | epsilon
    '''
    print('escritura2')

def p_escritura_string(p):
    '''
    escritura_string : STRING
    '''
    print('escritura_string')
    string = p[1][1:-1]
    stringSize = len(string)
    stringAddress = VirtualMemory.storeConstant(string[0], 'char')
    for char in string[1:]:
        VirtualMemory.storeConstant(char, 'char')
    CodeGeneration.operands.append(stringSize)
    CodeGeneration.operands.append(stringAddress)
    CodeGeneration.types.append('string')
    CodeGeneration.operators.append('write')
    CodeGeneration.generateOutput()

def p_escritura_expresion(p):
    '''
    escritura_expresion : expresion
    '''
    print('escritura_expresion')
    CodeGeneration.operators.append('write')
    CodeGeneration.generateOutput()

def p_condicion(p):
    '''
    condicion : IF OPENPAR expresion CLOSEPAR THEN condicion_punto1 OPENCURLY estatutos CLOSECURLY condicion1
    '''
    print('condicion')

def p_condicion1(p):
    '''
    condicion1 : ELSE condicion_punto3 OPENCURLY estatutos CLOSECURLY condicion_punto4
               | condicion_punto2 epsilon
    '''
    print('condicion1')

def p_condicion_punto1(p):
    '''
    condicion_punto1 : epsilon
    '''
    print('condicion_punto1')
    CodeGeneration.condicionPoint1()

def p_condicion_punto2(p):
    '''
    condicion_punto2 : epsilon
    '''
    print('condicion_punto2')
    CodeGeneration.condicionPoint2()

def p_condicion_punto3(p):
    '''
    condicion_punto3 : epsilon
    '''
    print('condicion_punto3')
    CodeGeneration.condicionPoint3()

def p_condicion_punto4(p):
    '''
    condicion_punto4 : epsilon
    '''
    print('condicion_punto4')
    CodeGeneration.condicionPoint4()

def p_while(p):
    '''
    while : WHILE while_punto1 OPENPAR expresion CLOSEPAR while_punto2 DO OPENCURLY estatutos CLOSECURLY while_punto3
    '''
    print('while')

def p_while_punto1(p):
    '''
    while_punto1 : epsilon
    '''
    print('while_punto1')
    CodeGeneration.whilePoint1()

def p_while_punto2(p):
    '''
    while_punto2 : epsilon
    '''
    print('while_punto2')
    CodeGeneration.whilePoint2()

def p_while_punto3(p):
    '''
    while_punto3 : epsilon
    '''
    print('while_punto3')
    CodeGeneration.whilePoint3()

def p_for(p):
    '''
    for : FOR for1 IS exp for_punto1 TO exp for_punto2 DO OPENCURLY estatutos CLOSECURLY for_punto3
    '''
    print('for')

def p_for1(p):
    '''
    for1 : ID OPENBOX exp CLOSEBOX
         | ID
    '''
    print('for1')
    if (len(p) > 2):
        if (CodeGeneration.types.pop() != 'int'):
            print('ERROR: Array size has to be of type integer!')
            exit()
        variableData = FunctionDirectory.getVariableData(p[1])
        if (variableData[2] == None):
            print('ERROR: Variable < ', p[1], ' > is not an array!')
            exit()
        arrayData = [CodeGeneration.operands.pop(), VirtualMemory.storeConstant('0', 'int'), VirtualMemory.storeConstant(str(variableData[2]), 'int')]
        CodeGeneration.arregloPoint1(variableData[0], VirtualMemory.storeConstant(variableData[1], 'int'), arrayData, VirtualMemory.memory)
    else:
        variableData = FunctionDirectory.getVariableData(p[1])
        CodeGeneration.operands.append(variableData[1])
        CodeGeneration.types.append(variableData[0])

def p_for_punto1(p):
    '''
    for_punto1 : epsilon
    '''
    print('for_punto1')
    CodeGeneration.forPoint1()

def p_for_punto2(p):
    '''
    for_punto2 : epsilon
    '''
    print('for_punto2')
    CodeGeneration.forPoint2(VirtualMemory.memory)

def p_for_punto3(p):
    '''
    for_punto3 : epsilon
    '''
    print('for_punto3')
    CodeGeneration.forPoint3()

def p_est_exp(p):
    '''
    est_exp : expresion SEMICOLON
    '''
    print('est_exp')
    CodeGeneration.operands.pop()
    CodeGeneration.types.pop()

def p_expresion(p):
    '''
    expresion : and generate_expresion
              | and generate_expresion expresion1 expresion
    '''
    print('expresion')

def p_expresion1(p):
    '''
    expresion1 : OR
    '''
    print('expresion1')
    CodeGeneration.operators.append(p[1])

def p_generate_expresion(p):
    '''
    generate_expresion : epsilon
    '''
    print('generate_expresion')
    CodeGeneration.generateQuadruple(['||'], VirtualMemory.memory)

def p_and(p):
    '''
    and : equal generate_and
        | equal generate_and and1 and
    '''
    print('and')

def p_and1(p):
    '''
    and1 : AND
    '''
    print('and1')
    CodeGeneration.operators.append(p[1])

def p_generate_and(p):
    '''
    generate_and : epsilon
    '''
    print('generate_and')
    CodeGeneration.generateQuadruple(['&&'], VirtualMemory.memory)

def p_equal(p):
    '''
    equal : compare generate_equal
          | compare generate_equal equal1 equal
    '''
    print('equal')

def p_equal1(p):
    '''
    equal1 : EQ
           | NE
    '''
    print('equal1')
    CodeGeneration.operators.append(p[1])

def p_generate_equal(p):
    '''
    generate_equal : epsilon
    '''
    print('generate_equal')
    CodeGeneration.generateQuadruple(['==', '!='], VirtualMemory.memory)

def p_compare(p):
    '''
    compare : exp generate_compare
            | exp generate_compare compare1 compare
    '''
    print('compare')

def p_compare1(p):
    '''
    compare1 : LT
             | LE
             | GT
             | GE
    '''
    print('compare1')
    CodeGeneration.operators.append(p[1])

def p_generate_compare(p):
    '''
    generate_compare : epsilon
    '''
    print('generate_compare')
    CodeGeneration.generateQuadruple(['<', '<=', '>', '>='], VirtualMemory.memory)

def p_exp(p):
    '''
    exp : termino generate_exp
        | termino generate_exp exp1 exp
    '''
    print('exp')

def p_exp1(p):
    '''
    exp1 : PLUS
         | MINUS
    '''
    print('exp1')
    CodeGeneration.operators.append(p[1])

def p_generate_exp(p):
    '''
    generate_exp : epsilon
    '''
    print('generate_exp')
    CodeGeneration.generateQuadruple(['+', '-'], VirtualMemory.memory)

def p_termino(p):
    '''
    termino : factor generate_termino
            | factor generate_termino termino1 termino
    '''
    print('termino')

def p_termino1(p):
    '''
    termino1 : MULTIPLY
             | DIVIDE
             | MODULO
    '''
    print('termino1')
    CodeGeneration.operators.append(p[1])

def p_generate_termino(p):
    '''
    generate_termino : epsilon
    '''
    print('generate_termino')
    CodeGeneration.generateQuadruple(['*', '/', '%'], VirtualMemory.memory)

def p_factor(p):
    '''
    factor : factor1
           | openpar expresion closepar
           | funcion
           | factor2 varcte
    '''
    print('factor')

def p_factor1(p):
    '''
    factor1 : ID OPENBOX exp CLOSEBOX
            | ID
    '''
    print('factor1')
    if (len(p) > 2):
        if (CodeGeneration.types.pop() != 'int'):
            print('ERROR: Array size has to be of type integer!')
            exit()
        variableData = FunctionDirectory.getVariableData(p[1])
        if (variableData[2] == None):
            print('ERROR: Variable < ', p[1], ' > is not an array!')
            exit()
        arrayData = [CodeGeneration.operands.pop(), VirtualMemory.storeConstant('0', 'int'), VirtualMemory.storeConstant(str(variableData[2]), 'int')]
        CodeGeneration.arregloPoint1(variableData[0], VirtualMemory.storeConstant(variableData[1], 'int'), arrayData, VirtualMemory.memory)
    else:
        variableData = FunctionDirectory.getVariableData(p[1])
        CodeGeneration.operands.append(variableData[1])
        CodeGeneration.types.append(variableData[0])

def p_factor2(p):
    '''
    factor2 : PLUS
            | MINUS
            | epsilon
    '''
    print('factor2')
    if (p[1] == '+'):
        CodeGeneration.extraOperator = '+'
    elif (p[1] == '-'):
        CodeGeneration.extraOperator = '-'
    else:
        CodeGeneration.extraOperator = ''

def p_openpar(p):
    '''
    openpar : OPENPAR
    '''
    print('openpar')
    CodeGeneration.operators.append(p[1])

def p_closepar(p):
    '''
    closepar : CLOSEPAR
    '''
    print('closepar')
    CodeGeneration.operators.pop()

def p_varcte(p):
    '''
    varcte : ID
           | int
           | float
           | char
    '''
    print('varcte')
    if (p[1] != None):
        #CodeGeneration.operands.append(''.join([CodeGeneration.extraOperator, str(p[1])]))
        variableData = FunctionDirectory.getVariableData(p[1])
        CodeGeneration.operands.append(variableData[1])
        CodeGeneration.types.append(variableData[0])

def p_int(p):
    '''
    int : INT
    '''
    print('int')
    #CodeGeneration.operands.append(''.join([CodeGeneration.extraOperator, str(p[1])]))
    CodeGeneration.operands.append(VirtualMemory.storeConstant(p[1], 'int'))
    CodeGeneration.types.append('int')

def p_float(p):
    '''
    float : FLOAT
    '''
    print('float')
    #CodeGeneration.operands.append(''.join([CodeGeneration.extraOperator, str(p[1])]))
    CodeGeneration.operands.append(VirtualMemory.storeConstant(p[1], 'float'))
    CodeGeneration.types.append('float')

def p_char(p):
    '''
    char : CHAR
    '''
    print('char')
    #CodeGeneration.operands.append(''.join([CodeGeneration.extraOperator, str(p[1])]))
    CodeGeneration.operands.append(VirtualMemory.storeConstant(p[1], 'char'))
    CodeGeneration.types.append('char')


def p_epsilon(p):
    '''
    epsilon :
    '''
    print('epsilon')

def p_error(p):
    print('PARSER ERROR: ', p)
    exit()

parser = yacc.yacc()

while True:
    FunctionDirectory.resetFunctionDirectory()
    CodeGeneration.resetCodeGeneration()
    VirtualMemory.resetMemory()
    try:
        path_to_file = input('>> ')
        with open(path_to_file) as file:
            s = file.readlines()
    except EOFError:
        break
    print('\n\n> ------------------------------------------------------------ <\n                      Analizador Semántico                      \n> ------------------------------------------------------------ <')
    parser.parse(''.join(s).replace('\n', ' '))
    print('\n\n> ------------------------------------------------------------ <\n                  Directorio de Procedimientos                  \n> ------------------------------------------------------------ <')
    FunctionDirectory.printFunctionDirectory()
    print('\n\n> ------------------------------------------------------------ <\n                         Cubo Semántico                         \n> ------------------------------------------------------------ <')
    SemanticCube.printSemanticCube()
    print('\n> ------------------------------------------------------------ <\n                         Memoria Virtual                        \n> ------------------------------------------------------------ <')
    VirtualMemory.printMemory()
    print('\n\n> ------------------------------------------------------------ <\n                           Cuádruplos                           \n> ------------------------------------------------------------ <')
    CodeGeneration.printQuadruples()
