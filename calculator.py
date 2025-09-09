a=int(input("enter a no"))
operator=input("enter the operator(+,-,*,/)")
b=int(input("enter a no"))


if operator=="+":
    print(a+b)
elif operator=="-":
    print(a-b)
elif operator=="/":
   
   
    result="a/b" if b!=0 else"not dividable by zero"
    print(result)
   
    
elif operator=="*":
    print(a*b)
else:
    print("error")
