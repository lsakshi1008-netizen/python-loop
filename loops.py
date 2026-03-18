# #what is a loop?
# #A loop is used to repeat a block of code multiple
# #times until a conditions is met.

# #Types of loops in python
# #1. For loop
# #used when we know how many times we want repeat.

# #syntax:
# #for variable in sequence:
#     #code to be executed 

# #range() function is used to generate a sequence of numbers.
# #range comes with 3 parameters: start, stop, step
# #1.start:(inclusive)
# #2.stop:(exclusive)
# #3.step:(optional) default is 1

# #range(start, stop-1, step)

# #Example of for loop
# for i in range(1,5):
#     print(i)

# #key points:
# #range(start,stop)generates numbers
# #loops runs fixed number of times


# #2. While loop
# #used when we don't know how many times we want to repeat.
# #syntax:
# #while condition:
#     #code to be executed

# #Example of while loop
# i=1
# while i<=5:  
#     print(i)
#     i+=1 #i=i+1
# #output: 1 2 3 4 5

# #key points:


# #loop control statements:
# #1. break:
# #stops the loop immediately.

# #example of break statement
# for i in range(1,6):
#     if i==3:
#         break
#     print(i)
# #output: 1 2

# #2. continue:
# #skips the current iteration.
# for i in range(1,6):
#     if i==3:
#         continue
#     print(i)
# #output: 1 2 4 5


# #3. pass:
# #Does nothing(placeholder)
# for i in range(5):
#     pass #to be implemented later

#_________________________________________________________________________#


# #Task 1:
# #print numbers from 1 to 10 using a for loop.
# for i in range(1,11):
#     print(i)
# #output: 1 2 3 4 5 6 7 8 9 10 (each number in new line)

# #Task 2:
# #print even numbers from 1 to 20 using a for loop.    
# for i in range(2, 21, 2):
#     print(i)

# for i in range(1, 21):
#     if i%2==0:
#         print(i, end=' ')  
# #output: 2 4 6 8 10 12 14 16 18 20          

# #Task 3:
# #print odd numbers from 1 to 15 using a for loop.
# for i in range(1, 16, 2):
#     print(i, end=' ')
# #output: 1 3 5 7 9 11 13 15    

# #decreasing order of odd numbers from 21 to 3
# for i in range(21, 1, -2):
#     print(i, end=' ')
# #output: 21 19 17 15 13 11 9 7 5 3     

# #Task 4:
# #print each chracter of string.
# #text = "python"
# string = "python"
# for char in string:
#     print(char) 
# #output: p y t h o n (each character in new line)

# #Task 5: 
# #print all items in a list.
# data = ["Data","Science", "AI"]
# for item in data:
#     print(item)
# #output:
# #  Data 
# #  Science 
# #  AI     

# #Task 6:
# #find the sum of numbers from 1 to 10.
# total = 0
# for i in range(1, 11):
#     total += i #total = total + i
# print("The sum of numbers from 1 to 10 is:", total)
# #output: The sum of numbers from 1 to 10 is: 55

#Task 7:
#print the multiplication table of 5.
number = 5
for i in range(1, 11):
    print(f"{number} x {i} = {number*i}")
    #f-string is used to format the string.

for i in range(1, 11):
    print(f"5 x {i} = {5 * i}") 
#output:
# 5 x 1 = 5 
# 5 x 2 = 10
# 5 x 3 = 15    
# 5 x 4 = 20
# 5 x 5 = 25
# 5 x 6 = 30
# 5 x 7 = 35
# 5 x 8 = 40
# 5 x 9 = 45
# 5 x 10 = 50

#Task 8:
#count the number of vowels in a string.
string = "hello world"
vowels = "aeiouAEIOU"
count = 0
for char in string:
    if char in vowels:
        count += 1
print("The number of vowels in the string is:", count)
#output: The number of vowels in the string is: 3

#Task 9:
#print numbers in reverse order from 10 to 1
for i in range(10, 0, -1):
    print(i, end=' ')
#output: 10 9 8 7 6 5 4 3 2 1

#Task 10:
#print squares of numbers from 1 to 5.
for i in range(1, 6):
    print(f"The square of {i} is {i**2}")
    #print(i ** 2)
    #** is used to calculate the power of a number.
#output:
# The square of 1 is 1
# The square of 2 is 4
# The square of 3 is 9
# The square of 4 is 16
# The square of 5 is 25

