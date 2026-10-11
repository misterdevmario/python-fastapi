

class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def __str__(self):
        return f'{self.name} : {self.balance}'   

    def __add__(self, other):
        return Account("Cmbined = ", self.balance + other.balance)


user1 = Account("Mario", 10000000)        
user2 = Account("Lizeth", 10000000)        

combined = user1 + user2

print(combined)