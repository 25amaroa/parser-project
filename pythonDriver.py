from platform import node
import sys
import os
from antlr4 import *
from grammar.pythonGrammarLexer import pythonGrammarLexer
from grammar.pythonGrammarParser import pythonGrammarParser
from antlr4 import ParserRuleContext


def printTree(node, parser, level=0):
        indent = "  " * level
        name = parser.ruleNames[node.getRuleIndex()]
        result = f"{indent}{name}\n"

        
        for i in range(node.getChildCount()):
                child = node.getChild(i)

                if isinstance(child, ParserRuleContext):
                        result += printTree(child, parser, level + 1)
                else:
                        result += f"{indent}  {child.getText()}\n"

        return result


file = "tests/project_deliverable_2.py"
with open(file, "r") as f:
        code = f.read()



input = InputStream(code)
lexer = pythonGrammarLexer(input)
stream = CommonTokenStream(lexer)
parser = pythonGrammarParser(stream)


tree = parser.program() 


print("\nSlightly more easy to read:\n")
print(printTree(tree, parser))

print("\nRaw Tree version:\n")
print(tree.toStringTree(recog=parser), "\n")
