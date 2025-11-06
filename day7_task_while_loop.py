#1.print numbers from 10 to 1
count=10
while count>0:
    print(count)
    count=count-1
    
#2.Find the sum of even digits
number=int(input("sum of even digits:"))
sum=0
while number>0:
    last_digit=number%10
    if last_digit%2==0:
        sum=last_digit+sum
    number=number//10
print(sum)

#3.Count how many digits are in a number
number=int(input("how many digits are in a number:"))
count=0
while number>0:
    count=count+1
    number=number//10
print(count)

#4.Check if a number is palindrome:
original_value=int(input("Enter the number to check palindrome:"))
working_copy=original_value
reverse_value=0
while working_copy>0:
    last_digit=working_copy%10
    reverse_value = (reverse_value * 10) + last_digit
    working_copy=working_copy//10
if reverse_value==original_value:
    print("Its palindrome")
else:
    print("Its not palindrome")

#5.Find the reverse of a number
original_value=int(input("Reverse of a number:"))
working_value=original_value
reverse_value=0
while working_value>0:
    last_digit=working_value%10
    reverse_value=(reverse_value*10)+last_digit
    working_value=working_value//10
print("Reverse value:",reverse_value)

#6.Fibonacci series upto 100
a=0
b=1
print("First Number:",a)
print("Second Number:",b)
next_number=a+b
while next_number<=100:
    next_number=a+b
    if next_number<=100:
        print(next_number)
    a=b
    b=next_number    

#7.compute the power of a number manually(without ** or pow())
base=int(input("Enter the base number:"))
exponent=int(input("Enter the exponent number:"))
result=1
count=0
while count<exponent:
    result=base*result
    count=count+1
print(result)

#8.keep dividing a number by 2 until it beccomes less than 1 and count how many divisions
num=int(input("Enter the number to divide:"))
count=0
while num>=1:
    num=num/2
    count=count+1
print(count)

#9.print the digits of  a number from last to first one per line
number=int(input("Enter the number to get last to first:"))
while number>0:
    last_digit=number%10
    print(last_digit)
    number=number//10

#10.#compute the sum of squares of digits of a numbers
n=int(input("Enter the number to find sum of squares:"))
total=0
while n>0:
    last_digit=n%10
    total+=last_digit*last_digit
    n=n//10
print(total)