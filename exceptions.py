l = [1,2,3]
print(l[0])
try:
    print(l[10])
    print("This will never show")
except IndexError as err:
    print("Index error - ", err)

n = 1

try:
    c = 1/n
    print(l[10])
except ZeroDivisionError:
    print("Zero division")
    c = "not defined"  
else:
    print("else in exception - no exception happend")
finally:
    print("always execute")

print("This is the rest of programm")
print("value = " , c)

try:
    f = open("hosts.txt")
    content = f.read()
    1/0
finally:
    f.close()


with open("hosts.txt") as f:
    content = f.read()
    1/0


print("Finish")
