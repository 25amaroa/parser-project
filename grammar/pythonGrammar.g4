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


// lowest
arithExpression : arith (('+' | '-' ) arith)*
                ;
// 2nd highest                 
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
     | rangeFunc
     | TRUE
     | FALSE
     | NONE
     ;

// I added in this to handle range calls in the for loops
// I'm assuming we only need to handle the two cases shown in the assignment 
rangeFunc : RANGE '(' arithExpression ',' arithExpression ')'    // range (start, end)
          | RANGE '(' arithExpression ')'                        // range (end)
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
     : FOR VAR IN arithExpression ':' NEWLINE block
     ;

block
     : (simpleStmt | compoundStmt)+
     ;
/*********************** Deliverable 3 ***********************/
loops : LOOP ;
// I think this is needed 
//comments : COMMENT ;

// The point of these tests are now to create lexing rules for our parser
// the order here matters when lexing so i've laid out the different sections we need

// keywords
IF    : 'if';
ELIF  : 'elif';
ELSE  : 'else';
LOOP  : 'loop';
// COMMENT : 'comment';
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
// skip I think matches, unless he wants this apart of the tree which I don't think makes sense
// if you use skip we can remove the above calls for comment since skip just handles it by ignoring
// I was wondering why this wasn't working but looking at your link this method was used in ATLR3? -> warning(131): pythonGrammar.g4:130:64: greedy block ()* contains wildcard; the non-greedy syntax ()*? may be preferred
SINGLE_LINE_COMMENT : '#' ~[\r\n]* -> skip;
MULTIPLE_LINE_COMMENT : '\'\'\'' .*? '\'\'\'' -> skip;

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