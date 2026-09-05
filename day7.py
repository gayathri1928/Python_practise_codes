fruits=["apple", "banana", "cherry"]
uppercase=list(map(str.upper, fruits))
print(uppercase)

num=input("Enter 5 numbers separated by a comma: ")
mapped=tuple(map(int,num.split(",")))
print(mapped)

words=["cat", "tiger", "elephant"]
length=list(map(len,words))
print(length)

nums= ["10","20","30","40","50"]
x=list(map(int,nums))
print(x)

numbers=[2,4,6,8,10]
cubes=list(map(lambda x: x**3, numbers))
print(cubes)

a=int("25")
print(a)
print(type(a))

b=int(5.9)
print(b)
print(type(b))

c=float(7)
print(c)
print(type(c))

d=float("6.5")
print(d)
print(type(d))

e=int("123")
print(e*2)
print(type(e))

f=float(input("Enter a float number: "))
print(int(f))

bool=True
integer_value = int(bool)
float_value = float(bool)
print(integer_value)
print(float_value)

ch="A"
print(ord(ch))
print(type(ch))

g=str(45.67)
print(g)
print(type(g))

txt=("Hello World")
a=txt[:5]
print(a)

txt=("Python Program")
b=txt[3:]
print(b)

txt="Programming"
c=txt[-6:-2]
print(c)

txt="DataScience"
d=txt[:11:2]
print(d)

txt=("Python is fun")
e=txt[::-1]
print(e)

txt=input("Enter a sentence: ")
space=txt.strip()
print(space)

txt1="Good"
txt2="Morning"
txt3=txt1+" "+txt2
print(txt3.upper())

num=42
txt="My favorite number is {} "
print(txt.format(num))














