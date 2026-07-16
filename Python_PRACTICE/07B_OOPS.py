import csv
import os

# Always find loan_data.csv in the same folder as this script
loan_data = os.path.join(os.path.dirname(os.path.abspath(__file__)), "loan_data.csv")

old_user = False   

class loan:
    def __init__(self,name,salary,loan_amount,phone_number,credit_score):
        self.name = name
        self.salary = salary
        self.loan_amount = loan_amount
        self.credit_score = credit_score
        self.phone_number = phone_number
    def search_phone(self, phone_number):
        with open(loan_data, mode="r", encoding="utf-8", newline="") as loan_data_file:
            data_reader = csv.reader(loan_data_file)
            for row in data_reader:
                if row and row[0] == phone_number:
                    print("Phone Number Already Exists")
                    global old_user
                    old_user = True
                    info = row[0], row[1], row[2], row[3], row[4]
                    print(f"name {info[1]}\nsalary {info[2]}\nLoan Amount {info[3]}\nphone number {info[0]}\ncredit score {info[4]}")
                    return info
        print("enter details")
    def requirements(self):
        if self.salary >= 20000:
            print(f"Salary  {self.salary} ✅ ")
        else:
            print(f"Salary  {self.salary} ❌ ")
            print("Salary should be greater than 20000")
        if (self.loan_amount <= (8 * self.salary)):
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
    def new_user(self):
        name = input("Enter the name ")
        salary = int(input("Enter the salary "))
        loan_amount = int(input("Enter the loan amount "))
        credit_score = int(input("Enter the credit score "))
        loan1 = loan(name,salary,loan_amount,phone_number,credit_score)
        loan1.loan_evalute()
        with open(loan_data,"a",encoding="utf-8",newline="") as loan_data_file:
            data_writer = csv.writer(loan_data_file)
            data_writer.writerow([phone_number,name,salary,loan_amount,credit_score])
    def update_user(self):
        name = input("Enter new name (leave blank to keep current): ").strip() or self.name
        salary = input("Enter new salary (leave blank to keep current): ").strip()
        salary = int(salary) if salary else self.salary
        loan_amount = input("Enter new loan amount (leave blank to keep current): ").strip()
        loan_amount = int(loan_amount) if loan_amount else self.loan_amount
        credit_score = input("Enter new credit score (leave blank to keep current): ").strip()
        credit_score = int(credit_score) if credit_score else self.credit_score

        all_rows = []
        with open(loan_data, mode="r", encoding="utf-8", newline="") as loan_data_file:
            data_reader = csv.reader(loan_data_file)
            for row in data_reader:
                if row[0] == self.phone_number:
                    all_rows.append([self.phone_number, name, salary, loan_amount, credit_score])
                else:
                    all_rows.append(row)
        with open(loan_data, mode="w", encoding="utf-8", newline="") as loan_data_file:
            data_writer = csv.writer(loan_data_file)
            data_writer.writerows(all_rows)
        print("User details updated successfully.")
        updated = loan(name, salary, loan_amount, self.phone_number, credit_score)
        updated.loan_evalute()


if __name__ == "__main__":
    while True:
        try:
            phone_number = (input("Enter the phone number  ")).strip()
            if len(phone_number) == 10 and phone_number.isdigit():
                break
            else:
                print("Phone number should be 10 digits")
        except:
            print("Invalid phone number ")
    loan_obj = loan.__new__(loan)
    info = loan_obj.search_phone(phone_number)
    if old_user == False:
        loan_obj.new_user()
    elif old_user == True:
        # Reinitialize loan_obj with actual data so update_user() can access attributes
        loan_obj = loan(info[1], int(info[2]), int(info[3]), info[0], int(info[4]))
        invalid_input = True
        while invalid_input:
            try:
                choise_1 = (input("press enter to evalute or 1 to update detail")).strip()
                if choise_1 == "1":
                    invalid_input = False
                    loan_obj.update_user()
                elif not choise_1:
                    invalid_input = False
                    if info:
                        loan_detail = loan(info[1], int(info[2]), int(info[3]), info[0], int(info[4]))
                        loan_detail.loan_evalute()
                    else:
                        print("No info found")
                else:
                    print("Invalid choise  try again ")
            except Exception as e:
                print(f"An error occurred: {e}")