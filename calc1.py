def add(num1,num2):
    S = num1 + num2
    return S

def multiply(num1,num2):
    P = num1 * num2
    return P

def subtract(num1,num2):
    R = num1 - num2
    return R

def divide(dividend,divisor):
    if divisor>dividend:
        l=[0,0]
    else:
        Q = dividend//divisor
        Re = dividend-(Q*divisor)
        l=[Q,Re]
    return l

def exponent(num1,num2):
    R = num1**num2
    return R


print("Welcome to Calculator")
print("Enter 1 to add, 2 to subtract, 3 to multiply, 4 to divide and 5 for exponentiaion.")
choice = int(input("Enter your choice : "))
n1 = int(input("Enter first number (dividend, in case of  division) : "))
n2 = int(input("Enter second number (divisor, in case of division) : "))
if choice==1:
    R=add(n1,n2)
    print("The result is :",R)
elif choice==2:
    R=subtract(n1,n2)
    print("The result is :",R)
elif choice==3:
    R=multiply(n1,n2)
    print("The result is :",R)
elif choice==4:
    R=divide(n1,n2)
    print("The result is :",R)
elif choice==5:
    R=exponent(n1,n2)
    print("The result is :",R)
else:
    print("Wrong Choice, Sorry")
