# 1. Write a function to print "Hello World"
def hello():
    print("Hello World")
hello()
# 2. Write a function that takes name and prints greeting
def greet():
    name=input("Enter your name:")
    print("hello",name)
greet()
# 3. Write a function to add two numbers and return result
def add_num(a,b):
    return a+b
n1=int(input("enter 1st number: "))
n2=int(input("enter 2nd number: "))
add=add_num(n1,n2)
print(add)
   
# 4. Write a function to subtract two numbers
def sub(a,b):
    return a-b
n1=int(input("enter 1st number: "))
n2=int(input("enter 2nd number: "))
result=sub(n1,n2)
print(result)

# 5. Write a function to multiply two numbers
def mul(a,b):
    return a*b
n1=int(input("enter 1st number: "))
n2=int(input("enter 2nd number: "))
result=mul(n1,n2)
print(result)

# 6. Write a function to divide two numbers
def div(a,b):
    if b==0:
        return "Divisiion by zero not allowed"
    return a/b
n1=int(input("enter 1st number: "))
n2=int(input("enter 2nd number: "))
result=div(n1,n2)
print(result)

# 7. Write a function to find square of a number
def sqr(a):
    return a*a
n1=int(input("enter a number:"))
print(sqr(n1))

# 8. Write a function to find cube of a number
def cube(a):
    return a**3
n1=int(input("enter a number: "))
print(cube(n1))
# 9. Write a function to check if number is even or odd
def check(a):
    if a%2==0:
        print(a,"is even")
    else:
        print(a,"is odd")
n1=int(input("enter a number:"))
check(n1)
#or
def c(a):
    if a%2==0:
        return "even"
    else:
        return "odd"
n=int(input("enter a number: "))
print(check(n))
        
# 10. Write a function to check if number is positive or negative
def pos(a):
    if a<0:
        return "negative"
    elif a==0:
        return "zero"
    else:
        return "positive"
n=int(input("enter a number: "))
print(pos(n))
    
# 11. Write a function with default parameter for city = "Bangalore"
def info(city="Bangalore"):
    return "city is: "+city
print(info("mysore"))
print(info())
# 12. Write a function to calculate simple interest
def simple(p,r,t):
    return (p*r*t)/100
principal=int(input("enter the amount: "))
rate=int(input("enter the rate: "))
time=int(input("enter years: "))
result=simple(principal,rate,time)
print(result)
# 13. Write a function to convert celsius to fahrenheit
def convert(c):
    return (9/5*c)+32
temp=float(input("enter celsius: "))
print("Fahrenheit:",convert(temp))

# 14. Write a function to find area of rectangle
def area(l,b):
    return l*b
length=float(input("enter the length: "))
breadth=float(input("enter the breadth: "))
print(area(length,breadth))
# 15. Write a function to find area of circle
def circle(r):
    return 3.14*r*r
radius=float(input("enter the radius: "))
print("area of circle:",circle(radius))
# 16. Write a function to find perimeter of rectangle
def peri(l,b):
    return 2*(l+b)
length=float(input("enter the length: "))
breadth=float(input("enter the breadth: "))
print("perimeter of rectangle:",peri(length,breadth))
# 17. Write a function that returns multiple values (sum and diff)
def cal(a,b):
    return a+b,a-b
n1=int(input("enter 1st number: "))
n2=int(input("enter 2nd number: "))
sum_result,diff_result=cal(n1,n2)
print("sum=",sum_result)
print("diff=",diff_result)

# 18. Write a function to print multiplication table of a number
def table(n):
    for i in range(1,11):
        print(n,"x",i,"=",n*i)
num=int(input("enter a number: "))
table(num)
# 19. Write a function to check if a number is divisible by 5
def check(n):
    if n%5==0:
        print("it is divisible")
    else:
        print("its not divisible")
num=int(input("enter a number: "))
check(num)
# 20. Write a function to find maximum of two numbers
def maximum(a,b):
    if a>b:
        print(a,"is greater")
    elif a<b:
        print(b,"is greater")
    else:
        print("both are equal")
a=int(input("enter 1st number: "))
b=int(input("enter 2nd number: "))
maximum(a,b)

# 1. Write a function to find factorial without recursion
def factorial(a):
    fac=1
    for i in range(a,0,-1):
         fac*=i
    return fac
print(factorial(5))
        
# 2. Write a function to check if a number is prime
def prime(a):
    if a<=1:
        return False
    for i in range(2,a):
        if a%i==0:
            return False
    return True
