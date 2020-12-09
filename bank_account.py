class BankAccount:
    __interest_rate = 0.01

    def __init__(self, owner, balance):
        self.__balance = balance
        self.__owner = owner

    def info(self):
        print("owner:", self.__owner, " - balance:", self.__balance)

    def withdraw(self, amount):
        if (self.__balance < amount):
            amount = self.__balance
            print("insufficent funds")
        self.__balance -= amount
        return amount

    def deposit(self, amount):
        self.__balance += amount

    @staticmethod
    def get_bank_info():
        print("HtB bank")

    @staticmethod
    def add(a, b):
        return a + b

    @classmethod
    def get_interest_rate(cls):
        print(cls.__interest_rate)

    ## @staticmethod equals to:
    ## get_bank_info = staticmethod(get_bank_info)

#print(BankAccount.__name__)

person1acc = BankAccount(owner="Leszek", balance=100)
person2acc = BankAccount("Ola", 200)

bank_log = []
bank_log.append(person1acc)
bank_log.append(person2acc)
bank_log.append(BankAccount("Sonia", 300))

for account in bank_log:
    account.info()
    amount = account.withdraw(200)
    print("asked for:", 200, "withdrawed:", amount)
 
#print(person1acc.__balance)
#person1acc.balance = -100

print("-"*20)
for account in bank_log:
    account.info()

## print(person1acc._BankAccount__balance) <- you shouldn't do it
## This is my interface
person1acc.deposit(200)
person1acc.withdraw(100)
person1acc.info()

person1acc.get_bank_info()

BankAccount.get_bank_info()
BankAccount.get_interest_rate()

BankAccount.add(2, 4)
