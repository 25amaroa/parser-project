import sys
import os
from antlr4 import *
from grammar.pythonGrammarLexer import pythonGrammarLexer
from grammar.pythonGrammarParser import pythonGrammarParser
from antlr4 import ParserRuleContext
from antlr4.tree.Tree import TerminalNode
from graphviz import Digraph

# Function to print the parse tree in a more readable format using indentation
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

def drawTree(graph, root, parser):
    stack = [(root, None)]   # (node, parentID)

    while stack:
        node, parentID = stack.pop()
        nodeID = str(id(node))

        # Create node label
        if isinstance(node, TerminalNode):
            label = f"'{node.getText()}'"
        else:
            ruleName = parser.ruleNames[node.getRuleIndex()]
            label = ruleName

        graph.node(nodeID, label=label)

        # Connect to parentID
        if parentID:
            graph.edge(parentID, nodeID)

        # you have to go in reverse to keep left to right 
        for i in reversed(range(node.getChildCount())):
            child = node.getChild(i)
            stack.append((child, nodeID))



file = "tests/project_deliverable_3.py"
with open(file, "r") as f:
        code = f.read()


input = InputStream(code)
lexer = pythonGrammarLexer(input)
stream = CommonTokenStream(lexer)
parser = pythonGrammarParser(stream)


tree = parser.program() 


# print("\nSlightly more easy to read:\n")
# print(printTree(tree, parser))

print("\n Raw Tree version:\n")
print(tree.toStringTree(recog=parser), "\n")


graph = Digraph(format='jpg')
drawTree(graph, tree, parser)
graph.render("tree")