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

#4.Problem Statement: 
# Design a Python program with an Inventory class to manage the stock of products. 
# The class should allow updating the stock for products and displaying the current stock levels.
class INVENTORY:
    def __init__(self,name,stock):
        self.name = name
        self.stock= stock
    def full_update_inventory(self,amount):
        self.stock += amount
        print(f"{self.name} updated to : {self.stock}")
    def add_stock(self,amount):
        self.stock += amount
        print(f"{self.name} added to : {self.stock}")
    def remove_stock(self,amount):
        if amount < self.stock:
            self.stock -= amount
            print(f"{self.name} removed : {self.stock}")
        else:
            print("insufficient stock")
    def display(self):
        print(f"current stock : {self.stock}")

inventory = INVENTORY("Shiva-kumar",100)
inventory.display()
inventory.add_stock(50)
inventory.remove_stock(25)
inventory.display()

#4.Problem Statement: 
# Design a program that uses a Book class to store details of books in a library. 
# Allow users to search for books by title or author and display the details of the matching book(s).

class bookstore:
    def __init__(self,title,author):
        self.title = title
        self.author = author

    def search(self,title,author):
        if self.title == title or self.author == author:
            print(f"Book found : {self.title}")
            print(f"Author : {self.author}")
        else:
            print("Book not found")

    def display(self):
        print(f"Book : {self.title}")
        print(f"Author : {self.author}")

book1 = bookstore("Shiva-kumar","Shiva-kumar")
book1.display()
book1.search("Shiva-kumar","Shiva-kumar")

#5.Problem Statement: 
# Create a Loan class that evaluates if a person qualifies for a loan based on their salary and the loan amount requested. 
#The class should have methods to check if the loan can be approved or rejected based on simple criteria.
class loan:
    def __init__(self,name,salary,loan_amount):
        self.name = name
        self.salary = salary
        self.loan_amount = loan_amount
    def loan_evalute(self):
        if self.salary > self.loan_amount * 4:
           print(f"Name : {self.name}")
           print("Loan Approved")
        else:
           print(f"Name : {self.name}")
           print("Loan Rejected")

loan1 = loan("Shiva-kumar",1000,10000)
loan1.loan_evalute()

__init__