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


arithOperators : 'arith' ;
assOperators : 'opp' ;


// later problem
blocks : 'block' ;
conStatement : 'con' ;
// needs to support nested structures
loops : 'loop' ;
comments : 'comment' ;