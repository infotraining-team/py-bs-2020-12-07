l = [1,2,3,4,5]
s = "Abrakadabra"

print(l[1:3])
print(s[1:5])
print(l[:3])
print(l[3:])

print(s[:4])
print(s[-4:])

l2 = l[:]
l2.append(6)
print(l)
print(id(l), id(l2))

print(s[::2])
print(s[1::2])
print(s[::-2])