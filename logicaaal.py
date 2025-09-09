a= int(input("enter the length"))
b=list(map(int,input("enter the elements")))
print(b)

# 1 largest element in array
largest_number = b[0]  
for number in b:
    if number > largest_number:
        largest_number = number
print(largest_number)


# 2 smallest
smallest = b[0]
for number in b:
    if number < smallest:
        smallest = number

print(smallest)


# 3 sum
from functools import reduce

sum = reduce(lambda x, y: x + y, b)
print(sum)


for i in b:
    if i % 2 == 0:
        print(i)


# for i in b:
#     if i % 2 == 1:
#         print(i)



sum1 = 0
for i in b:
    if i % 2 == 0:
        sum1 = sum1 + i
print(sum1)


sum1 = 0
for i in b:
    if i % 2 == 1:
        sum1 = sum1 + i
print(sum1)








# 6 odd and even num count
odd_count = 0
even_count = 0

arr = list(map(int, input("Enter the array: ").split()))

for number in arr:
    if number % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Even num count is:", even_count)
print("Odd num count is:", odd_count)


n = int(input("Enter the num of rows: "))

for i in range(n, 0, -1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()



# n = int(input("enter the no of rows"))

# for i in range(n, 0, -1):
#     for j in range(n - i):
#         print(" ", end="")

#     for k in range(1, i + 1):
#         print(k, end=" ")

#     print()