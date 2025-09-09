# using built in fn

# my_array=[12,27,54]
# reversed_array=[int(str(num)[::-1]) for num in my_array]
# print(*reversed_array)


# without built in fn

def reversed_digit(arr):
    reversed_arr=[]
    for num in arr:
        reversed_num = 0
        while num>0:
            reversed_num=reversed_num*10+num%10
            num//=10
        reversed_arr.append(reversed_num)
    return reversed_arr


arr=[12,27,54]
result=reversed_digit(arr)
print("original arr:",arr)
print("reversed arr:",result)
