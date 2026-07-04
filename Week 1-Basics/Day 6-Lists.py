# 1. Create a list of 5 fruits and print it
lis=["apple","banana","mango","grapes","pineapple"]
print(lis)

# 2. Print first element of a list
lis=["apple","banana","mango","grapes","pineapple"]
print(lis[0])

# 3. Print last element of a list
lis=["apple","banana","mango","grapes","pineapple"]
print(lis[-1])

# 4. Print length of a list
lis=["apple","banana","mango","grapes","pineapple"]
print(len(lis))

# 5. Add a new item to end of list using append
lis.append("orange")
print(lis)

# 6. Add an item at beginning of list using insert
lis.insert(0,"jackfruit")
print(lis)

# 7. Remove a specific item from list
lis.remove("banana")
print(lis)

# 8. Remove last item from list using pop
lis.pop(-1)
print(lis)

# 9. Sort a list of numbers in ascending order
lis=[23,13,75,24,15,86,43,32]
lis.sort()
print(lis)

# 10. Sort a list of numbers in descending order
lis=[23,13,75,24,15,86,43,32]
lis.sort(reverse=True)
print(lis)

# 11. Reverse a list
lis=[23,13,75,24,15,86,43,32]
lis.reverse()
print(lis)

# 12. Check if an item exists in a list
lis=[23,13,75,24,15,86,43,32]
print(40 in lis)

# 13. Count how many times an item appears in list
lis=[23,13,75,24,15,86,43,32,86,75,75,75]
print(lis.count(75))

# 14. Find index of a specific item in list
lis=[23,13,75,24,15,86,43,32]
print(lis.index(13))

# 15. Create a list of numbers 1 to 10 using range
num=list(range(1,11))
print(num)

# 16. Print all elements of list using loop
lis=[23,13,75,24,15,86,43,32]
for i in lis:
    print(i)

# 17. Find sum of all numbers in a list
lis=[23,13,75,24,15,86,43,32]
print(sum(lis))

# 18. Find largest number in a list
lis=[23,13,75,24,15,86,43,32]
print(max(lis))

# 19. Find smallest number in a list
lis=[23,13,75,24,15,86,43,32]
print(min(lis))

# 20. Copy one list into another list
lis=[23,13,75,24,15,86,43,32]
lis2=lis.copy()
print(lis2)

# 1. Find average of numbers in a list
lis=[23,13,75,24,15,86,43,32]
leng=len(lis)
total=sum(lis)
avg=total/leng
print("avg:",avg)

# 2. Count even numbers in a list
lis=[23,13,75,24,15,86,43,32]
count=0
for i in lis:
    if i%2==0:
        count+=1
print(count)

# 3. Count odd numbers in a list
lis=[23,13,75,24,15,86,43,32]
count=0
for i in lis:
    if i%2!=0:
        count+=1
print(count)

# 4. Print only even numbers from a list
lis=[23,13,75,24,15,86,43,32]
for i in lis:
    if i%2==0:
        print(i,end=" ")

# 5. Print only odd numbers from a list
lis=[23,13,75,24,15,86,43,32]
for i in lis:
    if i%2!=0:
        print(i)

# 6. Find second largest number in a list
lis=[23,13,75,24,15,86,43,32]
first=lis[0]
second=lis[0]
for i in lis:
    if i>first:
        second=first
        first=i
    elif i>second and i!=first:
        second=i
print("largest:",first)
print("second largest:",second)

# 7. Find second smallest number in a list
lis=[23,13,75,24,15,86,43,32]
first=lis[0]
second=lis[0]
for i in lis:
    if i<first:
        second=first
        first=i
    elif i<second and i!=first:
        second=i
print("first smallest:",first)
print("second smallest:",second)

# 8. Remove duplicate elements from a list
lis=[23,13,75,24,15,86,43,32,24]
new_lis=[]
for i in lis:
    if i not in new_lis:
        new_lis.append(i)
print(new_lis)

# 9. Merge two lists into one
list1=[1,2,3,4]
list2=["a","b","c","d","e"]
print(list1+list2)

