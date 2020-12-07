print("Something")
print(type(print))

c = 10

def inc(a):
    print("inside inc function")
    a += 1
    return a

print(inc(5))
print(inc(5.5))
#print(inc("5.5"))

a = 10
print("a = ", a)
inc(a)
print("a = ", a)
