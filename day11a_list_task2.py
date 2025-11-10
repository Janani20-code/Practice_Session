#1.	Write a Python program to create a list of 5 numbers and print it.
print("create a list of 5 numbers and print")
a=[1,2,3,4,5]
print(a)

#2.	Write a program to find the length of a list using len().
print("Length of the list")
a=[1,2,3,4,5]
print(len(a))

#3.	Write a program to access elements from a list using positive and negative indexes.
print("accessing an element using positive and negative indexes")
list1=['dog','cat','lion','tiger']
print(list1[1:3])
print(list1[-3:-1])

#4.	Write a program to update the 3rd element of a list.
print("update 3rd element")
list1=['dog','cat','lion','tiger']
list1[2]='fish'
print(list1)

#5.	Write a program to delete an element from a list using del.
print("delete an element")
list1=['dog','cat','lion','tiger']
del list1[0]
print(list1)

#6.	Write a program to append a new element to the list using append().
print("append an element")
list1=['dog','cat','lion','tiger']
list1.append('fish')
print(list1)

#7.	Write a program to insert an element at a specific position using insert().
print("using insert")
list1=['dog','cat','lion','tiger']
list1.insert(2,'fish')
print(list1)

#8.	Write a program to remove an element using remove().
print("removing an element")
list1=['dog','cat','lion','tiger']
list1.remove('cat')
print(list1)

#9.	Write a program to remove the last element using pop().
print("using pop")
list1=['dog','cat','lion','tiger']
print(list1.pop(2))
print(list1)

#10.	Write a program to clear all elements using clear().
print("using clear")
list1=['dog','cat','lion','tiger']
list1.clear()
print(list1)

#11.	Write a program to print all elements of a list using a for loop.
print("to print all elements of a list using a for loop")
list1=['dog','cat','lion','tiger']
for x in list1:
    print(x)

#12.	Write a program to find the sum of all elements using sum().
print("to find sum of all elements")
a=[1,2,3,4,5]
print(sum(a))

#13.	Write a program to find the maximum and minimum values using max() and min().
print("to find the maximum and minimum values")
a=[1,2,3,4,5]
print("max:",max(a))
print("min",min(a))

#14.	Write a program to count how many times an element appears using count().
print("counting the occurrence of an element")
a=['hakuna','matata']
print(a.count('hakuna'))
#15.	Write a program to find the index of a specific element using index().
print("to find the index of a specific element")
a=['raja','rani','policeman','minister','theif','milkman']
print(a.index('theif'))

#16.	Write a program to reverse a list using reverse().
print("to reverse")
a=['raja','rani','policeman','minister','theif','milkman']
a.reverse()
print(a)

#17.	Write a program to sort a list in ascending and descending order using sort().
print("sort a list in ascending and descending order")
a=[1,2,3,4,5]
a.sort()
print("ascending",a)
a.sort(reverse=True)
print("descending:",a)

#18.Write a program to copy one list to another using copy().
print("copy of a element")
a=['raja','rani','policeman','minister','theif','milkman']
b=a.copy()
print(b)

#19.Write a program to print only even numbers from a list.
print("print even numbers")
a=[1,2,3,4,5,6]
for x in a:
    if x%2==0:
        print(x)
    
#20.Write a program to print only odd numbers from a list.
print("odd numbers")
a=[1,2,3,4,5,6]
for x in a:
    if x%2!=0:
        print(x)

#21.Write a program to add two lists using + operator.
print("add two list using + operator")
list1=['cute','cringe','sad','joy']
list2=['violent','silent','psycho']
list3=list1+list2
print("adding element:",list3)

#22.Write a program to repeat list elements using * operator.
print("to repeat list element using * operator")
list1=['cute','cringe','sad','joy']
repeated=list1*2
print(repeated)

#23.Write a program to check if an element exists in a list using in.
a=['a','p','p','l','e']
if 'p' in a:
    print("yes")
