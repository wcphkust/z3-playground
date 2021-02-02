from z3 import *

# Check the validity of commutativity of (add, add) in HashSet
# b1 = s.add(k1); b2 = s.add(k2) is equivalent to b2 = s.add(k2); b1 = s.add(k1) if k1 is not equal to k2
# Equivalence condition: b1, b2, content of set are consistent.

K = DeclareSort('K')
V = BoolSort()
k1, k2 = Consts('k1 k2', K)
v1, v2 = Consts('v1 v2', V)
k = Const('k', K)

s1_0 = Array('m1_0', K, V)
s1_1 = Array('m1_1', K, V)
s1_2 = Array('m1_2', K, V)
s2_0 = Array('m2_0', K, V)
s2_1 = Array('m2_1', K, V)
s2_2 = Array('m2_2', K, V)

s = Solver()
s.add(k1 != k2)
s.add(ForAll(k, Select(s1_0, k) == Select(s2_0, k)))
s.add(ForAll(k, Implies(k != k1, Select(s1_1, k) == Select(s1_0, k))), Select(s1_1, k1) == True)
s.add(ForAll(k, Implies(k != k2, Select(s1_2, k) == Select(s1_1, k))), Select(s1_2, k2) == True)
s.add(ForAll(k, Implies(k != k2, Select(s2_1, k) == Select(s2_0, k))), Select(s2_1, k2) == True)
s.add(ForAll(k, Implies(k != k1, Select(s2_2, k) == Select(s2_1, k))), Select(s2_2, k1) == True)
s.add(Not(ForAll(k, Select(s1_2, k) == Select(s2_2, k))))     # Equality checking
## TO BE POLISHED: Equivalence checking of b1 and b2
print(s.check())
