#1.Create 5 variables of different data types (int, float, str, bool, list).
#Use print() and type() to display each variable and its type.

a=int(input("Enter the integer value:"))
b=float(input("Enter the float value:"))
c=input("Enter the string:")
d=True
e=["a",1,1.2,True]
print("Integer value:",type(a))
print("Float value:",type(b))
print("String vaue:",type(c))
print("Boolean value:",type(d))
print("List value:",type(e))

#2.Print a sentence using variables:
name=input("Enter your name:")
age=int(input("Enter your age:"))
print(f"my name is {name} and my age is {age}")

#3.Take two numbers as variables and print their sum, difference, product, and quotient.
a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
print("sum:",a+b)
print("difference:",a-b)
print("multiplication:",a*b)
print("division:",a/b)

#4.Print the result of combining string and integer properly using f-string (avoid type error).
name=input("Enter your name:")
age=int(input("Enter your age:"))
print(f"my name is {name} and my age is {age}")

#5.Use arithmetic operators to find:

#1.Square of a number
print("Square of a number:",a**2)

#2.Cube of a number
print("Cube of a number:",a**3)

#3.Finding average
a1=int(input("Enter the first number:"))
b1=int(input("Enter the second number:"))
c1=int(input("Enter the third number:"))
average=(a1+b1+c1)/3
print("Average:",average)

#6.Compare two variables a and b using all relational operators (>, <, ==, !=, >=, <=)
a=int(input("Enter the value:"))
b=int(input("Enter the value:"))
print("relational operators:",a>b)
print("relational operators:",a<b)
print("relational operators:",a>=b)
print("relational operators:",a<=b)
print("relational operators:",a!=b)
print("relational operators:",a==b)

#7.Use logical operators (and, or, not) to check:
if a%2==0 and a>0:
    print("It is even and positive")
else:
    print("It's not even and positive")

#8.to check whether it is negative or zero
if a<0 or a==0:
    print("It is negative or zero")
else:
    print("Its not negative value or zero")

#9.swapping method
# Swap using arithmetic operators
a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))

a = a + b
b = a - b
a = a - b

print("After swapping:")
print("a =", a)
print("b =", b)

#10.To check which greater
# Take two numbers as input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Compare the numbers
if num1 > num2:
    print(f"{num1} is greater than {num2}")
elif num1 < num2:
    print(f"{num2} is greater than {num1}")
else:
    print("Both numbers are equal")

#11.Write a program that checks whether a given number is even or odd.
num=int(input("Enter a number:"))
if num%2==0:
    print("The given number is even")
else:
    print("The given number is odd")

#12.Write a program to find whether a number is positive, negative, or zero (use elif).
# Take a number as input
num = float(input("Enter a number: "))

# Check whether the number is positive, negative, or zero
if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

#13.Take a student’s mark and print:
# Take student's mark as input
mark = float(input("Enter the student's mark: "))

# Determine grade using conditional statements
if mark >= 90:
    print("Grade A")
elif mark >= 75:
    print("Grade B")
elif mark >= 50:
    print("Grade C")
else:
    print("Fail")

#14.Check if a year is a leap year or not.
# Take year as input
year = int(input("Enter a year: "))

# Check leap year condition
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

#15.	Write a program to check whether a person is eligible to vote (age ≥ 18).
# Take age as input
age = int(input("Enter your age: "))

# Check voting eligibility
if age >= 18:
    print("You are eligible to vote.")
else:
    years_left = 18 - age
    print(f"You are not eligible to vote. You need to wait {years_left} more year(s).")

#16.Write a program that takes three numbers and prints which one is the largest.
# Take three numbers as input
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

# Compare and find the largest number
if a >= b and a >= c:
    print(f"{a} is the largest number.")
elif b >= a and b >= c:
    print(f"{b} is the largest number.")
else:
    print(f"{c} is the largest number.")

#17.Using nested if, check:
# Take a number as input
num = int(input("Enter a number: "))

# Outer if to check if the number is positive
if num > 0:
    print("The number is positive.")
    
    # Nested if to check even or odd
    if num % 2 == 0:
        print("It is even.")
    else:
        print("It is odd.")
else:
    print("The number is negative or zero.")

#18.Using nested if, print:
# Take age as input
age = int(input("Enter your age: "))

# Check age category using nested if
if age >= 0:  # Ensuring valid age
    if age < 13:
        print("Child")
    else:
        if age < 20:
            print("Teen")
        else:
            if age < 60:
                print("Adult")
            else:
                print("Senior Citizen")
else:
    print("Invalid age! Age cannot be negative.")

#19.Write a program that checks whether a character is a vowel or consonant.
# Take a single character as input
ch = input("Enter a single alphabet letter: ")

# Check if it's a single alphabetic character
if len(ch) == 1 and ch.isalpha():
    # Convert to lowercase for easy comparison
    ch = ch.lower()

    # Check if vowel or consonant
    if ch in ('a', 'e', 'i', 'o', 'u'):
        print(f"{ch} is a vowel.")
    else:
        print(f"{ch} is a consonant.")
else:
    print("Please enter a valid single alphabet letter.")

#20.Take three subject marks from a student.
# Take three subject marks as input
m1 = float(input("Enter mark for subject 1: "))
m2 = float(input("Enter mark for subject 2: "))
m3 = float(input("Enter mark for subject 3: "))

# Check pass or fail
if m1 >= 40 and m2 >= 40 and m3 >= 40:
    print("Pass")

    # Nested if to check for outstanding performance
    avg = (m1 + m2 + m3) / 3
    if avg >= 90:
        print("Outstanding")
else:
    print("Fail")
