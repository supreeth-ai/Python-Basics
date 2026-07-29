# 1. Create a tuple with 5 fruits and print it
fruits=("banana","mango","pine apple","apple")
print(fruits)
# 2. Print first element of tuple
fruits=("banana","mango","pine apple","apple")
print(fruits[0])
# 3. Print last element of tuple
fruits=("banana","mango","pine apple","apple")
print(fruits[-1])
# 4. Print length of tuple
fruits=("banana","mango","pine apple","apple")
print(len(fruits))
# 5. Access second and third element of tuple
fruits=("banana","mango","pine apple","apple")
print(fruits[1:3])
# 6. Slice tuple to get first 3 elements
fruits=("banana","mango","pine apple","apple")
print(fruits[0:3])
# 7. Count how many times 5 appears in (1,2,5,3,5,5)
num=(1,2,5,3,5,5)
count=0
for i in num:
    if i==5:
        count+=1
print(count)
# 8. Find index of "mango" in fruits tuple
fruits=("banana","mango","pine apple","apple")
for i in range(len(fruits)):
    if fruits[i]=="mango":
        print(i)

# 9. Unpack tuple (10, 20, 30) into 3 variables
tup=(10,20,30)
a,b,c=tup
print(a)
print(b)
print(c)

# 10. Create a tuple with single element
single=(1,)
print(single)

# 11. Check if "apple" exists in fruits tuple
fruits=("banana","mango","pine apple","apple")
if "apple" in fruits:
    print("apple is in tuple")
else:
    print("its not in tuple")
        
# 12. Convert a list to tuple
fruits=["banana","mango","pine apple","apple"]
tup=tuple(fruits)
print(tup)

# 13. Convert a tuple to list
fruits=("banana","mango","pine apple","apple")
lis=list(fruits)
print(lis)

# 14. Concatenate two tuples
tup1=(1,2,3)
tup2=(4,5,6)
print(tup1 + tup2)

# 15. Print tuple in reverse
fruits=("banana","mango","pine apple","apple")
print(fruits[::-1])

# 1. Create nested tuple and access inner elements
tup=((1,2,3),(4,7,6),(3,7,1))
print(tup[0])
print(tup[1])
print(tup[2])
print(tup[0][1])
print(tup[0][2])
print(tup[2][1])
# 2. Find minimum value in a number tuple
tup=(5,8,3,1,5,2)
small=tup[0]
for i in tup:
    if i<small:
        small=i
print("smallest:",small)
# 3. Find maximum value in a number tuple
tup=(5,8,3,1,5,2)
maximum=tup[0]
for i in tup:
    if i>maximum:
        maximum=i
print("maximum:",maximum)
# 4. Find sum of all elements in number tuple
tup=(5,8,3,1,5,2)
total=0
for i in tup:
    total+=i
print(total)
# 5. Unpack first and rest of elements separately
tup=(5,8,3,1,5,2)
first,*rest=tup
print(first)
print(rest)
# 6. Compare two tuples if they are equal
tup1=(1,2,3,4)
tup2=(1,2,5,4)
if tup1==tup2:
    print("equal")
else:
    print("not equal")
# 7. Loop through a tuple and print each element
tup=(1,2,3,4)
for i in tup:
    print(i)
# 8. Create tuple from user input of 3 numbers
numbers=[]
for i in range(3):
    num=int(input("enter a number: "))
    numbers.append(num)
tup=tuple(numbers)
print(tup)


# 9. Find how many elements are greater than 3
#    in (1, 2, 3, 4, 5, 6)
tup=(1, 2, 3, 4, 5, 6)
count=0
for i in tup:
    if i>3:
        count+=1
print(count)
# 10. Swap two variables using tuple unpacking
a=10
b=20
a,b=b,a
print(a)
print(b)

# 1. What is difference between list and tuple?
#    Show with example
lists=[1,4,3] #we use square brackets
tup=(3,6,6) #we use parenthesis
#lists are mutable
#tuples are immutable
#lists need more memory
#tuples need less memory
#lists are slower
#tuples are faster


# 2. Why are tuples faster than lists?
#    Create both and show

# Tuples are immutable  (No need to allocate extra memory for adding/removing elements).
# Less memory usage  (Tuples use slightly less memory than lists.)
#Faster iteration and access  (Python can optimize tuple operations.)

# 3. Create a function that returns multiple values
#    using tuple
# Function that returns multiple values using a tuple

def student():
    name = "Supreeth"
    age = 22
    cgpa = 8.2
    return name, age, cgpa   # Returns a tuple
result = student()

print(result)
print(type(result))

# 4. Find second largest in a tuple without sorting

tup=(3,6,1,8,9,4)
largest=tup[0]
second=tup[0]
for i in tup:
    if i>largest:
        second=largest
        largest=i
    elif i>second and i!=largest:
        second=i
print("largest:",largest)
print("second_largest:",second)

# 5. Check if tuple is a palindrome
tup=(1,2,1)
if tup==tup[::-1]:
    print("palindrome")
else:
    print("not palindrome")


