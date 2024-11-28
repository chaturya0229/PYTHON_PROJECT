def num(num):
    if num>0 and num%2==0:
        print("positive and even")
    elif num>0 and num%2==1 or num%2!=0:
        print("positive and odd")
    elif num<0 and num%2==0:
        print("negative and even")
    elif num<0 and num%2==1 or num%2!=0:
        print("negative and odd")
    else:
        print("zero")

def xyz():
    x=int(input())
    y=int(input())
    z=int(input())
    if x>y and x>z:
        print("x is greater")
    elif y>x and y>z:
        print("y is greater")
    elif z>x and z>y:
        print("z is greater")
xyz()

def palindrome(n):
    if(n==n[::-1]):
        print("it is a palindrome")
    else:
        print("it is not a palindrome")
n=input("enter the string:-")
print(palindrome(n))

def number(n):
    if n>1:
        for i in range(2,n):
            if i%2==1:
                print("not a prime")
                break
            else:
                print("prime")
    else:
        print("not prime")
number(5)

def hcf(a,b):
    while b:
        a,b=b,a%b
    return a
hcf(36,60)










