# a="mridhula"
# print(a)
# age=18
# print(age)
# float=3904.35
# print(float)
# x=[10,10.5,5]
# print(x)
# print(x[0])
# print(x[2])
# print(x[-1])
# x.append(6)
# print(x)
# x.insert(1,8)
# print(x)
# x.pop()
# print(x)
# x.pop(2)
# print(x)
# z=("midh","drishh","vara","aami")
# print(z)
# m=(1,2,4,5,6,7,8,9)
# c=list(m)
# c.append(3)
# m=tuple(c)
# print(m)
#Check if a number is positive or negative.

num=int(input("enter a number:"))
if (num>=0):
    print("positive")
else:
    print("negative")

#Check whether a number is even or odd.

a=int(input("enter a num:"))
if (a%2==0):
    print("Even number")
else:
    print("Odd number")   

#Check if a person is eligible to vote (age ≥ 18).

vote=int(input("enter age:"))
if vote<=18:
    print("Not eligible to vote")
else:
    print("eligible to vote")    

#Check whether a number is divisible by 5.

b=int(input("enter a num:"))
if b%5==0:
    print("Divisible by 5")
else:
    print("Not divisible")  

