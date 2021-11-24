# Grammar
PROGRAMA → Program PROGRAMA1 PROGRAMA2 main() { PROGRAMA3 }  
PROGRAMA1 → id ; VARS | id ;  
PROGRAMA2 → FUNCIONES | ε  
PROGRAMA3 → ESTATUTOS | ε  
VARS → ‘VARS’ VARS1  
VARS1 → TIPO : VARS2  
VARS2 → id VARS3  
VARS3 → [ cte-l ] VARS4 | VARS4  
VARS4 → ; VARS5 | COMMA VARS2  
VARS5 → VARS1 | ε  
LISTA_IDS → id [ EXP ] LISTA_IDS1 | id LISTA_IDS2  
LISTA_IDS1 → COMMA LISTA_IDS | ε  
TIPO → int | float | char  
FUNCIONES → function FUNCIONES1 | ε  
FUNCIONES1 → TIPO FUNCIONES2 FUNCIONES3 | void FUNCIONES2 FUNCIONES3  
FUNCIONES2 → id (  
FUNCIONES3 → PARAMETERS FUNCIONES4 | FUNCIONES4  
FUNCIONES4 → ) FUNCIONES5  
FUNCIONES5 → VARS { FUNCIONES6 | { FUNCIONES6  
FUNCIONES6 → ESTATUTOS FUNCIONES6 | } FUNCIONES  
PARAMETROS → TIPO id PARAMETERS1  
PARAMETROS1 → , PARAMETERS | ε  
ESTATUTOS → ASIGNACION ; ESTATUTOS1 | LLAMADA ; ESTATUTOS1 | RETORNO ; ESTATUTOS1 | LECTURA ; ESTATUTOS1 | ESCRITURA ; ESTATUTOS1 | CONDICION  ESTATUTOS1 | WHILE ESTATUTOS1 | FOR ESTATUTOS1 | EXPRESION ; ESTATUTOS1  
ESTATUTOS1 → ESTATUTOS | ε  
ASIGNACION → ASIGNACION1 EXPRESION ;  
ASIGNACION1 → id [ EXP ] = | id =  
LLAMADA → FUNCION ;  
FUNCION → id ( FUNCION1  
FUNCION1 → EXP FUNCION2 | )  
FUNCION2 → , FUNCION1 | )  
RETORNO → return ( EXP )  
LECTURA → read ( LISTA_IDS )  
ESCRITURA → write ( ESCRITURA1 )  
ESCRITURA1 → cte.string ESCRITURA2 | EXPRESION ESCRITURA2  
ESCRITURA2 → , ESCRITURA1 | ε  
CONDICION → if ( EXPRESION ) then { ESTATUTOS } CONDICION1   
CONDICION1 → else { ESTATUTOS } | ε  
WHILE → while ( EXPRESION ) do { ESTATUTOS }  
FOR → for id FOR1 = EXP to EXP do { ESTATUTOS }  
FOR1 → id [ EXP ] | id  
EST_EXP → EXPRESION ;  
EXPRESION → AND | AND EXPRESION1 EXPRESION  
EXPRESION1 → ||  
AND → EQUAL | EQUAL AND1 AND  
AND1 → '&&'  
EQUAL → COMPARE | COMPARE EQUAL1 EQUAL  
EQUAL1 → == | !=  
COMPARE → EXP | EXP COMPARE1 COMPARE  
COMPARE1 → < | <= | > | >=  
EXP → TERMINO | TERMINO EXP1 EXP  
EXP1 → + | -  
TERMINO → FACTOR | FACTOR TERMINO1 TERMINO  
TERMINO1 → * | / | %  
FACTOR → FACTOR1 | ( EXPRESION ) | FUNCION | FACTOR2 cte  
FACTOR1 → id [ EXP ] | id  
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
