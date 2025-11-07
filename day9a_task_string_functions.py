#23.replace the word "java" with "python" in a sentencce using replace()
word="I am a java developer"
print("replacing:",word.replace("java","python"))

#24.remove extra spaces from both sides of string using strip()
a=" Data Analyst "
print("Removing space from both sides:",a.strip())

#25.capitalize the first letter of a sentence using capitalize()
a="janani"
print("Capitalize first letter:",a.capitalize())

#26.split a sentence into words using split()
a="All is Well"
print("Splitting the words:",a.split())

#27.join a list of words using join()
words = ["I", "am", "a", "data", "analyst"]
sentence = " ".join(words)
print("joining the words:", sentence)

#28.check if a string has only alphabets using isalpha()
a="janani"
print("checking if it is alphabets:",a.isalpha())

#29.check if a string has only numbers using isdigit()
a="1234"
print("checking if it is number:",a.isnum())

#30.check if a string has both alphabets and numbers using isalnum()
a="janani20code"
print("checking both of them are alphabets and number:",a.isalnum())

#31.check if all characters in a string are in lowercase using islower()
a="janani"
print("checking whether it is lowercase:",a.islower())

#32.check if all characters in a string are in uppercase using isupper()
a="JANANI MALLIKA"
print("checking whether it is uppercase:",a.isupper())

#33.swap lowercase to uppercase and vice versa using swapcase()
a="Donald Trump"
print("swapcase:",a.swapcase())

#34.convert every word's first letter to uppercase using title()
a="i am a data analyst working at a zoho company"
print("using title for first letter into capital letter:",a.title())

#35.check if a string contains only spaces using isspacce()
a="   "
print("Checking spaces:",a.isspace())

#36.count the number of vowels in a given string
a="python developer"
vowels="aeiou"
count=0
for i in a:
    if i in vowels:
        count=count+1
print("counting the vowels:",count)

#37.chack if a given word is a palindrome
a="level"
reverse=a[::-1]
if a==reverse:
    print("It is palindrome")
else:
    print("It is not palindrome")
    
#38.remove all digits from a given string
a="DataAnalyst2025"
result=""
for i in a:
    if not i.isdigit():
        result=result+i
print("removing the digits:",result)

#39.replace all spaces in a sentence with underscore
a="Data Analyst has lots of work"
print("replacing with underscore:",a.replace(" ","_"))

#40.extract only numbers from a mixed string llike "a2gL7"
a="contact number 87965433"
result=""
for i in a:
    if i.isdigit():
        result=result+i
print("only numbers:",result)


#41.fIND and print all wordss in a sentence that start with capital letter
a = "I am Good At Coding And Logical Thinking"
words=a.split()
print("words starting with capital letters:")
for word in words:
    if word[0].isupper():
        print(word)

#42.input a sentence and print how many times each letter occurs
a="I am good at coding and logical thinking"
a=a.replace(" ","").lower()
letter_count={}
for ch in a:
    if ch in letter_count:
        letter_count[ch]+=1
    else:
        letter_count[ch]=1
print("Letter occurrences:")
for key, value in letter_count.items():
    print(key, ":", value)



#43.remove all puncturation marks from a given sentence
a = "Hello, I am learning Python! It's fun, right?"
clean_text = ""
for ch in a:
    if ch.isalnum() or ch.isspace():  # Keep letters, numbers, spaces
        clean_text += ch

print("Text without punctuation:", clean_text)


#44.input an email and check if it ends with "@gmail.com"
a="janani@gmail.com"
print("checking endswith",a.endswith("@gmail.com"))

#45.reverse a given string without using slicing
a = "python"
reverse = ""
for ch in a:
    reverse = ch + reverse  # Add each character at the front
print("Reversed string:", reverse)

