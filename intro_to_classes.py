l = str("a string")
print(type(l))
print(id(l))
print(l)
print(l.upper())
print(l.upper)

class MyClass:
    def __init__(self, param=None):
        print("in constructor")
        self.param = param

    def my_fun(self):
        print("myfun:", self.param)

print(type(MyClass))
inst1 = MyClass()
print(type(inst1))

list_of_strings = ["ala", "leszek"]
for s in list_of_strings:
    s.upper()

list_of_instances = [MyClass("First"), MyClass("Second")]
for i in list_of_instances:
    i.my_fun()
    print(id(i))
    print(i.param)