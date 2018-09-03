#!/bin/python3
n= int(input())
if n<1 or n>100:
    n=int(input())
    exit()
x=n%2
if x!=0:
    print("Weird")
elif n==2 or n==4:
    print("Not Weird")
elif n>6 and n<=20:
    print("Weird")
elif n>20:
    print("Not weird")
