


#  1: Take input marks for English, Islamiat, and Maths
# english_marks = int(input("Enter marks in English (out of 100): "))
# islamiat_marks = int(input("Enter marks in Islamiat (out of 100): "))
# maths_marks = int(input("Enter marks in Maths (out of 100): "))

# #  2: Assign the total marks
# total_marks = 300

# #  3: Calculate the percentage
# obtained_marks = english_marks + islamiat_marks + maths_marks
# percentage = (obtained_marks / total_marks) * 100

# #  4: Assign grades using conditional statements
# if percentage >= 90:
#     grade = 'A'
# elif percentage >= 80:
#     grade = 'B'
# elif percentage >= 70:
#     grade = 'C'
# elif percentage >= 60:
#     grade = 'D'
# else:
#     grade = 'F'

# # Printing  results
# print("Obtained Marks: {}".format(obtained_marks))
# print("Percentage: {:.2f}%".format(percentage))
# print("Grade: {}".format(grade))

# Assignment 1B
# 1. Write a Python program to print the following string in a specific format (see the  output).  
# Twinkle, twinkle, little star,  
#  How I wonder what you are!  
#  Up above the world so high,  
# Like a diamond in the sky.  
#  Twinkle, twinkle, little star,  
#  How I wonder what you are  
  

# def print_twinkle():
#     lines = [
#         "Twinkle, twinkle, little star,",
#         "                   How I wonder what you are!",
#         "                                 Up above the world so high,",
#         "                                  Like a diamond in the sky.",
#         "",
#         "Twinkle, twinkle, little star,",
#         "                   How I wonder what you are"
#     ]

#     for line in lines:
#         print(line)

# print_twinkle()

# Write the python program to get the python version we are using

# import sys

# python_version = sys.version
# print("Python version:", python_version)

# 2. Display current date and time in python

# from datetime import datetime

# current_datetime = datetime.now()
# print("Current date and time:", current_datetime)

# 3. Write python program which accepts the radius of a circle from user and compute the area

# import math

# radius = float(input("Enter the radius of the circle: "))
# area = math.pi * radius**2

# print("The area of the circle is:", area)

# 4. Write the python program which accepts the user's first name and print them in reverse order with a space between them

# first_name = input("Enter your first name: ")
# reversed_name = ' '.join(reversed(first_name))

# print("Reversed name:", reversed_name)

# 4. Write a program which takes two inputs from user and print them addition

# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))

# addition = num1 + num2

# print("The addition is:", addition)

# 5. A program that takes 5 inputs from user for different subjects marks, total it and generate mark sheet using grades

# subject_names = ['English', 'Islamiat', 'Maths', 'Science', 'History']
# total_marks = 0

# marks = []
# grades = []

# for subject in subject_names:
#     mark = float(input("Enter marks for {}: ".format(subject)))
#     marks.append(mark)
#     total_marks += mark

# percentage = (total_marks / (len(subject_names) * 100)) * 100

# for mark in marks:
#     if mark >= 90:
#         grade = 'A'
#     elif mark >= 80:
#         grade = 'B'
#     elif mark >= 70:
#         grade = 'C'
#     elif mark >= 60:
#         grade = 'D'
#     else:
#         grade = 'F'
#     grades.append(grade)

# print("Subject-wise Marks:")
# for i in range(len(subject_names)):
#     print("{}: {}".format(subject_names[i], marks[i]))

# print("\nTotal Marks: {}".format(total_marks))
# print("Percentage: {:.2f}%".format(percentage))
# print("Grades:", ' '.join(grades))

# 6. A program taking input from user and identify that the given number is even or odd

# num = int(input("Enter a number: "))

# if num % 2 == 0:
#     print("The number is even.")
# else:
#     print("The number is odd.")
#9. Write a program which print the length of the list?  

# def main():
    
#     my_list = [10, 20, 30, 40, 50]

#     list_length = len(my_list)
#     print("The length of the list is:", list_length)

