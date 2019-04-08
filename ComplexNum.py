import math


class ComplexNum:
    def __init__(self, a, b):
        self.real = a
        self.imag = b

    def re(self):
        return self.real

    def im(self):
        return self.imag

    def to_tuple(self):
        return self.real, self.imag

    def __repr__(self):
        if self.imag >= 0:
            return str(self.real) + " + " + str(self.imag) + "i"
        else:
            return str(self.real) + " - " + str(-self.imag) + "i"

    def __eq__(self, other):
        if not isinstance(other, ComplexNum):
            raise TypeError("Complex Comparison only defined for Complex Numbers")
        return self.real == other.real and self.imag == other.imag

    def __add__(self, other):
        if not isinstance(other, ComplexNum):
            raise TypeError("Complex add only defined for Complex Numbers")
        return ComplexNum(self.real + other.real, self.imag + other.imag)

    def __neg__(self):
        return ComplexNum(-self.real, -self.imag)

    def __sub__(self, other):
        if not isinstance(other, ComplexNum):
            raise TypeError("Complex sub only defined for Complex Numbers")
        return self + other.__neg__()

    def __mul__(self, other):
        if not isinstance(other, ComplexNum):
            raise TypeError("Complex multiplication only defined for Complex Numbers")
        return ComplexNum(self.real * other.real - self.imag * other.imag, self.real * other.imag + self.imag * other.real)

    def conjugate(self):
        return ComplexNum(self.real, -self.imag)

    def __abs__(self):
        mul = self * self.conjugate()
        return math.sqrt(float(mul.real + mul.imag))
