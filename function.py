def greet(name, age):
    return f"hi iam {name},{age} years old"
print(greet("murshida",20))

# task

def greet(num1,num2):
    return num1*num2
print(greet(3,6)+10)


# map()
num=[1,2,3,4,5,6]
squared=map(lambda x:x**2,num)
print(list(squared))


# filter()
num=[1,2,3,4,5,6]
squared=filter(lambda x:x%2==0,num)
print(list(squared))


# reduce()
from functools import reduce
num=[1,2,3,4,5,6]
squared=reduce(lambda x,y:x+y,num)
print(squared)





