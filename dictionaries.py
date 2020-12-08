dictionary = { "one": 1, "two": 2, "three": 3}
print(dictionary["one"])

for key in dictionary:
    print(dictionary[key])

print("ola" in dictionary)
print("three" in dictionary)

dictionary["four"] = 4
dictionary["one"] = 123
#print(dictionary["ola"])
print(dictionary)

for k, v in dictionary.items():
    print(k, v)

new_dict = {}
for k, v in dictionary.items():
    new_dict[v] = k

print(new_dict)

one_to_many = {}
one_to_many["Leszek"] = [7123213, 123123, 123123]
one_to_many["Ola"] = [7213, 123, 123]

print(one_to_many)
for number in one_to_many["Leszek"]:
    print(number)
