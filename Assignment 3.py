#1
print ("Question 1")
string = input('Enter your String : ')
n = string.strip() #remove spaces from left and right
L = []
if " " in n:
  m = n.split()      #converts string into list
  for i in m:
     if i not in L:   
      L.append(i)     #adds elements to end of list
      x = m.count(i)
      print(i,"occurred",x,"time")
else:
    for i in n:
        if i not in L:
         L.append(i)   
         x = n.count(i)
         print(i,"occurred",x,"time")
#2
print("Question 2")
D = int(input("Day -")) #Day
M = int(input("Month -")) #Month
Y = int(input("Year -")) #Year
if Y%4 == 0 and Y>=1800 and Y<=2025 and M == 2 and D>=1 and D<=29:
        if D == 29:
            D = 1
            M = M+1
            print("Next Date is: %02d/%02d/%d"%(D,M,Y))
        else:
            D = D+1
            print("Next Date is: %02d/%02d/%d"%(D,M,Y))
elif M == 1 or M == 3 or M == 5 or M == 7 or M == 8 or M == 10 or M == 12 and D>=1 and D<=31 and Y>=1800 and Y<=2025:
    if M == 12 and D == 31:
            Y = Y+1
            D = 1
            M = 1
            print("Next Date is: %02d/%02d/%d"%(D,M,Y))
    elif D == 31:
            D = 1
            M = M+1
            print("Next Date is: %02d/%02d/%d"%(D,M,Y))
    else:
            D = D+1
            print("Next Date is: %02d/%02d/%d"%(D,M,Y))
elif M == 4 or M == 6 or M == 9 or M == 11 and D>=1 and D<=30 and Y>=1800 and Y<=2025:
    if   D == 30:
            D = 1
            M = M+1
            print("Next Date is: %02d/%02d/%d"%(D,M,Y))
    else:
            D = D+1
            print("Next Date is: %02d/%02d/%d"%(D,M,Y))
elif M == 2 and D>=1 and D<=28 and Y>=1800 and Y<=2025:
    if   D == 28:
            D = 1
            M = M+1
            print("Next Date is: %02d/%02d/%d"%(D,M,Y))
    else:
            D = D+1
            print("Next Date is: %02d/%02d/%d"%(D,M,Y))
else:
    print("Date is Invalid")
#3
print("Question 3")
a = int(input("Enter first number :"))
b = int(input("Enter second number :"))
c = int(input("Enter third number :"))
t1 = (a,a*a)
t2 = (b,b*b)
t3 = (c,c*c)
L = [t1,t2,t3]
print(L)
#4
print("Question 4")
grade = int(input("Enter Grade Point :"))
if grade == 10:
    print("Your Grade is 'A+' and Outstanding.")
elif grade == 9:
    print("Your Grade is 'A' and Excellent Performance.")
elif grade == 8:
    print("Your Grade is 'B+' and Very Good.")
elif grade == 7:
    print("Your Grade is 'B' and Good.")
elif grade == 6:
    print("Your Grade is 'C+' and Average.")
elif grade == 5:
    print("Your Grade is 'C' and Below Average.")
elif grade == 4:
    print("Your Grade is 'D' and Poor.")
else:
    print("Error: Enter Valid Grade Point")
#5
print("Question 5")
s = input("Enter String: ")
x = ""
z = (len(s)+1)/2
z = int(z)
print(s)
for i in range(1,z):
    print (x,s[:-2*i])
    y = " "
    x = x+y
#6
print("Question 6")
dic = {}
cont = "Y"
while cont == "Y":
       cont = ""
       name = input("Enter Name : ")
       SID = int(input("Enter SID : "))
       cont = input("Continue(Y/N) : ")
       dic.update({SID:name})
       if cont == "N":
           break   
#a
print("Student details : ",dic)
#b
print("Sorted Names : ",sorted(dic.values()))
#c
print("Soarted SID : ",sorted(dic.keys()))
#d
stu = int(input("Enter SID : "))
print("Name of student : ",dic.get(stu))
#7
print ("Question 7")
n = int(input("Enter the number of sequence : "))
a = 0
b = 1
if n == 1:
       print(a)
elif n > 2:
        print(a)
        print(b)
        for i in range(2,n):
            c = a+b
            print(c)
            a = b
            b = c
else:
    print("Invalid Input")
#8
print("Question 8")
Set1 = {1,2,3,4,5}
Set2 = {2,4,6,8}
Set3 = {1,5,9,13,17}
#a
Set4 = Set1.symmetric_difference(Set2)
print ("a:",Set4)
#b
Set5 = Set3.symmetric_difference(Set4)
print ("b:",Set5)
#c
U1 = Set1.union(Set2)
isc1 = U1.intersection(Set3)
U2 = Set1.union(Set3)
isc2 = U2.intersection(Set2)
U3 = Set2.union(Set3)
isc3 = U3.intersection(Set1)
Set6 = isc1.union(isc2,isc3)
print("c:",Set6)
#d
t = {1}
a = 1
while a<=10:
    t.add(a)
    a += 1

Set7 = t.difference(Set1)
print("d:",Set7)
#e
U = Set1.union(Set2,Set3)
Set8 = t.difference(U)
print("e:",Set8)