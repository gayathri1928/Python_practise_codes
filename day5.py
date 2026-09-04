data=(19,10.5,'Hello',True,28)
print(data[3])

num=(1,2,7,3,4,7,5,6,7)
print(num.count(7))

type=(10,"python",5.5,True,1)
print(type)

single=(5)
print(single)

print(type[0])

print(type[4])

print(type[-1])

num1=(1,2,3,1,4,5)
print(num1.count(1))

num2=(10,20,30,40,50)
print(num2.index(30))

dic={
    "name":"gayu",
    "age":20,
    "city":"pondy"
    }
print(dic)
print(dic.get("country","India"))

dic.update({"profession":"engineer"})
print(dic)

stu={
    "name":"suba",
    "age":30,
    "dep":"CSE"
    }
print(stu)
print(stu.items())

stu.pop("age")
print(stu)

car={
    "brand":"BMW",
    "model":3,
    "year":1975
    }
print(car)
print(car.values())
last_item=car.popitem()
print(last_item)
print(car)

person={
    "name":"tom",
    "grade":"A",
    "sub":"python"
    }
print(person)
print(person.keys())
print(person.clear())
print(person)

prod={
    "prodct":"pen",
    "price":20
    }
print(prod)

prod.update({"stock":100})
print(prod)
print(prod.items())































