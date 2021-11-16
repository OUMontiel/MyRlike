import ply.lex as lex
import ply.yacc as yacc
import sys
import FunctionDirectory
import SemanticCube
import CodeGeneration

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
    print("LEXER ERROR: ", t.value)
    t.lexer.skip(1)

lexer = lex.lex()

def p_programa(p):
    '''
    programa : PROGRAM programa1 programa2 main OPENPAR CLOSEPAR OPENCURLY programa3 CLOSECURLY
    '''
    print('programa')

def p_programa1(p):
    '''
    programa1 : ID SEMICOLON vars
              | ID SEMICOLON
    '''
    print('programa1')
    FunctionDirectory.functionIDs.append(p[1])
    FunctionDirectory.functionKinds.append('program')
    FunctionDirectory.storeFunction()

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

def p_main(p):
    '''
    main : MAIN
    '''
    print('main')
    print(FunctionDirectory.functionIDs[0])
    FunctionDirectory.currentFunction = FunctionDirectory.functionIDs[0]

def p_vars(p):
    '''
    vars : VARS vars1
    '''
    print('vars')
    FunctionDirectory.buildTable()
    FunctionDirectory.variableTypesCountStack.clear()
    FunctionDirectory.variableTypesCounter = -1

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
    vars3 : OPENBOX exp CLOSEBOX vars4
          | vars4
    '''
    print('vars3')

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
    lista_ids : ID OPENBOX exp CLOSEBOX lista_ids1
              | ID lista_ids1
              | STRING lista_ids1
    '''
    print('lista_ids')
    if (p[1][0] == '"' or p[1][0] == '\''):
        CodeGeneration.operands.append(p[1][1:-1])
    else:
        CodeGeneration.operands.append(p[1])
    CodeGeneration.operators.append('read_write')

def p_lista_ids1(p):
    '''
    lista_ids1 : COMMA lista_ids
               | epsilon
    '''
    print('lista_ids1')

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
    funciones5 : vars guardar_func OPENCURLY funciones6
               | guardar_func OPENCURLY funciones6
    '''
    print('funciones5')

def p_funciones6(p):
    '''
    funciones6 : estatutos funciones6
               | CLOSECURLY funciones
    '''
    print('funciones6')

def p_guardar_func(p):
    '''
    guardar_func : epsilon
    '''
    print('guardar_func')
    FunctionDirectory.functionKinds.append('function')
    FunctionDirectory.storeFunction()
    FunctionDirectory.currentFunction = FunctionDirectory.functionIDs[-1]

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
    if (p[2] == '='):
        CodeGeneration.operands.append(p[1])
        CodeGeneration.types.append(FunctionDirectory.getVariableType(p[1]))
        CodeGeneration.operators.append(p[2])

def p_llamada(p):
    '''
    llamada : funcion SEMICOLON
    '''
    print('llamada')

def p_funcion(p):
    '''
    funcion : ID OPENPAR funcion1
    '''
    print('funcion')

def p_funcion1(p):
    '''
    funcion1 : exp funcion2
    '''
    print('funcion1')

def p_funcion2(p):
    '''
    funcion2 : COMMA funcion1
             | CLOSEPAR
    '''
    print('funcion2')

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
    CodeGeneration.generateOutput()

def p_escritura1(p):
    '''
    escritura1 : lista_ids escritura2
    '''
    print('escritura1')

def p_escritura2(p):
    '''
    escritura2 : COMMA escritura1
               | epsilon
    '''
    print('escritura2')

def p_condicion(p):
    '''
    condicion : IF OPENPAR expresion CLOSEPAR THEN OPENCURLY condicion1
    '''
    print('condicion')

def p_condicion1(p):
    '''
    condicion1 : estatutos condicion1
               | CLOSECURLY condicion2
    '''
    print('condicion1')

def p_condicion2(p):
    '''
    condicion2 : ELSE OPENCURLY condicion3
               | epsilon
    '''
    print('condicion2')

def p_condicion3(p):
    '''
    condicion3 : estatutos condicion3
               | CLOSECURLY
    '''
    print('condicion3')

def p_while(p):
    '''
    while : WHILE OPENPAR expresion CLOSEPAR DO OPENCURLY while1
    '''
    print('while')

def p_while1(p):
    '''
    while1 : estatutos while1
           | CLOSECURLY
    '''
    print('while1')

def p_for(p):
    '''
    for : FOR ID for1 IS exp TO exp DO OPENCURLY for2 CLOSECURLY
    '''
    print('for')

def p_for1(p):
    '''
    for1 : OPENBOX exp CLOSEBOX
         | epsilon
    '''
    print('for1')

def p_for2(p):
    '''
    for2 : estatutos for2
         | epsilon
    '''
    print('for2')

def p_est_exp(p):
    '''
    est_exp : expresion SEMICOLON
    '''
    print('est_exp')

def p_expresion(p):
    '''
    expresion : and guardar_expresion
              | and guardar_expresion expresion1 expresion
    '''
    print('expresion')

def p_expresion1(p):
    '''
    expresion1 : OR
    '''
    print('expresion1')
    CodeGeneration.operators.append(p[1])

def p_guardar_expresion(p):
    '''
    guardar_expresion : epsilon
    '''
    print('guardar_expresion')
    temp = CodeGeneration.generateQuadruple(['+', '-'])
    if (temp != None):
        CodeGeneration.operands.append(temp[0])
        CodeGeneration.types.append(temp[1])

def p_and(p):
    '''
    and : equal guardar_and
        | equal guardar_and and1 and
    '''
    print('and')

def p_and1(p):
    '''
    and1 : AND
    '''
    print('and1')
    CodeGeneration.operators.append(p[1])

def p_guardar_and(p):
    '''
    guardar_and : epsilon
    '''
    print('guardar_and')
    temp = CodeGeneration.generateQuadruple(['&&'])
    if (temp != None):
        CodeGeneration.operands.append(temp[0])
        CodeGeneration.types.append(temp[1])

def p_equal(p):
    '''
    equal : compare guardar_equal
          | compare guardar_equal equal1 equal
    '''
    print('equal')

def p_equal1(p):
    '''
    equal1 : EQ
           | NE
    '''
    print('equal1')
    CodeGeneration.operators.append(p[1])

def p_guardar_equal(p):
    '''
    guardar_equal : epsilon
    '''
    print('guardar_equal')
    temp = CodeGeneration.generateQuadruple(['==', '!='])
    if (temp != None):
        CodeGeneration.operands.append(temp[0])
        CodeGeneration.types.append(temp[1])

def p_compare(p):
    '''
    compare : exp guardar_compare
            | exp guardar_compare compare1 compare
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

