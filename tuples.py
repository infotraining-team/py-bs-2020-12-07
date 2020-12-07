atuple = 1, 2, 3
print(atuple)
atuple = "Ola", 2, 3
print(atuple)

alist = list(atuple)
alist.append(10)
print(alist)

def full_division(a, b):
    res = a // b
    mod = a % b
    return res, mod

print(full_division(7, 2))

res = full_division(7, 2)
print(res[0], res[1])

div, rest = full_division(7, 2)
print(div, rest)

a = 10
b = 20
a, b = b, a  # neat trick
print(a, b)

i = 0
for l in "Leszek":
    print(i, l)
    i += 1

for i, l in enumerate("Leszek"):
    print(i, l)