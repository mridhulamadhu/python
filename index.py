# # a="mridhula"
# # print(a)
# # age=18
# # print(age)
# # float=3904.35
# # print(float)
# # x=[10,10.5,5]
# # print(x)
# # print(x[0])
# # print(x[2])
# # print(x[-1])
# # x.append(6)
# # print(x)
# # x.insert(1,8)
# # print(x)
# # x.pop()
# # print(x)
# # x.pop(2)
# # print(x)
# # z=("midh","drishh","vara","aami")
# # print(z)
# # m=(1,2,4,5,6,7,8,9)
# # c=list(m)
# # c.append(3)
# # m=tuple(c)
# # print(m)
# #Check if a number is positive or negative.

# num=int(input("enter a number:"))
# if (num>=0):
#     print("positive")
# else:
#     print("negative")

# #Check whether a number is even or odd.

# a=int(input("enter a num:"))
# if (a%2==0):
#     print("Even number")
# else:
#     print("Odd number")   

# #Check if a person is eligible to vote (age ≥ 18).

# vote=int(input("enter age:"))
# if vote<=18:
#     print("Not eligible to vote")
# else:
#     print("eligible to vote")    

# #Check whether a number is divisible by 5.

# b=int(input("enter a num:"))
# if b%5==0:
#     print("Divisible by 5")
# else:
#     print("Not divisible") 

# #Check if a character is a vowel or consonant.
# c=input("enter a character:")
# if c in("aeiou"):
#     print("vowels")
# else:
#     print("consonant")    

# #Write a program to check if a number is zero, positive, or negative.

# d=int(input("Enter a num:"))
# if d<0:
#     print("negative")
# elif d>0:
#     print("Positive")
# else:
#     print("zero")        

# #Check whether a number is a multiple of 3 and 7.

# e=int(input("Enter a num"))
# if e%3==0 and e%7==0:
#     print("num is divisible by both 3 and 7")
# else: 
#     print("not divisible by 3 and 7")   

# #Take a password input and check if it matches a predefined password.

f=input("enter your password:")
if f=="midhu123":
    print("matches")
else:
    print("doesn't match")   

#Check whether a year is a leap year or not.

g=int(input("Enter a year:"))
if (g%4==0 and g%100!=0) or (g%400==0):
    print("It is a leap year")
else:
    print("not a leap year")    

#Simple calculator using if-elif (add, subtract, multiply, divide).
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Choose operation (+, -, *, /): ")

# 2. Use if-elif to perform calculations
if operation == '+':
    print(f"Result: {num1 + num2}")
elif operation == '-':
    print(f"Result: {num1 - num2}")
elif operation == '*':
    print(f"Result: {num1 * num2}")
elif operation == '/':
    # Check for division by zero to avoid errors
    if num2 != 0:
        print(f"Result: {num1 / num2}")
    else:
        print("Error: Cannot divide by zero")
else:
    print("Invalid operator selected.")

#check a number is divisible by 2 and 5  

h=int(input("enter a number:"))
if h%2==0 and h%5==0:
    print("It is divisible by 2 and 5")
else:
    print("Not divisible by 2 and 5")    

#Check whether a number lies between 1 and 100.
    
j=int(input("Enter a number"))
if 1<h<100:
    print("It lies between")
else:
    print("It is not between 1 and 100")    




