# practice 1
# Think of a Car class as a template for creating car objects.
# The class defines what properties every car will have, like the car's color, brand, and speed.
class car:
    def __init__(self,model,color,speed,year):
        self.model = model
        self.color = color
        self.speed = speed
        self.year = year

    def detail(self):
        print(f"MODEL :- ",self.model)
        print(f"COLOR OF {self.model} :-",self.color)
        print(f"SPEED OF {self.model} :-",self.speed)
        print(f"DATE OF MANUFACTURE OF {self.model}",self.year)

car1 = car("zzz","nigga",00,2026)
car1.detail()

#practice 2
#**Scenario: ---- Managing a Personal Bank Account----
#Simulate managing a bank account using a Python class to perform deposits, withdrawals, and balance checks:
#1.Create Account:
#2.Deposit Money:
#3.Withdraw Money:
#4.Check Balance:

class account:
    def __init__(self,username,balance=0):
        self.username = username
        self.balance = balance

    def deposits(self, amount):
        self.balance += amount
        print(f"{self.username} deposited ${amount}")
        print(f"current balance : {self.balance}")

    def withdraw(self,amount):
        if amount < self.balance:
            self.balance -= amount
            print(f"{self.username} withdrew ${amount}")
            print(f"current balance : {self.balance}")
        else:
            print("insufficient balance")
    def check_balance(self):
        print(self.balance)

customer1 = account("Shiva-kumar")
customer1.deposits(100)
customer1.withdraw(20)
customer1.check_balance()


#PRACTICE 3
#Create a Student class with the following:
#Attributes:name, marks
#Methods:
#add_marks(marks) → adds marks to the student
#deduct_marks(marks) → deducts marks (if marks are sufficient)
#display_result() → displays student name and final marks
class student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def add_marks(self,marks):
        self.marks += marks
        print(f"{self.name} added marks : {self.marks}")
    def deduct_marks(self,marks):
        if marks < self.marks:
            self.marks -= marks
            print(f"{self.name} deducted marks : {self.marks}")
        else:
            print("insufficient marks")
    def display_marks(self):
        print(f"{self.name} display marks : {self.marks}")

student1 = student("Shiva-kumar",400)
student1.add_marks(100)
student1.deduct_marks(50)
student1.display_marks()