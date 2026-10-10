#palindrone number x=121

x=121
temp = x
rev = 0
while x > 0:
    digit = x % 10
    rev = rev * 10 + digit
    x = x // 10
if temp == rev:
    print("The number is a palindrome.")
else:
    print("The number is not a palindrome.")