# if __name__ == "__main__":
#     main()


# 10.Write a Python program to sum all the numeric items in a list?  

# my_list = [10, 20, 30, "hello", 40, 50.5, "world", 60.75]

# result = sum(item for item in my_list if isinstance(item, (int, float)))
# print("The sum of numeric items in the list is:", result)

# 11.Write a Python program to get the largest number from a numeric list.  


# numeric_list = [15, 82, 47, 59, 33, 70, 21, 95]

# largest_number = max(numeric_list)
# print("The largest number in the list is:", largest_number)


# 12. Take a list, say for example this one:  
  
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]  
#  Write a program that prints out all the elements of the list that are less than 5. 


# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

# result = [element for element in a if element < 5]
# print(result)
 

        #    ASSIGNMENT === 4

# 1. Make a calculator using Python with addition , subtraction ,  multiplication ,division and power.

# def add(x, y):
#     return x + y

# def subtract(x, y):
#     return x - y

# def multiply(x, y):
#     return x * y

# def divide(x, y):
#     if y != 0:
#         return x / y
#     else:
#         return "Cannot divide by zero"

# def power(x, y):
#     return x ** y

# # Dictionary to map operation symbols to functions
# operations = {
#     '+': add,
#     '-': subtract,
#     '*': multiply,
#     '/': divide,
#     '**': power
# }

# def main():
#     print("Available operations:")
#     for symbol in operations:
#         print(symbol)

#     operation = input("Enter operation symbol: ")

#     if operation in operations:
#         num1 = float(input("Enter first number: "))
#         num2 = float(input("Enter second number: "))
#         result = operations[operation](num1, num2)
#         print("Result:", result)
#     else:
#         print("Invalid operation")

# if __name__ == "__main__":
#     main()

# 2. Write a program to check if there is any numeric value in list using for  loop.

# def main():
    
#     my_list = [10, "hello", 3.14, "world", True]


#     has_numeric = any(isinstance(item, (int, float)) for item in my_list)

#     if has_numeric:
#         print("The list contains numeric values.")
#     else:
#         print("The list does not contain numeric values.")

# if __name__ == "__main__":
#     main()

# 3. Write a Python script to add a key to a dictionary. 

# def key_add():
    
#     my_dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}

#     my_dict['occupation'] = 'Engineer'


#     print(my_dict)

# if __name__ == "__main__":
#     key_add()

# 4. Write a Python program to sum all the numeric items in a dictionary

# def calculate_sum_of_numbers(custom_dict):
#     total_sum = 0

#     for val in custom_dict.values():
#         if isinstance(val, (int, float)):
#             total_sum += val

#     return total_sum

# def main():
#     data = {'x': 15, 'y': 25, 'z': 30.5, 'w': "hello", 'v': 40}

#     result = calculate_sum_of_numbers(data)
#     print("The sum of numeric items in the dictionary is:", result)

# if __name__ == "__main__":
#     main()

# 5. Write a program to identify duplicate values from list.

# def find_duplicates(input_list):
#     duplicates = []
#     unique_elements = set()
    
#     for item in input_list:
#         if item in unique_elements:
#             duplicates.append(item)
#         else:
#             unique_elements.add(item)
    
#     return duplicates

# input_list = [1, 2, 3, 4, 3, 5, 6, 2, 7, 8, 9, 1]
# duplicate_values = find_duplicates(input_list)

# if duplicate_values:
#     print("Duplicate values:", duplicate_values)
# else:
#     print("No duplicate values found.")

# 6. Write a Python script to check if a given key already exists in a  dictionary

# def key_exists(dictionary, key):
#     if key in dictionary:
#         return True
#     else:
#         return False

# # Example usage
# my_dict = {'a': 1, 'b': 2, 'c': 3}
# given_key = 'b'

# if key_exists(my_dict, given_key):
#     print(f"The key '{given_key}' exists in the dictionary.")
# else:
#     print(f"The key '{given_key}' does not exist in the dictionary.")





























































































