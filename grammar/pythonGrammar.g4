grammar pythonGrammar;

// change "+" to "*" later 
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

assOperators : 'opp' ;


arithExpression : arithExpression ('+' | '-' | '*' | '/' | '%') arithExpression
                | '(' arithExpression ')'
                | value
                ;

value : VAR | NUM ;


// later problem
blocks : 'block' ;
conStatement : 'con' ;
// needs to support nested structures
loops : 'loop' ;
comments : 'comment' ;


// variable naming
VAR : [a-zA-Z_][a-zA-Z_0-9]* ;
NUM : [0-9]+ ('.'[0-9]+)? ;


// newline handling
NEWLINE : ('\r'? '\n')+ ;
WHITESPACE : [\t]+ -> skip ;