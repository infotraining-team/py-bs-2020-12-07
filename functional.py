l = [1, 2, 3, 4, 5]

def inc(a):
    return a + 1

def add(a, b):
    return a + b

l2 = []
for elem in l:
    l2.append(inc(elem))

print(l2)

l3 = map(inc, l)
print(list(l3))

print([inc(x) for x in l])

l4 = map(add, l, l2)
print(list(l4))

def greater_than_three(a):
    return a > 3

l5 = filter(greater_than_three, l)
print(list(l5))

l6 = filter(lambda a : a > 3, l)
print(list(l6))

l7 = map(lambda a : a + 1, l)
print(list(l7))
