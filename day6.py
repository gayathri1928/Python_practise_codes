fruits={'apple','banana','orange'}
print(fruits)

fruits.add('mango')
print(fruits)

fruits.remove('orange')
print(fruits)

fruits.discard('orange')
print(fruits)

even={2,4,6}
odd={1,3,5}
print(even|odd)
union=even.union(odd)
print(union)

set1={1,2,3}
set2={3,4,5}
sym_diff_set=set1.symmetric_difference(set2)
print(sym_diff_set)
print(set1^set2)

num={1, 2, 3, 4}
element=num.pop()
print(element)
print(num)

num.clear()
print(num)

a={1,2,3}
b={2,3,4,5}
print(a|b)
print(a&b)
print(a-b)

num1={1,2,3}
num2={1,2,3,4,5}
print(num1.issubset(num2))

num3=num1.copy()
print(num3)


num=([1,2,3,4,2,1])
fs=frozenset(num)
print(fs)

fs1 = frozenset([1, 2])
fs2 = frozenset([3, 4])
container=frozenset([fs1,fs2])
print(container)
