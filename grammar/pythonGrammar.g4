grammar pythonGrammar;

program: (func)+ EOF;

// project requirements
func : arithOperators   // deliverable #1
     | assOperators     // deliverable #1
     | blocks           // deliverable #2
     | conStatement     // deliverable #2
     | loops            // deliverable #3
     | comments         // deliverable #3
     ;

// Deliverable 1

// contines for each newline in file
arithOperators : arithExpression (NEWLINE)*; // EOF Removed EOF so antlr doesn't expect it after every expression

assOperators : assExpression (NEWLINE)*; // EOF ;


arithExpression : arithExpression ('+' | '-' | '*' | '/' | '%') arithExpression
                | '(' arithExpression ')'
                | value
                ;

assExpression : VAR assignOp arithExpression ;

assignOp : '=' | '+=' | '-=' | '*=' | '/=' ;

value : VAR | NUM | STRING | arrayExp;

// // This solves the array cases by looking for the brackets and values (including value: ...)
arrayExp : '[' (value (',' value)*)? ']';

// Deliverable 2              PLACEHOLDER
blocks : 'block' ;
conStatement : 'con' ;
// Deliverable 3              PLACEHOLDER
loops : 'loop' ;
comments : 'comment' ;

// variable naming
VAR : [a-zA-Z_][a-zA-Z_0-9]* ;
NUM : [0-9]+ ('.'[0-9]+)? ;

// does single and doubled quotes... originally had just ''
STRING : ('\'' [a-zA-Z0-9_]+ '\'' ) | ('"' [a-zA-Z0-9_]+ '"' ) ;

// newline handling
NEWLINE : ('\r'? '\n')+ ;
WHITESPACE : [ \t\r]+ -> skip; // I added /r here

// COMMENTPOUND : '#' ;