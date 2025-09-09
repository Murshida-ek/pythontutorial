try:
    n=input("enter a name of file")
    with open(n,'r')as abc:
        a=abc.read()
        print(a)
except FileNotFoundError:
   print("file not found")
   