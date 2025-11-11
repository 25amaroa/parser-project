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
        4,1,20,90,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,1,0,4,0,26,8,0,11,
        0,12,0,27,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,3,1,38,8,1,1,2,1,2,5,2,
        42,8,2,10,2,12,2,45,9,2,1,2,1,2,1,3,1,3,5,3,51,8,3,10,3,12,3,54,
        9,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,3,4,64,8,4,1,4,1,4,1,4,5,4,69,
        8,4,10,4,12,4,72,9,4,1,5,1,5,1,5,1,5,1,6,1,6,1,7,1,7,1,8,1,8,1,9,
        1,9,1,10,1,10,1,11,1,11,1,11,0,1,8,12,0,2,4,6,8,10,12,14,16,18,20,
        22,0,3,1,0,1,5,1,0,8,12,1,0,17,18,87,0,25,1,0,0,0,2,37,1,0,0,0,4,
        39,1,0,0,0,6,48,1,0,0,0,8,63,1,0,0,0,10,73,1,0,0,0,12,77,1,0,0,0,
        14,79,1,0,0,0,16,81,1,0,0,0,18,83,1,0,0,0,20,85,1,0,0,0,22,87,1,
        0,0,0,24,26,3,2,1,0,25,24,1,0,0,0,26,27,1,0,0,0,27,25,1,0,0,0,27,
        28,1,0,0,0,28,29,1,0,0,0,29,30,5,0,0,1,30,1,1,0,0,0,31,38,3,4,2,
        0,32,38,3,6,3,0,33,38,3,16,8,0,34,38,3,18,9,0,35,38,3,20,10,0,36,
        38,3,22,11,0,37,31,1,0,0,0,37,32,1,0,0,0,37,33,1,0,0,0,37,34,1,0,
        0,0,37,35,1,0,0,0,37,36,1,0,0,0,38,3,1,0,0,0,39,43,3,8,4,0,40,42,
        5,19,0,0,41,40,1,0,0,0,42,45,1,0,0,0,43,41,1,0,0,0,43,44,1,0,0,0,
        44,46,1,0,0,0,45,43,1,0,0,0,46,47,5,0,0,1,47,5,1,0,0,0,48,52,3,10,
        5,0,49,51,5,19,0,0,50,49,1,0,0,0,51,54,1,0,0,0,52,50,1,0,0,0,52,
        53,1,0,0,0,53,55,1,0,0,0,54,52,1,0,0,0,55,56,5,0,0,1,56,7,1,0,0,
        0,57,58,6,4,-1,0,58,59,5,6,0,0,59,60,3,8,4,0,60,61,5,7,0,0,61,64,
        1,0,0,0,62,64,3,14,7,0,63,57,1,0,0,0,63,62,1,0,0,0,64,70,1,0,0,0,
        65,66,10,3,0,0,66,67,7,0,0,0,67,69,3,8,4,4,68,65,1,0,0,0,69,72,1,
        0,0,0,70,68,1,0,0,0,70,71,1,0,0,0,71,9,1,0,0,0,72,70,1,0,0,0,73,
        74,5,17,0,0,74,75,3,12,6,0,75,76,3,8,4,0,76,11,1,0,0,0,77,78,7,1,
        0,0,78,13,1,0,0,0,79,80,7,2,0,0,80,15,1,0,0,0,81,82,5,13,0,0,82,
        17,1,0,0,0,83,84,5,14,0,0,84,19,1,0,0,0,85,86,5,15,0,0,86,21,1,0,
        0,0,87,88,5,16,0,0,88,23,1,0,0,0,6,27,37,43,52,63,70
    ]

