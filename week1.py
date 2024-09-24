# v1 = float(input("enter n 1: "))
# v2 = float(input("enter n 2: "))
# vs = str("enter a name")
# print(v1*v2)

# print (v1%v2)
# student=[(str,int)]

# student = input("name and grade")

# for key, value in student:
#     max(value)
#     print(student)

# Python Practice Problems:

# 1. Create a function which takes as an input two
# numbers and returns the remainder when dividing
# first number by second number
# x=int(input("enter 1st number"))
# y=int(input("enter 2nd number"))

# def remainder(x,y):
#  return (x % y)

# result = remainder(x,y)
# print(result)

#2. Create a function which takes as an input a name,
# and returns a message with the following format
# “Hello There, nameInputHere”, where
# nameInputHere is the input to the function

# name =input("enter name : ")
# print("Hello There," +name+ "!")


# 3. Create a function that takes as an input the radius
# of the circle and returns the area of the circle (area
# of circle =pi*radius^2)

# import math

# r = float(input("enter the radius: "))
# def area(r):
#     return math.pi * (r ** 2)

# print(area(r))

students = []

# Input loop
# while True:
#     name = input("Enter student's name (or type 'done' to finish): ")
#     if name.lower() == 'done':
#         break
#     try:
#         grade = float(input("Enter student's grade: "))
#         students.append((name, grade))
#     except ValueError:
#         print("Please enter a valid number for the grade.")

# # Finding the student with the maximum grade
# if students:  # Check if the list is not empty
#     max_student = max(students, key=lambda student: student[1])
#     print(f"The student with the highest grade is {max_student[0]} with a grade of {max_student[1]}.")
# else:
#     print("No students were entered.")


# x=0
# while True:
#     name = int(input("Enter student's name (or type 'stop' to finish):"))
#     if name==-1:
#         break
#     if name%5==0:
#         continue
#     x += name 
#     print(f"the of given number is {x}")
    
# assume we have a lisy of nummber, and we need to loop
# over those numbers to print the sum

# using while loop
# list= []

# while True:
#     num = int(input("Enter a number (or type 'stop' to finish): "))
#     if num =='stop':
#         break
#     try:

# list=[10,4,4,5,2]

sum1=0
i=0
for i in range(0,list[i],1):
    list=int(input("enter:1"))
    sum1+=list[i]
print(sum1)