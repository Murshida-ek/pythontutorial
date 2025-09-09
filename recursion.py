def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n* factorial(n-1)
print(factorial(6))


def tail_factorial(n,accumulator=1):
    if n==0 or n==1:
        return accumulator
    else:
        return tail_factorial(n-1,accumulator*n)
print(tail_factorial(10))


def fibonnocci(n):
    if n==0: 
        return 0
    elif n==1:
        return 1    
    else:
        return(n-1)+fibonnocci(n-2)
print(fibonnocci(5))



def sum_list(a):
    if not a:
        return 0
    else:
        return a[0]+sum_list(a[1:])
print(sum_list([1,2,3,4,5]))


# factorial

def factorial(n):
    result=1
    for i in range(1,6):
        result*=i
    return result
print(factorial(5))

     
   
        
    