def p_guardar_compare(p):
    '''
    guardar_compare : epsilon
    '''
    print('guardar_compare')
    temp = CodeGeneration.generateQuadruple(['<', '<=', '>', '>='])
    if (temp != None):
        CodeGeneration.operands.append(temp[0])
        CodeGeneration.types.append(temp[1])

def p_exp(p):
    '''
    exp : termino guardar_exp
        | termino guardar_exp exp1 exp
    '''
    print('exp')

def p_exp1(p):
    '''
    exp1 : PLUS
         | MINUS
    '''
    print('exp1')
    CodeGeneration.operators.append(p[1])

def p_guardar_exp(p):
    '''
    guardar_exp : epsilon
    '''
    print('guardar_exp')
    temp = CodeGeneration.generateQuadruple(['+', '-'])
    if (temp != None):
        CodeGeneration.operands.append(temp[0])
        CodeGeneration.types.append(temp[1])

def p_termino(p):
    '''
    termino : factor guardar_termino
            | factor guardar_termino termino1 termino
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

def p_guardar_termino(p):
    '''
    guardar_termino : epsilon
    '''
    print('guardar_termino')
    temp = CodeGeneration.generateQuadruple(['*', '/', '%'])
    if (temp != None):
        CodeGeneration.operands.append(temp[0])
        CodeGeneration.types.append(temp[1])

def p_factor(p):
    '''
    factor : ID factor1
           | openpar expresion closepar
           | funcion
           | factor2 varcte
    '''
    print('factor')
    if (p[1] != '(' and p[1] != None):
        CodeGeneration.operands.append(p[1])
        CodeGeneration.types.append(FunctionDirectory.getVariableType(p[1]))

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

def p_factor1(p):
    '''
    factor1 : OPENBOX exp CLOSEBOX
            | epsilon
    '''
    print('factor1')

def p_factor2(p):
    '''
    factor2 : PLUS
            | MINUS
            | epsilon
    '''
    print('factor2')

def p_varcte(p):
    '''
    varcte : ID
           | INT
           | FLOAT
           | CHAR
    '''
    print('varcte')

def p_epsilon(p):
    '''
    epsilon :
    '''
    print('epsilon')

def p_error(p):
	print("PARSER ERROR: ", p)

parser = yacc.yacc()

while True:
    FunctionDirectory.resetFunctionDirectory()
    try:
        path_to_file = input('>> ')
        with open(path_to_file) as file:
            s = file.readlines()
    except EOFError:
        break
    print('\n\n> ------------------------------------------------------------ <\n                      Analizador Semántico                      \n> ------------------------------------------------------------ <')
    parser.parse(''.join(s).replace("\n", " "))
    print('\n\n> ------------------------------------------------------------ <\n                  Directorio de Procedimientos                  \n> ------------------------------------------------------------ <')
    FunctionDirectory.printFunctionDirectory()
    print('\n\n> ------------------------------------------------------------ <\n                         Cubo Semántico                         \n> ------------------------------------------------------------ <')
    SemanticCube.printSemanticCube()
    print('\n\n> ------------------------------------------------------------ <\n                           Estatutos                            \n> ------------------------------------------------------------ <')
    print(CodeGeneration.operands)
    print(CodeGeneration.types)
    print(CodeGeneration.operators)
    print(CodeGeneration.quadruples)
