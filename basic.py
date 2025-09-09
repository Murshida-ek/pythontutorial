# #1. print("hello world")

# # strings
# s="hello,world!"


# #string slicing
# print(s[0:5])


# # skipping characters

# print(s[0:12:2])

# # negative indices

# print(s[-6:-1])

# #reversing string

# print(s[::-1])

# #2. modifying stringss

# #replace method
# new_s=s.replace("world","python")
# print(new_s)

# # uppercase and lowercase

# print(s.upper())
# print(s.lower())

# #3.string concatination

# s1="hello"
# s2="world"
# result=s1 +","+s2
# print(result)

# # using join() method

# words=["python","is","awesome"]
# sentence=" ".join(words)
# print(sentence)


# # 4.format strings

# # using % operator

# name="alice"
# age=25
# formated_string="my name is %s,and my age is %d"%(name,age)
# print(formated_string)

# # using format()method

# name="murshi"
# age=20
# formatted_string="my name is {},my age is{}".format(name,age)
# print(formatted_string)

# keyword argument

# formatted_string="my name is {name},my age is{age}".format(name="murshi",age=19)
# print(formatted_string)

# # using f string

# name="murshi"
# age=20
# v=f"  my name is{name},age is{age}"
# print(v)


# string methods

# print(len(v))
# print(v.strip())
# print(s.split("w"))
# print(s.find("world"))
# print(s.count("l"))
# print(s.startswith("h"))
# print(s.endswith("d!"))


# list in python

my_list=['apple','banana','cherry']
print(my_list)


# accesing list item

my_list=['apple','banana','cherry']
print(my_list[1])

print(my_list[-1])

# range of index

list=[10,30,20,60,75]
print(list[1:3])

# change list items

my_list=['apple','banana','cherry']
my_list[1]='orenge'
print(my_list)


# changing multiple items

list=[10,30,20,60,75]
list[1:3]=['a','b']
print(list)

# adding items to list

# append()
listt=['apple','banana']
listt.append('cherry')
print(listt)

# insert()

listt=['apple','banana']
listt.insert(0,'cherry')
print(listt)

# extend()

listt=['apple','banana']
new_list=['cherry','orenge']
listt.extend(new_list)
print(listt)



# removing items from list

# remove()

my_list=['apple','banana','cherry']
my_list.remove('banana')
print(my_list)

# pop()
my_list=['apple','banana','cherry']
popped=my_list.pop(1)
print(popped)
print(my_list)

# del()

my_list=['apple','banana','cherry']
del my_list[0]
print(my_list)


# clear()
my_list=['apple','banana','cherry']
my_list.clear()
print(my_list)

# list methods

# count()
my_list=[1,2,3,2,2]
print(my_list.count(2))

# index()

my_list=['apple','banana','cherry']
print(my_list.index('banana'))

# reverse()

my_list=['apple','banana','cherry']
my_list.reverse()
print(my_list)

my_list=[3,1,2]
my_list.sort()
print(my_list)


# copy()
org_list=[1,2,3]
copied_list=org_list.copy()
print(copied_list)


# sorting a list
num=[1,4,6,2,3,8,7]
num.sort()#assending order
print(num)

num=[1,4,6,2,3,8,7]
num.sort(reverse=True)#desending order
print(num)

# sorted()

original = [3, 1, 4] 
sorted_list = sorted(original) 
print(sorted_list)  

# copying list

original_list = ['apple', 'banana', 'cherry'] 
copied_list = original_list.copy() #copy method
copied_list = original_list[:] #slicing method


#join lists
#using +
list1 = ['apple', 'banana'] 
list2 = ['cherry', 'orange'] 
combined_list = list1 + list2 
print(combined_list)

#using extend
list1 = ['apple', 'banana'] 
list2 = ['cherry', 'orange'] 
list1.extend(list2) 
print(list1)  