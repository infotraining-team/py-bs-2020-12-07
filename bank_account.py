class BankAccount:
    def __init__(self, owner, balance):
        self.balance = balance
        self.owner = owner

    def info(self):
        print("owner:", self.owner, " - balance:", self.balance)

    def withdraw(self, amount):
        print("withdraw called for", self.owner)
        self.balance -= amount
        return amount

#print(BankAccount.__name__)

person1acc = BankAccount(owner="Leszek", balance=100)
person2acc = BankAccount("Ola", 200)

person1acc.owner = "Leszek"
person1acc.balance = 100

bank_log = []
bank_log.append(person1acc)
bank_log.append(person2acc)
bank_log.append(BankAccount("Sonia", 300))

for account in bank_log:
    account.info()
    account.withdraw(100)

print("-"*20)
for account in bank_log:
    account.info()