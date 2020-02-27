class Account:

    def __init__(self, name, start_balance=0):
        self.name = name
        self.start_balance = start_balance
        self._transactions = []

    @property
    def balance(self):
        return self.start_balance + sum(self._transactions)

    # add dunder methods below
    def __len__(self):
        return len(self._transactions)
     
    def __eq__(self, other):
        return self.balance == other.balance

    def __gt__(self, other):
        return self.balance > other.balance

    def __ge__(self, other):
        return self.balance >= other.balance

    def __lt__(self, other):
        return self.balance < other.balance

    def __le__(self, other):
        return self.balance <= other.balance

    def __getitem__(self, index):
        return self._transactions[index] 

    def __iter__(self):
        return iter(self._transactions)

    @classmethod
    def check_number(cls, number):
        try:
            0 + number
        except:
            raise ValueError('Not a number')

    def __add__(self, number):
        Account.check_number(number)
        self._transactions.append(number) 

    def __sub__(self, number):
        Account.check_number(number)
        self._transactions.append(-number) 

    def __str__(self):
        return f'{self.name} account - balance: {self.balance}'

a = Account('Giro')
b = Account('Savings', 100)
a + 10
a - 50
a + 40
print(len(a))
print(a)