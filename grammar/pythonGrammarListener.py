# Generated from grammar/pythonGrammar.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .pythonGrammarParser import pythonGrammarParser
else:
    from pythonGrammarParser import pythonGrammarParser

# This class defines a complete listener for a parse tree produced by pythonGrammarParser.
class pythonGrammarListener(ParseTreeListener):

    # Enter a parse tree produced by pythonGrammarParser#program.
    def enterProgram(self, ctx:pythonGrammarParser.ProgramContext):
        pass

    # Exit a parse tree produced by pythonGrammarParser#program.
    def exitProgram(self, ctx:pythonGrammarParser.ProgramContext):
        pass


    # Enter a parse tree produced by pythonGrammarParser#func.
    def enterFunc(self, ctx:pythonGrammarParser.FuncContext):
        pass

    # Exit a parse tree produced by pythonGrammarParser#func.
    def exitFunc(self, ctx:pythonGrammarParser.FuncContext):
        pass


    # Enter a parse tree produced by pythonGrammarParser#arithOperators.
    def enterArithOperators(self, ctx:pythonGrammarParser.ArithOperatorsContext):
        pass

    # Exit a parse tree produced by pythonGrammarParser#arithOperators.
    def exitArithOperators(self, ctx:pythonGrammarParser.ArithOperatorsContext):
        pass


    # Enter a parse tree produced by pythonGrammarParser#assOperators.
    def enterAssOperators(self, ctx:pythonGrammarParser.AssOperatorsContext):
        pass

    # Exit a parse tree produced by pythonGrammarParser#assOperators.
    def exitAssOperators(self, ctx:pythonGrammarParser.AssOperatorsContext):
        pass


    # Enter a parse tree produced by pythonGrammarParser#arithExpression.
    def enterArithExpression(self, ctx:pythonGrammarParser.ArithExpressionContext):
        pass

    # Exit a parse tree produced by pythonGrammarParser#arithExpression.
    def exitArithExpression(self, ctx:pythonGrammarParser.ArithExpressionContext):
        pass


    # Enter a parse tree produced by pythonGrammarParser#value.
    def enterValue(self, ctx:pythonGrammarParser.ValueContext):
        pass

    # Exit a parse tree produced by pythonGrammarParser#value.
    def exitValue(self, ctx:pythonGrammarParser.ValueContext):
        pass


    # Enter a parse tree produced by pythonGrammarParser#blocks.
    def enterBlocks(self, ctx:pythonGrammarParser.BlocksContext):
        pass

    # Exit a parse tree produced by pythonGrammarParser#blocks.
    def exitBlocks(self, ctx:pythonGrammarParser.BlocksContext):
        pass


    # Enter a parse tree produced by pythonGrammarParser#conStatement.
    def enterConStatement(self, ctx:pythonGrammarParser.ConStatementContext):
        pass

    # Exit a parse tree produced by pythonGrammarParser#conStatement.
    def exitConStatement(self, ctx:pythonGrammarParser.ConStatementContext):
        pass


    # Enter a parse tree produced by pythonGrammarParser#loops.
    def enterLoops(self, ctx:pythonGrammarParser.LoopsContext):
        pass

    # Exit a parse tree produced by pythonGrammarParser#loops.
    def exitLoops(self, ctx:pythonGrammarParser.LoopsContext):
        pass


    # Enter a parse tree produced by pythonGrammarParser#comments.
    def enterComments(self, ctx:pythonGrammarParser.CommentsContext):
        pass

    # Exit a parse tree produced by pythonGrammarParser#comments.
    def exitComments(self, ctx:pythonGrammarParser.CommentsContext):
        pass



del pythonGrammarParser