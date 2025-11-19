import sys
import os
from antlr4 import *
from grammar.pythonGrammarLexer import pythonGrammarLexer
from grammar.pythonGrammarParser import pythonGrammarParser



file = "tests/project_deliverable_2.py"
with open(file, "r") as f:
        code = f.read()



input = InputStream(code)
lexer = pythonGrammarLexer(input)
stream = CommonTokenStream(lexer)
parser = pythonGrammarParser(stream)

tree = parser.program() 
print("Raw Tree:\n\n",tree.toStringTree(recog=parser),"\n\n")
