from src.lexer import Lexer
from src.parser import Parser
import sys

lexer = Lexer().build()
parser = Parser().build()

with open(sys.argv[1], "r", encoding="utf8") as f:
    a = f.read()
    parser.parse(lexer.lex(a)).eval()


