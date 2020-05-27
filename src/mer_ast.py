variables = {}


class Statements:
    def __init__(self, nodes):
        self.nodes = nodes
    
    def eval(self):
        for node in self.nodes:
            node.eval()

class Boolean:
    def __init__(self, value):
        self.value = value.getstr()

    def eval(self):
        if (self.value == "doğru"):
            return True
        elif (self.value == "yanlış"):
            return False


class Integer:
    def __init__(self, value):
        self.value = value.getstr()

    def eval(self):
        return int(self.value)


class Float:
    def __init__(self, value):
        self.value = value.getstr()

    def eval(self):
        return float(self.value)


class String:
    def __init__(self, value):
        self.value = value.getstr()

    def eval(self):
        return str(self.value)

class Null:
    def eval(self):
        return self
    def getstr(self):
        return 'yok'


class BinOp:
    def __init__(self, left, binop, right):
        self.left = left
        self.binop = binop
        self.right = right

    def eval(self):
        if self.binop == "ADD":
            return self.left.eval() + self.right.eval()
        elif self.binop == "SUB":
            return self.left.eval() - self.right.eval()
        elif self.binop == "MUL":
            return self.left.eval() * self.right.eval()
        elif self.binop == "DIV":
            return self.left.eval() / self.right.eval()
        elif self.binop == "MOD":
            return self.left.eval() % self.right.eval()
        else:
            raise AssertionError("Something went super wrong.")

class If:
    def __init__(self, condition, body, else_body=None):
        self.condition = condition
        self.body = body
        self.else_body = else_body

    def eval(self):
        if self.condition.eval():
            return self.body.eval()
        elif self.else_body is not None:
            return self.else_body.eval()
        return Null()


class Print:
    def __init__(self, value):
        self.value = value

    def eval(self):
        print(self.value.eval())


class Loop:
    def __init__(self, time, function):
        self.time = time
        self.function = function

    def eval(self):
        for x in range(self.time.eval()):
            self.function.eval()


class Assign:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def eval(self):
        variables[self.name.getstr()] = self.value.eval()


class Variable:
    def __init__(self, name):
        self.name = name

    def eval(self):
        if self.name.getstr() in variables.keys():
            return variables[self.name.getstr()]
        else:
            raise RuntimeError("Not Declared:", self.name)
