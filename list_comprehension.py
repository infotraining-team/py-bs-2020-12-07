l = [1,2,3,4,5,6]

# l2 -> l elements squared

l2 = []
for elem in l:
    if elem > 3:
        l2.append(elem ** 2)

print(l2)
l3 = [elem ** 2 for elem in l if elem > 3]
print(l3)



# Task
# 2 ** 8 -> 256
# 2 + 5 + 6 = 13
# 2 ** 9 -> 512 -> 8

# what is the sum of 2**1000

print(2**1000)
# 
# str <-> int
# 
string_number = str(2**1000)
print(type(string_number))
print(string_number[0])
print(string_number[-1])
sum([1,2,3,4]) # -> 10

result = 0
for digit in string_number:
    result += int(digit)
print(result)

res = sum( int(digit) for digit in str(2**1000) )
print(res)

for i in [0,1,2,3]:
    print(i)

for i in range(3):
    print(i)
