import csv

loan_data = "loan_data.csv"

old_user = False

        
while True:
    try:
        phone_number = int(input("Enter the phone number  "))
        if len(phone_number) == 10:
            break
        else:
            print("Phone number should be 10 digits")
    except:
        print("Invalid phone number ")



    

class loan:
    def __init__(self,name,salary,loan_amount,phone_number,credit_score):
        self.name = name
        self.salary = salary
        self.loan_amount = loan_amount
        self.credit_score = credit_score
        self.phone_number = phone_number
    def load_data(self, loan_data):
        with open(loan_data, mode="r", encoding="utf-8", newline="") as loan_data_file:
            data_reader = csv.reader(loan_data_file)
            return data_reader

    def search_phone(self, phone_number):
        data_reader = self.loan_data(loan_data)
        for row in data_reader:
            if row[3] == phone_number:
                print("Phone Number Found")
                old_user = True
                info = row[0],row[1],row[2],row[3],row[4]
            print(f"name {info[0]}\nsalary {info[1]}\nLoan Amount {info[2]}\nphone number {info[3]}\ncredit score {info[4]}")
       
    
    def requirements(self):
        if self.salary >= 20000:
            print(f"Salary  {self.salary} ✅ ")
        else:
            print(f"Salary  {self.salary} ❌ ")
            print("Salary should be greater than 20000")
        if self.loan_amount >= self.salary:
            print(f"Loan Amount : {self.loan_amount} ✅ ")
        else:
            print(f"Loan Amount : {self.loan_amount} ❌ ")
            print("Loan Amount should be less than or equal to Salary")
        if self.credit_score >= 600:
            print(f"Credit Score : {self.credit_score} ✅ ")
        else:
            print(f"Credit Score : {self.credit_score} ❌ ")
            print("Credit Score should be greater than or equal to 600")

    def loan_evalute(self):
        if (self.salary >= 20000) and (self.loan_amount <= (8 * self.salary)) and (self.credit_score >= 600):
           print(f"Name : {self.name}")
           self.requirements()
           print("Loan Approved")
        else:
           print(f"Name : {self.name}")
           self.requirements()
           print("Loan Rejected")
        

loan1 = loan("Shiva-kumar",1000,10000,676464564,720)
loan1.loan_evalute()