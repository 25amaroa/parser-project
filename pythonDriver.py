# src/test_parser.py
import sys
import os
from antlr4 import *
from grammar.pythonGrammarLexer import pythonGrammarLexer
from grammar.pythonGrammarParser import pythonGrammarParser




# will add more tomorrow to visualize the tree 

file = "tests/project_deliverable_1.py"
with open(file, "r") as f:
        code = f.read()



input = InputStream(code)
lexer = pythonGrammarLexer(input)
stream = CommonTokenStream(lexer)
parser = pythonGrammarParser(stream)

tree = parser.assOperators()  # or parser.program()
print(tree.toStringTree(recog=parser))
