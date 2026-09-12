num1=8
num2=2
Total=num1+num2
print("The addition is:",Total)

a=int(input("Enter num1: "))
b=int(input("Enter num2: "))
prod=a*b
print("Product is:",prod)

a=int(input("Enter num1: "))
b=int(input("Enter num2: "))
print("Addition is:",a+b)
print("Subtraction is:",a-b)
print("Multiplication is:",a*b)
print("Division is:",a/b)

value1 = int(input("Enter value1: "))
value2 = 234
if value1 > value2:
    print(value1, "number is greater than", value2)
elif value2 > value1:
    print(value2, "number is greater than", value1)
else:
    print("Both numbers are equal")
if value1 == value2:
    print("Both values are equal")
else:
    print("Both values are not equal")

number1=9,3,4,56,9
number2=9,3,4,1,3
print(9 in number1)
print("9 is available in the list thanks")

name="Top Skilled"
username="topskilled@21"
print(type(name),type(username))

name = ["Top", "skilled"]
username = ["topskilled@21"]
print(name)
print(username)

name = ["Top", "skilled"]
username = ["topskilled@21"]
print(name)
print(username)
    
number=int(input("Enter a number:"))
if(number%2==0):
    print(True)
else:
    print(False)

a=int(input("Enter num1: "))
b=int(input("Enter num2: "))
print("Remainder is:",a%b)

P = float(input("Enter principal amount: "))
r = float(input("Enter rate of interest: "))
t = float(input("Enter time: "))
A = P * (1 + r / 100) ** t
CI = A - P
print("Amount is :", A)
print("Compound Interest is :", CI)

number1 = float(input("Enter first number: "))
number2 = float(input("Enter second number: "))
total = number1 + number2
print("Sum is :", round(total, 2))

number=int(input("Enter a number:"))
if number % 5 == 0 and number > 50:
    print(True)
else:
    print(False)

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if (a > b and a < c) or (a > c and a < b):
    second = a
elif (b > a and b < c) or (b > c and b < a):
    second = b
else:
    second = c
print("Second largest number is :", second)

x = list(map(int, input("Enter numbers: ").split(",")))
if all(i > 0 for i in x):
    print(True)
else:
    print(False)

list1 = [10, 20, 30]
list2 = [10, 20, 30, 40, 50]
if all(i in list2 for i in list1):
    print(True)
else:
    print(False)

a = [10, 20, 30]
b = a
print(a is b)
print(a == b)

text = input("Enter a string: ")
if text.isupper():
    print(True)
else:
    print(False)
 































