#1.Print numbers from 1 to 20
for i in range(1,21):
    print("printing numbers form 1 to 20:",i)

#2.print all even numbers from 2 to 50
for i in range(2,51,2):
    print("printing even numbers from 2 to 50",i)

#3.print all odd numbers from 1 to 50
for i in range(1,51,2):
    print("printing odd numbers from 1 to 50",i)

#4.print the square of numbers from 1 to 15
for i in range(1,16):
    print("print the square of numbers from 1 to 15",i*i)

#5.print the cube of numbers from 1 to 10
for i in range(1,10):
    print("print the cube of numbers from 1 to 10:",i*i*i)

#6.print numbers from 10 down to 1 in reverse order
for i in range(10,0,-1):
    print("print the numbers from 10 down to 1 in reverse order:",i)

#7.print the multiplication table of 5
for i in range(1,11):
    print(f"{i} * 5 = {i*5}")

#8.print all characters of a string one by one
name="janani"
for i in name:
    print("printing all characters of a string one by one:",i)

#9.print number divisible by 3 between 1 and 30
for i in range(1,31):
   if i%3==0:
       print("number divisible by 3:",i)