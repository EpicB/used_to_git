#! /usr/bin/env  python3
from math import *
name = "potato"
print("hello")
print("potato")
print(name.index("o",2))
print(name.replace("o","a"))
number = 55
numbers = [50,5,3,5]
number2 = str(55)

print(number2 + " yes")

print(abs(-5))
print(min(numbers))
print(max(1,2,5))
print(round(3.62))
print(bin(12))
names = input("tell me your name you fat fuck : ")
print(names + " nice name faggot")

a_list = ["hello","yes","no"]

print(a_list[len(a_list)-1:])

print(a_list[:-1])
b_list = list(("hello",2,False))

print(b_list)

tuble = (1,2,3,4)

print("the tuble is : ")
print(tuble)

def myfunc(*names):
    print(names[0]);
myfunc("yes_sir")


