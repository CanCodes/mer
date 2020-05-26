from rply import ParserGenerator
from src.mer_ast import *

class Parser():
    def __init__(self):
        self.pg = ParserGenerator(
            ['INTEGER', 'PRINT', 'STRING',
             'FLOAT', 'ADD', 'SUB', 'DIV',
             'MUL', '(', ')'
            ],
            precedence=[
                ('left', ['ADD', 'SUB']),
                ('left', ['MUL', 'DIV'])
            ]
        )

    def build(self):
        @self.pg.production('function : PRINT ( expression )')
        def exp_print(p):
            return Yaz(p[2])

        @self.pg.production('expression : INTEGER')
        def exp_number(p):
            return Integer(p[0])
        
        @self.pg.production('expression : FLOAT')
        def exp_float(p):
            return Float(p[0])
        
        @self.pg.production('expression : STRING')
        def exp_string(p):
            return String(p[0])
        
        @self.pg.production('expression : ( expression )')
        def exp_parens(p):
            return p[1]

        @self.pg.production('expression : expression ADD expression')
        @self.pg.production('expression : expression SUB expression')
        @self.pg.production('expression : expression MUL expression')
        @self.pg.production('expression : expression DIV expression')
        def expression(p):
            left = p[0]
            right = p[2]
            binop = p[1].gettokentype()
            if binop == "ADD":
                return Sum(left, right)
            elif binop == "SUB":
                return Sub(left, right)
            elif binop == "MUL":
                return Mul(left, right)
            elif binop == "DIV":
                return Div(left, right)
            else:
                raise AssertionError("Something went super wrong.")

        return self.pg.build()

