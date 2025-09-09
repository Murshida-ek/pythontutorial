# positional argumentss

def greet(name,age):
    return f"name {name},age {age}"
print(greet("murshi",20))

# default arguments

def greet(name="murshi",msg="good"):
    print(f"{name}")
greet()


# doc string

def add(a,b):
    """this fn add add two no"""
    return a+b
print(add.__doc__)


# lambda function(anonymous fn in python)

add=lambda a,b:a+b

print(add(2,3))


# higherorder function