class pythonGrammarParser ( Parser ):

    grammarFileName = "pythonGrammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'+'", "'-'", "'*'", "'/'", "'%'", "'('", 
                     "')'", "'='", "'+='", "'-='", "'*='", "'/='", "'block'", 
                     "'con'", "'loop'", "'comment'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "VAR", "NUM", "NEWLINE", "WHITESPACE" ]

    RULE_program = 0
    RULE_func = 1
    RULE_arithOperators = 2
    RULE_assOperators = 3
    RULE_arithExpression = 4
    RULE_assExpression = 5
    RULE_assignOp = 6
    RULE_value = 7
    RULE_blocks = 8
    RULE_conStatement = 9
    RULE_loops = 10
    RULE_comments = 11

    ruleNames =  [ "program", "func", "arithOperators", "assOperators", 
                   "arithExpression", "assExpression", "assignOp", "value", 
                   "blocks", "conStatement", "loops", "comments" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    VAR=17
    NUM=18
    NEWLINE=19
    WHITESPACE=20

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
            self.state = 25 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 24
                self.func()
                self.state = 27 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 516160) != 0)):
                    break

            self.state = 29
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
            self.state = 37
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 31
                self.arithOperators()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 32
                self.assOperators()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 33
                self.blocks()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 34
                self.conStatement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 35
                self.loops()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 36
                self.comments()
                pass


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

        def arithExpression(self):
            return self.getTypedRuleContext(pythonGrammarParser.ArithExpressionContext,0)


        def EOF(self):
            return self.getToken(pythonGrammarParser.EOF, 0)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(pythonGrammarParser.NEWLINE)
            else:
                return self.getToken(pythonGrammarParser.NEWLINE, i)

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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self.arithExpression(0)
            self.state = 43
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==19:
                self.state = 40
                self.match(pythonGrammarParser.NEWLINE)
                self.state = 45
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 46
            self.match(pythonGrammarParser.EOF)
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

        def assExpression(self):
            return self.getTypedRuleContext(pythonGrammarParser.AssExpressionContext,0)


        def EOF(self):
            return self.getToken(pythonGrammarParser.EOF, 0)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(pythonGrammarParser.NEWLINE)
            else:
                return self.getToken(pythonGrammarParser.NEWLINE, i)

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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            self.assExpression()
            self.state = 52
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==19:
                self.state = 49
                self.match(pythonGrammarParser.NEWLINE)
                self.state = 54
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 55
            self.match(pythonGrammarParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArithExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arithExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pythonGrammarParser.ArithExpressionContext)
            else:
                return self.getTypedRuleContext(pythonGrammarParser.ArithExpressionContext,i)


        def value(self):
            return self.getTypedRuleContext(pythonGrammarParser.ValueContext,0)


        def getRuleIndex(self):
            return pythonGrammarParser.RULE_arithExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArithExpression" ):
                listener.enterArithExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArithExpression" ):
                listener.exitArithExpression(self)



    def arithExpression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = pythonGrammarParser.ArithExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 8
        self.enterRecursionRule(localctx, 8, self.RULE_arithExpression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                self.state = 58
                self.match(pythonGrammarParser.T__5)
                self.state = 59
                self.arithExpression(0)
                self.state = 60
                self.match(pythonGrammarParser.T__6)
                pass
            elif token in [17, 18]:
                self.state = 62
                self.value()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 70
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = pythonGrammarParser.ArithExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_arithExpression)
                    self.state = 65
                    if not self.precpred(self._ctx, 3):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                    self.state = 66
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 62) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 67
                    self.arithExpression(4) 
                self.state = 72
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class AssExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(pythonGrammarParser.VAR, 0)

        def assignOp(self):
            return self.getTypedRuleContext(pythonGrammarParser.AssignOpContext,0)


        def arithExpression(self):
            return self.getTypedRuleContext(pythonGrammarParser.ArithExpressionContext,0)


        def getRuleIndex(self):
            return pythonGrammarParser.RULE_assExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssExpression" ):
                listener.enterAssExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssExpression" ):
                listener.exitAssExpression(self)




    def assExpression(self):

        localctx = pythonGrammarParser.AssExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_assExpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            self.match(pythonGrammarParser.VAR)
            self.state = 74
            self.assignOp()
            self.state = 75
            self.arithExpression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return pythonGrammarParser.RULE_assignOp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignOp" ):
                listener.enterAssignOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignOp" ):
                listener.exitAssignOp(self)




    def assignOp(self):

        localctx = pythonGrammarParser.AssignOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_assignOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 7936) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(pythonGrammarParser.VAR, 0)

        def NUM(self):
            return self.getToken(pythonGrammarParser.NUM, 0)

        def getRuleIndex(self):
            return pythonGrammarParser.RULE_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValue" ):
                listener.enterValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValue" ):
                listener.exitValue(self)




    def value(self):

        localctx = pythonGrammarParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_value)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            _la = self._input.LA(1)
            if not(_la==17 or _la==18):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
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
        self.enterRule(localctx, 16, self.RULE_blocks)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            self.match(pythonGrammarParser.T__12)
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
        self.enterRule(localctx, 18, self.RULE_conStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            self.match(pythonGrammarParser.T__13)
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
        self.enterRule(localctx, 20, self.RULE_loops)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85
            self.match(pythonGrammarParser.T__14)
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
        self.enterRule(localctx, 22, self.RULE_comments)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            self.match(pythonGrammarParser.T__15)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[4] = self.arithExpression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def arithExpression_sempred(self, localctx:ArithExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         