else:
    print("no")

#24.Write a program to slice a list (print first 3 and last 3 elements).
print("to slice a list")
a=[1,2,3,4,5]
print("first 3 element:",a[:3])
print("last 3 element:",a[-3:])

#25.Write a program to find the largest 2 numbers in a list.
print("largest twon numbers")
a=[98,97,95,93]
a.sort()
print(a[-1],a[-2])

#26.Write a program to find duplicate elements in a list.
print("finding duplicates")
a=[1,2,3,2,4]
seen_list=[]
dup_list=[]
for x in a:
    if x in seen_list:
        dup_list.append(x)
    else:
        seen_list.append(x)
print("duplicate :",dup_list)

#27.Write a program to remove duplicate elements from a list.
print("removing duplicates")
a=[1,2,3,4,4,2]
seen_list=[]
for x in a:
    if x not in seen_list:
        seen_list.append(x)
print("final:",seen_list)

#28.Write a program to merge two sorted lists into one sorted list.
print("to merge two sorted list into one sorted list")
a=[2,4,6]
b=[1,3,5]
merge=a+b
merge.sort()
print("merged list:",merge)

#29.Write a program to create a list of squares of numbers from 1 to 10 using a loop.
print("to create a list of squares of numbers from 1 to 10 using a loop")
a=[]
for x in range(1,11):
    b=x*x
    a.append(b)
print("square of a number using loop:",a)

#30.Write a program to separate even and odd numbers into two lists.
print("to separate even and odd number")
a=[1,2,3,4,5,6]
even_list=[]
odd_list=[]
for x in a:
    if x%2==0:
        even_list.append(x)
    else:
        odd_list.append(x)
print("even list",even_list)
print("odd list",odd_list)

#31.•  Write a program to create a nested list (list inside a list).
print("to create a nested list")
a=[1,2,3,4]
b=[3,4]
nested=[a,b]
print("nested list",nested)

#32.•  Write a program to access elements from a nested list.
print("to access elements from a nested list")
print("accessing element:",nested[1][0])

#33.•  Write a program to flatten a nested list (convert to one single list).
print("to flatten a nested list")
flat=[]
for sublist in nested:
    for item in sublist:
        flat.append(item)
print("flattened list:",flat)

#34.•  Write a program to find common elements between two lists.
print("to find common elements between two list")
a = [1, 2, 3, 4, 5]
b = [4, 5, 6, 7, 8]
common = list(set(a) & set(b))
print("Common elements:", common)


#35.•  Write a program to find elements present in one list but not in another.
print("to find elements present in one lisst but not in another")
a = [1, 2, 3, 4, 5]
b = [4, 5, 6, 7, 8]
unique = list(set(a) - set(b))
print("Elements in a but not in b:", unique)


#36.•  Write a program to remove all occurrences of a specific element from a list.
print("to remove all occurrences of a specific element from a list")
a=[1,2,3,4,5,1,23,4,5]
element=5
b=[]
for x in a:
    if x!=element:
        b.append(x)
print(b)

#37.•  Write a program to convert a list into a tuple.
print("to convert a list into a tuple")
a=[1,2,3,4,5]
b=tuple(a)
print(b)

#38.•  Write a program to find the average of list elements.
print("to find the average of list elements")

a = [10, 20, 30, 40, 50]

total = sum(a)           # sum of all elements
count = len(a)           # number of elements
average = total / count  # formula

print("Average of list elements:", average)


#39.•  Write a program to count positive, negative, and zero numbers in a list.
print("To count positive, negative, and zero numbers in a list")

a = [10, -5, 0, 7, -3, 0, 8]

positive = 0
negative = 0
zero = 0

for x in a:
    if x > 0:
        positive += 1
    elif x < 0:
        negative += 1
    else:
        zero += 1

print("Positive numbers:", positive)
print("Negative numbers:", negative)
print("Zeros:", zero)

      
