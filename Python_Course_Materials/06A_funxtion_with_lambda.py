#1.Problem Statement:
# Write a lambda function that takes two numbers and returns their sum.
first_num = int(input("Enter first number: "))
second_num = int(input("enter the second number"))
sum_of_two = lambda x,y: x + y
result = sum_of_two(first_num,second_num)
print(result)

#2.Problem Statement:
# Write a lambda function that takes two numbers and returns the larger number.
first_num = int(input("Enter first number: "))
second_num = int(input("enter the second number"))
larger_num = lambda x,y: x if x > y else y
result = larger_num(first_num,second_num)
print(result)

#3.Problem Statement:
# Write a lambda function that takes three parameters and returns their average.
first_num = int(input("Enter first number: "))
second_num = int(input("enter the second number"))
third_num = int(input("enter the third number"))
average = lambda x,y,z: (x + y + z)/3
result = average(first_num,second_num,third_num)
print(result)

#4.Problem Statement:
# Write a lambda function to check if a given string is a palindrome.
# The lambda function should return True if the string is the same when read forwards and backwards, and False otherwise.
str_inp = input("Enter the string: ")
palindrome = (lambda x: x == x[::-1])
print(palindrome(str_inp))

#5.Problem Statement:
# Write a lambda function that takes a string as input and returns the length of the string.
length = lambda x : len(x)
check = length(input("enter the word "))
print(check)

#6.Problem Statement:
# Write a lambda function that takes a number as input and checks if it is divisible by both 2 and 3.
# The function should return True if the number is divisible by both, otherwise return False.
check_div = lambda x : x % 2 == 0 and x % 3 == 0
enter_num = check_div(int(input("enter the number ")))
print(enter_num)

#7.Problem Statement:
# Write a program that uses the map() function along with a lambda function to multiply each element in the given list by 2.
# The output should be a new list with each element multiplied by 2.
user_input_str = input("enter the list (comma-separated numbers): ")
user_input = list(map(int, user_input_str.split(',')))
multi_2 = (map (lambda x : x*2, user_input))
new_list = (list(multi_2))
print(new_list)

#8.Problem Statement:
# Write a program that uses the map() function along with a lambda function to return the length of each word in the given list of words.
# The output should be a list containing the length of each word.
input_list = list(map(str, input("enter the list ").split(",")))
word_len = list(map(lambda x : len(x),input_list))
print(word_len)

#9.Problem Statement:
# Write a program that uses the map() function along with a lambda function to convert a list of strings to integers.
# The output should be a list containing the integer representation of each string in the input list.
inp_list = list(map(str, input("enter the list ").split(",")))
int_list = (map(lambda x : int(x) ,inp_list))
print(list(int_list))

#10.Problem Statement:
# Write a Python program that uses the map() function and a lambda function to add corresponding elements from two lists of equal length.
# The program should return a list of sums where each element is the sum of the corresponding elements from both lists.
num_list_1 = list(str(input("enter the list ")))
num_list_2 = list(str(input("enter the list ")))
cal_list = list(map(lambda x,y : int(x)+int(y),num_list_1,num_list_2))
print(cal_list)

#11.Problem Statement:
# Write a Python program that uses the map() function and a lambda function to find the product of corresponding elements in two tuples of equal length.
# The program should return a list where each element is the product of the corresponding elements from both tuples.
inp_tuple_1 = tuple(input("enter the tuple ").split(","))
inp_tuple_2 = tuple(input("enter the tuple ").split(","))
mul_map = list(map(lambda x,y : int(x)*int(y),inp_tuple_1,inp_tuple_2))
print(mul_map)

#12.Problem Statement:
#Write a Python program using a lambda function to calculate the product of three numbers.
product_of_3 = lambda x,y,z : x*y*z
enter_num = product_of_3(int(input("enter the number ")),int(input("enter the number ")),int(input("enter the number")))
print(enter_num)

#13.Problem Statement:
# Write a program using a lambda function to find the minimum of two numbers.
min_2  = (lambda x,y : min(x,y))
two_num = int(input("enter the number "))
one_num = int(input("enter the number "))
result_num = min_2(two_num,one_num)
print(result_num)

#14.Problem Statement:
# Write a Python program using a lambda function to concatenate three strings.
str_1 = input("enter the string :-")
str_2 = input("enter the string :-")
str_3 = input("enter the string :-")
concatenation = lambda x,y,z : x+y+z
print(concatenation(str_1,str_2,str_3))