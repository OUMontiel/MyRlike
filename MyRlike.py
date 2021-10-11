import ply.lex as lex
import ply.yacc as yacc
import sys
from pydoc import locate
import VariableSemantics

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
    'MULTIPLY',
    'DIVIDE',
    'MODULO',
    'PLUS',
    'MINUS',
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
t_MULTIPLY = r'\*'
t_DIVIDE = r'\/'
t_MODULO = r'\%'
t_PLUS = r'\+'
t_MINUS = r'\-'

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
    programa : PROGRAM ID SEMICOLON programa1 programa2 MAIN OPENPAR CLOSEPAR OPENCURLY programa3 CLOSECURLY
    '''
    print('programa')
    VariableSemantics.functionIDsStack.append(p[2])

def p_programa1(p):
    '''
    programa1 : vars
              | epsilon
    '''
    print('programa1')

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

def p_vars(p):
    '''
    vars : VARS vars1
    '''
    print('vars')
    VariableSemantics.buildTable()
    VariableSemantics.variableTypesCountStack.clear()
    VariableSemantics.variableTypesCounter = -1

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
    VariableSemantics.variableIDsStack.append(p[1])
    VariableSemantics.variableTypesCountStack[VariableSemantics.variableTypesCounter] += 1

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
    VariableSemantics.variableTypesCounter += 1
    VariableSemantics.variableTypesCountStack.append(0)

def p_lista_ids(p):
    '''
    lista_ids : ID lista_ids1
    '''
    print('lista_ids')

def p_lista_ids1(p):
    '''
    lista_ids1 : lista_ids2
               | OPENBOX exp CLOSEBOX lista_ids2
    '''
    print('lista_ids1')

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
    print('----------------> ', p[1], ' : ', locate(p[1]))
    VariableSemantics.typesStack.append(p[1])

def p_funciones(p):
    '''
    funciones : FUNCTION funciones1
              | epsilon
    '''
    print('funciones')

def p_funciones1(p):
    '''
    funciones1 : tipo funciones2
               | TYPEVOID funciones2
    '''
    print('funciones1')
    if (p[1] == 'void'):
        print()
        VariableSemantics.typesStack.append(p[1])

def p_funciones2(p):
    '''
    funciones2 : ID OPENPAR funciones3
    '''
    print('funciones2')
    VariableSemantics.functionIDsStack.append(p[1])

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
    funciones5 : vars OPENCURLY funciones6
               | OPENCURLY funciones6
    '''
    print('funciones5')

def p_funciones6(p):
    '''
    funciones6 : estatutos funciones6
               | CLOSECURLY funciones
    '''
    print('funciones6')

def p_parameters(p):
    '''
    parameters : tipo ID parameters1
    '''
    print('parameters')
    VariableSemantics.parameterIDsStack.append(p[2])

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
              | expresion estatutos1
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
    asignacion : ID asignacion1 IS expresion SEMICOLON
    '''
    print('asignacion')

def p_asignacion1(p):
    '''
    asignacion1 : OPENBOX exp CLOSEBOX
                | epsilon
    '''
    print('asignacion1')

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

def p_lectura(p):
    '''
    lectura : READ OPENPAR lista_ids CLOSEPAR SEMICOLON
    '''
    print('lectura')

def p_escritura(p):
    '''
    escritura : WRITE OPENPAR escritura1 CLOSEPAR SEMICOLON
    '''
    print('escritura')

def p_escritura1(p):
    '''
    escritura1 : STRING escritura2
               | lista_ids escritura2
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

def p_expresion(p):
    '''
    expresion : or
    '''
    print('expresion')

def p_or(p):
    '''
    or : and or1
    '''
    print('or')

def p_or1(p):
    '''
    or1 : OR or
        | epsilon
    '''
    print('or1')

def p_and(p):
    '''
    and : equal and1
    '''
    print('and')

def p_and1(p):
    '''
    and1 : AND and
         | epsilon
    '''
    print('and1')

def p_equal(p):
    '''
    equal : compare equal1
    '''
    print('equal')

def p_equal1(p):
    '''
    equal1 : EQ equal
           | NE equal
           | epsilon
    '''
    print('equal1')

def p_compare(p):
    '''
    compare : exp compare1
    '''
    print('compare')

def p_compare1(p):
    '''
    compare1 : LT compare
             | LE compare
             | GT compare
             | GE compare
             | epsilon
    '''
    print('compare1')

def p_exp(p):
    '''
    exp : termino exp1
    '''
    print('exp')

def p_exp1(p):
    '''
    exp1 : PLUS exp
         | MINUS exp
         | epsilon
    '''
    print('exp1')

def p_termino(p):
    '''
    termino : factor termino1
    '''
    print('termino')

def p_termino1(p):
    '''
    termino1 : MULTIPLY termino
             | DIVIDE termino
             | MODULO termino
             | epsilon
    '''
    print('termino1')

def p_factor(p):
    '''
    factor : ID factor1
           | OPENPAR expresion CLOSEPAR
           | funcion
           | factor2 varcte
    '''
    print('factor')

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
    try:
        path_to_file = input('>> ')
        with open(path_to_file) as file:
            s = file.readlines()
    except EOFError:
        break
    parser.parse(''.join(s).replace("\n", " "))
    VariableSemantics.buildFunctionDirectory()
    VariableSemantics.printFunctionDirectory()
