class Boolean():
    def __init__(self, value):
        self.value = value.getstr()
    def eval(self):
        if(self.value == "doğru"):
            return True
        elif(self.value == "yanlış"):
            return False

class Integer():
    def __init__(self, value):
        self.value = value.getstr()

    def eval(self):
        return int(self.value)


class Float():
    def __init__(self, value):
        self.value = value.getstr()

    def eval(self):
        return float(self.value)


class String():
    def __init__(self, value):
        self.value = value.getstr()

    def eval(self):
        return str(self.value)


class BinOp():
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

class Print():
    def __init__(self, value):
        self.value = value

    def eval(self):
        print(self.value.eval())

class Loop():
    def __init__(self, time, function):
        self.time = time
        self.function = function
    def eval(self):
        for x in range(self.time.eval()):
            self.function.eval()