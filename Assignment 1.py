#1
a = int(input("Enter first Number:"))
b = int(input("Enter second Number:"))
c = int(input("Enter Third Number:"))
print("Average = ",(a+b+c)/3)
#2
Tax_Rate = 20/100
SD = 10000 #Standard Deduction
DD = 3000  #Dependent Deduction
GI = int(input("Enter Your Gross Income: ")) #Gross Income
nd = int(input("Enter no of Dependents: "))  #no of dependents
TI = GI-SD-(DD*nd)
print("Your Taxable Income: ",TI)
print("Tax = ",TI*Tax_Rate)
#3
SID = int(input('SID : '))
Name = input('Name : ')
Gender = input('Gender : ')
Course_Name = input('Course Name : ')
CGPA = float(input('CGPA : '))
Student_list = [SID, Name, Gender, Course_Name, CGPA]
print(Student_list)
#4
n1 = int(input("Marks of first student: "))
n2 = int(input("Marks of second student: "))
n3 = int(input("Marks of Third student: "))
n4 = int(input("Marks of fourth student: "))
n5 = int(input("Marks of fifth student: "))
num_list = [n1,n2,n3,n4,n5] #List of Marks
num_list.sort()
print(num_list)
#5
#a
color = ['Red','Green','White','Black','Pink','Yellow']
color.pop(3) #Removes 4th element
print('color',color)
#b
color = ['Red','Green','White','Black','Pink','Yellow']
color[3]=color[4]='Purple'
print('color',color)