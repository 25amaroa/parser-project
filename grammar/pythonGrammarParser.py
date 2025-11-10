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
        4,1,16,73,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,1,0,4,0,22,8,0,11,0,12,0,23,1,0,1,0,1,
        1,1,1,1,1,1,1,1,1,1,1,3,1,34,8,1,1,2,1,2,5,2,38,8,2,10,2,12,2,41,
        9,2,1,2,1,2,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,3,4,53,8,4,1,4,1,4,1,
        4,5,4,58,8,4,10,4,12,4,61,9,4,1,5,1,5,1,6,1,6,1,7,1,7,1,8,1,8,1,
        9,1,9,1,9,0,1,8,10,0,2,4,6,8,10,12,14,16,18,0,2,1,0,2,6,1,0,13,14,
        71,0,21,1,0,0,0,2,33,1,0,0,0,4,35,1,0,0,0,6,44,1,0,0,0,8,52,1,0,
        0,0,10,62,1,0,0,0,12,64,1,0,0,0,14,66,1,0,0,0,16,68,1,0,0,0,18,70,
        1,0,0,0,20,22,3,2,1,0,21,20,1,0,0,0,22,23,1,0,0,0,23,21,1,0,0,0,
        23,24,1,0,0,0,24,25,1,0,0,0,25,26,5,0,0,1,26,1,1,0,0,0,27,34,3,4,
        2,0,28,34,3,6,3,0,29,34,3,12,6,0,30,34,3,14,7,0,31,34,3,16,8,0,32,
        34,3,18,9,0,33,27,1,0,0,0,33,28,1,0,0,0,33,29,1,0,0,0,33,30,1,0,
        0,0,33,31,1,0,0,0,33,32,1,0,0,0,34,3,1,0,0,0,35,39,3,8,4,0,36,38,
        5,15,0,0,37,36,1,0,0,0,38,41,1,0,0,0,39,37,1,0,0,0,39,40,1,0,0,0,
        40,42,1,0,0,0,41,39,1,0,0,0,42,43,5,0,0,1,43,5,1,0,0,0,44,45,5,1,
        0,0,45,7,1,0,0,0,46,47,6,4,-1,0,47,48,5,7,0,0,48,49,3,8,4,0,49,50,
        5,8,0,0,50,53,1,0,0,0,51,53,3,10,5,0,52,46,1,0,0,0,52,51,1,0,0,0,
        53,59,1,0,0,0,54,55,10,3,0,0,55,56,7,0,0,0,56,58,3,8,4,4,57,54,1,
        0,0,0,58,61,1,0,0,0,59,57,1,0,0,0,59,60,1,0,0,0,60,9,1,0,0,0,61,
        59,1,0,0,0,62,63,7,1,0,0,63,11,1,0,0,0,64,65,5,9,0,0,65,13,1,0,0,
        0,66,67,5,10,0,0,67,15,1,0,0,0,68,69,5,11,0,0,69,17,1,0,0,0,70,71,
        5,12,0,0,71,19,1,0,0,0,5,23,33,39,52,59
    ]

class pythonGrammarParser ( Parser ):

    grammarFileName = "pythonGrammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'opp'", "'+'", "'-'", "'*'", "'/'", "'%'", 
                     "'('", "')'", "'block'", "'con'", "'loop'", "'comment'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "VAR", "NUM", "NEWLINE", "WHITESPACE" ]

    RULE_program = 0
    RULE_func = 1
    RULE_arithOperators = 2
    RULE_assOperators = 3
    RULE_arithExpression = 4
    RULE_value = 5
    RULE_blocks = 6
    RULE_conStatement = 7
    RULE_loops = 8
    RULE_comments = 9

    ruleNames =  [ "program", "func", "arithOperators", "assOperators", 
                   "arithExpression", "value", "blocks", "conStatement", 
                   "loops", "comments" ]

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
    VAR=13
    NUM=14
    NEWLINE=15
    WHITESPACE=16

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
            self.state = 21 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 20
                self.func()
                self.state = 23 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 32386) != 0)):
                    break

            self.state = 25
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
            self.state = 33
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7, 13, 14]:
                self.enterOuterAlt(localctx, 1)
                self.state = 27
                self.arithOperators()
                pass
            elif token in [1]:
                self.enterOuterAlt(localctx, 2)
                self.state = 28
                self.assOperators()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 3)
                self.state = 29
                self.blocks()
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 4)
                self.state = 30
                self.conStatement()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 5)
                self.state = 31
                self.loops()
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 6)
                self.state = 32
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
            self.state = 35
            self.arithExpression(0)
            self.state = 39
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==15:
                self.state = 36
                self.match(pythonGrammarParser.NEWLINE)
                self.state = 41
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 42
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
            self.state = 44
            self.match(pythonGrammarParser.T__0)
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
            self.state = 52
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                self.state = 47
                self.match(pythonGrammarParser.T__6)
                self.state = 48
                self.arithExpression(0)
                self.state = 49
                self.match(pythonGrammarParser.T__7)
                pass
            elif token in [13, 14]:
                self.state = 51
                self.value()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 59
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = pythonGrammarParser.ArithExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_arithExpression)
                    self.state = 54
                    if not self.precpred(self._ctx, 3):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                    self.state = 55
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 124) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 56
                    self.arithExpression(4) 
                self.state = 61
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
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
        self.enterRule(localctx, 10, self.RULE_value)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62
            _la = self._input.LA(1)
            if not(_la==13 or _la==14):
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
        self.enterRule(localctx, 12, self.RULE_blocks)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self.match(pythonGrammarParser.T__8)
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
        self.enterRule(localctx, 14, self.RULE_conStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            self.match(pythonGrammarParser.T__9)
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
        self.enterRule(localctx, 16, self.RULE_loops)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self.match(pythonGrammarParser.T__10)
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
        self.enterRule(localctx, 18, self.RULE_comments)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            self.match(pythonGrammarParser.T__11)
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
         




