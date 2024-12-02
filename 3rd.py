11.Write a program to find largest number among three number.
 
def find_largest(a,b,c):
    if a>=b and a>=c:
        return a
    elif b>=a and b>=c:
        return b
    else:
        return c
 
 
num1 = float(input("Enter the Frst number: = "))
num2 = float(input("Enter the second number: = "))
num3 = float(input("Enter the third number: = "))
 
largest = find_largest(num1,num2,num3)
 
print(f"The largest number {num1},{num2} and {num3} is {largest}")
 
 
 
 
 
 
12.Write a program to find the gcd.
 
def mygcd(x,y):
    while y:
        x,y = y, x%y
    return x
 
num1 = int(input("Enter the Frst number:  "))
num2 = int(input("Enter the second number:  "))
 
result = mygcd(num1,num2)
 
print(f"GCD of {num1} and {num2} is = {result} ")
 
 
 
 
13.Write a program to find the lcm.
 
def mygcd(x,y):
    while y:
        x,y = y, x%y
    return x
 
def mylcd(x,y):
    return abs(x*y) // mygcd(x,y)
 
num1 = int(input("Enter the Frst number:  "))
num2 = int(input("Enter the second number:  "))
 
result = mylcd(num1,num2)
 
print(f"GCD of {num1} and {num2} is = {result} ")
 
 
 
 
14.Write a program to convert Celsius to Fahrenheit.
 
 
def cel_to_fahren(c):
    return (c*9/5)+32
 
 
Celsius = float(input("Enter temperature in Celsius: "))
 
fahrenheit = cel_to_fahren(Celsius)
 
 
print(f"{Celsius} C is equal to {fahrenheit} F")
 
 
 
 
 
15.Write a program to generate random number.
 
import random
def randfloat(x,y):
    return random.uniform(x,y)   ##int->randint
 
 
a = float(input("Enter the lower bound: "))
b = float(input("Enter the upper bound: "))
 
myRandom = randfloat(a,b)
 
 
print(f"The random float number between {a} and {b} is = {myRandom}")
 
 
 
 
 
16.Write a program to find the sum of n natural numbers.
 
 
 
"""
def sum_ofNaturalNum(n):
    return n*(n+1)//2
 
 
n = int(input("Enter a positive integer: "))
 
if n>0:
    total_sum = sum_ofNaturalNum(n)
    print(f"The sum of the first{n} natural number is : {total_sum}")
 
else:
    print("Please enter a positive integer")
 
"""
 
 
 
def sum_ofNaturalNum(start, n):
    sum = 0
    for i in range(start, n+1):
        sum += i
        return sum
 
    return n*(n+1)//2
 
start = int(input("Enter the starting value: "))
n = int(input("Enter a ending value: "))
 
if start >0 and start <= n:
    total_sum = sum_ofNaturalNum(start, n)
    print(f"The sum of the natural number from {start} to {n} is : {total_sum}")
 
else:
    print("Please enter valid values where start is less than or equal to n.")
 
 
 
 
 
 
17.Write a program to count the vowel.
 
 
def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
 
    for char in s:
        if char in vowels:
            count += 1
    return count
 
 
 
user_input = input("Enter a string: ")
 
vowel_count = count_vowels(user_input)
 
 
 
print(f"The number of vowels in the given string is : {vowel_count}")
 
 
 
 
 
18.Write a program to remove punctuation from a string.
 
import string
 
 
def remove_punctuatuions(s):
    translator = s.maketrans('','',string.punctuation)
    return s.translate(translator)
 
user_input = input("Enter a string: ")
cleaned_string = remove_punctuatuions(user_input)
 
print(f"String without punctuation: {cleaned_string}")
 
 
 
 
 
 
19. Write a program to ACII value of character.
 
char = input("Enter a character: ")
ascii_value = ord(char)
print(f"The ASCII value of '{char}' is {ascii_value}")
 
 
 
 
 
20.Write a program to reverse a number.
 
def reverse(num):
    s = str(num)
    s = s[::-1]
    return int(s)
 
n = int(input("enter a number : "))
print(f"{n} in Reversed :{reverse(n)}")