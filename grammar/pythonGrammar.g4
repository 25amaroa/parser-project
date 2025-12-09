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
     | TRUE
     | FALSE
     | NONE
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
     | whileStatement
     | forStatement
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

whileStatement
     : WHILE conExpression ':' NEWLINE block
     ;

forStatement
     : FOR VAR IN VAR ':' NEWLINE block
     ;

block
     : (simpleStmt)+
     ;
/*********************** Deliverable 3 ***********************/
loops : LOOP ;
comments : COMMENT_KW ;

// The point of these tests are now to create lexing rules for our parser
// the order here matters when lexing so i've laid out the different sections we need

// keywords
IF    : 'if';
ELIF  : 'elif';
ELSE  : 'else';
LOOP  : 'loop';
COMMENT_KW : 'comment';
TRUE  : 'True';
FALSE : 'False';
AND   : 'and';
OR    : 'or';
NOT   : 'not';
NONE  : 'None';
WHILE : 'while'; 
FOR   : 'for';   
IN    : 'in';    
RANGE : 'range'; 

// comment types
SINGLE_LINE_COMMENT : '#' ~[\r\n]* -> skip;
MULTI_LINE_COMMENT : '\'\'\'' ( options {greedy=false;} : . )* '\'\'\'' -> skip;

// variable naming
VAR : [a-zA-Z_][a-zA-Z_0-9]* ;
NUM : [0-9]+ ('.'[0-9]+)? ;

// strings
STRING 
     : '"' ( ~["\r\n] )* '"'     
     | '\'' ( ~['\r\n] )* '\''   
     ;

// whitespace handling
NEWLINE : ('\r'? '\n')+ ;
WHITESPACE : [ \t\r]+ -> skip;