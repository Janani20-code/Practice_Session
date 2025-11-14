#Question:

#1 Write a Python program to find and print all prime numbers between 1 and 100 using a for loop.
'''
At the end, print the total count of prime numbers.
Hint:
•	A number is prime if it’s divisible only by 1 and itself.
•	Use a loop inside a loop (but keep it mainly in the for logic).
Example Output:
Prime numbers between 1 and 100 are:
2 3 5 7 11 13 17 ... 97  
Total primes = 25
______
'''
prime_count=0
for i in range(1, 101):
    flag = 0
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                flag = 1
                break
        if flag == 0:
            print("prime numbers from 1 to 100 are:", i)
            prime_count += 1

print("count of prime number:",prime_count)



'''
Question:

2 Write a program to print the following pyramid pattern using nested for loops:
        1
      1 2 1
    1 2 3 2 1
  1 2 3 4 3 2 1
1 2 3 4 5 4 3 2 1
Hint:
•	You’ll need three parts:
o	One loop for rows.
o	One inner loop for spaces.
o	One inner loop for numbers (increasing then decreasing).
________________________________________
'''
for i in range(1, 6):
    # print spaces
    for s in range(5 - i):
        print("  ", end="")

    # print increasing numbers
    for num in range(1, i + 1):
        print(num, end=" ")

    # print decreasing numbers
    for num in range(i - 1, 0, -1):
        print(num, end=" ")

    print()



'''
Question:

3 Write a Python program to calculate the electricity bill based on the following conditions:
Units Consumed	Rate per Unit
0 – 100	₹1.5
101 – 200	₹2.5
201 – 300	₹4.0
Above 300	₹5.0
If total bill is above ₹1000 → Add 10% surcharge.
Example Input / Output:
Enter units consumed: 350  
Total Bill: ₹1575.0
Diamond Pattern
Question:
'''
units = int(input("Enter the units: "))

if units <= 100:
    bills = units * 1.5

elif units <= 200:
    bills = (100 * 1.5) + (units - 100) * 2.5

elif units <= 300:
    bills = (100 * 1.5) + (100 * 2.5) + (units - 200) * 4

else:
    bills = (100 * 1.5) + (100 * 2.5) + (100 * 4) + (units - 300) * 5

if bills > 1000:
    bills = bills * 1.10

print("Total bill:", bills)


'''
4 Write a program to print this pattern using nested for loops:
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
Hint:
•	Use one loop for the upper half and another for the lower half.
•	Handle spaces carefully.
'''
n = 5  # This is the middle row (number of rows in upper half)

# Upper half of the diamond
for i in range(1, n+1):
    # Print spaces
    for j in range(n-i):
        print(" ", end="")
    # Print stars (2*i - 1)
    for j in range(2*i - 1):
        print("*", end="")
    print()  # Move to next line

# Lower half of the diamond
for i in range(n-1, 0, -1):
    # Print spaces
    for j in range(n-i):
        print(" ", end="")
    # Print stars (2*i - 1)
    for j in range(2*i - 1):
        print("*", end="")
    print()  # Move to next line




'''
Multiplication Table Grid
Question:

5 Write a Python program using nested for loops to print the multiplication table (1–10) in grid format.
Expected Output:
1  2  3  4  5  6  7  8  9  10  
2  4  6  8 10 12 14 16 18  20  
...
10 20 30 40 50 60 70 80 90 100
________________________________________
'''
# Multiplication Table (1-10)
for i in range(1, 11):  # Outer loop for rows
    for j in range(1, 11):  # Inner loop for columns
        # Print product with spacing
        print(f"{i*j:4}", end="")  # :4 ensures each number takes 4 spaces
    print()  # Move to next row


'''
Question:

6 Write a Python program to print Pascal’s Triangle up to n rows.
Example Output (n=5):
      1
     1 1
    1 2 1
   1 3 3 1
  1 4 6 4 1
'''
n = 5  # Number of rows

for i in range(n):
    # Print leading spaces
    print(" " * (n - i - 1), end="")

    val = 1
    for j in range(i + 1):
        print(val, end=" ")
        val = val * (i - j) // (j + 1)
    print()  # Move to next row
