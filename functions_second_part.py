def print_person(name, surname, age=0):
    print("name:", name, "sn:", surname, "age:", age)

print_person("Jan", "Kowalski", 24)
print_person("Greg", "Newborn")
print_person(name="Leszek", age=43, surname="Tarkowski")

def almost_sort(key=None, reverse=False):
    pass

almost_sort(reverse=True)
almost_sort(None, True)
almost_sort(key=len)

def add(a, b):
    return a + b

# def add(a, b, c):
#     return a + b + c

print(add(3, 4))

def many_args(a, b, *c):
    print(a, b, c)

#many_args(3)
many_args(3, 4)
many_args(3, 4, 5)
many_args(3, 4, 5, 6)

# summae(1,2,3,4,5)  -> return 15
# summae(1,2,3)  -> return 6
# summae()  -> not working
# summae(2)  -> return 2

def summae(first, *args):
    for n in args:
        first += n
    return first

print("------")
print(summae(2))
print(summae(1,2,3,4,5))

def full_function(a, b, *args, **kwargs):
    print(a, b, args, kwargs)

print("------")
full_function(3, 4)
full_function(3, 4, 5, 6, 123)
full_function(3, 4, name="Leszek", age=43)

t = (1,2,3,4)

full_function(t[0], t[1], t[2], t[3])
full_function(*t)

d = {'a' : 3, 'b' : 4, 'name' : "Ola"}
full_function(**d)


