#1
x = "Python is a case sensitive language" #given input string
#a
print(len(x)) #print length
#b
print (x[::-1]) #reverse the string
#c
y = x[10:26] #print specific part of string
print(y)
#d
print(x.replace("a case sensitive","object oriented")) #replace substring
#e
print(x.index("a")) #index of substring
#f
print(x.replace(" ","")) #remove white space

#2
name = "Ashwin Jaiprakash Toppo"
sid = 21105119
department= "ECE"
CGPA = 9.5
print("Hey, %s Here!"%name)
print("My SID is %d"%sid)
print("I am from %s department and my CGPA is %.1f"%(department,CGPA))

#3
a=56
b=10
#a
print(a&b)
#b
print(a|b)
#c
print(a^b)
#d
print(a<<2,b<<2)
#e
print(a>>2,b>>4)

#4
a = int(input("Enter Number a: "))
b = int(input("Enter Number b: "))
c = int(input("Enter Number c: "))
if a>b and a>c:
    print("Greatest of three number is a =",a)
elif b>a and b>c:
    print("Greatest of three number is b =",b)
elif c>a and c>b:
    print("Greatest of three number is c =",c)
else:
    print("All numbers are equal")

#5
string = input("Enter a String ")
if "name" in string:
    print("yes")
else:
    print("No")

#6
a = int(input("Enter side a of triangle "))
b = int(input("Enter side b of triangle "))
c = int(input("Enter side c of triangle "))
if a+b<c or b+c<a or a+c<b:
    print("No")
else:
    print("Yes")