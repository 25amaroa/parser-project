# Generated from grammar/pythonGrammar.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,6,44,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,6,
        2,7,7,7,1,0,4,0,18,8,0,11,0,12,0,19,1,0,1,0,1,1,1,1,1,1,1,1,1,1,
        1,1,3,1,30,8,1,1,2,1,2,1,3,1,3,1,4,1,4,1,5,1,5,1,6,1,6,1,7,1,7,1,
        7,0,0,8,0,2,4,6,8,10,12,14,0,0,41,0,17,1,0,0,0,2,29,1,0,0,0,4,31,
        1,0,0,0,6,33,1,0,0,0,8,35,1,0,0,0,10,37,1,0,0,0,12,39,1,0,0,0,14,
        41,1,0,0,0,16,18,3,2,1,0,17,16,1,0,0,0,18,19,1,0,0,0,19,17,1,0,0,
        0,19,20,1,0,0,0,20,21,1,0,0,0,21,22,5,0,0,1,22,1,1,0,0,0,23,30,3,
        4,2,0,24,30,3,6,3,0,25,30,3,8,4,0,26,30,3,10,5,0,27,30,3,12,6,0,
        28,30,3,14,7,0,29,23,1,0,0,0,29,24,1,0,0,0,29,25,1,0,0,0,29,26,1,
        0,0,0,29,27,1,0,0,0,29,28,1,0,0,0,30,3,1,0,0,0,31,32,5,1,0,0,32,
        5,1,0,0,0,33,34,5,2,0,0,34,7,1,0,0,0,35,36,5,3,0,0,36,9,1,0,0,0,
        37,38,5,4,0,0,38,11,1,0,0,0,39,40,5,5,0,0,40,13,1,0,0,0,41,42,5,
        6,0,0,42,15,1,0,0,0,2,19,29
    ]

class pythonGrammarParser ( Parser ):

    grammarFileName = "pythonGrammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'arith'", "'opp'", "'block'", "'con'", 
                     "'loop'", "'comment'" ]

    symbolicNames = [  ]

    RULE_program = 0
    RULE_func = 1
    RULE_arithOperators = 2
    RULE_assOperators = 3
    RULE_blocks = 4
    RULE_conStatement = 5
    RULE_loops = 6
    RULE_comments = 7

    ruleNames =  [ "program", "func", "arithOperators", "assOperators", 
                   "blocks", "conStatement", "loops", "comments" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(pythonGrammarParser.EOF, 0)

        def func(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pythonGrammarParser.FuncContext)
            else:
                return self.getTypedRuleContext(pythonGrammarParser.FuncContext,i)


        def getRuleIndex(self):
            return pythonGrammarParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = pythonGrammarParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 17 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 16
                self.func()
                self.state = 19 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 126) != 0)):
                    break

            self.state = 21
            self.match(pythonGrammarParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arithOperators(self):
            return self.getTypedRuleContext(pythonGrammarParser.ArithOperatorsContext,0)


        def assOperators(self):
            return self.getTypedRuleContext(pythonGrammarParser.AssOperatorsContext,0)


        def blocks(self):
            return self.getTypedRuleContext(pythonGrammarParser.BlocksContext,0)


        def conStatement(self):
            return self.getTypedRuleContext(pythonGrammarParser.ConStatementContext,0)


        def loops(self):
            return self.getTypedRuleContext(pythonGrammarParser.LoopsContext,0)


        def comments(self):
            return self.getTypedRuleContext(pythonGrammarParser.CommentsContext,0)


        def getRuleIndex(self):
            return pythonGrammarParser.RULE_func

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunc" ):
                listener.enterFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunc" ):
                listener.exitFunc(self)




    def func(self):

        localctx = pythonGrammarParser.FuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_func)
        try:
            self.state = 29
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 23
                self.arithOperators()
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 24
                self.assOperators()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 3)
                self.state = 25
                self.blocks()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 4)
                self.state = 26
                self.conStatement()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 5)
                self.state = 27
                self.loops()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 6)
                self.state = 28
                self.comments()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArithOperatorsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return pythonGrammarParser.RULE_arithOperators

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArithOperators" ):
                listener.enterArithOperators(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArithOperators" ):
                listener.exitArithOperators(self)




    def arithOperators(self):

        localctx = pythonGrammarParser.ArithOperatorsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_arithOperators)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31
            self.match(pythonGrammarParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssOperatorsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return pythonGrammarParser.RULE_assOperators

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssOperators" ):
                listener.enterAssOperators(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssOperators" ):
                listener.exitAssOperators(self)




    def assOperators(self):

        localctx = pythonGrammarParser.AssOperatorsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_assOperators)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 33
            self.match(pythonGrammarParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlocksContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return pythonGrammarParser.RULE_blocks

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlocks" ):
                listener.enterBlocks(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlocks" ):
                listener.exitBlocks(self)




    def blocks(self):

        localctx = pythonGrammarParser.BlocksContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_blocks)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            self.match(pythonGrammarParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return pythonGrammarParser.RULE_conStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConStatement" ):
                listener.enterConStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConStatement" ):
                listener.exitConStatement(self)




    def conStatement(self):

        localctx = pythonGrammarParser.ConStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_conStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self.match(pythonGrammarParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LoopsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return pythonGrammarParser.RULE_loops

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLoops" ):
                listener.enterLoops(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLoops" ):
                listener.exitLoops(self)




    def loops(self):

        localctx = pythonGrammarParser.LoopsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_loops)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self.match(pythonGrammarParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CommentsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return pythonGrammarParser.RULE_comments

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComments" ):
                listener.enterComments(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComments" ):
                listener.exitComments(self)




    def comments(self):

        localctx = pythonGrammarParser.CommentsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_comments)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            self.match(pythonGrammarParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





