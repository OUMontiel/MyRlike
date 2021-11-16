
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND CHAR CLOSEBOX CLOSECURLY CLOSEPAR COLON COMMA DIVIDE DO ELSE EQ FLOAT FOR FUNCTION GE GT ID IF INT IS LE LT MAIN MINUS MODULO MULTIPLY NE OPENBOX OPENCURLY OPENPAR OR PLUS PROGRAM READ RETURN SEMICOLON STRING THEN TO TYPECHAR TYPEFLOAT TYPEINT TYPEVOID VARS WHILE WRITE\n    programa : PROGRAM programa1 programa2 main OPENPAR CLOSEPAR OPENCURLY programa3 CLOSECURLY\n    \n    programa1 : ID SEMICOLON vars\n              | ID SEMICOLON\n    \n    programa2 : funciones\n              | epsilon\n    \n    programa3 : estatutos\n              | epsilon\n    \n    main : MAIN\n    \n    vars : VARS vars1\n    \n    vars1 : tipo COLON vars2\n    \n    vars2 : ID vars3\n    \n    vars3 : OPENBOX exp CLOSEBOX vars4\n          | vars4\n    \n    vars4 : SEMICOLON vars5\n          | COMMA vars2\n    \n    vars5 : vars1\n          | epsilon\n    \n    lista_ids : ID OPENBOX exp CLOSEBOX lista_ids1\n              | ID lista_ids1\n              | STRING lista_ids1\n    \n    lista_ids1 : COMMA lista_ids\n               | epsilon\n    \n    tipo : TYPEFLOAT\n         | TYPEINT\n         | TYPECHAR\n    \n    tipo_void : TYPEVOID\n    \n    funciones : FUNCTION funciones1\n              | epsilon\n    \n    funciones1 : tipo funciones2 funciones3\n               | tipo_void funciones2 funciones3\n    \n    funciones2 : ID OPENPAR\n    \n    funciones3 : parameters funciones4\n               | funciones4\n    \n    funciones4 : CLOSEPAR funciones5\n    \n    funciones5 : vars guardar_func OPENCURLY funciones6\n               | guardar_func OPENCURLY funciones6\n    \n    funciones6 : estatutos funciones6\n               | CLOSECURLY funciones\n    \n    guardar_func : epsilon\n    \n    parameters : tipo ID parameters1\n    \n    parameters1 : COMMA parameters\n                | epsilon\n    \n    estatutos : asignacion estatutos1\n              | llamada estatutos1\n              | retorno estatutos1\n              | lectura estatutos1\n              | escritura estatutos1\n              | condicion estatutos1\n              | while estatutos1\n              | for estatutos1\n              | est_exp estatutos1\n    \n    estatutos1 : estatutos\n               | epsilon\n    \n    asignacion : asignacion1 expresion SEMICOLON\n    \n    asignacion1 : ID OPENBOX exp CLOSEBOX IS\n                | ID IS\n    \n    llamada : funcion SEMICOLON\n    \n    funcion : ID OPENPAR funcion1\n    \n    funcion1 : exp funcion2\n    \n    funcion2 : COMMA funcion1\n             | CLOSEPAR\n    \n    retorno : RETURN OPENPAR exp CLOSEPAR SEMICOLON\n    \n    lectura : READ OPENPAR lista_ids CLOSEPAR SEMICOLON\n    \n    escritura : WRITE OPENPAR escritura1 CLOSEPAR SEMICOLON\n    \n    escritura1 : lista_ids escritura2\n    \n    escritura2 : COMMA escritura1\n               | epsilon\n    \n    condicion : IF OPENPAR expresion CLOSEPAR THEN OPENCURLY condicion1\n    \n    condicion1 : estatutos condicion1\n               | CLOSECURLY condicion2\n    \n    condicion2 : ELSE OPENCURLY condicion3\n               | epsilon\n    \n    condicion3 : estatutos condicion3\n               | CLOSECURLY\n    \n    while : WHILE OPENPAR expresion CLOSEPAR DO OPENCURLY while1\n    \n    while1 : estatutos while1\n           | CLOSECURLY\n    \n    for : FOR ID for1 IS exp TO exp DO OPENCURLY for2 CLOSECURLY\n    \n    for1 : OPENBOX exp CLOSEBOX\n         | epsilon\n    \n    for2 : estatutos for2\n         | epsilon\n    \n    est_exp : expresion SEMICOLON\n    \n    expresion : and expression1\n              | and expression1 expression2 expresion\n    \n    expression1 : epsilon\n    \n    expression2 : OR\n    \n    and : equal and1\n        | equal and1 and2 and\n    \n    and1 : epsilon\n    \n    and2 : AND\n    \n    equal : compare equal1\n          | compare equal1 equal2 equal\n    \n    equal1 : epsilon\n    \n    equal2 : EQ\n           | NE\n    \n    compare : exp compare1\n            | exp compare1 compare2 compare\n    \n    compare1 : epsilon\n    \n    compare2 : LT\n             | LE\n             | GT\n             | GE\n    \n    exp : termino exp1\n        | termino exp1 exp2 exp\n    \n    exp1 : epsilon\n    \n    exp2 : PLUS\n         | MINUS\n    \n    termino : factor termino1\n            | factor termino1 termino2 termino\n    \n    termino1 : epsilon\n    \n    termino2 : MULTIPLY\n             | DIVIDE\n             | MODULO\n    \n    factor : ID factor1\n           | openpar expresion closepar\n           | funcion\n           | factor2 varcte\n    \n    openpar : OPENPAR\n    \n    closepar : CLOSEPAR\n    \n    factor1 : OPENBOX exp CLOSEBOX\n            | epsilon\n    \n    factor2 : PLUS\n            | MINUS\n            | epsilon\n    \n    varcte : ID\n           | INT\n           | FLOAT\n           | CHAR\n    \n    epsilon :\n    '
    
