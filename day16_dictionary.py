
#1. Check whether a given key abeady exists in a dictionary.
student={"name":"janani","age":24,"course":"python"}
key="age"
if key in student:
    print("the key is exist")
else:
    print("not exist")

#2. herate over dictionaries using for loops
student={"name":"janani","age":24,"course":"python"}
for key,value in student.items():
    print(key,":",value)


#3. Print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are squre of keys Sample Dictionary
#1:12:43:9, 4: 16, 5:25. 6: 36, 7:49,864,981, 10: 100, 11: 121, 12: 144, 13: 169, 14:196, 15:225)
numbers={}
for i in range(1,16):
    numbers[i]=i*i
print(numbers)

#4. Merge two Python dictionaries.
dict1 = {1: "a", 2: "b"}
dict2 = {3: "c", 4: "d"}
merge_dict=dict1|dict2
print(merge_dict)

#5.Sum all the items values) in a dictionary. Sum(dict) values())
marks = {"Math": 80, "Science": 70, "English": 75}
adding=sum(marks.values())
print(adding)

#6 Multiply all the items in a dictionary
dict1={"a":5,"b":3,"c":2}
result=1
for value in dict1.values():
    result=value*result
print(result)

#7.Remove a key from a dictionary.
dict1={"a":5,"b":3,"c":2}
dict1.pop("a")
print(dict1)

#8. Python program to find the size of a Dictionary
dict1={"a":5,"b":3,"c":2}
print(len(dict1))

#9 initialize dictionary with default values
keys=["name","age","course"]
default_dict=dict.fromkeys(keys,None)
print(default_dict)


#10. Create a new dictionary by extracting the keys from a dictionary
student={"name":"janani","age":24,"course":"python"}
keys_to_extract=["name"]
new_dict={k: student[k] for k in keys_to_extract}
print(new_dict)

#11. Find the type of the Datatype
print(type(student))