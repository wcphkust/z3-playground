from z3 import *

# Abstraction of Map
# Introduce uninterpreted function to interprete hashing function
# Aim to prove: two different keys must not correspond to the same index after hashing
# Reference: Slide of Dillig's POPL 2011
# URL: https://www.cs.utexas.edu/~isil/popl2011-talk.pdf

K = DeclareSort('K')
V = DeclareSort('V')
f = Function('f', K, V)
k1, k2 = Consts('k1 k2', K)
x1, x2 = Consts('x1 x2', K)
v = Const('v', V)

s = Solver()
s.add(ForAll([x1, x2], Implies(f(x1) == f(x2), x1 == x2)))
s.add(k1 != k2)
s.add(Exists(v, And(v == f(k1), v == f(k2))))
print(s.check())

