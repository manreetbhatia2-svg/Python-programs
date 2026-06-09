from abc import ABC, abstractmethod
class BankAccount(ABC):
    def __init__(self,balance):
        self.balance = balance 

    @abstractmethod
    def withdraw(self,amount):
        pass

    def deposit(self,amount):
        self.balance += amount
        return(f"Balance after deposit: {self.balance}")
    
class SavingsAccount(BankAccount):
    def withdraw(self, amount):
        if (self.balance - amount) >= 1000:
            self.balance -= amount
            return(f"Balance after withdrawal: {self.balance} ")
        else:
            return("You can't witdraw the amount as minimum balance of Rs.1000 is required ")
    
class CurrentAccount(BankAccount):
    def withdraw(self, amount):
        self.balance -= amount
        return(f"Balance after withdrawal: {self.balance} ")
    
print("       ****SAVING ACCOUNT****        ")
saving = SavingsAccount(1500)
print(saving.deposit(600))
print(saving.withdraw(1100),"\n")
print("       ****CURRENT ACCOUNT****       ")
current = CurrentAccount(8000)
print(current.deposit(500))
print(current.withdraw(6000))