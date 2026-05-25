# METHODS IN SETS
s={1,2,3}
s.add(4)
s.update([5,6])
s.remove(4)
s.discard(4)
print(s)


# OPERATIONS IN SETS

s1={1,2,3,4}
s2={3,4,5,6}
print(s1.union(s2))

s1={1,2,3,4}
s2={3,4,5,6}
print(s1.intersection(s2))

s1={1,2,3,4}
s2={3,4,5,6}
s1.intersection_update(s2)
print(s1)

s1={1,2,3,4}
s2={3,4,5,6}
print(s1.difference(s2))

s1={1,2,3,4}
s2={3,4,5,6}
print(s1.symmetric_difference(s2))

s1={1,2,3}
s2={1,2,3,4,5}
print(s1.issubset(s2))
print(s1.issuperset(s2))

s1={1,2}
s2={3,4,5,6}
print(s1.isdisjoint(s2))

#SOME BASIC PROBLEMS IN SETS

l=[1,2,2,3,4,5,6,6,7]
s=set(l)
print(s)

l1=[1,2,3,4]
l2=[3,4,5,6]
s1=set(l1)
s2=set(l2)
print(s1.intersection(s2))

x={1,2,3,4}
t=20
if t in x:
    print("found")
else:
    print("not found")