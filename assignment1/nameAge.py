name=input("Enter your name: ")
age=input("Enter your age: ")
height=input("Enter your height: ")
print(f"name{name},age: {age} , height:{height}")

num=1
num2=1.5
num3=1+7j
print(type(num))
print(type(num2))
print(type(num3))

a=5
b=10
print(f"initially a is {a} and b is {b}")
temp=a
a=b
b=temp
print(f"after swap a is {a} b is {b}")

a=int(input("Enter num1: "))
b=int(input("Enter num2: "))
print(f"Sum of {a} and {b} is: {a+b}")
print(f"Difference of {a} and {b} is: {a-b}")
print(f"Product of {a} and {b} is: {a*b}")
print(f"Division of {a} and {b} is: {a/b}")
print(f"Int Division of {a} and {b} is: {a//b}")
print(f"mod of {a} and {b} is: {a%b}")
print(f"exponent of {a} and {b} is: {a**b}")
