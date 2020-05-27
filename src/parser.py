from rply import ParserGenerator
from src.mer_ast import *


class Parser:

    def __init__(self):
        self.pg = ParserGenerator(
            ['INTEGER', 'PRINT', 'STRING',
             'FLOAT', 'ADD', 'SUB', 'DIV',
             'MUL', '(', ')', 'LOOP', ',',
             'BOOLEAN', 'IDENTIFIER', '=',
             '+=', '-='
            ],
            precedence=[
                ('left', ['INTEGER', 'FLOAT']),
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

        @self.pg.production('statement : LOOP ( expression , statements )')
        def loop(p):
            return Loop(p[2], p[4])

        @self.pg.production('statement : IDENTIFIER = expression')
        def variable(p):
            return Assign(p[0], p[2])

        @self.pg.production('statement : IDENTIFIER += expression')
        def plus_equals(p):
            return Assign(p[0], BinOp(Variable(p[0]), "ADD", p[2]))

        @self.pg.production('statement : IDENTIFIER -= expression')
        def plus_equals(p):
            return Assign(p[0], BinOp(Variable(p[0]), "SUB", p[2]))

        @self.pg.production('expression : expression SUB expression')
        @self.pg.production('expression : expression ADD expression')
        @self.pg.production('expression : expression MUL expression')
        @self.pg.production('expression : expression DIV expression')
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
            return Integer(p[0])
        
        @self.pg.production('expression : FLOAT')
        def exp_float(p):
            return Float(p[0])
        
        @self.pg.production('expression : STRING')
        def exp_string(p):
            return String(p[0])

        @self.pg.production('expression : BOOLEAN')
        def exp_boolean(p):
            return Boolean(p[0])

        @self.pg.production('expression : IDENTIFIER')
        def call(p):
            return Variable(p[0])
        
        @self.pg.error
        def error_handler(token):
            raise ValueError(f"Ran into a {token} where it wasn't expected")

        return self.pg.build()


