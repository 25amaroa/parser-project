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
arithOperators : arithExpression (NEWLINE)* EOF ;

assOperators : assExpression (NEWLINE)* EOF ;


arithExpression : arithExpression ('+' | '-' | '*' | '/' | '%') arithExpression
                | '(' arithExpression ')'
                | value
                ;

assExpression : VAR assignOp arithExpression ;

assignOp : '=' | '+=' | '-=' | '*=' | '/=' ;

value : VAR | NUM ;


// Deliverable 2
blocks : 'block' ;
conStatement : 'con' ;
// Deliverable 3
loops : 'loop' ;
comments : 'comment' ;

// variable naming
VAR : [a-zA-Z_][a-zA-Z_0-9]* ;
NUM : [0-9]+ ('.'[0-9]+)? ;


// newline handling
NEWLINE : ('\r'? '\n')+ ;
WHITESPACE : [\t]+ -> skip ;


// COMMENTPOUND : '#' ;