num=int(input("enter a number: "))
if prime(num):
    print(num,"is a prime number")
else:
    print(num,"is not a prime number")

    #or
import math
def is_prime(n):
    if n<=1:
        return False
    for i in range(2,int(math.sqrt(n)+1)):
        if n%i==0:
            return False
    return True
num=int(input("enter a number: "))
if is_prime(num):
    print("prime")
else:
    print("not prime")
    
# 3. Write a function to find sum of digits of a number
def sum_digits(n):
    total=0
    while n>0:
        digit=n%10
        total+=digit
        n //= 10
    return total
print(sum_digits(12345))
    
# 4. Write a function to reverse a number
def reverse_num(n):
    reverse=0
    while n>0:
        digit=n%10
        reverse=reverse*10+digit
        n //= 10
    return reverse
print(reverse_num(12345))

# 5. Write a function to check if a number is palindrome
def palindrome(n):
    original=n
    reverse=0
    while n>0:
        digit=n%10
        reverse=reverse*10+digit
        n //= 10
    if reverse==original:
        return "palindrome"
    else:
        return "not palindrome"
print(palindrome(121))

# 6. Write a function to find maximum of three numbers
def maximum(a,b,c):
    if a>=b and a>=c:
        return a
    elif b>=a and b>=c:
        return b
    else:
        return c
n1=int(input())
n2=int(input())
n3=int(input())
print(maximum(n1,n2,n3))

# 7. Write a function that takes *args and returns their sum
def total(*args):
    sum_num=0
    for i in args:
        sum_num+=i
    return sum_num
print(total(2,3))

# 8. Write a function that takes *args and returns the average
def average(*args):
    total=0
    for i in args:
        total+=i
    return total/len(args)
print(average(3,5))
# 9. Write a function to calculate compound interest
def compound(p,r,t):
    amount=p(1+(r/100))**t
    return amount-p
principal=float(input("enter the principal amount: "))
rate=float(input("enter the rate: "))
time=float(input("enter time(in years): "))
ci=compound(principal,rate,time)
print("compound interest: ",ci)

# 10. Write a function to convert kilometers to miles
def distance(km):
    return km*0.6213
kilometer=float(input("enter the kilometer: "))
print(distance(kilometer))
# 11. Write a function to calculate BMI given weight and height
def bmi(weight,height):
    return weight/(height*height)
w=float(input("enter the weight(in kg): "))
h=float(input("enter the height(in m): "))
print(bmi(w,h))

# 12. Write a function to find percentage given marks and total
def percentage(marks,total):
    return (marks/total)*100
print(percentage(90,100))

# 13. Write a function to check leap year
def leapyear(year):
    if year%400==0:
        return "leap year"
    elif year%100==0:
        return "not a leap year"
    elif year%4==0:
        return "leap year"
    else:
        return "not a leap year"
print(leapyear(2026))
# 14. Write a function that returns grade based on marks
def grade(marks):
    if marks>=90:
        return "A"
    elif marks>=80:
        return "B"
    elif marks>=70:
        return "C"
    elif marks>=60:
        return "D"
    else:
        return "E"
marks=int(input("enter the marks: "))
print(grade(marks))

# 15. Write a function to count vowels in a string
def vowels(v):
    vowel="aeiou"
    string=v
    count=0
    for i in string:
        if i in vowel:
            count+=1
    return count
print(vowels("sdfgjsiaoix"))

# 16. Write a function to check if string is palindrome
def palindrome(s):
    reverse=s[::-1]
    if s==reverse:
        return "palindrome"
    else:
        return "not palindrome"
print(palindrome("aba"))

# 17. Write a function to find length of a string without len()
def length(s):
    count=0
    for i in s:
        count+=1
    return count
word=input("enter the word: ")
print(length(word))

# 18. Write a function to calculate electricity bill (slab based)
#    First 100 units → ₹2 per unit
# Next 100 units (101–200) → ₹3 per unit
# Above 200 units → ₹5 per unit

def bill(units):
    if units<=100:
        return units*2
    elif units<=200:
        return units*3
    else:
        return units*5
units=int(input("enter the units: "))
print(bill(units))

# 19. Write a function with two default parameters
def addition(a=1,b=2):
    return a+b
print(addition())
    
# 20. Write a function to swap two numbers and return both
def swap(a,b):
    temp=a
    a=b
    b=temp
    return a,b
print(swap(1,2))



