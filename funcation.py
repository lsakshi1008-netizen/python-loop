#what is a function?
#A function is a block of code that runs when it is called.
# to avoid repetition of code we use functions.

#why use functions?
#1.avoid repetition of code.
#2.makes program clean and organized.
#3.easy to debug and reuse.
#syntax:
#def function_name():
    #code to be executed

#example of function
def greet():
    print("hello student") 
    greet() #calling the function   

#function with parameters
#used to pass values to a function.
def greet(name):
    print(f"hello {name}") 

greet("student") #calling the function with argument
greet("john") #calling the function with argument 

#bydefault parameters
def greet(name="student"):
    print(f"hello {name}")
greet() #calling the function without argument
greet("john") #calling the function with argument


#Function with return value
#used when we want to send result back.
def add(a,b):
    return a+b
result = add(5, 3)
print(result)

# #_______________________________________________________________________________________________#

#Task 1:
#Create a function to calculate and return result of 
#multiplication,addition ,subtraction ,division of two numbers.
def calculator(a,b):
    multiplication = a*b
    addition = a+b
    subtraction = a-b
    division = a/b
    return multiplication, addition, subtraction, division
result = calculator(10, 5)
print(f"Multiplication: {result[0]}")
print(f"Addition: {result[1]}")
print(f"Subtraction: {result[2]}")
print(f"Division: {result[3]}")

#Task 2:
#create a function to check if a number is even or odd.
def check_even_odd(number):
    if number%2==0:
        return "even"
    else:
        return "odd"

check = check_even_odd(10)
print(check)
check = check_even_odd(7)
print(check)

#user input
number = int(input("Enter a number: "))
def check_even_odd(number):
    if number%2==0:
        return "even"
    else:
        return "odd"
check = check_even_odd(number)
print(f"The number {number} is {check}.")

#Task 3:
#create a function to find the factorial of a number using loop.
#user input
number = int(input("Enter a number: "))
def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result
result = factorial(number)
print(f"The factorial of {number} is {result}.")

#Task 4:
#create a function to find maximum of three numbers.
#user input
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

def find_maximum(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
max_number = find_maximum(a, b, c)
print(f"The maximum number is: {max_number}")

#Task 5:
#create a function to check if a string is palindrome or not.
def is_palindrome(s):
    s = s.replace(" ", "").lower() 
    #remove spaces and convert to lowercase
    return s == s[::-1] 
    #check if string is equal to its reverse


# Example usage
string = input("Enter a string: ")
if is_palindrome(string):
    print(f"'{string}' is a palindrome.")
else:
    print(f"'{string}' is not a palindrome.")

#second method
def check_palindrome(s):
    if s == s[::-1]:
        return "Palindrome"
    else:
        return "Not Palindrome"

text = input("Enter a string: ")
result = check_palindrome(text)

print("Result:", result) 

#Task 6:
#create a function to calculate the area of a circle.
import math
def area_of_circle(radius):
    area = math.pi * radius**2
    return area

radius = float(input("Enter the radius of the circle: "))
print("Area of the circle:", area_of_circle(radius))

#second method
def area_circle(r):
    area = 3.14 * r * r
    return area

radius = float(input("Enter radius: "))
result = area_circle(radius)

print("Area of circle is:", result)
