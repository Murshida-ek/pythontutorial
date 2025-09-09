my_tuple=(1,2,3,'python',4.5)

# single item tuple
single_tuple=(5,)
print(type(single_tuple))

my_tuple=('apple','banana','cherry')
print(my_tuple[1])
print(my_tuple[-1])

# slicing tuple
my_tuple=(1,2,3,4,5,6)
print(my_tuple[1:4])

# updating tuple
# reassingning
my_tuple=(1,2,3)
my_tuple=(4,5,6)
print(my_tuple)

# convert tuple to list

my_tuple=('apple','banana','cherry')
temp_list=list(my_tuple)
temp_list[1]='orenge'
my_tuple=tuple(temp_list)
print(my_tuple)

# unpacking tuple
my_tuple=('apple','banana','cherry')
(fruit1,fruit2,fruit3)=my_tuple
print(fruit1)
print(fruit2)
print(fruit3)


# using asterisk
my_tuple=(1,2,3,4,5)
(first,*middle,last)=my_tuple
print(first)
print(middle)
print(last)

# joining tuples
tuple1=(1,2,3)
tuple2=(4,5,6)
join=tuple1+tuple2
print(join)

# tuple methods

# count()

my_tuple=(1,2,3,4,5)
print(my_tuple.count(2))

# index()

my_tuple=(1,2,3,4,5)
print(my_tuple.index(2))

# deleting tuple
my_tuple=(1,2,3,4,5)
del my_tuple
print(my_tuple)
