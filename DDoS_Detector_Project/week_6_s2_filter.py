
#1.Problem Statement:
#Filter names from a list, keeping those that are longer than 5 characters.
names =['Alice', 'Bob', 'Catherine', 'David']
filtered_name = list(filter(lambda nam: len(nam) > 5,names))
print(filtered_name)


#2.Problem Statement:
# Filter out all negative numbers from a list.
numbers = [1, -2, 3, -4, 5]
filtered_num  = list(filter(lambda num: num >= 0,numbers))
print(filtered_num)


#3.Problem Statement:
#Filter out employees earning more than $50,000.
employees  = {'Jhon': 45000,'jane':55000,'Alice':60000}
filtered_employees = list(filter(lambda emp: employees[emp] > 50000,employees))
print(filtered_employees)


#4.Problem Statement: 
#Filter out students scoring more than 40 marks.
students = {'Alice': 35, 'Bob': 45, 'Catherine': 30, 'David': 50}
filtered_students = list(filter(lambda mark: students[mark] > 40, students))
print(filtered_students)


#5.Problem Statement:
#Remove empty strings from a list.
words = ['apple', '', 'banana', '', 'cherry']
without_empty = list(filter(lambda word: word != '',words))
print(without_empty) 


#6.Problem Statement: 
# Filter employees who have worked for 5 or more years.
employees = {'John': 4, 'Jane': 6, 'Alice': 5}
more_than_5 = list(filter(lambda employ: employees[employ] >= 5, employees))
print(more_than_5)


#7.Problem Statement: 
# Filter words from a list that have an even number of characters.
words = ['hello', 'world', 'python', 'data']
even_num_char = list(filter(lambda word: len(word) % 2 == 0,words))
print(even_num_char)

#8.Problem Statement:
#A teacher has a list of students' marks and wants to identify which students have passed the exam.
# The passing criteria are marks greater than or equal to 40.
student_marks = {'Alice': 35, 'Bob': 45, 'Catherine': 30, 'David': 50}
passed_students = list(filter(lambda mark: student_marks[mark] >= 40, student_marks))
print(passed_students)


#9.Problem Statement:
#An e-commerce store wants to identify customers who spent more than $100 in their latest orders.
#These high-spending customers will be targeted for exclusive offers or loyalty programs.
customer_spending = {"sushant":75,"madhu":200,"nehaz":50,"sudarshan":125,"ankit":300,"sohan":95,"rahul":80}
high_spenders = list(filter(lambda cost: customer_spending[cost] > 100,customer_spending))
print(high_spenders)


#10.problem Statement
#Scenario: Identifying Top Performers for Promotion**
#A company wants to shortlist employees for a special promotion. The criteria for eligibility are:
#The employee must earn a salary of more than ₹50,000 per year.
#The employee must have at least 5 years of work experience.
#The HR department provides three lists: employee names, their salaries (in thousands), and their years of experience. 
# Using these details, the company filters out the eligible employees to create the final list for consideration.
employees = ["John", "Jane", "Sam","Anna", "Tom"]
salaries = [50, 70, 60, 40, 80]
experience = [5, 7, 3, 2, 10]
top_performers = list(filter(lambda o: salaries[o] > 50 and experience[o] >= 5, range(len(employees))))
top_emp = [employees[x] for x in top_performers]
print(top_emp)