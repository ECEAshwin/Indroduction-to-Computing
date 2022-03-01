#1
def TowerOfHanoi(n , col1, last_col, aux_col):
    if n == 0:
        return
    TowerOfHanoi(n-1,col1, aux_col, last_col)
    print("Move disk",n,"from column",col1,"to column",last_col)
    TowerOfHanoi(n-1, aux_col, last_col,col1)

n = 3
TowerOfHanoi(n,"A","B","C")
#2
print("Question 2")
n = int(input("Enter Number of Rows : "))
print("Using recursions")
def pas_tri(n, m=n):
    if n == 0:
        return

    pas_tri(n-1, m)
    print('  '*(m-n), end='')
    x = 1
    for i in range(1, n+1):
        print(x, end='   ')
        x= x * (n - i) // i
    print()


pas_tri(n)

print("Using Loops")
for row in range(1, n+1):
    print('  '*(n - row), end='')
    z = 1
    for c in range(1,row+1):
        print(z, end='   ')
        z = z * (row - c) // c
    print()
#3
print("Question 3")
a = int(input("Enter number a : "))
b = int(input("Enter number b : "))
q = a/b
r = a%b
L = [q,r]
#a
def division():
    q = a/b
    r = a%b
    print("Quotient =",q,"\nRemainder:",r)
division()
print("(a)",callable(division))
#b
if a!= 0 and b!= 0 and q!= 0 and r!= 0:
    print("(b) All values are non zero")
else:
    print("(b) All values are not non zero")
#c
L.extend([4,5,6])
print("(c)",L)
filtered = filter(lambda n: n > 4, L)
print("    Filtered", list(filtered))
#d
S = set(L)
#e
S = frozenset(S)
#f
M = max(S)
print("(f) Max Value =",M,"and Hash Value =",str(hash(M)))
#4
print("Question 4")
class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
        print("Student created")
    def __del__(self):
        print("Student deleted")
# storing data in the Student
s1 = Student("Rupesh", 1)
s2 = Student("Firoz", 2)
s3 = Student("Piyush", 3)
del s1
del s2
del s3
#5
print("Question 5")
class Employees:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    # defining a function to print the details of all employees
    def record(self):
        print("Employee Name : ", self.name.title())
        print("Employee Salary : ", self.salary)
        print("\n")
e1 = Employees("Mehak", 40000)
e2 = Employees("Ashok", 50000)
e3 = Employees("Viren", 60000)
print("Record of all employees\n")
e1.record()
e2.record()
e3.record()
#a
print("(a)")
print("Updated record of Mehak:")
e1.Salary = 70000
e1.record()
#b
print("(b)")
del e3
print("Record of Vivek deleted")
#6
print("Question 6")
word1 = input("Enter first word : ")
word2 = input("Enter second word : ")
word1 = sorted(word1)
word2 = sorted(word2)
if word1 == word2:
    C = input("Is the word meaningful(Y/N) : ")
    if C.upper()=="Y":
        print("Friendship is True")
    elif C.upper()=="N":
        print("Friendship is Fake")
else:
    print("Friendship is Fake")