import math

from Ex2 import ComplexNum
from Ex2 import numSubclassPPL, for_all_red, there_exists, numInstancePPL

c = complex(1, 2)
c2 = complex(1, 3)
print c * c2
z = ComplexNum(1, 2)
t = z.to_tuple()
print t
print z

z2 = ComplexNum(1, 3)
z3 = ComplexNum(1, 2)

print z == z2

print z == z3

# print z == 2

print z - z2

print z * z2

print abs(z)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class X(object):
    def __init__(self):
        self.x = 1


class Y(X):
    def __init__(self):
        X.__init__(self)
        self.y = 2


class Z(Y):
    def __init__(self):
        Y.__init__(self)
        self.z = 3


class T(Z):
    def __init__(self):
        Z.__init__(self)
        self.t = 4


x = X()
t = T()
y = Y()
z = Z()

print numInstancePPL(Y, object)  # 0
print numInstancePPL(X, object)  # 0
print numInstancePPL(X, Y)  # 0
print numInstancePPL(int, object)  # 0
print numSubclassPPL(int, object)  # 2
print numInstancePPL(y, object)  # 3
print numInstancePPL("fff", object)  # 3
print numInstancePPL(2, 3)  # 0
print numInstancePPL(2, Y)  # 0
print numInstancePPL(y, 3)  # 0
print numInstancePPL(int, int)  # 0
print numInstancePPL(object, 5)  # 0
print numInstancePPL([], list)  # 1
print numInstancePPL(2, int)  # 1
print numInstancePPL(y, T)  # 0
print numInstancePPL(z, Y)  # 2
print numInstancePPL(y, X)  # 2
print numInstancePPL(z, Z)  # 1
print numInstancePPL(x, X)  # 1
print numInstancePPL(z, X)  # 3
print numInstancePPL(t, Y)  # 3
print numInstancePPL(5, 4)  # 0
print numSubclassPPL(object, int)  # 0
print numSubclassPPL(T, X)  # 4
print numSubclassPPL(Z, X)  # 3
print numSubclassPPL(Y, X)  # 2
print numSubclassPPL(T, Y)  # 3
print numSubclassPPL(Y, Y)  # 1
print numSubclassPPL(int, object)  # 2
print numSubclassPPL(Y, object)  # 3
print numSubclassPPL(str, object)  # 3
print numSubclassPPL(2, 3)  # 0
print numSubclassPPL(int, int)  # 1
print numSubclassPPL(object, 5)  # 0
print numSubclassPPL(object, object)  # 1
print numSubclassPPL([], list)  # 0
print numSubclassPPL(list, list)  # 1
print numSubclassPPL(2, int)  # 0
print numSubclassPPL(y, T)  # 0

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

print for_all_red([1, 0, 8], lambda x, y: x * y, lambda x: x > 0)
print for_all_red([1, 1, 8], lambda x, y: x * y, lambda x: x > 7)
print there_exists([1, 1, 8], 1, lambda x: x > 7)
print there_exists([1, 1, 8], 2, lambda x: x > 7)
