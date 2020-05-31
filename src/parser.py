from rply import ParserGenerator
from rply.errors import ParserGeneratorWarning
from src.mer_ast import *
import warnings


class Parser:

    def __init__(self):
        self.pg = ParserGenerator(
            ['INTEGER', 'PRINT', 'STRING',
             'FLOAT', 'ADD', 'SUB', 'DIV',
             'MUL', 'MOD', '(', ')', ',',
             'LOOP', 'BOOLEAN', 'IDENTIFIER',
             '=', '+=', '-=', '{', '}', 'IF',
             'ELSE', 'READ', '==', '!=', '>',
             '<', '>=', '<='
             ],
            precedence=[
                ('left', ['INTEGER', 'FLOAT']),
                ("left", ["IF", "LOOP", "ELSE"]),
                ('left', ["<=", ">=", "==", "="]),
                ('left', ['ADD', 'SUB']),
                ('left', ['MUL', 'DIV'])
            ]
        )

    def build(self):
        @self.pg.production("statements : statements statements")
        @self.pg.production("statements : statement")
        def statements_all(p):
            return Statements(p)

        @self.pg.production('statement : PRINT ( expression )')
        def exp_print(p):
            return Print(p[2])

        @self.pg.production('expression : READ ( expression )')
        def reading(p):
            return Read(p[2])

        @self.pg.production('statement : LOOP ( expression ) block')
        def loop(p):
            return Loop(p[2], p[4])

        @self.pg.production('expression : expression == expression')
        def equals(p):
            return BinOp(p[0], "==", p[2])

        @self.pg.production('expression : expression != expression')
        def not_equals(p):
            return BinOp(p[0], "!=", p[2])

        @self.pg.production('expression : expression < expression')
        def smaller(p):
            return BinOp(p[0], "<", p[2])

        @self.pg.production('expression : expression > expression')
        def bigger(p):
            return BinOp(p[0], ">", p[2])

        @self.pg.production('expression : expression >= expression')
        def big_equals(p):
            return BinOp(p[0], ">=", p[2])

        @self.pg.production('expression : expression <= expression')
        def small_equals(p):
            return BinOp(p[0], "<=", p[2])

        @self.pg.production('statement : IDENTIFIER = expression')
        def variable(p):
            return Assign(p[0].getstr(), p[2])

        @self.pg.production('statement : IDENTIFIER += expression')
        def plus_equals(p):
            return Assign(p[0].getstr(), BinOp(Variable(p[0].getstr()), "ADD", p[2]))

        @self.pg.production('statement : IDENTIFIER -= expression')
        def minus_equals(p):
            return Assign(p[0].getstr(), BinOp(Variable(p[0].getstr()), "SUB", p[2]))

        @self.pg.production('block : { statements }')
        @self.pg.production('block : { }')
        def closure_statements(p):
            if len(p[1:-1]) == 0:
                return Statements([])
            else:
                return p[1]

        @self.pg.production('statement : expression IF block')
        @self.pg.production('statement : expression IF block ELSE block')
        def if_else(p):
            if len(p) > 3:
                return If(p[0], p[2], p[4])
            else:
                return If(p[0], p[2])

        @self.pg.production('expression : expression SUB expression')
        @self.pg.production('expression : expression ADD expression')
        @self.pg.production('expression : expression MUL expression')
        @self.pg.production('expression : expression DIV expression')
        @self.pg.production('expression : expression MOD expression')
        def expression(p):
            left = p[0]
            right = p[2]
            binop = p[1].gettokentype()
            return BinOp(left, binop, right)

        @self.pg.production('expression : ( expression )')
        def exp_parens(p):
            return p[1]

        @self.pg.production('expression : INTEGER')
        def exp_number(p):
            return Integer(p[0].getstr())

        @self.pg.production('expression : FLOAT')
        def exp_float(p):
            return Float(p[0].getstr())

        @self.pg.production('expression : STRING')
        def exp_string(p):
            return String(p[0].getstr())

        @self.pg.production('expression : BOOLEAN')
        def exp_boolean(p):
            if p[0].getstr() == "doğru":
                return Boolean(True)
            else:
                return Boolean(False)

        @self.pg.production('expression : IDENTIFIER')
        def call(p):
            return Variable(p[0].getstr())

        @self.pg.error
        def error_handler(token):
            raise ValueError(f"Ran into a {token} where it was not expected")

        # Build
        warnings.filterwarnings("ignore", category=ParserGeneratorWarning)
        return self.pg.build()


