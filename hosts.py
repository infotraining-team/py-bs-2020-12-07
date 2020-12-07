content = open("hosts.txt").read()
print(content)

for line in content.splitlines():
    both_names, domain = line.split("@")
    name, surname = both_names.split(".")
    print("{:15} {:15} {}".format(name, surname, domain))

### print something like that:
## Jan        Nowak        apollo.pl
## Wanda      Kowalski     mrr.gov.pl
####
## Bonus - use RegExp
## import re
## re.match