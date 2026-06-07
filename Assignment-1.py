#********************ASSIGNMENT-1*************************************

"""" 
1.	Write a program to check whether a number is positive or negative

num = int(input("enter any Number..:"))
if num > 0 :
    print("Number is Positive")
else:
    print("Number is Negative")
     """
""""
2.	Write a program to check whether a number is even or odd. 

num = int(input("enter any Number..:"))
if num % 2 == 0:
    print("Number is Even")
else:
    print("Number is Odd")
    """

3#.	Write a program to find the greater number between two numbers
"""""
num1 = int(input("enter number1..:"))
num2 = int(input("enter number2..:"))
if num1 > num2:
    print("Num1 is greater")
else :
    print("Num2 is greater")"""

#4.	Write a program to check whether a person is eligible to vote (age ≥ 18). 
"""""
age = int(input("Enter the age of person..:"))
if age >= 18:
    print("The person is eligible to vote")
else:
    print("The person is not eligible to vote")"""

#5.	Write a program to check whether a number is divisible by 5.
"""""
Num = int(input("Enter any Number...:"))
if Num % 5 == 0:
    print("Number is divisible")
else :
    print("number is not divisible") """

#6.	Write a program to check whether a given year is a leap year or not. 
"""""
Year = int(input("Enter the year..:"))
if Year % 4 == 0:
    print("This year is Leap Year")
else:
    print("This year is not Leap Year")"""

#7.	Write a program to check whether a character is a vowel or a consonant
""""
ch = input("Enter any character..:")
if ch == 'A' or 'a':
    print("This character is vowel")
elif ch == 'E' or'e':
    print("vowel")
elif ch == 'I' or 'i':
    print("vowel")
elif ch == 'O'or'o':
    print("vowel")
elif ch == 'u'or'U':
    print("vowel")
else:
    print("consonant")"""

#8.	Write a program to find the largest among three numbers
"""""
Num1 = int(input("enter first number..:"))
Num2 = int(input("Enter second number..:"))
Num3 = int(input("Enter third number..:"))
if Num1 > Num2:
    if Num1 > Num3:
        print("Num1 is greater")
    else:
        print("Num3 is greater")
else:
    if Num2 > Num3:
        print("Num2 is greater")
    else:
        print("Num3 is greater")"""

#9.	Write a program to assign grades based on marks: 
#	90 and above → A 
#	75 to 89 → B 
#	50 to 74 → C 
#	Below 50 → Fail 
"""""
Marks = int(input("Enter your marks..:"))
if Marks >= 90:
    print("Grade A")
elif Marks > 75 or Marks<= 89:
    print("Grade B")
elif Marks >50 or Marks<= 74:
    print("Grade C")
else:
    print("Fail")"""

#10. Write a program to check whether a number is within the range of 1 to 100.
"""""
Num = int(input("Enter any number..:"))
if Num<=1 or Num<=100:
    print("The number is in range")
else :
    print("Number is not in the range")"""

#****************************************************************************************************

#1.	Write a program to print numbers from 1 to 10 using a for loop. 
"""""
for i in range(1,11):
    print(i)"""

#2.	Write a program to print numbers from 10 to 1 in reverse order
"""""
for i in range(10,0,-1):
    print(i)"""

#3.	Write a program to print all even numbers between 1 and 20
"""""
for i in range(1,21):
    if i % 2 == 0:
        print(i)"""

#4.	Write a program to print all odd numbers between 1 and 20. 
"""""
for i in range(1,21):
    if i % 2 != 0:
        print(i)"""

#5.	Write a program to find the sum of numbers from 1 to 100. 
"""""
sum=0
for i in range(1,101):
    sum = sum+i

print("Sum=",sum)"""

#6.	Write a program to print the multiplication table of a given number
"""""
num=int(input("enter a number for table :"))
for i in range(num,(num*10)+1,num):
    print(i)"""

#7.	Write a program using nested for loops to print pattern
"""""
for i in range(5):
    for j in range(5):
        print("*", end=" ")
        
    print()"""

#8.	Write a program to print each character of a string using a for loop
"""""
ch ="sanskruthi"
for i in range(0,len(ch)):
    print(ch[i])"""

#9.	Write a program to find the factorial of a given number using a for loop
"""""
Num= int(input("Enter any Number..:"))
fact=1
for i in range(1,Num):
    fact= fact*i
print("factorial",fact)"""

#10.	Write a program to print the following pattern:
"""""
for i in range(1,6):
    for j in range(1,i+1):
        print("*",end=" ")
    print()"""

#***************************************************************************************************

#1.Write a program to print numbers from 1 to 10 using a while loop
"""""
a=1
while a<=10:
    print(a)
    a=a+1 """

#2.Write a program to print numbers from 10 to 1 in reverse order using a while loop
"""""
a=10
while(a>0):
    print(a)
    a=a-1"""

#3.Write a program to print all even numbers between 1 and 20 using a while loop.
"""""
a=1
while(a<21):
    if a % 2 ==0:
        print(a)
    a=a+1"""

#4.Write a program to print all odd numbers between 1 and 20 using a while loop.
"""""
a=1
while a<21:
    if a % 2 !=0:
        print(a)
    a=a+1
"""

#5.Write a program to find the sum of numbers from 1 to 100 using a while loop
"""""
a=1
while a < 101:
    print(a)
    a=a+1"""

#6.Write a program to print the multiplication table of a given number using a while loop
"""""
num= int(input("enter any number..:"))
a=1
while a<11:
    print(num*a)
    a=a+1"""

#7.Write a program to count the number of digits in a given number using a while loop
""""'"
number= int(input("enter any number..:"))
count=0
while number!=0:
    number=number//10
    count=count+1
print("the number of digits in the given number is:", count)"""

#8.Write a program to reverse a given number using a while loop.




#9.Write a program to find the factorial of a given number using a while loop.
"""""
num = int(input("Enter any number: "))
fact = 1

while num >= 1:
    fact = fact * num
    num = num - 1

print("The factorial of the given number is:", fact)"""

#10.Write a program to keep asking the user for a password until the correct password is entered
"""""
correct_password = "password123"
password = ""
while password != correct_password:
    password = input("Enter the password: ")
print("Password correct!")
"""


