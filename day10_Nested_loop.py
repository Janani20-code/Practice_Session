#1.To print right triangle
row=5
for i in range(1,row+1):
    print("*" * i)
'''
*
**
***
****
*****
'''
#2.to print left triangle
row=5
for i in range(1,row+1):
    space=row-i
    print(" "*space+"*"*i)
'''
    *
   **
  ***
 ****
*****
'''
#3.to print square
n=4
for i in range(1,n+1):
    for j in range(1,n+1):
        print("*",end=" ")
    print()
#or
'''
* * * *
* * * *
* * * *
* * * *
'''
#4.to print 8
for i in range(7):
    for j in range(5):
        if i in[0,3,6]:
            print("*",end="")
        elif j==0 or j==4:
            print("*",end="")
        else:
            print(" ",end="")
    print()
'''
*****
*   *
*   *
*****
*   *
*   *
*****
'''
#5.to print hollow square
for i in range(4):
    for j in range(4):
        if i in[0,3]:
            print("*",end="")
        elif j==0 or j==3:
            print("*",end="")
        else:
            print(" ",end="")
    print()
'''
****
*  *
*  *
****
'''
#6.to print hollow right triangle
n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        if i==5:
            print("*",end="")
        elif j==1 or j==i:
            print("*",end="")
        else:
            print(" ",end="")
    print()

'''
*
**
* *
*  *
*****
'''
#7.to print inverse right triangle
n=4
for i in range(n+1,0,-1):
    print("*" * i)

'''
*****
****
***
**
*
'''

#8.to print inverse left triangle
n = 5
for i in range(n, 0, -1):
    space = n - i
    print(" " * space + "*" * i)
'''
*****
 ****
  ***
   **
    *
'''
#9.to print the pattern as shown below
#a
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end="")
    print()
'''
1
12
123
1234
12345
'''
#b
n = 5
for i in range(0, n):
    for j in range(1, n - i + 1):
        print(j, end="")
    print()
'''
12345
1234
123
12
1
1
'''
#c
for i in range(1,6):
    for j in range(1,i+1):
        if j==1 or j==i:
            print(j,end="")
        elif i==5:
            print(j,end="")
        else:
            print(" ",end="")
    print()
'''
1
12
1 3
1  4
12345
'''
#d
l=['A','B','C','D','E']
for i in range(len(l)):
    for j in range(0,i+1):
        print(l[j],end="")
    print()
'''
A
AB
ABC
ABCD
ABCDE
'''
#e
l=['A','B','C','D','E','F']
for i in range(len(l)):
    for j in range(0,i+1):
        print(l[i],end="")
    print()
'''
A
BB
CCC
DDDD
EEEEE
FFFFFF
'''
#f
l=['A','B','C','D','E']
for i in range(len(l)):
    for j in range(0,i+1):
        print(l[i],end="")
    print()
'''
A
BB
CCC
DDDD
EEEEE
'''
#g
l=['A','B','C','D','E','F']
for i in range(len(l)):
    for j in range(0,i+1):
        print(l[i],end="")
    print()
'''
A
BB
CCC
DDDD
EEEEE
FFFFFF
'''
#h capital letters
n=5
ch=65
for i in range(1,n+1):
    for j in range(1,i+1):
        print(chr(ch),end="")
        ch=ch+1
    print()
'''
A
BC
DEF
GHIJ
KLMNO
'''
#small letters
n=5
ch=97
for i in range(1,n+1):
    for j in range(1,i+1):
        print(chr(ch),end="")
        ch=ch+1
    print()
'''
a
bc
def
ghij
klmno
'''