# 10. Find common elements between two lists
letters=["a","d","b","f","a"]
letters2=["d","w","s","f"]
for i in letters:
    for j in letters2:
        if i==j:
            print(i)

            #OR

letters = ["a", "d", "b", "f", "a"]
letters2 = ["d", "w", "s", "f"]
common = []
for i in letters:
    if i in letters2 and i not in common:
        common.append(i)
print(common)

# 11. Find elements present in list1 but not in list2
letters=["a","d","b","f","a"]
letters2=["d","w","s","f"]
new_list=[]
for i in letters:
    if i in letters2:
        continue
    else:
        new_list.append(i)
print(new_list)

# 12. Swap first and last element of a list
lis=[23,13,75,24,15,86,43,32,24]
temp=lis[0]
lis[0]=lis[-1]
lis[-1]=temp
print(lis)

# 13. Create a list of squares of numbers 1 to 10
sq=[]
for i in range(1,11):
    num=i**2
    sq.append(num)
print(sq)

# 14. Slice a list to get middle 3 elements
lis = [23, 13, 75, 24, 15, 86, 43]
print(lis[2:5])

# 15. Check if a list is sorted or not
lis = [23, 13, 75, 24, 15, 86, 43]
if sorted(lis)==lis:
    print("the list is sorted")
else:
    print("its not sorted")
              
              #OR

lis = [23, 13, 75, 24, 15, 86, 43]
for i in range(len(lis)-1):
    if lis[i]>lis[i+1]:
        print("not sorted")
        break
else:
    print("its sorted")

# 16. Find sum of even numbers in a list
lis = [23, 13, 75, 24, 15, 86, 43]
total=0
for i in lis:
    if i%2==0:
        total+=i
print(total)

# 17. Find sum of odd numbers in a list
lis = [23, 13, 75, 24, 15, 86, 43]
odd=0
for i in lis:
    if i%2!=0:
        odd+=i
print(odd)

# 18. Convert a list of strings to uppercase
lis=["a","s","e","o"]
lis1=[]
for i in lis:
    up=i.upper()
    lis1.append(up)
print(lis1)

# 19. Count how many strings vs numbers in a mixed list
lis=["as",1,56,"we","arjun",1,"w"]
str_count=0
num_count=0
for i in lis:
    if type(i)==int:
        num_count+=1
    elif type(i)==str:
        str_count+=1
print("strings:",str_count)
print("numbers:",num_count)

# 20. Create list comprehension for cubes 1 to 10
cu=[]
for i in range(1,11):
    cube=i**3
    cu.append(cube)
print(cu)

# 1. Find all pairs in a list that sum to a target number
target=10
lis=[8,2,1,4,9,5,5,6]
for i in range(len(lis)):
    for j in range(i+1,len(lis)):
        if lis[i]+lis[j]==target:
            print(lis[i],",",lis[j])

# 2. Rotate a list by one position to the right
lis=[8,2,1,4,9,5,5,6]
print([lis[-1]]+lis[:-1])

# 3. Rotate a list by one position to the left
lis=[8,2,1,4,9,5,5,6]
print(lis[1:]+[lis[0]])

# 4. Find the most frequent element in a list
lis=[8,2,1,4,9,5,5,6]
max_count=0
most=lis[0]
for i in lis:
    count=0
    for j in lis:
        if i==j:
            count+=1
    if count>max_count:
        max_count=count
        most=i
print(most)

# 5. Flatten a nested list [[1,2],[3,4]] to [1,2,3,4]
lis=[[1,2],[3,4]]
flat=[]
for i in lis:
    for j in i:
        flat.append(j)
print(flat)

# 6. Find the difference between max and min in a list
lis=[8,2,1,4,9,5,5,6]
max=lis[0]
min=lis[0]
for i in lis:
    if i>max:
        max=i
for j in lis:
    if j<min:
        min=j
print("smallest:",min)
print("largest:",max)
print("difference:",max-min)

# 7. Split a list into two halves
lis=[8,2,1,4,9,5,5,6]
half=len(lis)//2
print(lis[0:half])
print(lis[half:])

