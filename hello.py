# https://github.com/infotraining-team/py-bs-2020-12-07
# https://infotraining.bitbucket.io/python-basic-en/

print("Hello world")

a = 10

if a > 3:
    print("Greater than 3")
    print("Still in first block")
else:
    print("Less than 3")

print("End of script")

while a > 5:
    print(a)
    a = a - 1

for x in "an example":
    print(x)    

print("-------")
for x in range(2, 10, 2):
    print(x)

# not working - int is not iterable
# for x in a:
#     print(x)