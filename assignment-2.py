#***********************FUNCTION*****************************
#1.	Write a function to check whether a number is positive, negative, or zero.
"""""
def number():
    num = int(input("Enter a number: "))
    if num > 0:
        print("The number is positive.")
    elif num < 0:
        print("The number is negative.")
    else:
        print("The number is zero.")

number()
"""
#2.	Write a function to check whether a number is even or odd. 
"""""
def EvenOdd():
    num = int(input("enter any number:"))
    if num % 2 == 0:
        print("The nmber is even.")
    else:
        print("the number is Odd.")

EvenOdd()
"""
#3.	Write a function that accepts two numbers and returns the greater number
"""""
def greater(a,b):
    if a > b:
        return a
    else:
        return b
    
print(greater(10,20))
"""

#4.	Write a function to check whether a person is eligible to vote (age ≥ 18). 
"""""
def Vote(age):
    if age >= 18:
        print("The person is eligible to vote.")
    else:
        print("The person is not eligible to vote.")
Vote(20)
"""
#5.	Write a function to check whether a number is divisible by 5. 
"""""
def divisible(num):

    if num % 5 == 0:
        print("The number is divisible by 5.")
    else:
        print("the number is not divisible by 5.")
divisible(34)
"""
#6.	Write a function to check whether a given year is a leap year or not. 
"""""
def Leapyear(year):
    if (year % 4 == 0):
        print("The year is a leap year.")
    else:
        print("The year is not a leap year.")
Leapyear(2022)
"""
# 7.	Write a function to check whether a character is a vowel or a consonant. 
"""""
def character():
    
    ch = input("Enter a character: ")
    if ch == 'a' or ch=='A':
        print("The character is a vowel.")
    elif ch == 'e' or ch == 'E' :
        print("The character is a vowel.")
    elif ch =='i' or ch== 'I':
        print("The character is a vowel.")
    elif ch == 'o' or ch == 'O':
        print("The character is a vowel.")  
    elif ch == 'u' or ch == 'U':
        print("The character is a vowel.")
    else:
        print("The character is not a vowel.")

character()
"""

#8.	Write a function to find the largest among three numbers
"""""
def Largest():

    num1 = int(input("Enter any number:"))
    num2 = int(input("Enter second number:"))
    num3 = int(input("Enter third number:"))

    if num1 > num2:
        if num1 > num3:
            print("The largest number is num1:", num1)
        else:
            print("The largest number is num3:", num3)
    else:
        if num2 > num3:
            print("The largest number is num2:", num2)
        else:
            print("The largest number is num3:", num3)
Largest()
"""
#9.	Write a function to calculate the sum of numbers from 1 to 100. 
"""""
def sum():

    sum=0
    for i in range(1,101):
        sum=sum+i
        
    print("The sum of first 100 numbers is:",sum)
sum()
"""
#10.	Write a function that prints the multiplication table of a given number. 
"""""
def Multiplication():

    num = int(input("Enter any number:"))
    for i in range(1,11):
        print(num,"*",i,"=",num*i)

Multiplication()
"""
#11.	Write a function to calculate and return the square of a number. 
"""""
def square():

    num = int(input("enter any number:"))
    return num*num
print("Square of number:",square())
"""

#12.	Write a function to calculate the factorial of a number using a loop. 
"""""
def factorial():
    num = int(input("Enter any number:"))
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    return fact
print("Factorial of the number:", factorial())
"""
#13.	Write a function to check whether a number is prime
"""""
def prime():
    num = int(input("Enter any number:"))
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                print(num, "is not a prime number.")
                break
        else:
            print(num, "is a prime number.")
    else:
        print(num, "is not a prime number.")
prime()
"""
#14.	Write a function to calculate the sum of digits of a number
"""""
def sum():
    sum=0
    num = int(input("Enter any number:"))
    for i in range(1,num+1):
        sum=sum+i

    print("sum of digits=",sum)
sum()
"""

