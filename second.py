4.Write a program to calculate area of triangular.
 
 
 
def triangle_d(a,b,c):
    s = (a+b+c)/2
    if a**2 == b**2 + c**2:
        return 0.5*b*c
    else:
        return s*(s-a)*(s-b)*(s-c)
 
 
a = int(input("enter larger side of T."))
b = int(input("enter secound side of T."))
c = int(input("enter 3rd side fof T."))
sum = triangle_d(a,b,c)
print(sum)
 
 
 
 
 
 
 
5.Write a program to cheque Odd number & Even number.
 
 
def check_odd_even(n):
    if n%2==0:
        return "is an even number "
    else :
        return "is an odd number"
mynum = int(input("enter a num : "))
check = check_odd_even(mynum)
print(f"answare : {check}")
 
 
 
 
 
 
6.Write a program to cheke prime number.
 
 
def check_p(n):
    if n<=1:
        return False
    else:
        for i in range(2,int(n**0.5)+1):
            if n%i == 0:
                return False
            return True
 
mynum = int(input("enter a num : "))
check = check_p(mynum)
 
if check_p(mynum):
    print(f"{mynum} is a prime num ")
else:
    print(f"{mynum} is not a prime num ")
 
 
 
 
 
 
 
 
7.Write a program to Print Fibonacci series.
 
def fibo(x):
    first = 0
    second = 1
    print(f"{first} {second}",end=" ")
    for i in range(3,x+1):
        fibo = first+second
        first = second
        second = fibo
        print(fibo,end=" ")
 
 
n = int(input("Enter a range : "))
if n<=0:
    print("Please enter a positive integer")
else:
    print(f"Fibonacci series till {n}th ")
    fibo(n)
 
 
 
 
 
8.Write a program to calculate factorial.
 
def factorial(x):
    fact = 1
    for i in range(1,x+1):
        fact*=i
    return fact
 
n = int(input("Enter a positive number : "))
ans = factorial(n)
print(f"Factorial of {n} = {ans}")
 
 
 
 
 
 
9.Write a program to swap two number.
 
 
def mySwap(x,y):
    x,y = y,x
    return x,y
 
a = int(input("Enter the first number, A = "))
b = int(input("Enter the second number, B = "))
print(f"Before Swap A = {a} & B = {b}")
 
Result = mySwap(a,b)
 
print(f"After Swap = {Result}")
 
 
 
 
 
10.Write a program to cheke palindrome of number.
 
 
def is_palindrome(s):
 
    s = s.replace(" ", "").lower()
 
    return s == s[::-1]
 
 
Given = input("Enter a string = ")
 
if is_palindrome(Given):
    print(f"{Given} is a Palindrome")
 
else:
    print(f"{Given} is not a Palindrome")
 
 
 
 
"""    
###N_palindrome
 
    def is_palindrome(s):
 
        s = str(s)
 
        return s == s[::-1]
 
 
    Given = input("Enter a valid number = ")
 
    if is_palindrome(Given):
        print(f"{Given} is a Palindrome")
 
    else:
        print(f"{Given} is not a Palindrome")
 
"""
 