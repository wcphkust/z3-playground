from z3 import *

# Check the validity of commutativity of (put, put) in HashMap
# b1 = m.put(k1, v1); b2 = m.put(k2, v2) is equivalent to b2 = m.put(k2, v2); b1 = m.put(k1, v1) if k1 is not equal to k2.
# Equivalence condition: b1, b2, content of hashmap are consistent.

K = DeclareSort('K')
V = DeclareSort('V')
k1, k2 = Consts('k1 k2', K)
v1, v2 = Consts('v1 v2', V)
k = Const('k', K)

m1_0 = Array('m1_0', K, V)
m1_1 = Array('m1_1', K, V)
m1_2 = Array('m1_2', K, V)
m2_0 = Array('m2_0', K, V)
m2_1 = Array('m2_1', K, V)
m2_2 = Array('m2_2', K, V)

s = Solver()
s.add(k1 != k2)
s.add(ForAll(k, Select(m1_0, k) == Select(m2_0, k)))
s.add(ForAll(k, Implies(k != k1, Select(m1_1, k) == Select(m1_0, k))), Select(m1_1, k1) == v1)
s.add(ForAll(k, Implies(k != k2, Select(m1_2, k) == Select(m1_1, k))), Select(m1_2, k2) == v2)
s.add(ForAll(k, Implies(k != k2, Select(m2_1, k) == Select(m2_0, k))), Select(m2_1, k2) == v2)
s.add(ForAll(k, Implies(k != k1, Select(m2_2, k) == Select(m2_1, k))), Select(m2_2, k1) == v1)
s.add(Not(And(ForAll(k, Select(m1_2, k) == Select(m2_2, k)))))     # Equivalence checking: content of hashmap is consistent
## TO BE POLISHED: Equivalence checking of b1 and b2
print(s.check())
