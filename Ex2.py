from ComplexNum import ComplexNum

z = ComplexNum(1, 2)
t = z.to_tuple()
print t
print z

z2 = ComplexNum(1, 3)
z3 = ComplexNum(1, 2)

print z == z2

print z == z3

print z == 2

print z-z2

