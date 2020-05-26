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
    def __init__(self, left, right):
        self.left = left
        self.right = right


class Sum(BinOp):
    def eval(self):
        return self.left.eval() + self.right.eval()


class Sub(BinOp):
    def eval(self):
        return self.left.eval() - self.right.eval()


class Mul(BinOp):
    def eval(self):
        return self.left.eval() * self.right.eval()


class Div(BinOp):
    def eval(self):
        return self.left.eval() / self.right.eval()


class Yaz():
    def __init__(self, value):
        self.value = value

    def eval(self):
        print(self.value.eval())
