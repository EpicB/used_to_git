#! usr/bin/env python3


num1 = int(input("enter a number "))

num2 = int (input("enter the 2nd number "))

ope = input("enter the operator ")

def calcu(n1,n2,ope):
    if ope == "+":
        return n1+n2
    elif ope == "*":
        return n1*n2
    elif ope == "/":
        return n1/n2
    elif ope == "-":
        return n1-n2
    else:
        return "not a valid operator"

print(calcu(num1,num2,ope))
        
