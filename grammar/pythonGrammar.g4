grammar pythonGrammar;

program: (stmt)+ EOF;

// project requirements
stmt : simpleStmt
     | compoundStmt
     ;

/*********************** Deliverable 1 ***********************/

// contines for each newline in file
arithOperators : arithExpression (NEWLINE)*; // EOF Removed EOF so antlr doesn't expect it after every expression

assOperators : assExpression (NEWLINE)*; // EOF ;

arithExpression : arith (('+' | '-' ) arith)*
                ;
arith
     : factor (('*' | '/' | '%') factor)*
     ;

// () will be highest presendence
factor 
     : '(' arithExpression ')'
     | value
     ;

assExpression : VAR assignOp arithExpression ;

assignOp : '=' | '+=' | '-=' | '*=' | '/=' ;

value 
     : VAR 
     | NUM 
     | '-' NUM 
     | STRING 
     | arrayExp
     ;

// This solves the array cases by looking for the brackets and values (including value: ...)
arrayExp : '[' (value (',' value)*)? ']';

/*********************** Deliverable 2 ***********************/
compOp : '==' | '!=' | '<' | '<=' | '>' | '>=' ;
boolOp : 'and' | 'or' ;  // Can't include 'not' here becuase it's unary i.e. "not x"

conExpression 
     : conExpression boolOp conExpression
     | conExpression compOp conExpression
     | 'not' conExpression
     | '(' conExpression ')'           
     | value
     ;

compoundStmt
     : ifStatement
     | loops // Assuming 'loops' also contains a block allows us to nest (what we lost points for)
     ;

simpleStmt
     : arithOperators 
     | assOperators
     | compOp 
     | boolOp 
     | comments
     ;

     //if / elif/ else
ifStatement
     : 'if' conExpression ':' NEWLINE block (elifStatement)* (elseStatement)? 
     ;              

elifStatement
     : 'elif' conExpression ':' NEWLINE block
     ;

elseStatement
     : 'else' ':' NEWLINE block
     ;

block
     : (simpleStmt)+
     ;
/*********************** Deliverable 3 ***********************/
loops : 'loop' ;
comments : 'comment' ;

// variable naming
VAR : [a-zA-Z_][a-zA-Z_0-9]* ;
NUM : [0-9]+ ('.'[0-9]+)? ;

// does single and doubled quotes... originally had just ''
STRING 
     : '\'' (~['\n])* '\''  
     | '"' (~['\n])* '"'  
     ;

// newline handling
NEWLINE : ('\r'? '\n')+ ;
WHITESPACE : [ \t\r]+ -> skip; // I added /r here

// COMMENTPOUND : '#' ;