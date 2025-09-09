# if condition

x=10
if x>5:
    print("x is greater than 5")

    # if else condition
    
x=10
if x>15:
    print("x is greater than 5")
else:
        print("x is less than or equal to 5")

        # if elif else statement

x=7
if x>10:
        print("x is greater than 10")
elif x>5:
      print("x is greater than 5 but less than or equal to 10")
     
else:
        print("x is less than or equal to 5")


# nested if 
x=10
y=5
if x>5:
    if y<10:
          print("x is greater than 5 and less than 10")


        #   pythons logical operators
    x=10
    y=5
    if x>5 and y<10:
     print("both are true")

     if x>5 or y>10:
          print("atleast one is true")

          if not x<5:
               print("x is not less than 5")


            #    conditional expression(ternary operator)

          x=15
          result="greater than 10"if x>10 else "10 or less"
    print(result)

    # control flow statements

    # pass statement

    # x=5
    # if x>3:
    #      pass
    for i in range(5):
         if i==3:
              continue
         print(i)

    for i in range(5):
         if i==3:
              break
         print(i)




