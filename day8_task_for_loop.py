#1.print all numbers between 1 and 100 that are divisible by 6 but not by 9
for i in range(1,101):
    if i%6==0 and i%9!=0:
        print("numbers between 1 and 100:",i)

#2.Find sum of all odd numbers from 1 to 50
count=0
for i in range(1,51):
    if i%2!=0:
        count+=i
print("sum of odd numbers:",count)

#3.count how many numbers between 1 and 200 are divisible by both 4 and 6
count=0
for i in range(1,201):
    if i%4==0 and i%6==0:
        count=count+1
print("number divisible by 4 and 6:",count)

#4.print the multiplication table of a given number n from 1 to 10
n=int(input("Enter number to multiply:"))
for i in range(1,11):
    print(f"{i}*{n}={i*n}")

#5.Find the factoriall of a given number n
n=int(input("factorial:"))
fact=1
for i in range(1,n+1):
    fact=i*fact
print("factorial:",fact)

#6.Find all prime numbers between 1 and 50(using flag to check)
for i in range(2,51):
    flag=0
    for j in range(2,i):
        if i%j==0:
            flag=1
            break
    if flag==0:
        print("prime numbers:",i)

#7.calculate the sum of the digits of a number using arithmeticc only
n = int(input("Sum of digits: "))
total = 0

for digit in str(n):
    total += int(digit)

print("sum of digits:",total)


#or 


n = int(input("Sum of digits: "))
total = 0
num_digits = len(str(n))  # count digits

for i in range(num_digits):
    last_digit = n % 10
    total += last_digit
    n //= 10

print("sum of digits 2:",total)


#8.count how many numbers between 1 and 500 are perfect cubes
for i in range(1,501):
    cube_root=round(i**(1/3))
    if cube_root**3==i:
        print("cube root:",i)

#9.print the reverse of a number using arithmetic only
n = int(input("Reverse of a number: "))
rev = 0
num_digits = len(str(n))   # count how many digits the number has

for i in range(num_digits):
    last_digit = n % 10
    rev = rev * 10 + last_digit
    n //= 10

print("reverse of a number:",rev)



#10.print numbers from 1 to 100 but skip numbers ending with digit 5
for i in range(1,101):
    last_digit=i%10
    if last_digit!=5:
        print("skip numbers if it is 5:",i)