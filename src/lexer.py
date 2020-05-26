from rply import Token, LexerGenerator

class Lexer:
    def __init__(self):

        self.lg = LexerGenerator()

        self.lg.ignore(r"\s+")
        self.lg.ignore(r"//.*")

        self.lg.add("PRINT", r"yazdır")
        self.lg.add("LOOP", r"tekrar")

        self.lg.add("ASSIGN", r"=")
        self.lg.add("ASSIGN_INC", r"\+=")
        self.lg.add("ASSIGN_DEC", r"\-=")

        self.lg.add("STRING", r"'.*'")
        self.lg.add("FLOAT",  r"\d+(\.\d+)") #r"[-]?\d+(\.\d+)"
        self.lg.add("INTEGER", r"\d+") # [-]?\d+
        self.lg.add("BOOLEAN", r"(doğru|yanlış)")
        self.lg.add("ADD", r"\+")
        self.lg.add("SUB", r"-")
        self.lg.add("MUL", r"\*")
        self.lg.add("DIV", r"\/")
        self.lg.add("MOD", r"\%")

        self.lg.add("(", r"\(")
        self.lg.add(")", r"\)")

        self.lg.add("[", r"\[")
        self.lg.add("]", r"\]")
        self.lg.add("{", r"\{")
        self.lg.add("}", r"\}")
        self.lg.add(",", r",")

        self.lg.add("IDENTIFIER", r"[_\w]*[_\w0-9]+")

    def build(self):
        return self.lg.build()
