from ComplexNum import *
import operator
from itertools import product

n_range = 30
ints = map(int, range(-n_range, n_range))


class complex_stub_int(complex):
    def __new__(cls, *args, **kwargs):
        obj = super(complex_stub_int, cls).__new__(cls, *args)
        return obj

    def __neg__(self):
        return complex_stub_int(-self.real, -self.imag)

    def __repr__(self):
        if self.imag >= 0:
            return '{} + {}i'.format(int(self.real), int(self.imag))
        else:
            return '{}{}i'.format(int(self.real), int(self.imag))

    def __str__(self):
        return repr(self)


stub = complex_stub_int()


def sum_add(cs):
    return reduce(operator.add, cs)


def sum_neg(cs):
    return reduce(operator.sub, cs)


def sum_mul(cs):
    return reduce(operator.mul, cs)


def stubs():
    return map(lambda x: complex_stub_int(*x), product(ints, repeat=2))


def impls():
    return map(lambda x: ComplexNum(*x), product(ints, repeat=2))


c_stubs = stubs()
c_impl = impls()
# assert (repr(complex_stub_int(sum_add(c_stubs))) == repr(sum_add(c_impl)))
# assert (repr(complex_stub_int(sum_neg(c_stubs))) == repr(sum_neg(c_impl)))

for (c_s, c_i) in zip(c_stubs, c_impl):
    print -c_s
    print -c_i
    assert repr(-c_s) == repr(-c_i)
    assert repr(complex_stub_int(c_s * c_s)) == repr(c_i * c_i)
    assert repr(complex_stub_int(c_s.conjugate())) == repr(c_i.conjugate())
    assert repr(math.sqrt((c_s * c_s.conjugate()).real)) == repr(abs(c_i))
    assert repr(complex_stub_int(c_s - c_s)) == repr(c_i - c_i)
    assert c_s.real == c_i.re() and c_s.imag == c_i.im()



## simple tests ##
re, im = 1,2
n = ComplexNum(re, im)

print 'constructor + re + im'
assert n.re() == re and n.im() == im

print 'simple repr tests'
assert repr(n) == '1 + 2i' and repr(ComplexNum(1,-2)) == '1-2i'

print 'test we get back a tuple'
assert n.to_tuple() == (1,2) and type(n.to_tuple()) == tuple

print 'test repr with str...'
assert str(n) == '1 + 2i' and str(ComplexNum(1,-2)) == '1-2i'

print 'eq tests'
assert n == ComplexNum(1,2) and not n == ComplexNum(1,-2)

print 'test __add__'
assert n + n == ComplexNum(re+re,im+im) and ComplexNum(1,-2) + n == ComplexNum(re + re,0)

print 'testing neg method'
assert -n == ComplexNum(-re,-im)

print 'testing __sub__'
assert n - n == ComplexNum(0,0)


print 'All tests passed... (didnt check some...)'




