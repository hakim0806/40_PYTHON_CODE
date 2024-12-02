#2.Write a program to sum of two number.
 
firstnum = int(input("enter a number :"))
secnum = int(input("enter a number :"))
add = firstnum + secnum
#print(add)
print(f"sum is = {add}")
## 3.Write a program to calculate the sqrt of number.
def sqr_root(n):
    if n<0:
        print("This number's root is not real")
    else:
        return n**0.5
 
 
mynum = int(input("Enter a number = "))
root_num = sqr_root(mynum)
print(f"The root of{mynum} is = {root_num}")