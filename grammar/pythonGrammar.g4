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
boolOp : AND | OR ;  // Can't include 'not' here becuase it's unary i.e. "not x"

conExpression 
     : conExpression boolOp conExpression
     | conExpression compOp conExpression
     | NOT conExpression
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
     : IF conExpression ':' NEWLINE block (elifStatement)* (elseStatement)? 
     ;              

elifStatement
     : ELIF conExpression ':' NEWLINE block
     ;

elseStatement
     : ELSE ':' NEWLINE block
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

// comment types - reference https://stackoverflow.com/questions/4676827/how-can-i-access-blocks-of-text-as-an-attribute-that-are-matched-using-a-greedy
SINGLE_LINE_COMMENT : '#' ~[\r\n]* -> skip;
MULTIPLE_LINE_COMMENT : '\'\'\'' ( options {greedy=false;} : . )* '\'\'\'' -> skip;

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