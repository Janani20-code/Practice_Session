#Operators Practice Session:

#Getting input values
a=int(input("Enter the number a:"))
b=int(input("Enter the number b:"))
c=int(input("Enter the number c:"))

#1.Addition
print("Addition:",a+b)

#2.subtraction
print("Subtraction:",a-b)

#3.Multiplication
print("Multiplication:",a*b)

#4.Division
print("Division:",a/b)

#5.Getting Remainder
print("Remainder:",a%b)

#6.Square of a number
print("Square of a number:",a**2)

#7.Cube of a number
print("Cube of a number:",a**3)

#8.Finding average
average=(a+b+c)/3
print("Average:",average)

#9.Swapping the number 
one=int(input("Enter the number 1:"))
two=int(input("Enter the number 2:"))
d=one
one=two
two=d
print("Swap the value of one:",one)
print("Swap the value of two:",two)

#10.Checking the datatype
print("Checking datatype:",type(a))

#11.Add integer and float
num1=int(input("Enter integer value:"))
num2=float(input("Enter float value:"))
num=num1+num2
print("Adding integer and float:",num,",checking type:",type(num))

#12.Simple Comparison
print("Checking which is greater",a>b)

#13.Check Equal or not
print("Checking equal or not:",a==b)

#14.Find Total and Average marks
mark1=int(input("Enter mark1:"))
mark2=int(input("Enter mark2:"))
mark3=int(input("Enter mark3:"))
mark4=int(input("Enter mark4:"))
mark5=int(input("Enter mark5:"))
total=mark1+mark2+mark3+mark4+mark5
average_marks=total/5
print("Total marks:",total)
print("average:",average_marks)

#15.Convert Hours to Minutes
hours=float(input("Enter the number of hours:"))
minutes=hours*60
print("Converting hours into minutes:",minutes)

#16.Calculate Simple Interest
principal=int(input("Enter the principal:"))
rate=int(input("Enter the rate:"))
time=int(input("Enter the time period:"))
simple_interest=(principal*rate*time)/100
print("simple interest:",simple_interest)

#17.Find Area of a Rectangle
l=int(input("Enter the length:"))
b=int(input("Enter the breadth:"))
area=l*b
print("Area of a rectangle:",area)

#18.Check Positive or Negative
number=float(input("Enter the number:"))
print("Checking if the number is positive:",number>0)
print("Checking if the number is negative:",number<0)
print("checking if the number is zero:",number==0)

#19.Calculate Total Cost
cost_per_item=float(input("Enter the cost of an item:"))
number_of_item=int(input("Enter the number of an item:"))
total_price_of_item=cost_per_item*number_of_item
print("Total cost:",total_price_of_item)

#20.Small Calculator
alpha=int(input("Enter the value of alpha:"))
beta=int(input("Enter the value of beta:"))
print("Add:",alpha+beta)
print("subtraction:",alpha-beta)
print("Multiplication:",alpha*beta)
print("Division:",alpha/beta)
