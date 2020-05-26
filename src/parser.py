from rply import ParserGenerator
from src.mer_ast import *

class Parser():
    def __init__(self):
        self.pg = ParserGenerator(
            ['INTEGER', 'PRINT', 'STRING',
             'FLOAT', 'ADD', 'SUB', 'DIV',
             'MUL', '(', ')', 'LOOP', ',',
             'BOOLEAN'
            ],
            precedence=[
                ('left', ['ADD', 'SUB']),
                ('left', ['MUL', 'DIV'])
            ]
        )

    def build(self):
        @self.pg.production('function : PRINT ( expression )')
        def exp_print(p):
            return Print(p[2])

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

        @self.pg.production('expression : ( expression )')
        def exp_parens(p):
            return p[1]

        @self.pg.production('expression : expression SUB expression')
        @self.pg.production('expression : expression ADD expression')
        @self.pg.production('expression : expression MUL expression')
        @self.pg.production('expression : expression DIV expression')
        def expression(p):
            left = p[0]
            right = p[2]
            binop = p[1].gettokentype()
            return BinOp(left, binop, right)



        @self.pg.production('function : LOOP ( expression , function )')
        def loop(p):
            return Loop(p[2], p[4])

        return self.pg.build()

