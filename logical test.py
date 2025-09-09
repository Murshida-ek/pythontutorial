n = 5
for i in range(n):
    print(' ' * (n - i - 1) + '*' * (2 * i + 1))
for i in range(n - 2, -1, -1):
    print(' ' * (n - i - 1) + '*' * (2 * i + 1))







def palindrome(s):
    i = 0
    j = len(s) - 1
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True
s = input("Enter a string: ")
if palindrome(s):
    print("Palindrome")
else:
    print("Not Palindrome")




