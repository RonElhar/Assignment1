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

