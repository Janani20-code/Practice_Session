#1.To check whether a number is positive, negative, or zero.
a=int(input("Enter the value:"))
if a>0:
    print("The number is positive")
elif a<0:
    print("The number is negative")
else:
    print("The number is zero")

#2.To check whether a number is even or odd.
num=int(input("Enter a number:"))
if num%2==0:
    print("The given number is even")
else:
    print("The given number is odd")

#3.To check if a person is eligible to vote (age ≥ 18).
age=int(input("Enter the age:"))
if age>=18:
    print("The person is eligible to vote")
else:
    print("The person should wait until he/she turn 18 to vote")

#4.To check if a student passed or failed based on marks.
marks=int(input("Enter the marks:"))
if marks>=35:
    print("The given mark is pass")
else:
    print("The given mark is fail")

#5.To find the largest of two numbers
a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
if a>b:
    print("A is greater than b")
else:
    print("B is greater than a")

#6.To display grade (A, B, C, D, Fail) based on marks.
marks=int(input("Enter the marks:"))
if marks>80:
    print("A grade")
elif marks>60 & marks <= 80:
    print("B grade")
elif marks>40 & marks <=60:
    print("c grade")
elif marks>35:
    print("D grade")
else:
    print("Fail")

#7.To print the day name based on a number (1–7).
day_value=int(input("Enter the day number:"))
if day_value==1:
    print("Sunday")
elif day_value==2:
    print("Monday")
elif day_value==3:
    print("Tuesday")
elif day_value==4:
    print("Wednesday")
elif day_value==5:
    print("Thursday")
elif day_value==6:
    print("Friday")
elif day_value==7:
    print("Saturday")
else:
    print("The given number is not valid")

#8.To check whether a character is an alphabet, digit, or special character.  
ch=input("Enter a character")
if len(ch)!=1:
    print("Give exactly one character")
else:
    if ch.isalpha():
        print("The given character is alphabetic")
    elif ch.isdigit():
        print("The given character is digit")
    else:
        print("The given character is special character") 

#9.To find the largest among three numbers.
num1=int(input("Enter the number 1:"))
num2=int(input("Enter the number 2:"))
num3=int(input("Enter the number 3:"))
if num1>num2:
    print("num1 is greater")
elif num2>num3:
    print("num2 is greater")
else:
    print("num3 is greater")

#10. To display a message based on temperature (e.g., Hot, Warm, Cool, Cold). 
temp=int(input("Enter the temperature:"))
if temp>100:
    print("Its hot")
elif temp>80 & temp<=100:
    print("Its Warm")
elif temp>30 & temp<=60:
    print("Its cool")
else:
    print("Cold")

#11.to check whether a number is positive and even using nested if.
number=int(input("Enter the number:"))
if number>0 and number%2==0:
    print("The number is positive and even")
else:
    print("The given number is odd or negative")

#12.to simulate a login system that checks username and password using nested if.
username="Janani"
password="Dataanalyst2025"
user=input("Enter the username:")
pass_word=input("Enter the password:")
if user==username:
    print("please enter your password")
    if pass_word==password:
        print("successfully login")
    else:
        ("incorrect password")
else:
    ("incorrect username")

#13.to check if a person is eligible for a job:
#	Must be above 18
#	Must have experience
age=int(input("Enter your age:"))
experience=int(input("Enter your experience year:"))
if age>18 and experience>0:
    print("The person is eligible for the job")
else:
    print("Better luck next time")

#14.to check if a year is leap year or not using if-else.
year=int(input("Enter the year:"))
if year%4==0:
    print("The given year is leap year")
else:
    print("The given year is not leap year")

#15.to check whether a student qualifies for a scholarship:
#	Marks ≥ 85
#	Attendance ≥ 90%
marks=int(input("Enter the marks:"))
attendance=int(input("Enter the attendance percentage:"))
if marks>=85 & attendance>=90:
    print("The student qualifies for a scholarship")
else:
    print("The student is not eligible for scholarship")