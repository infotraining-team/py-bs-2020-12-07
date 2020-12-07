# https://github.com/infotraining-team/py-bs-2020-12-07

name_list = ['Dionizy', 'Natalia', 'anna', 'Artur', 'Stefan', 'Kinga', 'Aleksandra', 
           'Katarzyna', 'Zofia', 'Ksawery', 'Maciej', 'monika', 'Tomasz', 'Weronika',
           'Marcin', 'Dominik', 'Ewa']

foreign_name = ['Jean', 'Paul', 'Mao', 'Aurielie']

# 1 - print from name_list names ending in 'a'
for name in name_list:
    if name[-1] == 'a':
        print(name)

# 2 - remove from name_list Artur and Stefan
name_list.remove("Artur")
name_list.remove("Stefan")
if "Leszek" in name_list:
    name_list.remove("Leszek")
else:
    print("Leszek not in the list")
print(name_list)

# 3 - create a list with names starting with M
big_m_list = []
for name in name_list:
    if name[0] == "M":
        big_m_list.append(name)
print(big_m_list)

# 4 - sort the combined list of names

name_list.extend(foreign_name)
# print(name_list)
name_list.sort(key=str.lower)
# big_list = name_list + foreign_name
print(name_list)

# 5 - sort according to name length
name_list.sort(key=len)

# 6 - reverse list from excercise 5
name_list.sort(key=len, reverse=True)