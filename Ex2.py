# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Part1~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


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
        return ComplexNum(self.real * other.real - self.imag * other.imag,
                          self.real * other.imag + self.imag * other.real)

    def conjugate(self):
        return ComplexNum(self.real, -self.imag)

    def __abs__(self):
        mul = self * self.conjugate()
        return math.sqrt(float(mul.real + mul.imag))


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Part2~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def getSubClasses(cls):
    lst = []
    if cls.__bases__ is ():
        return []
    lst.append(cls.__bases__[0])
    return set(lst).union([s for c in lst for s in getSubClasses(c)])


def isInstancePPL(object1, classInfo):
    if classInfo is object:
        return str(type(object1)) != '<type \'classobj\'>' and str(type(object1)) != '<type \'type\'>'
    return ((str(type(object1)) == '<type \'instance\'>' or '<class' in str(type(object1))) and
            (str(type(classInfo)) == '<type \'classobj\'>' or str(type(classInfo)) == '<type \'type\'>')) and \
           len([cls for cls in getSubClasses(object1.__class__) if classInfo is cls]) > 0


def numInstancePPL(object1, classInfo):
    if str(type(object1)) != '<type \'classobj\'>' and str(type(object1)) != '<type \'type\'>' and \
            (type(object1) is classInfo or object1.__class__ is classInfo):
        return 1
    elif isInstancePPL(object1, classInfo):
        sub_classes = list(getSubClasses(object1.__class__))
        if classInfo is object:
            if object in sub_classes:
                return 1 + len(sub_classes)
            return 2 + len(sub_classes)
        return 1 + len([cls for cls in sub_classes if cls not in getSubClasses(classInfo)])
    else:
        return 0


def isSubclassPPL(clas, classInfo):
    if clas is object and classInfo is object:
        return True
    elif clas is object and classInfo is not object:
        return False
    elif clas is not object and classInfo is object:
        return True
    return ((str(type(clas)) == '<type \'classobj\'>' or str(type(clas)) == '<type \'type\'>') and
            (str(type(classInfo)) == '<type \'classobj\'>' or str(type(classInfo)) == '<type \'type\'>')) and \
           len([cls for cls in getSubClasses(clas) if classInfo is cls]) > 0


def numSubclassPPL(clas, classInfo):
    if clas is classInfo:
        return 1
    if isSubclassPPL(clas, classInfo):
        sub_classes = list(getSubClasses(clas))
        if classInfo is object:
            if object in sub_classes:
                return 1 + len(sub_classes)
            return 2 + len(sub_classes)
        return 1 + len([cls for cls in sub_classes if cls not in getSubClasses(classInfo)])
    else:
        return 0


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Part3~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def count_if(lst, func):
    if not isinstance(lst, list):
        raise TypeError
    if not callable(func):
        raise TypeError
    return len(filter(func, lst))


def for_all_red(lst, apply, pred):
    if not isinstance(lst, list):
        raise TypeError
    if not callable(pred):
        raise TypeError
    if not callable(apply):
        raise TypeError
    return pred(reduce(apply, lst))


def there_exists(lst, n, pred):
    if not isinstance(lst, list):
        raise TypeError
    if not callable(pred):
        raise TypeError
    if not isinstance(n, int):
        raise TypeError
    return len(filter(pred, lst)) >= n
