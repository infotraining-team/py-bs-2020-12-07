class Parent:
    def __init__(self):
        print("Parent constructor")
        self.parent_attr = 123

    def method(self):
        print("parent method")

class Child(Parent):
    def __init__(self):
        super().__init__()
        print("Child constructor")

    def method(self):
        super().method()
        print("child method")

p = Parent()
p.method()
print(p.parent_attr)
print("-------")
c = Child()
c.method()
print(c.parent_attr)