# import basic
# while True:
#     text = input('mert > ')
#     tokens, errors = basic.run(text)
#     if errors: print(errors.as_string())
#     else: print(tokens)

from src.lexer import Lexer;
from src.parser import Parser;

lexer = Lexer().build()
parser = Parser().build()
tokens = lexer.lex("2+2")
print(tokens)
parser.parse(tokens).eval()