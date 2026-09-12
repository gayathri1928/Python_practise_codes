'''import random 
numbers=[1,2,3,4,5]
print(random.choice(numbers))

print(random.randint(1,5))

print(random.uniform(0,1))

names = ["Alli", "Baby", "Charls"]
print(random.choice(names))

print(random.sample(range(2,22),4))

numbers = [11, 22, 33, 44, 55]
random.shuffle(numbers)
print(numbers) 

print("--------------------------------------------------------------------------------")

a=int(input("Enter a number:"))
b=int(input("Enter a number:"))
if a>b:
    print("A is greater than B")
else:
    print("B is greater than A")

age=int(input("Enter a number:"))
if age>18:
    print("Your eligible to vote")
else:
    print("Your not eligible to vote")

z=int(input("Enter a number:"))
if z>=1:
    print("Number is positive")
elif z<=-1:
    print("Number is negative")
else:
    print("Number is zero")

x=int(input("Enter a number:"))
if x%4==0 and x%100!=0 or x%400==0:
    print("It is a leap year")
else:
    print("It is not a leap year")

y=int(input("Enter a number:"))
if y%2==0:
    print("Number is even")
else:
    print("Number is odd")

m1 = float(input("Enter Mark 1: "))
m2 = float(input("Enter Mark 2: "))
m3 = float(input("Enter Mark 3: "))
m4 = float(input("Enter Mark 4: "))
m5 = float(input("Enter Mark 5: "))
total = m1 + m2 + m3 + m4 + m5
print("Total:" ,total)
average = total / 5
print("Average:" ,average)
if average > 90:
    print("A")
elif average >= 70 and average <= 80:
    print("B")
elif average >= 60 and average < 70:
    print("C")
else:
    print("Fail")

text=input("Enter a string: ")
reverse_text=text[::-1]
if text==reverse_text:
    print("It is a Palindrome")
else:
    print("It is not a Palindrome")

x=int(input("Enter a number:"))
y=int(input("Enter a number:"))
z=int(input("Enter a number:"))
if x>y and x>z:
    print("largest number is:", x)
elif y>x and y>z:
    print("latrgest number is:", y)
else:
    print("largest number is:", z)
    
c=int(input("Enter a number:"))
if z>0:
    print("Number is positive")
elif z<0:
    print("Number is negative")
elif z==0:
    print("Number is zero")
else:
    print("Enter an integer")

age = int(input("Enter your age: "))
if age >= 0 and age <= 12:
    print("You are a child")
elif age >= 13 and age <= 19:
    print("You are a teenager")
elif age >= 20 and age <= 59:
    print("You are an adult")
elif age >= 60:
    print("You are a senior")
else:
    print("Please enter a valid age.")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
if num1 >= num2 and num1 >= num3:
    print("The largest number is:", num1)
elif num2 >= num1 and num2 >= num3:
    print("The largest number is:", num2)
else:
    print("The largest number is:", num3)

x=int(input("Enter a number:"))
if x%4==0 and x%100!=0 or x%400==0:
     print(x, "is a leap year.")
else:
    print(x, "is not a leap year.")

score = float(input("Enter the student's score: "))
if score >= 90 and score <= 100:
    print("Grade: A")
elif score >= 80 and score <= 89:
    print("Grade: B")
elif score >= 70 and score <= 79:
    print("Grade: C")
elif score >= 60 and score <= 69:
    print("Grade: D")
elif score >= 0 and score < 60:
    print("Grade: Fail")
else:
    print("Invalid score! Please enter a number between 0 and 100.")

username = input("Enter username: ")
password = input("Enter password: ")
if username != "admin":
    print("Invalid Username")
elif password != "1234":
    print("Invalid Password")
else:
    print("Access Granted")

celsius = float(input("Enter temperature in Celsius: "))
if celsius < 15:
    print("Cold")
elif celsius >= 15 and celsius <= 30:
    print("Warm")
else:
    print("Hot")'''


















































































    
