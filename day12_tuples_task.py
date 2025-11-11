#1. Write a Python program to create a tuple
print("to create a tuple")
t=[1,2,3,4,5]
a=tuple(t)
print("to create a tuple",a)

#2. Python program to Find the size of a Tuple
print("to find the size of a tuple using length")
t=(1,2,3,4,5)
print("length of a tuple:",len(t))
#or
print("to find the size of a tuple using getsizeof")
import sys
t = (1, 2, 3, 4, 5)
print("Memory size of tuple:", sys.getsizeof(t), "bytes")

#3. Python – Sort Tuples
print("sorting tuples")
t=(1,2,3,4,5)
sorted_list=sorted(t)
sorted_tuple=tuple(sorted_list)
print("sorting tuples:",sorted_tuple)

#4. Write a Python program to create a tuple with different data types
t=(1,2.5,'janani',True)
print("different data types:",t)

#5. Write a Python program to unpack a tuple in several variables
t=('jhon','antony','george')
(a,b,c)=t
print("unpacking:",b)

#6. Write a Python program to convert a tuple to a string
t=('h','e','l','l','o')
a="".join(t)
print("convert a tuple to a string",a)

#7. Write a Python program to get the 4th element and 4th element from last of a tuple
t=('h','e','l','l','o')
print("4th element from first:",t[3])
print("4th element from last:",t[-4])

#8. Write a Python program to find the repeated items of a tuple
t=('h','e','l','l','o')
repeated_items=[]
seen_items=[]
for x in t:
    if x in seen_items and x not in repeated_items:
        repeated_items.append(x)
    else:
        seen_items.append(x)
print("to find repeated items:",tuple(repeated_items))

#9. Write a Python program to check whether an element exists within a tuple
print("to check whether an elemeent exist")
t=('h','e','l','l','o')
ele='l'
if ele in t:
    print("yes its exist")
else:
    print("does not exist")

#10. Write a Python program to convert a list to a tuple
t=['h','e','l','l','o']
l=tuple(t)
print("convert list to a tuple:",l)

#11. Write a Python program to remove an item from a tuple
t=('h','e','l','l','o')
temp=list(t)
temp.remove('e')
t=tuple(temp)
print("to remove an item",t)

#12. Write a Python program to slice a tuple
t=('h','e','l','l','o')
a=t[1:4]
print("slicing a tuple:",a)

#13. Write a Python program to find the index of an item of a tuple
t=('h','e','l','l','o')
first_index=t.index('l')
second_index=t.index('l',first_index+1)
print("To find the index of an item:",second_index)

#14. Write a Python program to find the length of a tuple
t=('h','e','l','l','o')
print("length of a tuple:",len(t))

#15. Write a Python program to reverse a tuple
t=('h','e','l','l','o')
rev=t[::-1]
print("to find the reverse:",rev)

#16. Write a Python program convert a given string list to a tuple
t=['h','e','l','l','o']
l=tuple(t)
print("converting string to a list:",l)