# 1. Write a recursive function to find factorial
def factorial(n):
    if n==0 or n==1:
        return 1
    return n*factorial(n-1)
  
num=int(input("enter a number: "))
print(factorial(num))
        
# 2. Write a recursive function to find Fibonacci of nth term
def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
num=int(input("enter the nth term: "))
print(fibonacci(num))

# 3. Write a recursive function to find sum of first n numbers
def sum_num(n):
    if n==1:
        return 1
    else:
        return n+sum_num(n-1)
num=int(input("enter a number: "))
print(sum_num(num))

# 4. Write a function to find GCD of two numbers
def gcd(a,b):
    g=1
    for i in range(1,min(a,b)+1):
        if a%i==0 and b%i==0:
            g=i
    return g
print(gcd(12,18))

# 5. Write a function to find LCM of two numbers
def lcm(a,b):
    greatest=max(a,b)
    while True:
        if greatest%a==0 and greatest%b==0:
            return greatest
        greatest==1
print(lcm(12,18))
        
# 6. Write a function to check if number is Armstrong
def armstrong(n):
    total=0
    leng=len(str(n))
    original=n
    while n>0:
        digit=n%10
        total+=digit**leng
        n//=10
    if total==original:
        return "Armstrong number"
    else:
        return "Not Armstrong number"
    
print(armstrong(154))


# 7. Write a function to check if number is perfect number
def perfect(n):
    total=0
    for i in range(1,n):
        if n%i==0:
            total+=i
    if total==n:
        return "perfect number"
    else:
        return "not perfect number"
print(perfect(6))

        
# 8. Write a function that takes a list and returns largest number
def largest(lis):
    large=lis[0]
    for i in lis:
        if i>large:
            large=i
    return large
print(largest([8,1,5,3,7,9,3,1]))

   
# 9. Write a function that takes a list and returns smallest number
def smallest(lis):
    small=lis[0]
    for i in lis:
        if i<small:
            small=i
    return small
print(smallest([9,3,7,8,23,6,2,2,1,7]))
# 10. Write a function to count how many even numbers in *args
def even(*args):
    count=0
    for i in args:
        if i%2==0:
            count+=1
    return count
print(even(3,2,6,8,3,1,6,4,9))
# 11. Write a function inside another function (nested function)
def calculate(a,b):
    def add():
        return a+b
    return add()
print(calculate(12,23))
    
# 12. Write a function that calls itself only 3 times maximum
def display(count):
    print("hello")
    if count<3:
        display(count+1)
display(1)

# 13. Write a function to calculate power without using **
def power(base,power):
    result=1
    for i in range(power):
        result*=base
    return result
print(power(2,4))
   
# 14. Write a function to find all factors of a number
def factors(n):
    for i in range(1,n):
        if n%i==0:
            print(i)
factors(20)
# 15. Write a function to check if all numbers in *args are positive
def check(*args):
    for i in args:
        if i<=0:
            return "all are not positive"
    return "all are positive"
print(check(1,-3,3,5,6,-5))

# 16. Write a function that takes a number and returns

#     "Fizz" if divisible by 3, "Buzz" if divisible by 5,
#     "FizzBuzz" if both, else the number itself
def fizzbuzz(n):
    if n%3==0 and n%5==0:
        return "FizzBuzz"
    elif n%3==0:
        return "Fizz"
    elif n%5==0:
        return "Buzz"
    else:
        return n
print(fizzbuzz(8))

# 17. Write a recursive function to reverse a number
def reverse_num(n, rev=0):
    if n == 0:
        return rev
    digit = n % 10
    rev = rev * 10 + digit
    return reverse_num(n // 10, rev)
print(reverse_num(12345))

# 18. Write a function with keyword arguments (name, age, city)
def info(name,age,city):
    print(name,"is",age,"years old and he is from",city)
info(age=22,city="Bangalore",name="abc")

# 19. Write a function to find sum of even numbers in *args
def sum_num(*args):
    total=0
    for i in args:
        if i%2==0:
            total+=i
    return total
print(sum_num(3,6,4,1,4,8,7,5))

# 20. Write a function that takes two functions as behavior
#     (call add or subtract based on operator passed)
def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def calculate(func, a, b):
    return func(a, b)
print(calculate(add, 10, 5))
print(calculate(subtract, 10, 5))

#also
def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def calculate(operator, a, b):
    if operator == "+":
        return add(a, b)
    elif operator == "-":
        return subtract(a, b)
print(calculate("+", 10, 5))
print(calculate("-", 10, 5))