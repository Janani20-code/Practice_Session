#creating set variable
students={"Alice", "Bob", "Charlie","Bob"}
print(students)

#now adding new student in the set
students.add("David")
print(students)

#creating another set variable to update
new_students={"Divya","Ravi"}
students.update(new_students)
print(students)

#removing elements from the students
students.remove("David")
print(students)
students.add("David")
print(students)

#removing elements from the students using discard
students.discard("Bob")
print(students)

#removing elements from the students using pop
students.pop()
print(students)

#removing elements from the students using clear
students.clear()
print(students)

#joining the sets
A = {10, 20, 30, 40}
B = {30, 40, 50, 60}
union_set=A.union(B)
print(union_set)

#using intersection
A = {10, 20, 30, 40}
B = {30, 40, 50, 60}
intersection_set=A.intersection(B)
print(intersection_set)

#using difference
A = {10, 20, 30, 40}
B = {30, 40, 50, 60}
difference_set=A.difference(B)
print(difference_set)

#symmetric difference
A = {10, 20, 30, 40}
B = {30, 40, 50, 60}
symmetric_diff=A.symmetric_difference(B)
print(symmetric_diff)


