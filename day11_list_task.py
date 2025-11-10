#1.Reverse a given list in Python	 
print("reverse a given list")
l = [100, 200, 300, 400, 500]	 
l.reverse()
print(l)

#2.Concatenate two lists
print("concatenate two list")	 
list1 = ["Hello ", "Madam"]	 
list2 = ["Dear", "Sir"]	 
concat=list1+list2
print(concat)

#3. Remove empty strings from the list of strings
print("remove empty string")	 
list1 = ["Pen", "", "Pencil", "Eraser", "", "Scale"]
a=[]
for x in list1:
    if x !="":
        a.append(x)
print(a)   
         
#4.Write a Python program to convert a string to a list.
print("convert a string into a list")	 
a="janani"
b=list(a)
print(b)

#5.Check if a list contains an element	
print("checking if it contains a specified element")	  
list1= [1,2,3,'a','b','c']
element="a"
if element in list1:
    print("yes!")
else:
    print("not present")

#6. Remove all elements from a list
print("remove all elements from a list")	 	 
list1= [1,2,3,'a','b','c']
list1.clear()
print(list1)

#7. Count the occurrence of a specific object in a list
print("count the occurence of a specific object")	 
pets = ['dog','cat','fish','fish','cat']
print(pets.count('cat'))

#8.Return the length of a list
print("length of a list")	 	
pets = ['dog','cat','fish','fish','cat']
print(len(pets))

#9. Insert a value at a specific index in an existing list
print("inserting a value")	 
pets = ['dog','cat','fish','fish','cat']
pets.insert(3,'lion')
print(pets)

#10. Write a Python program to clone or copy a list.
print("copy of a list")	 
pets = ['dog','cat','fish','fish','cat']
pets1=pets.copy()
print(pets1)

#11. Write a Python program to extend a list without append.
print("using extend")	 
pets = ['dog','cat','fish','fish','cat']
pets1=['lion','tiger']
pets.extend(pets1)
print(pets)

#12. Remove duplicates from a list	 
print("removing duplicates")	 
li = [3, 2, 2, 1, 1, 1]	 
li=list(set(li))
print(li)

#13.Find the index of the 1st matching element
print("finding 1st matching of the index")	 
pets = ['dog','cat','fish','fish','cat']
a=pets.index('cat')
print(a)

#14.check if an element is not in a list
print("checking if it an element not in a list")	  
list1= [1,2,3,'a','b','c']
element="a"
if element not in list1:
    print("not present")
else:
    print("present")
