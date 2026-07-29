# 1. Create a set of 5 numbers and print it
numbers = {10, 20, 30, 40, 50}
print(numbers)
# 2. Add a new element to set
numbers.add(60)
print(numbers)
# 3. Remove an element from set
numbers.remove(20)
print(numbers)
# 4. Check if element exists in set
if 30 in numbers:
    print("30 exists")
else:
    print("30 does not exist")
# 5. Find length of set
print(len(numbers))
# 6. Create set from a list with duplicates
lst = [1, 2, 2, 3, 4, 4, 5]
s = set(lst)
print(s)
#    notice duplicates are removed
# 7. Convert set to list
my_set = {1, 2, 3}
my_list = list(my_set)
print(my_list)
# 8. Convert list to set to remove duplicates
numbers = [1, 2, 2, 3, 3, 4]
unique = set(numbers)
print(unique)
# 9. Clear all elements from set
numbers.clear()
print(numbers)
# 10. Create empty set (careful — {} creates dict)
empty = set()
print(empty)
# 11. Loop through set and print elements
fruits = {"apple", "banana", "orange"}

for fruit in fruits:
    print(fruit)
# 12. Find union of {1,2,3} and {3,4,5}
a = {1,2,3}
b = {3,4,5}

print(a | b)
# 13. Find intersection of {1,2,3} and {2,3,4}
a = {1,2,3}
b = {2,3,4}

print(a & b)
# 14. Find difference of {1,2,3} and {2,3,4}
a = {1,2,3}
b = {2,3,4}

print(a - b)
# 15. Check if one set is subset of another
a = {1,2}
b = {1,2,3,4}

print(a.issubset(b))

# 1. Remove duplicates from list using set
numbers = [1,2,2,3,4,4,5]

unique = list(set(numbers))
print(unique)
# 2. Find common elements between two lists using sets
list1 = [1,2,3,4]
list2 = [3,4,5,6]

common = set(list1) & set(list2)
print(common)
# 3. Find elements in list1 not in list2 using sets
list1 = [1,2,3,4]
list2 = [3,4,5]

result = set(list1) - set(list2)
print(result)
# 4. Find symmetric difference of two sets
a = {1,2,3}
b = {3,4,5}

print(a ^ b)
#    (elements in either but not both)
# 5. Check if two sets have no common elements
a = {1,2}
b = {3,4}

print(a.isdisjoint(b))
# 6. Find union of 3 sets together
a = {1,2}
b = {2,3}
c = {3,4}

print(a | b | c)
# 7. Add multiple elements to set at once using update
numbers = {1,2,3}
numbers.update([4,5,6])
print(numbers)
# 8. Find intersection of 3 sets
a = {1,2,3}
b = {2,3,4}
c = {2,5,3}

print(a & b & c)
# 9. Check if {1,2} is subset of {1,2,3,4}
print({1,2}.issubset({1,2,3,4}))
# 10. Create frozenset and try to add element
#     observe what happens
fs = frozenset([1,2,3])

fs.add(4) #AttributeError: 'frozenset' object has no attribute 'add' 
#frozensets are immutable

# 1. What is difference between set and list?
#    When to use which?

#Use List when order and duplicates matter.
#Use Set when you need unique values and fast membership testing.

# 2. Find all unique characters in "programming"
word = "programming"
unique = set(word)
print(unique)
# 3. Given two lists of student names
#    find students in both classes
#    find students only in class 1
#    find students in either class
class1 = ["Alice","Bob","Charlie","David"]
class2 = ["Charlie","David","Emma","Frank"]
set1 = set(class1)
set2 = set(class2)
print("Both classes:", set1 & set2)
print("Only class1:", set1 - set2)
print("Either class:", set1 | set2)
# 4. Remove all duplicate words from a sentence
#    using sets
sentence = "python is easy python is powerful"
words = sentence.split()
unique = set(words)
print(unique)
# 5. What is difference between remove() and discard()?
#    Show with example
# remove() removes an element but gives keyerror if the element is not present 
s = {1,2,3}
s.remove(2)
print(s)
s.remove(5)
# discard() removes an element if it exists.
# does not raise error if it not exist 


