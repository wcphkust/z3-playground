from z3 import *

# Check the satisfiability of commutativity
# K = DeclareSort('K')
# V = DeclareSort('V')
# k1, k2 = Consts('k1 k2', K)
# v1, v2 = Consts('v1 v2', V)
# k = Const('k', K)
# undefv = Const('undefv', V)
# m1_0 = Function('m1_0', K, V)
# m1_1 = Function('m1_1', K, V)
# m1_2 = Function('m1_2', K, V)
#
# m2_0 = Function('m2_0', K, V)
# m2_1 = Function('m2_1', K, V)
# m2_2 = Function('m2_2', K, V)
#
# s = Solver()
# s.add(v1 != undefv)
# s.add(v2 != undefv)
# s.add(k1 != k2)
# s.add(ForAll(k, m1_0(k) == undefv))
# s.add(ForAll(k, Implies(k != k1, m1_1(k) == m1_0(k))), m1_1(k1) == v1)
# s.add(ForAll(k, Implies(k != k2, m1_2(k) == m1_1(k))), m1_2(k2) == v2)
#
# s.add(ForAll(k, m2_0(k) == undefv))
# s.add(ForAll(k, Implies(k != k2, m2_1(k) == m2_0(k))), m2_1(k2) == v2)
# s.add(ForAll(k, Implies(k != k1, m2_2(k) == m2_1(k))), m2_2(k1) == v1)
#
# s.add(ForAll(k, m2_2(k) == m1_2(k)))     # Equality checking
# print(s.check())

# Check the validity of commutativity
K = DeclareSort('K')
V = DeclareSort('V')
k1, k2 = Consts('k1 k2', K)
v1, v2 = Consts('v1 v2', V)
k = Const('k', K)
undefv = Const('undefv', V)
m1_0 = Function('m1_0', K, V)
m1_1 = Function('m1_1', K, V)
m1_2 = Function('m1_2', K, V)

m2_0 = Function('m2_0', K, V)
m2_1 = Function('m2_1', K, V)
m2_2 = Function('m2_2', K, V)

s = Solver()
p1 = Not(v1 != undefv)
p2 = Or(Not(v2 != undefv), p1)
p3 = Or(Not(k1 != k2), p2)

p4 = Or(Not(ForAll(k, m1_0(k) == undefv)), p3)
p5 = Or(Not(ForAll(k, Implies(k != k1, m1_1(k) == m1_0(k)))), p4)
p6 = Or(Not(m1_1(k1) == v1), p5)
p7 = Or(Not(ForAll(k, Implies(k != k2, m1_2(k) == m1_1(k)))), p6)
p8 = Or(Not(m1_2(k2) == v2), p7)

p9 = Or(Not(ForAll(k, m2_0(k) == undefv)), p8)
p10 = Or(Not(ForAll(k, Implies(k != k2, m2_1(k) == m2_0(k)))), p9)
p11 = Or(Not(m2_1(k2) == v2), p10)
p12 = Or(Not(ForAll(k, Implies(k != k1, m2_2(k) == m2_1(k)))), p11)
p13 = Or(Not(m2_2(k1) == v1), p12)

p14 = Or(Not(ForAll(k, m2_2(k) == m1_2(k))), p13)   # Equality checking
s.add(p14)
print(s)
print(s.check())


# a && b valid
# !(!a || !b) valid
# (!a || !b) unsat

