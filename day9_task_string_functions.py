#1.To concatenate a given string to the end of another string
a="I got JOb at"
b="Zoho"
c=a+" "+b
print("concatenate:",c)

#2.to test if a given string contains the specified sequence of char values
a="I am a Data Analyst"
b="Data"
print("to check sequence of char values:",b in a)

#3.to convert all the characters in a string to lowercase
a="JANANI"
print("lowercase:",a.lower())

#4.to trim any leading or trailing whitespacce from a given string
a="    python developer   "
print("Trim the space:",a.strip())
#5.to reverse a string
a="Data Analyst"
print("Reverse a string:",a[::-1])

#6.replacce all spaces with undersscodres
a="Zoho company"
print("replace with underscore:",a.replace(" ","_"))

#7.create a string made of the middle three charac s="python123"
s="python123"
s1=len(s)//2
print("middle character:",s[s1-1:s1+2])


#8.the first and last letter to capital print("".join[i for i in s if not i.isdigit()])
s = "pyt89hon123"
# Remove digits
s = "".join([i for i in s if not i.isdigit()])
# Capitalize first and last letter
s = s[0].upper() + s[1:-1] + s[-1].upper()
print("Result:", s)


#9.write a program to get the length of a given string
a="scopetech institute"
print("Length of a given string:",len(a))

#10.write a program to print no of ocurrence of a given string with repetition
a="i am new to this office but not new to remove digits in strings"
print("repetition of the word",a.count("to"))

#11.write a program to ccount number of words in a strring 
a="i love coding"
print("count number of words:",len(a.split()))

#12.write a program to replace a specified character with another character
original_string="the quicck brown fox jumps over the lazy dog"
new_string=original_string.replace("o","0")
print("original_string",original_string)
print("new_string",new_string)

#13.How to count vowels in a sting
a="manufacture"
vowels="aeiou"
count=0
for i in a:
    if i in vowels:
        count=count+1
print("count vowels:",count)

#14.How to check if a string contains only whitespace
a="   "
print("checking whitespace:",a.isspace())

#15.how to remove all digits from a string
a="This truck has 18 wheels and 7 passangers"
result=""
for i in a:
    if not i.isdigit():
        result=result+i
print("strings after removing digits:",result)

#16.write a program to find the length of your name using len()
name="janani"
print("length of a name:",len(name))

#17.convert a given string to uppercase using upper()
name="janani"
print("uppercase:",name.upper())

#18.convert a given string to lowercase using lower()
name="JANANI"
print("lowercase:",name.lower())

#19.count how many times the letter "a" appears in a string using count()
a="attrocity"
print("counting letters:",a.count("t"))

#20.check if a string starts with the word "hello" using startswith()
a="hello world"
print("startswith:",a.startswith("hello"))

#21.check if a string ends with ".com" using endswith()
a="hellowworld.com"
print("endswith:",a.endswith(".com"))

#22.find the position of the word "python" in a sentence using find()
a="I like shinchan and doremon"
print("find:",a.find("doremon"))
