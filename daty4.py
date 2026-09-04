num=[10,20,30,40,50]
print(num[0])

print(num[4])

fruits= ["apple","banana","orange","grapes"]
print(len(fruits))

list=[1,2]
print(list*3)

prog=['c','c++','java','py','js']
print(prog)
print(prog[0],prog[4])

my_list = [10, 3.14, "Hello", True, [1, 2, 3]]
print("List: ",my_list)

tech=['HTML','CSS','Python']
tech.append('Javascript')
print("Technology: ",tech)

even=[2,4,6]
odd=[1,3,5]
even.extend(odd)
print(even)

fruits=['apple','grapes','berries','kiwi']
print(fruits)
fruits.insert(1,'banana')
print("After insert: ",fruits)

colors=['blue','pink','green','blue','orange']
print(colors)
colors.remove('blue')
print(colors)

animals=['lion','tiger','cheetah','fox']
print("Animals: ",animals)
b=animals.pop(2)
print(animals)

foods=['biryani','noodles','pasta']
print("Foods: ",foods)
foods.clear()
print(foods)

num=[12,20,25,30,20,45,50,20,65,20]
print(num)
count_20=num.count(20)
print("Count of 20: ",count_20)
index_30=num.index(30)
print("Index of 30: ",index_30)

scores=[30,15,25,45,20]
print("Scores: ",scores)
scores.sort()
print("After sorting: ",scores)
scores.reverse()
print("After reversing: ",scores)