_lr_action_items = {'PROGRAM':([0,],[2,]),'$end':([1,88,],[0,-1,]),'ID':([2,13,14,15,16,17,18,28,35,36,45,48,49,50,51,52,53,54,55,56,57,58,67,74,75,76,77,82,84,87,89,90,91,92,93,94,95,96,97,98,99,103,104,105,106,109,110,111,112,114,115,116,136,138,145,146,148,149,150,151,152,161,166,167,168,169,170,171,172,173,174,175,176,177,178,179,191,193,198,202,206,215,216,219,225,228,229,230,232,233,234,235,236,237,239,240,242,243,245,246,247,248,249,251,252,253,254,],[4,23,23,-23,-24,-25,-26,37,44,68,-119,-125,68,68,68,68,68,68,68,68,68,101,113,101,131,-123,-124,68,101,44,-43,-52,-53,-44,-45,-46,-47,-48,-49,-50,-51,-125,-83,-57,101,154,154,101,101,101,-56,101,68,68,-54,101,101,-100,-101,-102,-103,101,101,-87,101,-91,101,-95,-96,101,-107,-108,101,-112,-113,-114,101,154,154,101,101,-62,-63,-64,-55,68,68,101,-68,68,-130,-75,68,-77,-69,-70,-72,-76,68,68,-71,68,-74,68,-125,-73,-78,]),'FUNCTION':([3,9,19,25,43,83,85,86,139,141,142,143,144,213,],[8,-3,-2,-9,-10,-11,-13,-130,8,-14,-16,-17,-15,-12,]),'MAIN':([3,5,6,7,9,12,19,25,29,31,34,38,39,43,83,85,86,137,139,141,142,143,144,182,183,184,185,213,],[-130,11,-4,-5,-3,-27,-2,-9,-29,-33,-30,-32,-34,-10,-11,-13,-130,-36,-130,-14,-16,-17,-15,-35,-37,-38,-28,-12,]),'SEMICOLON':([4,44,59,60,62,68,69,70,71,72,73,100,101,102,107,108,117,118,119,120,121,122,123,124,125,126,127,128,130,131,132,133,134,164,180,181,186,188,189,190,196,204,205,207,208,209,210,211,212,214,226,],[9,86,104,105,-130,-130,-130,-130,-130,-130,-130,145,-130,-117,-97,-99,-115,-122,-84,-86,-88,-90,-92,-94,-104,-106,-109,-111,-118,-126,-127,-128,-129,-58,-116,-120,86,215,-98,216,219,-121,-59,-61,-85,-89,-93,-105,-110,-121,-60,]),'TYPEFLOAT':([8,20,22,24,33,79,86,],[15,15,15,15,-31,15,15,]),'TYPEINT':([8,20,22,24,33,79,86,],[16,16,16,16,-31,16,16,]),'TYPECHAR':([8,20,22,24,33,79,86,],[17,17,17,17,-31,17,17,]),'TYPEVOID':([8,],[18,]),'VARS':([9,32,],[20,20,]),'OPENPAR':([10,11,23,36,45,49,50,51,52,53,54,55,56,57,58,61,63,64,65,66,68,74,82,84,89,90,91,92,93,94,95,96,97,98,99,101,104,105,106,111,112,114,115,116,136,138,145,146,148,149,150,151,152,161,166,167,168,169,170,171,172,173,174,175,176,177,178,179,191,202,206,215,216,219,225,228,229,230,232,233,234,235,236,237,239,240,242,243,245,246,247,248,249,251,253,254,],[21,-8,33,45,-119,45,45,45,45,45,45,45,45,45,45,106,109,110,111,112,116,45,45,45,-43,-52,-53,-44,-45,-46,-47,-48,-49,-50,-51,116,-83,-57,45,45,45,45,-56,45,45,45,-54,45,45,-100,-101,-102,-103,45,45,-87,45,-91,45,-95,-96,45,-107,-108,45,-112,-113,-114,45,45,45,-62,-63,-64,-55,45,45,45,-68,45,-130,-75,45,-77,-69,-70,-72,-76,45,45,-71,45,-74,45,-73,-78,]),'COLON':([15,16,17,26,],[-23,-24,-25,35,]),'CLOSEPAR':([21,22,24,30,33,37,62,69,70,71,72,73,78,80,101,102,107,108,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,147,153,154,155,156,157,158,159,164,165,180,181,189,192,194,195,197,199,205,207,208,209,210,211,212,214,218,220,226,227,231,],[27,32,32,32,-31,-130,-130,-130,-130,-130,-130,-130,-40,-42,-130,-117,-97,-99,-115,-122,-84,-86,-88,-90,-92,-94,-104,-106,-109,-111,181,-118,-126,-127,-128,-129,-41,188,190,-130,-130,196,-130,200,201,-58,207,-116,-120,-98,-19,-22,-20,-65,-67,-59,-61,-85,-89,-93,-105,-110,-121,-21,-66,-60,-130,-18,]),'OPENCURLY':([25,27,32,40,41,42,43,81,83,85,86,141,142,143,144,213,221,222,241,244,],[-9,36,-130,-130,82,-39,-10,136,-11,-13,-130,-14,-16,-17,-15,-12,228,229,245,246,]),'CLOSECURLY':([36,46,47,48,49,50,51,52,53,54,55,56,57,82,89,90,91,92,93,94,95,96,97,98,99,104,105,136,138,145,215,216,219,228,229,232,233,234,235,236,237,239,240,242,243,245,246,247,248,249,250,251,252,253,254,255,],[-130,88,-6,-7,-130,-130,-130,-130,-130,-130,-130,-130,-130,139,-43,-52,-53,-44,-45,-46,-47,-48,-49,-50,-51,-83,-57,139,139,-54,-62,-63,-64,234,237,-68,234,-130,-75,237,-77,-69,-70,-72,-76,249,-130,-71,249,-74,254,-130,-82,-73,-78,-81,]),'INT':([36,45,48,49,50,51,52,53,54,55,56,57,58,74,75,76,77,82,84,89,90,91,92,93,94,95,96,97,98,99,103,104,105,106,111,112,114,115,116,136,138,145,146,148,149,150,151,152,161,166,167,168,169,170,171,172,173,174,175,176,177,178,179,191,202,206,215,216,219,225,228,229,230,232,233,234,235,236,237,239,240,242,243,245,246,247,248,249,251,252,253,254,],[-130,-119,-125,-130,-130,-130,-130,-130,-130,-130,-130,-130,-130,-130,132,-123,-124,-130,-130,-43,-52,-53,-44,-45,-46,-47,-48,-49,-50,-51,-125,-83,-57,-130,-130,-130,-130,-56,-130,-130,-130,-54,-130,-130,-100,-101,-102,-103,-130,-130,-87,-130,-91,-130,-95,-96,-130,-107,-108,-130,-112,-113,-114,-130,-130,-130,-62,-63,-64,-55,-130,-130,-130,-68,-130,-130,-75,-130,-77,-69,-70,-72,-76,-130,-130,-71,-130,-74,-130,-125,-73,-78,]),'FLOAT':([36,45,48,49,50,51,52,53,54,55,56,57,58,74,75,76,77,82,84,89,90,91,92,93,94,95,96,97,98,99,103,104,105,106,111,112,114,115,116,136,138,145,146,148,149,150,151,152,161,166,167,168,169,170,171,172,173,174,175,176,177,178,179,191,202,206,215,216,219,225,228,229,230,232,233,234,235,236,237,239,240,242,243,245,246,247,248,249,251,252,253,254,],[-130,-119,-125,-130,-130,-130,-130,-130,-130,-130,-130,-130,-130,-130,133,-123,-124,-130,-130,-43,-52,-53,-44,-45,-46,-47,-48,-49,-50,-51,-125,-83,-57,-130,-130,-130,-130,-56,-130,-130,-130,-54,-130,-130,-100,-101,-102,-103,-130,-130,-87,-130,-91,-130,-95,-96,-130,-107,-108,-130,-112,-113,-114,-130,-130,-130,-62,-63,-64,-55,-130,-130,-130,-68,-130,-130,-75,-130,-77,-69,-70,-72,-76,-130,-130,-71,-130,-74,-130,-125,-73,-78,]),'CHAR':([36,45,48,49,50,51,52,53,54,55,56,57,58,74,75,76,77,82,84,89,90,91,92,93,94,95,96,97,98,99,103,104,105,106,111,112,114,115,116,136,138,145,146,148,149,150,151,152,161,166,167,168,169,170,171,172,173,174,175,176,177,178,179,191,202,206,215,216,219,225,228,229,230,232,233,234,235,236,237,239,240,242,243,245,246,247,248,249,251,252,253,254,],[-130,-119,-125,-130,-130,-130,-130,-130,-130,-130,-130,-130,-130,-130,134,-123,-124,-130,-130,-43,-52,-53,-44,-45,-46,-47,-48,-49,-50,-51,-125,-83,-57,-130,-130,-130,-130,-56,-130,-130,-130,-54,-130,-130,-100,-101,-102,-103,-130,-130,-87,-130,-91,-130,-95,-96,-130,-107,-108,-130,-112,-113,-114,-130,-130,-130,-62,-63,-64,-55,-130,-130,-130,-68,-130,-130,-75,-130,-77,-69,-70,-72,-76,-130,-130,-71,-130,-74,-130,-125,-73,-78,]),'RETURN':([36,49,50,51,52,53,54,55,56,57,82,89,90,91,92,93,94,95,96,97,98,99,104,105,136,138,145,215,216,219,228,229,232,233,234,235,236,237,239,240,242,243,245,246,247,248,249,251,253,254,],[61,61,61,61,61,61,61,61,61,61,61,-43,-52,-53,-44,-45,-46,-47,-48,-49,-50,-51,-83,-57,61,61,-54,-62,-63,-64,61,61,-68,61,-130,-75,61,-77,-69,-70,-72,-76,61,61,-71,61,-74,61,-73,-78,]),'READ':([36,49,50,51,52,53,54,55,56,57,82,89,90,91,92,93,94,95,96,97,98,99,104,105,136,138,145,215,216,219,228,229,232,233,234,235,236,237,239,240,242,243,245,246,247,248,249,251,253,254,],[63,63,63,63,63,63,63,63,63,63,63,-43,-52,-53,-44,-45,-46,-47,-48,-49,-50,-51,-83,-57,63,63,-54,-62,-63,-64,63,63,-68,63,-130,-75,63,-77,-69,-70,-72,-76,63,63,-71,63,-74,63,-73,-78,]),'WRITE':([36,49,50,51,52,53,54,55,56,57,82,89,90,91,92,93,94,95,96,97,98,99,104,105,136,138,145,215,216,219,228,229,232,233,234,235,236,237,239,240,242,243,245,246,247,248,249,251,253,254,],[64,64,64,64,64,64,64,64,64,64,64,-43,-52,-53,-44,-45,-46,-47,-48,-49,-50,-51,-83,-57,64,64,-54,-62,-63,-64,64,64,-68,64,-130,-75,64,-77,-69,-70,-72,-76,64,64,-71,64,-74,64,-73,-78,]),'IF':([36,49,50,51,52,53,54,55,56,57,82,89,90,91,92,93,94,95,96,97,98,99,104,105,136,138,145,215,216,219,228,229,232,233,234,235,236,237,239,240,242,243,245,246,247,248,249,251,253,254,],[65,65,65,65,65,65,65,65,65,65,65,-43,-52,-53,-44,-45,-46,-47,-48,-49,-50,-51,-83,-57,65,65,-54,-62,-63,-64,65,65,-68,65,-130,-75,65,-77,-69,-70,-72,-76,65,65,-71,65,-74,65,-73,-78,]),'WHILE':([36,49,50,51,52,53,54,55,56,57,82,89,90,91,92,93,94,95,96,97,98,99,104,105,136,138,145,215,216,219,228,229,232,233,234,235,236,237,239,240,242,243,245,246,247,248,249,251,253,254,],[66,66,66,66,66,66,66,66,66,66,66,-43,-52,-53,-44,-45,-46,-47,-48,-49,-50,-51,-83,-57,66,66,-54,-62,-63,-64,66,66,-68,66,-130,-75,66,-77,-69,-70,-72,-76,66,66,-71,66,-74,66,-73,-78,]),'FOR':([36,49,50,51,52,53,54,55,56,57,82,89,90,91,92,93,94,95,96,97,98,99,104,105,136,138,145,215,216,219,228,229,232,233,234,235,236,237,239,240,242,243,245,246,247,248,249,251,253,254,],[67,67,67,67,67,67,67,67,67,67,67,-43,-52,-53,-44,-45,-46,-47,-48,-49,-50,-51,-83,-57,67,67,-54,-62,-63,-64,67,67,-68,67,-130,-75,67,-77,-69,-70,-72,-76,67,67,-71,67,-74,67,-73,-78,]),'PLUS':([36,45,49,50,51,52,53,54,55,56,57,58,60,68,72,73,74,82,84,89,90,91,92,93,94,95,96,97,98,99,101,102,104,105,106,111,112,114,115,116,117,118,125,126,127,128,130,131,132,133,134,136,138,145,146,148,149,150,151,152,161,164,166,167,168,169,170,171,172,173,174,175,176,177,178,179,180,181,191,202,204,205,206,207,212,214,215,216,219,225,226,228,229,230,232,233,234,235,236,237,239,240,242,243,245,246,247,248,249,251,253,254,],[76,-119,76,76,76,76,76,76,76,76,76,76,-117,-130,-130,-130,76,76,76,-43,-52,-53,-44,-45,-46,-47,-48,-49,-50,-51,-130,-117,-83,-57,76,76,76,76,-56,76,-115,-122,174,-106,-109,-111,-118,-126,-127,-128,-129,76,76,-54,76,76,-100,-101,-102,-103,76,-58,76,-87,76,-91,76,-95,-96,76,-107,-108,76,-112,-113,-114,-116,-120,76,76,-121,-59,76,-61,-110,-121,-62,-63,-64,-55,-60,76,76,76,-68,76,-130,-75,76,-77,-69,-70,-72,-76,76,76,-71,76,-74,76,-73,-78,]),'MINUS':([36,45,49,50,51,52,53,54,55,56,57,58,60,68,72,73,74,82,84,89,90,91,92,93,94,95,96,97,98,99,101,102,104,105,106,111,112,114,115,116,117,118,125,126,127,128,130,131,132,133,134,136,138,145,146,148,149,150,151,152,161,164,166,167,168,169,170,171,172,173,174,175,176,177,178,179,180,181,191,202,204,205,206,207,212,214,215,216,219,225,226,228,229,230,232,233,234,235,236,237,239,240,242,243,245,246,247,248,249,251,253,254,],[77,-119,77,77,77,77,77,77,77,77,77,77,-117,-130,-130,-130,77,77,77,-43,-52,-53,-44,-45,-46,-47,-48,-49,-50,-51,-130,-117,-83,-57,77,77,77,77,-56,77,-115,-122,175,-106,-109,-111,-118,-126,-127,-128,-129,77,77,-54,77,77,-100,-101,-102,-103,77,-58,77,-87,77,-91,77,-95,-96,77,-107,-108,77,-112,-113,-114,-116,-120,77,77,-121,-59,77,-61,-110,-121,-62,-63,-64,-55,-60,77,77,77,-68,77,-130,-75,77,-77,-69,-70,-72,-76,77,77,-71,77,-74,77,-73,-78,]),'COMMA':([37,44,72,73,101,102,117,118,125,126,127,128,130,131,132,133,134,154,155,157,164,165,180,181,186,192,194,195,205,207,211,212,214,218,226,227,231,],[79,87,-130,-130,-130,-117,-115,-122,-104,-106,-109,-111,-118,-126,-127,-128,-129,193,193,198,-58,206,-116,-120,87,-19,-22,-20,-59,-61,-105,-110,-121,-21,-60,193,-18,]),'OPENBOX':([44,68,101,113,154,],[84,114,146,161,191,]),'MULTIPLY':([60,68,73,101,102,117,118,127,128,130,131,132,133,134,164,180,181,204,205,207,214,226,],[-117,-130,-130,-130,-117,-115,-122,177,-111,-118,-126,-127,-128,-129,-58,-116,-120,-121,-59,-61,-121,-60,]),'DIVIDE':([60,68,73,101,102,117,118,127,128,130,131,132,133,134,164,180,181,204,205,207,214,226,],[-117,-130,-130,-130,-117,-115,-122,178,-111,-118,-126,-127,-128,-129,-58,-116,-120,-121,-59,-61,-121,-60,]),'MODULO':([60,68,73,101,102,117,118,127,128,130,131,132,133,134,164,180,181,204,205,207,214,226,],[-117,-130,-130,-130,-117,-115,-122,179,-111,-118,-126,-127,-128,-129,-58,-116,-120,-121,-59,-61,-121,-60,]),'LT':([60,62,68,72,73,101,102,107,108,117,118,125,126,127,128,130,131,132,133,134,164,180,181,204,205,207,211,212,214,226,],[-117,-130,-130,-130,-130,-130,-117,149,-99,-115,-122,-104,-106,-109,-111,-118,-126,-127,-128,-129,-58,-116,-120,-121,-59,-61,-105,-110,-121,-60,]),'LE':([60,62,68,72,73,101,102,107,108,117,118,125,126,127,128,130,131,132,133,134,164,180,181,204,205,207,211,212,214,226,],[-117,-130,-130,-130,-130,-130,-117,150,-99,-115,-122,-104,-106,-109,-111,-118,-126,-127,-128,-129,-58,-116,-120,-121,-59,-61,-105,-110,-121,-60,]),'GT':([60,62,68,72,73,101,102,107,108,117,118,125,126,127,128,130,131,132,133,134,164,180,181,204,205,207,211,212,214,226,],[-117,-130,-130,-130,-130,-130,-117,151,-99,-115,-122,-104,-106,-109,-111,-118,-126,-127,-128,-129,-58,-116,-120,-121,-59,-61,-105,-110,-121,-60,]),'GE':([60,62,68,72,73,101,102,107,108,117,118,125,126,127,128,130,131,132,133,134,164,180,181,204,205,207,211,212,214,226,],[-117,-130,-130,-130,-130,-130,-117,152,-99,-115,-122,-104,-106,-109,-111,-118,-126,-127,-128,-129,-58,-116,-120,-121,-59,-61,-105,-110,-121,-60,]),'EQ':([60,62,68,71,72,73,101,102,107,108,117,118,123,124,125,126,127,128,130,131,132,133,134,164,180,181,189,204,205,207,211,212,214,226,],[-117,-130,-130,-130,-130,-130,-130,-117,-97,-99,-115,-122,171,-94,-104,-106,-109,-111,-118,-126,-127,-128,-129,-58,-116,-120,-98,-121,-59,-61,-105,-110,-121,-60,]),'NE':([60,62,68,71,72,73,101,102,107,108,117,118,123,124,125,126,127,128,130,131,132,133,134,164,180,181,189,204,205,207,211,212,214,226,],[-117,-130,-130,-130,-130,-130,-130,-117,-97,-99,-115,-122,172,-94,-104,-106,-109,-111,-118,-126,-127,-128,-129,-58,-116,-120,-98,-121,-59,-61,-105,-110,-121,-60,]),'AND':([60,62,68,70,71,72,73,101,102,107,108,117,118,121,122,123,124,125,126,127,128,130,131,132,133,134,164,180,181,189,204,205,207,210,211,212,214,226,],[-117,-130,-130,-130,-130,-130,-130,-130,-117,-97,-99,-115,-122,169,-90,-92,-94,-104,-106,-109,-111,-118,-126,-127,-128,-129,-58,-116,-120,-98,-121,-59,-61,-93,-105,-110,-121,-60,]),'OR':([60,62,68,69,70,71,72,73,101,102,107,108,117,118,119,120,121,122,123,124,125,126,127,128,130,131,132,133,134,164,180,181,189,204,205,207,209,210,211,212,214,226,],[-117,-130,-130,-130,-130,-130,-130,-130,-130,-117,-97,-99,-115,-122,167,-86,-88,-90,-92,-94,-104,-106,-109,-111,-118,-126,-127,-128,-129,-58,-116,-120,-98,-121,-59,-61,-89,-93,-105,-110,-121,-60,]),'IS':([68,113,160,162,204,224,],[115,-130,202,-80,225,-79,]),'CLOSEBOX':([72,73,101,102,117,118,125,126,127,128,130,131,132,133,134,140,163,164,180,181,187,203,205,207,211,212,214,217,226,],[-130,-130,-130,-117,-115,-122,-104,-106,-109,-111,-118,-126,-127,-128,-129,186,204,-58,-116,-120,214,224,-59,-61,-105,-110,-121,227,-60,]),'TO':([72,73,101,102,117,118,125,126,127,128,130,131,132,133,134,164,180,181,205,207,211,212,214,223,226,],[-130,-130,-130,-117,-115,-122,-104,-106,-109,-111,-118,-126,-127,-128,-129,-58,-116,-120,-59,-61,-105,-110,-121,230,-60,]),'DO':([72,73,101,102,117,118,125,126,127,128,130,131,132,133,134,164,180,181,201,205,207,211,212,214,226,238,],[-130,-130,-130,-117,-115,-122,-104,-106,-109,-111,-118,-126,-127,-128,-129,-58,-116,-120,222,-59,-61,-105,-110,-121,-60,244,]),'STRING':([109,110,193,198,],[155,155,155,155,]),'THEN':([200,],[221,]),'ELSE':([234,],[241,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'programa':([0,],[1,]),'programa1':([2,],[3,]),'programa2':([3,],[5,]),'funciones':([3,139,],[6,184,]),'epsilon':([3,32,36,37,40,49,50,51,52,53,54,55,56,57,58,62,68,69,70,71,72,73,74,82,84,86,101,106,111,112,113,114,116,136,138,139,146,148,154,155,157,161,166,168,170,173,176,191,202,206,227,228,229,230,233,234,236,245,246,248,251,],[7,42,48,80,42,91,91,91,91,91,91,91,91,91,103,108,118,120,122,124,126,128,103,103,103,143,118,103,103,103,162,103,103,103,103,185,103,103,194,194,199,103,103,103,103,103,103,103,103,103,194,103,103,103,103,242,103,103,252,103,252,]),'main':([5,],[10,]),'funciones1':([8,],[12,]),'tipo':([8,20,22,24,79,86,],[13,26,28,28,28,26,]),'tipo_void':([8,],[14,]),'vars':([9,32,],[19,40,]),'funciones2':([13,14,],[22,24,]),'vars1':([20,86,],[25,142,]),'funciones3':([22,24,],[29,34,]),'parameters':([22,24,79,],[30,30,135,]),'funciones4':([22,24,30,],[31,31,38,]),'funciones5':([32,],[39,]),'guardar_func':([32,40,],[41,81,]),'vars2':([35,87,],[43,144,]),'programa3':([36,],[46,]),'estatutos':([36,49,50,51,52,53,54,55,56,57,82,136,138,228,229,233,236,245,246,248,251,],[47,90,90,90,90,90,90,90,90,90,138,138,138,233,236,233,236,248,251,248,251,]),'asignacion':([36,49,50,51,52,53,54,55,56,57,82,136,138,228,229,233,236,245,246,248,251,],[49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,]),'llamada':([36,49,50,51,52,53,54,55,56,57,82,136,138,228,229,233,236,245,246,248,251,],[50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,]),'retorno':([36,49,50,51,52,53,54,55,56,57,82,136,138,228,229,233,236,245,246,248,251,],[51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,]),'lectura':([36,49,50,51,52,53,54,55,56,57,82,136,138,228,229,233,236,245,246,248,251,],[52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,]),'escritura':([36,49,50,51,52,53,54,55,56,57,82,136,138,228,229,233,236,245,246,248,251,],[53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,]),'condicion':([36,49,50,51,52,53,54,55,56,57,82,136,138,228,229,233,236,245,246,248,251,],[54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,]),'while':([36,49,50,51,52,53,54,55,56,57,82,136,138,228,229,233,236,245,246,248,251,],[55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,]),'for':([36,49,50,51,52,53,54,55,56,57,82,136,138,228,229,233,236,245,246,248,251,],[56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,]),'est_exp':([36,49,50,51,52,53,54,55,56,57,82,136,138,228,229,233,236,245,246,248,251,],[57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,]),'asignacion1':([36,49,50,51,52,53,54,55,56,57,82,136,138,228,229,233,236,245,246,248,251,],[58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,]),'expresion':([36,49,50,51,52,53,54,55,56,57,58,74,82,111,112,136,138,166,228,229,233,236,245,246,248,251,],[59,59,59,59,59,59,59,59,59,59,100,129,59,158,159,59,59,208,59,59,59,59,59,59,59,59,]),'funcion':([36,49,50,51,52,53,54,55,56,57,58,74,82,84,106,111,112,114,116,136,138,146,148,161,166,168,170,173,176,191,202,206,228,229,230,233,236,245,246,248,251,],[60,60,60,60,60,60,60,60,60,60,102,102,60,102,102,102,102,102,102,60,60,102,102,102,102,102,102,102,102,102,102,102,60,60,102,60,60,60,60,60,60,]),'exp':([36,49,50,51,52,53,54,55,56,57,58,74,82,84,106,111,112,114,116,136,138,146,148,161,166,168,170,173,191,202,206,228,229,230,233,236,245,246,248,251,],[62,62,62,62,62,62,62,62,62,62,62,62,62,140,147,62,62,163,165,62,62,187,62,203,62,62,62,211,217,223,165,62,62,238,62,62,62,62,62,62,]),'and':([36,49,50,51,52,53,54,55,56,57,58,74,82,111,112,136,138,166,168,228,229,233,236,245,246,248,251,],[69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,209,69,69,69,69,69,69,69,69,]),'equal':([36,49,50,51,52,53,54,55,56,57,58,74,82,111,112,136,138,166,168,170,228,229,233,236,245,246,248,251,],[70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,210,70,70,70,70,70,70,70,70,]),'compare':([36,49,50,51,52,53,54,55,56,57,58,74,82,111,112,136,138,148,166,168,170,228,229,233,236,245,246,248,251,],[71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,189,71,71,71,71,71,71,71,71,71,71,71,]),'termino':([36,49,50,51,52,53,54,55,56,57,58,74,82,84,106,111,112,114,116,136,138,146,148,161,166,168,170,173,176,191,202,206,228,229,230,233,236,245,246,248,251,],[72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,212,72,72,72,72,72,72,72,72,72,72,72,72,]),'factor':([36,49,50,51,52,53,54,55,56,57,58,74,82,84,106,111,112,114,116,136,138,146,148,161,166,168,170,173,176,191,202,206,228,229,230,233,236,245,246,248,251,],[73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,]),'openpar':([36,49,50,51,52,53,54,55,56,57,58,74,82,84,106,111,112,114,116,136,138,146,148,161,166,168,170,173,176,191,202,206,228,229,230,233,236,245,246,248,251,],[74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,]),'factor2':([36,49,50,51,52,53,54,55,56,57,58,74,82,84,106,111,112,114,116,136,138,146,148,161,166,168,170,173,176,191,202,206,228,229,230,233,236,245,246,248,251,],[75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,]),'parameters1':([37,],[78,]),'vars3':([44,],[83,]),'vars4':([44,186,],[85,213,]),'estatutos1':([49,50,51,52,53,54,55,56,57,],[89,92,93,94,95,96,97,98,99,]),'compare1':([62,],[107,]),'factor1':([68,101,],[117,117,]),'expression1':([69,],[119,]),'and1':([70,],[121,]),'equal1':([71,],[123,]),'exp1':([72,],[125,]),'termino1':([73,],[127,]),'varcte':([75,],[130,]),'funciones6':([82,136,138,],[137,182,183,]),'vars5':([86,],[141,]),'compare2':([107,],[148,]),'lista_ids':([109,110,193,198,],[153,157,218,157,]),'escritura1':([110,198,],[156,220,]),'for1':([113,],[160,]),'funcion1':([116,206,],[164,226,]),'expression2':([119,],[166,]),'and2':([121,],[168,]),'equal2':([123,],[170,]),'exp2':([125,],[173,]),'termino2':([127,],[176,]),'closepar':([129,],[180,]),'lista_ids1':([154,155,227,],[192,195,231,]),'escritura2':([157,],[197,]),'funcion2':([165,],[205,]),'condicion1':([228,233,],[232,239,]),'while1':([229,236,],[235,243,]),'condicion2':([234,],[240,]),'condicion3':([245,248,],[247,253,]),'for2':([246,251,],[250,255,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> programa","S'",1,None,None,None),
  ('programa -> PROGRAM programa1 programa2 main OPENPAR CLOSEPAR OPENCURLY programa3 CLOSECURLY','programa',9,'p_programa','MyRlike.py',210),
  ('programa1 -> ID SEMICOLON vars','programa1',3,'p_programa1','MyRlike.py',216),
  ('programa1 -> ID SEMICOLON','programa1',2,'p_programa1','MyRlike.py',217),
  ('programa2 -> funciones','programa2',1,'p_programa2','MyRlike.py',226),
  ('programa2 -> epsilon','programa2',1,'p_programa2','MyRlike.py',227),
  ('programa3 -> estatutos','programa3',1,'p_programa3','MyRlike.py',233),
  ('programa3 -> epsilon','programa3',1,'p_programa3','MyRlike.py',234),
  ('main -> MAIN','main',1,'p_main','MyRlike.py',240),
  ('vars -> VARS vars1','vars',2,'p_vars','MyRlike.py',248),
  ('vars1 -> tipo COLON vars2','vars1',3,'p_vars1','MyRlike.py',257),
  ('vars2 -> ID vars3','vars2',2,'p_vars2','MyRlike.py',263),
  ('vars3 -> OPENBOX exp CLOSEBOX vars4','vars3',4,'p_vars3','MyRlike.py',271),
  ('vars3 -> vars4','vars3',1,'p_vars3','MyRlike.py',272),
  ('vars4 -> SEMICOLON vars5','vars4',2,'p_vars4','MyRlike.py',278),
  ('vars4 -> COMMA vars2','vars4',2,'p_vars4','MyRlike.py',279),
  ('vars5 -> vars1','vars5',1,'p_vars5','MyRlike.py',285),
  ('vars5 -> epsilon','vars5',1,'p_vars5','MyRlike.py',286),
  ('lista_ids -> ID OPENBOX exp CLOSEBOX lista_ids1','lista_ids',5,'p_lista_ids','MyRlike.py',294),
  ('lista_ids -> ID lista_ids1','lista_ids',2,'p_lista_ids','MyRlike.py',295),
  ('lista_ids -> STRING lista_ids1','lista_ids',2,'p_lista_ids','MyRlike.py',296),
  ('lista_ids1 -> COMMA lista_ids','lista_ids1',2,'p_lista_ids1','MyRlike.py',307),
  ('lista_ids1 -> epsilon','lista_ids1',1,'p_lista_ids1','MyRlike.py',308),
  ('tipo -> TYPEFLOAT','tipo',1,'p_tipo','MyRlike.py',314),
  ('tipo -> TYPEINT','tipo',1,'p_tipo','MyRlike.py',315),
  ('tipo -> TYPECHAR','tipo',1,'p_tipo','MyRlike.py',316),
  ('tipo_void -> TYPEVOID','tipo_void',1,'p_tipo_void','MyRlike.py',323),
  ('funciones -> FUNCTION funciones1','funciones',2,'p_funciones','MyRlike.py',330),
  ('funciones -> epsilon','funciones',1,'p_funciones','MyRlike.py',331),
  ('funciones1 -> tipo funciones2 funciones3','funciones1',3,'p_funciones1','MyRlike.py',337),
  ('funciones1 -> tipo_void funciones2 funciones3','funciones1',3,'p_funciones1','MyRlike.py',338),
  ('funciones2 -> ID OPENPAR','funciones2',2,'p_funciones2','MyRlike.py',344),
  ('funciones3 -> parameters funciones4','funciones3',2,'p_funciones3','MyRlike.py',351),
  ('funciones3 -> funciones4','funciones3',1,'p_funciones3','MyRlike.py',352),
  ('funciones4 -> CLOSEPAR funciones5','funciones4',2,'p_funciones4','MyRlike.py',358),
  ('funciones5 -> vars guardar_func OPENCURLY funciones6','funciones5',4,'p_funciones5','MyRlike.py',364),
  ('funciones5 -> guardar_func OPENCURLY funciones6','funciones5',3,'p_funciones5','MyRlike.py',365),
  ('funciones6 -> estatutos funciones6','funciones6',2,'p_funciones6','MyRlike.py',371),
  ('funciones6 -> CLOSECURLY funciones','funciones6',2,'p_funciones6','MyRlike.py',372),
  ('guardar_func -> epsilon','guardar_func',1,'p_guardar_func','MyRlike.py',378),
  ('parameters -> tipo ID parameters1','parameters',3,'p_parameters','MyRlike.py',387),
  ('parameters1 -> COMMA parameters','parameters1',2,'p_parameters1','MyRlike.py',394),
  ('parameters1 -> epsilon','parameters1',1,'p_parameters1','MyRlike.py',395),
  ('estatutos -> asignacion estatutos1','estatutos',2,'p_estatutos','MyRlike.py',401),
  ('estatutos -> llamada estatutos1','estatutos',2,'p_estatutos','MyRlike.py',402),
  ('estatutos -> retorno estatutos1','estatutos',2,'p_estatutos','MyRlike.py',403),
  ('estatutos -> lectura estatutos1','estatutos',2,'p_estatutos','MyRlike.py',404),
  ('estatutos -> escritura estatutos1','estatutos',2,'p_estatutos','MyRlike.py',405),
  ('estatutos -> condicion estatutos1','estatutos',2,'p_estatutos','MyRlike.py',406),
  ('estatutos -> while estatutos1','estatutos',2,'p_estatutos','MyRlike.py',407),
  ('estatutos -> for estatutos1','estatutos',2,'p_estatutos','MyRlike.py',408),
  ('estatutos -> est_exp estatutos1','estatutos',2,'p_estatutos','MyRlike.py',409),
  ('estatutos1 -> estatutos','estatutos1',1,'p_estatutos1','MyRlike.py',415),
  ('estatutos1 -> epsilon','estatutos1',1,'p_estatutos1','MyRlike.py',416),
  ('asignacion -> asignacion1 expresion SEMICOLON','asignacion',3,'p_asignacion','MyRlike.py',422),
  ('asignacion1 -> ID OPENBOX exp CLOSEBOX IS','asignacion1',5,'p_asignacion1','MyRlike.py',429),
  ('asignacion1 -> ID IS','asignacion1',2,'p_asignacion1','MyRlike.py',430),
  ('llamada -> funcion SEMICOLON','llamada',2,'p_llamada','MyRlike.py',440),
  ('funcion -> ID OPENPAR funcion1','funcion',3,'p_funcion','MyRlike.py',446),
  ('funcion1 -> exp funcion2','funcion1',2,'p_funcion1','MyRlike.py',452),
  ('funcion2 -> COMMA funcion1','funcion2',2,'p_funcion2','MyRlike.py',458),
  ('funcion2 -> CLOSEPAR','funcion2',1,'p_funcion2','MyRlike.py',459),
  ('retorno -> RETURN OPENPAR exp CLOSEPAR SEMICOLON','retorno',5,'p_retorno','MyRlike.py',465),
  ('lectura -> READ OPENPAR lista_ids CLOSEPAR SEMICOLON','lectura',5,'p_lectura','MyRlike.py',472),
  ('escritura -> WRITE OPENPAR escritura1 CLOSEPAR SEMICOLON','escritura',5,'p_escritura','MyRlike.py',479),
  ('escritura1 -> lista_ids escritura2','escritura1',2,'p_escritura1','MyRlike.py',486),
  ('escritura2 -> COMMA escritura1','escritura2',2,'p_escritura2','MyRlike.py',492),
  ('escritura2 -> epsilon','escritura2',1,'p_escritura2','MyRlike.py',493),
  ('condicion -> IF OPENPAR expresion CLOSEPAR THEN OPENCURLY condicion1','condicion',7,'p_condicion','MyRlike.py',499),
  ('condicion1 -> estatutos condicion1','condicion1',2,'p_condicion1','MyRlike.py',505),
  ('condicion1 -> CLOSECURLY condicion2','condicion1',2,'p_condicion1','MyRlike.py',506),
  ('condicion2 -> ELSE OPENCURLY condicion3','condicion2',3,'p_condicion2','MyRlike.py',512),
  ('condicion2 -> epsilon','condicion2',1,'p_condicion2','MyRlike.py',513),
  ('condicion3 -> estatutos condicion3','condicion3',2,'p_condicion3','MyRlike.py',519),
  ('condicion3 -> CLOSECURLY','condicion3',1,'p_condicion3','MyRlike.py',520),
  ('while -> WHILE OPENPAR expresion CLOSEPAR DO OPENCURLY while1','while',7,'p_while','MyRlike.py',526),
  ('while1 -> estatutos while1','while1',2,'p_while1','MyRlike.py',532),
  ('while1 -> CLOSECURLY','while1',1,'p_while1','MyRlike.py',533),
  ('for -> FOR ID for1 IS exp TO exp DO OPENCURLY for2 CLOSECURLY','for',11,'p_for','MyRlike.py',539),
  ('for1 -> OPENBOX exp CLOSEBOX','for1',3,'p_for1','MyRlike.py',545),
  ('for1 -> epsilon','for1',1,'p_for1','MyRlike.py',546),
  ('for2 -> estatutos for2','for2',2,'p_for2','MyRlike.py',552),
  ('for2 -> epsilon','for2',1,'p_for2','MyRlike.py',553),
  ('est_exp -> expresion SEMICOLON','est_exp',2,'p_est_exp','MyRlike.py',559),
  ('expresion -> and expression1','expresion',2,'p_expresion','MyRlike.py',565),
  ('expresion -> and expression1 expression2 expresion','expresion',4,'p_expresion','MyRlike.py',566),
  ('expression1 -> epsilon','expression1',1,'p_expression1','MyRlike.py',572),
  ('expression2 -> OR','expression2',1,'p_expression2','MyRlike.py',582),
  ('and -> equal and1','and',2,'p_and','MyRlike.py',589),
  ('and -> equal and1 and2 and','and',4,'p_and','MyRlike.py',590),
  ('and1 -> epsilon','and1',1,'p_and1','MyRlike.py',596),
  ('and2 -> AND','and2',1,'p_and2','MyRlike.py',606),
  ('equal -> compare equal1','equal',2,'p_equal','MyRlike.py',613),
  ('equal -> compare equal1 equal2 equal','equal',4,'p_equal','MyRlike.py',614),
  ('equal1 -> epsilon','equal1',1,'p_equal1','MyRlike.py',620),
  ('equal2 -> EQ','equal2',1,'p_equal2','MyRlike.py',630),
  ('equal2 -> NE','equal2',1,'p_equal2','MyRlike.py',631),
  ('compare -> exp compare1','compare',2,'p_compare','MyRlike.py',638),
  ('compare -> exp compare1 compare2 compare','compare',4,'p_compare','MyRlike.py',639),
  ('compare1 -> epsilon','compare1',1,'p_compare1','MyRlike.py',645),
  ('compare2 -> LT','compare2',1,'p_compare2','MyRlike.py',655),
  ('compare2 -> LE','compare2',1,'p_compare2','MyRlike.py',656),
  ('compare2 -> GT','compare2',1,'p_compare2','MyRlike.py',657),
  ('compare2 -> GE','compare2',1,'p_compare2','MyRlike.py',658),
  ('exp -> termino exp1','exp',2,'p_exp','MyRlike.py',665),
  ('exp -> termino exp1 exp2 exp','exp',4,'p_exp','MyRlike.py',666),
  ('exp1 -> epsilon','exp1',1,'p_exp1','MyRlike.py',672),
  ('exp2 -> PLUS','exp2',1,'p_exp2','MyRlike.py',682),
  ('exp2 -> MINUS','exp2',1,'p_exp2','MyRlike.py',683),
  ('termino -> factor termino1','termino',2,'p_termino','MyRlike.py',690),
  ('termino -> factor termino1 termino2 termino','termino',4,'p_termino','MyRlike.py',691),
  ('termino1 -> epsilon','termino1',1,'p_termino1','MyRlike.py',697),
  ('termino2 -> MULTIPLY','termino2',1,'p_termino2','MyRlike.py',707),
  ('termino2 -> DIVIDE','termino2',1,'p_termino2','MyRlike.py',708),
  ('termino2 -> MODULO','termino2',1,'p_termino2','MyRlike.py',709),
  ('factor -> ID factor1','factor',2,'p_factor','MyRlike.py',716),
  ('factor -> openpar expresion closepar','factor',3,'p_factor','MyRlike.py',717),
  ('factor -> funcion','factor',1,'p_factor','MyRlike.py',718),
  ('factor -> factor2 varcte','factor',2,'p_factor','MyRlike.py',719),
  ('openpar -> OPENPAR','openpar',1,'p_openpar','MyRlike.py',728),
  ('closepar -> CLOSEPAR','closepar',1,'p_closepar','MyRlike.py',735),
  ('factor1 -> OPENBOX exp CLOSEBOX','factor1',3,'p_factor1','MyRlike.py',742),
  ('factor1 -> epsilon','factor1',1,'p_factor1','MyRlike.py',743),
  ('factor2 -> PLUS','factor2',1,'p_factor2','MyRlike.py',749),
  ('factor2 -> MINUS','factor2',1,'p_factor2','MyRlike.py',750),
  ('factor2 -> epsilon','factor2',1,'p_factor2','MyRlike.py',751),
  ('varcte -> ID','varcte',1,'p_varcte','MyRlike.py',757),
  ('varcte -> INT','varcte',1,'p_varcte','MyRlike.py',758),
  ('varcte -> FLOAT','varcte',1,'p_varcte','MyRlike.py',759),
  ('varcte -> CHAR','varcte',1,'p_varcte','MyRlike.py',760),
  ('epsilon -> <empty>','epsilon',0,'p_epsilon','MyRlike.py',766),
]
