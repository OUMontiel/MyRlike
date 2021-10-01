# Grammar
PROGRAMA → Program id ; PROGRAMA1 PROGRAMA2 main() { PROGRAMA3 }  
PROGRAMA1 → VARS | ε  
PROGRAMA2 → FUNCIONES | ε  
PROGRAMA3 → ESTATUTOS | ε  
VARS → ‘VARS’ VARS1  
VARS1 → TIPO : LISTA_IDS VARS2  
VARS2 → VARS1 | ε  
LISTA_IDS → id LISTA_IDS1  
LISTA_IDS1 → LISTA_IDS2 | [ EXP ] LISTA_IDS2  
LISTA_IDS2 → COMMA LISTA_IDS | ε  
TIPO → int | float | char  
FUNCIONES → function FUNCIONES1 | ε  
FUNCIONES1 → TIPO FUNCIONES2 | void FUNCIONES2  
FUNCIONES2 → id ( FUNCIONES3  
FUNCIONES3 → FUNCIONES4 | FUNCIONES6  
FUNCIONES4 → TIPO id FUNCIONES5  
FUNCIONES5 → , funciones4 | FUNCIONES6  
FUNCIONES6 → ) FUNCIONES7  
FUNCIONES7 → VARS { FUNCIONES8 | { FUNCIONES8  
FUNCIONES8 → ESTATUTOS FUNCIONES8 | } FUNCIONES  
ESTATUTOS → ASIGNACION ESTATUTOS1 | LLAMADA ESTATUTOS1 | RETORNO ESTATUTOS1 | LECTURA ESTATUTOS1 | ESCRITURA ESTATUTOS1 | CONDICION  ESTATUTOS1 | WHILE ESTATUTOS1 | FOR ESTATUTOS1 | EXPRESION ESTATUTOS1  
ESTATUTOS1 → ESTATUTOS | ε  
ASIGNACION → id ASIGNACION1 = EXPRESION ;  
ASIGNACION1 → [ EXP ] | ε  
LLAMADA → FUNCION ;  
FUNCION → id ( FUNCION1  
FUNCION1 → EXP FUNCION2  
FUNCION2 → , FUNCION1 | )  
RETORNO → return ( EXP ) ;  
LECTURA → read ( LISTA_IDS ) ;  
ESCRITURA → write ( ESCRITURA1 ) ;  
ESCRITURA1 → cte.string ESCRITURA2 | LISTA_IDS ESCRITURA2  
ESCRITURA2 → , ESCRITURA1 | ε  
CONDICION → if ( EXPRESION ) then { CONDICION1  
CONDICION1 → ESTATUTOS CONDICION1 | } CONDICION2  
CONDICION2 → else { CONDICION3 | ε  
CONDICION3 → ESTATUTOS CONDICION3 | }  
WHILE → while ( EXPRESION ) do { WHILE1  
WHILE1 → ESTATUTOS WHILE1 | }  
FOR → for id FOR1 = EXP to EXP do { FOR2 }  
FOR1 → [ EXP ] | ε  
FOR2 → ESTATUTOS FOR2 | ε  
EXPRESION → OR  
OR → AND OR1  
OR1 → ‘|’ OR | ε  
AND → EQUAL AND1  
BITAND1 → & AND | ε  
EQUAL → COMPARE EQUAL1  
EQUAL1 → == EQUAL | != EQUAL | ε  
COMPARE → EXP COMPARE1  
COMPARE1 → < COMPARE | <= COMPARE | > COMPARE | >= COMPARE  
EXP → TERMINO EXP1  
EXP1 → + EXP | - EXP | ε  
TERMINO → FACTOR TERMINO1  
TERMINO1 → * TERMINO | / TERMINO | % TERMINO | ε  
FACTOR → id FACTOR1 | ( EXPRESION ) | FUNCION | FACTOR2 cte  
FACTOR1 → [ EXP ] | ε  
FACTOR2 → + | - | ε  
VARCTE → id | cte-l | cte-f | cte-c  


---
# RegEx
| Token | RegEx |
| --- | --- |
| id | `[a-zA-Z_][a-zA-Z_0-9]*` |
| int | `\d+` |
| float | `\d+\.\d+` |
| char | `\'([^\\\']\|(\\\')\|(\\\\))?\'` |
| strings | `\"([^\\\"]\|(\\\")\|(\\\\))*\"` |
| constants | `{‘program’, ‘main()’, ‘VARS’, ‘function’, ‘return’, ‘read’, ‘write’, ‘if’, ‘then’, ‘else’, ‘while’, ‘do’, ‘for’, ‘to’, ‘int’, ‘float’, ‘char’, ‘void’, ‘;’, ‘:’, ‘,’, ‘{‘, ‘}’, ‘[‘, ‘]’, ‘(‘, ‘)’, ‘=’, ‘\|\|’, ‘&&’, ‘==’, ‘!=’, ‘<’, ‘<=’, ‘>’, ‘>=’, ‘*’, ‘/’, ‘%’, ‘+’, ‘-’}` |