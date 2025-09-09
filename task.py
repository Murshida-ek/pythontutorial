# for i in range(1, 6):
#     print("*" * i)




# for i in range(5, 0, -1):
#     print("*" * i)



# for i in range(1, 5):
#     print(" " * (4 - i) + "*" * (2 * i - 1))



# n = 5
# for i in range(n):
#     print(' ' * (n - i - 1) + '*' * (2 * i + 1))
# for i in range(n - 2, -1, -1):
#     print(' ' * (n - i - 1) + '*' * (2 * i + 1))





# n = int(input("enter the no of rows"))

# for i in range(n, 0, -1):
#     for j in range(n - i):
#         print(" ", end="")

#     for k in range(1, i + 1):
#         print(k, end=" ")

#     print()



a= int(input("enter the length"))
b=list(map(int,input("enter the elements")))
print(b)

    # 3 sum
from functools import reduce

sum = reduce(lambda x, y: x + y, b)
print(sum)


for i in b:
    if i % 2 == 0:
        print(i)

for i in b:
    if i % 2 == 1:
        print(i)