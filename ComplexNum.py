class ComplexNum:
    def __init__(self, a, b):
        self.re = a
        self.im = b

    def re(self):
        return self.re

    def im(self):
        return self.im

    def to_tuple(self):
        return self.re, self.im

    def __repr__(self):
        return str(self.re) + " + " + str(self.im) + "i"

    def __eq__(self, other):
        if not isinstance(other, ComplexNum):
            return False
        return self.re == other.re and self.im == other.im

    def __add__(self, other):
        if not isinstance(other, ComplexNum):
            raise TypeError
        return ComplexNum(self.re + other.re, self.im + other.im)

    def __neg__(self):
        return ComplexNum(-self.re, -self.im)

    def __sub__(self, other):
        if not isinstance(other, ComplexNum):
            raise TypeError
        return self + other.__neg__()


