#list top

#1.Create a list of 5 of your favorite fruits.
print("favorite fruits")
fruits=['mango','strawberry','banana','orange','pommegranate']
print("favourite fruits:",fruits)

#2.Add a new fruit to the list using a list method.
fruits=['mango','strawberry','banana','orange','pommegranate']
new_fruit=fruits.append('cherry')
print("adding fruit:",new_fruit)

#3.Remove one fruit from the list.
fruits=['mango','strawberry','banana','orange','pommegranate']
fruits.remove('orange')
print("remove fruits:",fruits)

#4.Print the number of fruits in your list.
fruits=['mango','strawberry','banana','orange','pommegranate']
print("counting fruits:",len(fruits))

#5.Print all the fruits one by one using a for loop.
print("printing fruits one by one")
fruits=['mango','strawberry','banana','orange','pommegranate']
for i in fruits:
    print(i)

#6.Reverse the list and print it.
fruits=['mango','strawberry','banana','orange','pommegranate']
fruits.reverse()
print("reverse fruit:",fruits)

#7.Sort the list alphabetically and print it.
fruits=['mango','strawberry','banana','orange','pommegranate']
fruits.sort()
print("sort_fruits:",fruits)

#8.Check if a particular fruit (like "Apple") is in the list.
fruits=['mango','strawberry','banana','orange','apple']
if 'apple' in fruits:
    print("yes it exist")
else:
    print("not exist")

#Tuple
#1.	Create a tuple of 5 of your favorite colors.
colors=('green','blue','red','white','black')
print("creating colors using tuple",colors)

#2.	Print the first and last color from the tuple.
colors=('green','blue','red','white','black')
print("first element:",colors[0])
print("last element:",colors[-1])

#3.	Find the length of the tuple.
colors=('green','blue','red','white','black')
print("length of a tuple:",len(colors))

#4.	Count how many times a particular color appears in the tuple.
colors=('green','blue','red','red','white','black')
counted=colors.count('red')
print("counting colors",counted)
#5.	Print all colors one by one using a for loop.
colors=('green','blue','red','white','black')
for i in colors:
    print(i)

#6.	Combine two tuples of colors and print the result.
colors=('green','blue','red','white','black')
colors1=('yellow','brown')
colors2=colors+colors1
print("adding tuples:",colors2)

#7.	Find the maximum and minimum value from a tuple of numbers.
num=(1,2,3,4,5)
print("maximum number:",max(num))
print("minimum number:",min(num))

#8.	Try to change a value in the tuple and observe what happens.
colors=('green','blue','red','white','black')
colors.append('yellow')
print("change a value in the tuple:",colors)