#15.15.	Write a function that accepts a number n and returns the sum of all numbers from 1 to n.




#*************** List in Python***********************

#1.	Create a list of 10 numbers and print all the elements. 
"""""
numbers=[10,20,30,40,50]
print(numbers)
"""
#2.	Write a program to find the largest element in a list
"""""
numbers = [10,20,30,40,50]
largest = max(numbers)
print(largest)
"""
#3.	Write a program to find the smallest element in a list. 
"""""
numbers = [10,20,30,40,50]
largest = min(numbers)
print(largest)
"""
#4.	Write a program to calculate the sum of all elements in a list. 
"""""
numbers =[10,20,30,40,50]
sumall = sum(numbers)
print(sumall)
"""
#5.	Write a program to calculate the average of all elements in a list. 
"""""
numbers = [10, 20, 30, 40, 50]
total = 0
for num in numbers:
    total = total + num

average = total / len(numbers)

print("Average =", average)
"""

#6.	Write a program to count how many even numbers are present in a list. 
"""""
num = [2,5,8,9,3,7,4,6]
count = 0
for i in list:
    if NUM[i] % 2 == 0
    count = count+1
print(count)
    """
#7.	Write a program to create a new list containing only the odd numbers from an existing list. 
"""""
num =[1,2,3,4,5,6,7,8,9]
odd= []
for i in list:
if i % 2 != 0:
    odd.append(i)
print(odd)
"""
#8.	Write a program to find whether a given element exists in a list.
"""""
num = [1,2,3,4,5,6,7,8,9]
x = int(input("enter any number between 1-9..:))
if x in list:
    print("found")
else:
    print("Not Found")
"""

#9.	Write a program to reverse a list without using built-in reverse functions.
"""""
lst =[10,20,30,40,50,60]
rev=[]

for i in range(len(lst)-1,-1,-1):
    rev.append(lst[i])

print(rev[])
"""
#10.	Write a program to find the second largest element in a list.
"""""
number = [10,20,40,60,30,50]
number.sort()
print(number())
"""

#************************DICTIONARY***********************************************

#1.	Create a dictionary to store a student's name, age, and city, and print the dictionary. 
"""""
person ={"name":"John","age":30,"work":"student"}
for i in person.values():
    print(i)
"""

#2.	Write a program to print all the keys of a dictionary
"""""
d={"a":1,"b":2,"c":3,"d":4}
for i in d.keys():
   print(keys)
   """

#3.	Write a program to print all the values of a dictionary. 
"""""
d={"a":1,"b":2,"c":3,"d":4}
for i in d.values():
   print(value)
   """

#4.	Write a program to add a new key-value pair to an existing dictionary. 
"""""
person ={"name":"John","age":30,"work":"student"}
person["id"]=24

print(person)
    """

#5.	Write a program to update the value of an existing key in a dictionary. 
"""""
person ={"name":"John","age":30,"work":"student"}
person=["name"]= "Ram"
print(person)
"""

#6.	Write a program to check whether a given key exists in a dictionary. 
"""""
person ={"name":"John","age":30,"work":"student"}
if "name" in person:
    print("key Exists")
else:
    print("Key not found")
"""

#7.	Write a program to remove a key-value pair from a dictionary. 
"""""
person ={"name":"John","age":30,"work":"student"}
del person["name"]
print(person)
"""

#8.	Write a program to count the total number of key-value pairs in a dictionary.
"""""
person ={"name":"John","age":30,"work":"student"}
print(len(person))
"""

#9.	Write a program to iterate through a dictionary and print all keys and their corresponding values. 
"""""
person ={"name":"John","age":30,"work":"student"}
for key , value in person.items():
    print(key,":",value)
"""
#10.	Create a dictionary of student names and marks, then find the student with the highest marks.
"""""
students ={"Rahul":80,"Priya":95,"Amit":85}
highest=max(students,key=students.get)
print("Topper:",highest)
print("Marks:",student[highest])
"""

