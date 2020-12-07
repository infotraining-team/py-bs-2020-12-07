name = "Leszek"
astring = 'this is also a string'
astring2 = """This is a long string
and multiline too
"""
rawstring = r"Line\nanotherline"
print(rawstring)
polish_string = "żółw"
print(len(polish_string))

print(name.lower())
print(name.upper())
print(name.capitalize())

file = "file.txt"
print(file.endswith(".txt"))
print(file.startswith(".txt"))

print(astring.split())
print(file.split("."))
print(astring2.splitlines())

template = "Welcome {0}, please accept {1}"
print(template.format("User", "gift"))

template = "Welcome {user}, please accept {something}"
print(template.format(user="User", something="gift"))

print("{} {:>10.6f} {}".format(3, 3.14, 123.123))
