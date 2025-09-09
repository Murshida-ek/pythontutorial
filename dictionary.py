
# normal dictionary

my_dict={"name":"murshi","age":20,"city":"palakkad"}
print(my_dict)

# using dict

new_dict=dict(name="murshii",age="20",place="pattambi")
print(new_dict)

empty_dict={}
print(empty_dict)

# assceing dictionary items
my_dict={"name":"murshi","age":20,"city":"palakkad"}
print(my_dict["age"])

# using get
my_dict={"name":"murshi","age":20,"city":"palakkad"}
print(my_dict.get("name"))

# changing dictionary items
my_dict={"name":"murshi","age":20,"city":"palakkad"}
my_dict["age"]=21
print(my_dict)
my_dict["place"]="kerala"
print(my_dict)

# adding items to dictionary
my_dict={"name":"murshi","age":20,"city":"palakkad"}
my_dict["place"]="kerala"
print(my_dict)

# removing items from dictionary
#pop
my_dict={"name":"murshi","age":20,"city":"palakkad"}
age=my_dict.pop("age")
print(age)
print(my_dict)

#popitem
my_dict={"name":"murshi","age":20,"city":"palakkad"}
last_item=my_dict.popitem()
print(last_item)
print(my_dict)

#del
my_dict={"name":"murshi","age":20}
del my_dict["name"]
print(my_dict)

#clear
my_dict={"name":"murshi","age":20}
my_dict.clear()
print(my_dict)

#copying dictionary
my_dict={"name":"murshi","age":20}
copy_dict=my_dict.copy()
print(copy_dict)


my_dict={"name":"murshi","age":22}
copy_dict=dict(my_dict)
print(copy_dict)


#nested dictionary

nested_dict={

"prsn1":{"name":"murshh","age":19},
"prsn2":{"name":"murshhiii","age":30}
}
print(nested_dict["prsn2"]["name"])


#dictionary methods

# key()
my_dict={"name":"murshi","age":22}
print(my_dict.keys())

# values
my_dict={"name":"murshi","age":22}
print(my_dict.values())

# items

my_dict={"name":"murshi","age":22}
print(my_dict.items())

# update()
my_dict={"name":"murshi","age":22}
my_dict.update({"name":"fathima","city":"palakkad"})
print(my_dict)

# fromkeys
keys=["name","age","place"]
new=dict.fromkeys(keys,"unknown")
print(new)

# setdefult(key,values)already indenkil add avula
my_dict={"name":"murshi","age":22}
city=my_dict.setdefault("city","newyork")
print(city)
print(my_dict)


