# 8. Check if two lists have at least one common element
list1=[2,4,6,1]
list2=[9,7,2,5,3]
found=False
for i in list1:
    for j in list2:
        if i==j:
            found=True
            break
    if found:
        break
if found:
    print("two lists have atleast one common element")
else:
    print("they dont have any common element")

# 9. Remove all occurrences of a specific value from list
lis=[8,2,1,4,9,5,5,6]
new_lis=[]
for i in lis:
    if i!=5:
        new_lis.append(i)
print(new_lis)

# 10. Find the missing number in a list from 1 to 10
lis=[1,2,3,4,5,7,8,9,10]
for i in range(1,11):
    if i not in lis:
        print("missing number is:",i)

lis=[1,2,3,4,5,7,8,9,10]
for i in range(1,11):
    found=False
    for j in lis:
        if i==j:
            found=True
            break
    if not found:
        print("missing number is:",i)

# 11. Create a list of prime numbers between 1 and 50
lis=[]
for i in range(2,51):
    is_prime=True
    for j in range(2,i):
        if i%j==0:
            is_prime=False
            break
    if is_prime:
        lis.append(i)
print(lis)

# 12. Sort a list without using sort() method
lis=[3,1,7,4,3,8,9,5]
lis1=[]
for i in range(len(lis)-1):
    for j in range(len(lis)-1):
       if lis[j]>lis[j+1]:
        temp=lis[j]
        lis[j]=lis[j+1]
        lis[j+1]=temp
print(lis)

# 13. Find duplicate elements in a list
lis=[3,1,7,4,3,8,9,5]
dup=[]
for i in range(len(lis)):
    for j in range(i+1,len(lis)):
        if lis[i]==lis[j]:
            dupli=lis[i]
            dup.append(dupli)
            print(dup)

# 14. Merge two sorted lists into one sorted list

list1=[3,4,5,6,8]
list2=[1,4,9,12]
list3=[]
i=0
j=0
while i<len(list1) and j<len(list2):
    if list1[i]<list2[j]:
        list3.append(list1[i])
        i+=1
    else:
        list3.append(list2[j])
        j+=1
while j<len(list2):
    list3.append(list2[j])
    j+=1
while i<len(list1):
    list3.append(list1[i])
    i+=1
print(list3)

# 15. Find the longest string in a list of strings
strings=["abc","spirex","a","fjaiwm","sinfska"]
lar=strings[0]
for i in range(len(strings)-1):
    if len(lar)<len(strings[i+1]):
        lar=strings[i+1]
print(lar)

# 16. Reverse a list without using reverse() method
lis=[1,5,3,8,2,8]
rev=lis[::-1]
print(rev)
#or
lis=[1,5,3,8,2,8]
lis3=[]
for i in range(len(lis)-1,-1,-1):
    lis3.append(lis[i])
print(lis3)
#or
lis = [1,5,3,8,2,8]
left = 0
right = len(lis) - 1
while left < right:
    lis[left], lis[right] = lis[right], lis[left]
    left += 1
    right -= 1
print(lis)

# 17. Find sum of all elements without using sum() function
lis = [1,5,3,8,2,8]
total=0
for i in lis:
    total+=i
print(total)

# 18. Create a list of Fibonacci numbers up to n terms
first=0
second=1
lis=[]
n=int(input("enter the number of terms: "))
if n>=1:
    lis.append(first)
if n>=2:
    lis.append(second)
for i in range(2,n):
    next=first+second
    lis.append(next)
    first=second
    second=next
print(lis)


# 19. Check if a list is a palindrome (same forward and backward)
lis=[1,2,3,2,1]
lis2=[]
for i in range(len(lis)-1,-1,-1):
    lis2.append(lis[i])
if lis==lis2:
    print('its a palindrome')
else:
    print("its not a palindrome")

# 20. Group numbers in a list as even and odd in two separate lists
lis=[1,2,5,7,4,8]
even=[]
odd=[]
for i in lis:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print(even)
print(odd)










   



    


       

    


    
    

 

    


















