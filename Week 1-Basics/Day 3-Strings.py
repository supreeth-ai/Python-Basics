# 1. Store your full name in a variable and print it
a="abc"
print(a)

# 2. Print your name in all UPPERCASE
name="abcdef"
print(name.upper())

# 3. Print your name in all lowercase
name="abcdef"
print(name.lower())

# 4. Print length of your full name
name="abcdef"
print(len(name))

# 5. Print first character of your name
print(name[0])

# 6. Print last character of your name
print(name[5])

# 7. Print first 3 characters of your name
print(name[0:3])

# 8. Print last 3 characters of your name
print(name[3:6])

# 9. Reverse your name
print(name[::-1])

# 10. Check if "python" is in "I love python"
a="I love python python"
print(a.find("python"))# tell the index of where python is started

# 11. Concatenate "Data" and "Science" with space between
a="data "
b="science"
print(a+b)

# 12. Repeat "AI" 5 times
print("AI"*5)

# 13. Check if your name starts with "S"
name="Supreeth"
print(name.startswith("S"))

# 14. Check if your name ends with "h"
name="Supreeth"
print(name.endswith("h"))

# 15. Convert "hello world" to "Hello World"
a="hello world"
print(a.title())

# 16. Check if "Supreeth" is all alphabets
name="Supreeth"
print(name.isalpha())

# 17. Check if "12345" is all digits
num="12345"
print(num.isdigit())

# 18. Count characters in "Artificial Intelligence"
a="Artificial Intelligence"
print(len(a))

# 19. Print middle character of "Python"
name="Python"
print(name[2:4])

# 20. Print "Hello" + "World" using concatenation
print("Hello "+"World")

# 1. Replace all spaces with hyphens in "I love Data Science"
word="I love Data Science"
print(word.replace(" ","-"))

# 2. Count how many times "a" appears in "Bangalore Karnataka"
place="Bangalore Karnataka"
print(place.count("a"))

# 3. Remove whitespace from "   Hello World   "
w="   Hello World   "
print(w.strip())

# 4. Slice "Hello World" and print only "World"
wor="Hello World"
print(wor[6:])

# 5. Slice "Hello World" and print only "Hello"
wor="Hello World"
print(wor[:5])

# 6. Split "Python,SQL,Pandas,ML" into separate items
li="Python,SQL,Pandas,ML"
print(li.split(","))

# 7. Join ["Python", "SQL", "Pandas"] with space between
lis=["Python", "SQL", "Pandas"]
print(" ".join(lis))

# 8. Find index position of "o" in "Hello World"
word="Hello World"
print(word.find("o"))

# 9. Replace "bad" with "good" in "I am bad at coding"
sen="I am bad at coding"
print(sen.replace("bad","good"))

# 10. Count words in "I love Data Science and AI"
words="I love Data Science and AI"
print(len(words.split(" ")))
print(words.split())
print(words.split(" "))

# 11. Print string without first character
wor="string"
print(wor[1:])

# 12. Print string without last character
wor="python"
print(wor[:-1])

# 13. Print string without first and last character
wor="python"
print(wor[1:-1])

# 14. Check how many uppercase letters in "Hello World"
word="Hello World"
count=0
for ch in word:
    if ch.isupper():
         count+=1
print(count)

# 15. Check if "racecar" is same forwards and backwards
wor1="racecar"
wor2=wor1[::-1]
if wor1==wor2:
     print("it is same forward and backward")
else:
     print("its not same")

# 16. Convert "supreeth kumar" to "Supreeth Kumar"
name="supreeth kumar"
print(name.title())

# 17. Find if "AI" exists in "I love AI and ML"
wor="I love AI and ML"
print(wor.find("AI"))

# 18. Print every alternate character of "Python"
wor="Python"
print(wor[::2])

# 19. Print every alternate character starting from index 1
wor="Python"
print(wor[1::2])

# 20. Swap uppercase to lowercase in "Hello World"
wor="Hello World"
print(wor.lower())

# 1. Check if "madam" is palindrome without reverse()
name="madam"
name2=name[::-1]
if name==name2:
     print("it is a palindrome")
else:
     print("its not a palindrome")

# 2. Count vowels in "Artificial Intelligence"
word = "Artificial Intelligence"
count = word.lower().count("a") + word.lower().count("e") + word.lower().count("i") + word.lower().count("o") + word.lower().count("u")
print(count)

#or
word = "Artificial Intelligence"
vol="aeiou"
count=0
for i in word.lower():
     if i in vol:
          count+=1
print(count)
          
# 3. Remove all vowels from "Hello World"
word = "Hello World"

word = word.replace("a", "")
word = word.replace("e", "")
word = word.replace("i", "")
word = word.replace("o", "")
word = word.replace("u", "")

word = word.replace("A", "")
word = word.replace("E", "")
word = word.replace("I", "")
word = word.replace("O", "")
word = word.replace("U", "")

print(word)

#or

word = "Hello World"
vol="aeiouAEIOU"
result=""
for i in word:
     if i not in vol:
          result+=i
print(result)

# 4. Print only vowels from "Bangalore"
place="Bangalore"
vol="aeiouAEIOU"
result=""
for i in place:
     if i in vol:
          result+=i
print(result)

# 5. Find most repeated character in "programming"
word="programming"
max_count=0
max_char=""
for i in word:
     c=word.count(i)
     if c>max_count:
          max_count=c
          max_char=i
print("max_count=",max_count)
print("max_char=",max_char)

# 6. Remove duplicate characters from "programming"
word="programming"
count=0
char=""
for ch in word:
     if ch not in char:
          char+=ch
print(char)

# 7. Sort characters of "python" in alphabetical order
word="python"
sorted_=sorted(word)
print(sorted_)
sorted_="".join(sorted(word))
print(sorted_)

# 8. Reverse order of words in "I Love Python"
sen="I Love Python"
lis=sen.split()
print(lis)
lis.reverse()
print(" ".join(lis))

# 9. Remove all digits from "abc123def456"
al="abc123def456"
count=0
for i in al:
     if i.isnumeric():
          continue
     else:
          print(i)

# 10. Extract only numbers from "abc123def456"
num="abc123def456"
count=0
for i in num:
     if i.isalpha():
          continue
     else:
          print(i)

# 11. Check if "listen" and "silent" are anagrams
a="listen"
b="silent"
c=sorted(a)
d=sorted(b)
if c==d:
     print("listen and silent are anagrams")
else:
     print("they are not anagrams")

# 12. Find longest word in "I love Data Science"
word="I love Data Science"
longest=""
words=word.split()
for i in words:
     len(i)>len(longest)
     longest=i
print("longest:",longest)

# 13. Find shortest word in "I love Data Science"
word="I love Data Science"
words=word.split()
shortest=words[0]

for i in words:
     if len(i)<len(shortest):
          shortest=i
     
print("shortest:",shortest)

# 14. Compress "aaabbbccc" to "a3b3c3"
word="aaabbbccc"
word = "aaabbbccc"

result = ""
count = 1

for i in range(len(word) - 1):
    if word[i] == word[i + 1]:
        count += 1
    else:
        result += word[i] + str(count)
        count = 1

result += word[-1] + str(count)

print(result)

# 15. Remove all spaces from a string
word="i an aimd dqim "
words=word.replace(" ","")
print(words)

# 16. Count how many words start with capital letter
word="Aindf SNUHe jijdd"
count=0
for i in word.split():
            if i[0].isupper():
                 count+=1
     
print(count)
     












     
   

