alist = [1, 2, 3, "Ola"]
print(alist[0])
print(alist[3])

for elem in alist:
    print(elem)

print("len:", len(alist))
alist.append(5)
print("len:", len(alist), alist)

alist.extend([6, 7, 8])
print(alist)
alist.append([9, 10, 11])
print(alist)
alist.insert(0, "First")
print(alist)
alist.remove("Ola")
print(alist)

other = [4, 6, 10, 3, 1]
another = other  # this is not a copy!!
other.sort()
print(another, other)
print(id(other) == id(another))

other.sort(reverse=True)
print(other)

some_list = ["Ala", "Aleksander", "Leszek"]
some_list.sort(key=len, reverse=True)
print(some_list)




