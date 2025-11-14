#Task: Student Marks Analysis
#You have a list of tuples, where each tuple represents a student and their marks in 3 subjects:
'''students = [
    ("Alice", (85, 90, 78)),
    ("Bob", (75, 80, 82)),
    ("Charlie", (95, 88, 92))
]'''
'''
Your task:
1.	Use nested loops to print each student's marks for each subject in this format:
Alice: Subject 1: 85, Subject 2: 90, Subject 3: 78
Bob: Subject 1: 75, Subject 2: 80, Subject 3: 82
...'''
students = [
    ("Alice", (85, 90, 78)),
    ("Bob", (75, 80, 82)),
    ("Charlie", (95, 88, 92))
]
for student in students:
    name=student[0]
    marks=student[1]
    sub_num=1
    line=f"{name}:"
    for mark in marks:
        line=line+f"subject{sub_num}: {mark},"
    print(line)


'''
2.	Calculate and print each student’s average marks.
'''
students = [
    ("Alice", (85, 90, 78)),
    ("Bob", (75, 80, 82)),
    ("Charlie", (95, 88, 92))
]
for student in students:
    name=student[0]
    marks=student[1]
    total=sum(marks)
    count=len(marks)
    average=total/count
    print(f"{name} average marks is:{round(average,2)}")

'''
3.	Find the highest mark scored by each student using tuple methods.
'''
students = [
    ("Alice", (85, 90, 78)),
    ("Bob", (75, 80, 82)),
    ("Charlie", (95, 88, 92))
]
for student in students:
    name=student[0]
    marks=student[1]
    Highest=max(marks)
    print(f"{name} highest mark is:{Highest}")
'''
4.	Add a new student (“David”, (88, 76, 90)) to the list and repeat steps 1–3.
'''
students = [
    ("Alice", (85, 90, 78)),
    ("Bob", (75, 80, 82)),
    ("Charlie", (95, 88, 92))
]
students.append(("David", (88, 76, 90)))
for student in students:
   name=student[0]
   marks=student[1]
   sub_num=1
   line=f"{name}:"
   for mark in marks:
        line=line+f"subject{sub_num}: {mark},"
   print(line)
   total=sum(marks)
   count=len(marks)
   average=total/count
   print(f"{name} average marks is:{round(average,2)}")
   marks=student[1]
   Highest=max(marks)
   print(f"{name} highest mark is:{Highest}")


#New Task: Grocery Store Inventory
#You have a list of lists, where each inner list represents a category of items in a grocery store and the items in that category:
'''inventory = [
    ["Fruits", ["Apple", "Banana", "Mango"]],
    ["Vegetables", ["Carrot", "Tomato", "Spinach"]],
    ["Dairy", ["Milk", "Cheese", "Yogurt"]]
]
'''

'''
Your tasks:
1.	Use nested loops to print all categories and their items in this format:
Category: Fruits  
 - Apple  
 - Banana  
 - Mango  
Category: Vegetables  
 - Carrot  
 - Tomato  
 - Spinach  
'''
inventory = [
    ["Fruits", ["Apple", "Banana", "Mango"]],
    ["Vegetables", ["Carrot", "Tomato", "Spinach"]],
    ["Dairy", ["Milk", "Cheese", "Yogurt"]]
]
for i in inventory:
    category=i[0]
    items=i[1]
    print(f"{category}:")
    for item in items:
        print(f"-{item}")

'''
2.	Use a list method to add a new item "Orange" to the "Fruits" category.
'''
inventory = [
    ["Fruits", ["Apple", "Banana", "Mango"]],
    ["Vegetables", ["Carrot", "Tomato", "Spinach"]],
    ["Dairy", ["Milk", "Cheese", "Yogurt"]]
]
inventory[0][1].insert(3,"orange")
print(inventory)
'''
3.	Use a list method to remove "Spinach" from "Vegetables".
'''
inventory = [
    ["Fruits", ["Apple", "Banana", "Mango"]],
    ["Vegetables", ["Carrot", "Tomato", "Spinach"]],
    ["Dairy", ["Milk", "Cheese", "Yogurt"]]
]
inventory[1][1].remove("Spinach")
print(inventory)
'''
4.	Count how many items are there in each category using a list method.
'''
inventory = [
    ["Fruits", ["Apple", "Banana", "Mango"]],
    ["Vegetables", ["Carrot", "Tomato", "Spinach"]],
    ["Dairy", ["Milk", "Cheese", "Yogurt"]]
]
for x in inventory:
    categ=x[0]
    items=x[1]
    count=len(items)
    print(f"{categ} has {count} items")
'''
5.	After modifications, print the updated inventory using nested loops.
'''
inventory = [
    ["Fruits", ["Apple", "Banana", "Mango"]],
    ["Vegetables", ["Carrot", "Tomato", "Spinach"]],
    ["Dairy", ["Milk", "Cheese", "Yogurt"]]
]
inventory[0][1].insert(3,"orange")
print(inventory)
inventory[1][1].remove("Spinach")
print(inventory)
for x in inventory:
    category=x[0]
    items=x[1]
    print(f"{category}:")
    for item in items:
        print(f"-{item}")
    count=len(items)
    print(f"{category} has {count} items")

    