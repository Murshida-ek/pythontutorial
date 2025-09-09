# type error 
# # print("hi"
# print("hello"+5)


# value error
# int("abc")

# key error
# a={1,2,3}
# a.remove(6)
# print(a)


# # index error
# a=[1,2,3]
# print(a[5])

# file not found error
# file=open("sampl.txt","r")
# content=file.read()
# print(content)
# file.close()


# try Except
# n=int(input("enter a no:"))
# try:
#    result=10/n
# except ZeroDivisionError:
#    print("zero devision is not possible")
# else:
#    print("the result is",result)
# finally:
#    print("thankyou")



# raise error
# x=10
# a=x<10
# raise ValueError("nottt acceptable")



class heheheherror(Exception):
    pass
def check_num(num):
    if num<0:
     raise heheheherror("neg not acceptble")
    
# try:
#        check_num(num)
check_num(-10)
# except heheheherror as e:
#  print(e)






