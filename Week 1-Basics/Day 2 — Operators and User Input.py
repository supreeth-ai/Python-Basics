
# Note: Solved these ahead of schedule
# Formal conditions topic — Day 4

# 1. Take two numbers from user and print sum
num1=int(input("enter first number: "))
num2=int(input("enter second number: "))
print("sum:",num1+num2)

# 2. Take two numbers and print difference
num3=int(input("enter first number: "))
num4=int(input("enter second number: "))
print("difference:",num3-num4)

# 3. Take two numbers and print product
num5=int(input("enter first number: "))
num6=int(input("enter second number: "))
print("product:",num5*num6)

# 4. Take two numbers and print division
num7=int(input("enter first number: "))
num8=int(input("enter second number: "))
print("remainder:",num7/num8)

# 5. Take a number and print its square
sq=int(input("enter a number: "))
square=sq*sq
print("Square of",sq,"is",square)

# 6. Take a number and print its cube
cu=int(input("enter a number: "))
cube=cu**3
print("Cube of",cu,"is",cube)

# 7. Check if a number is even or odd
num=int(input("enter a number: "))
if num%2==0:
    print("The number",num,"is Even")
else:
    print("The number",num,"is odd")

# 8. Calculate simple interest — principal rate time
P=int(input("Enter the Principle: "))
R=int(input("Enter the Rate of interest: "))
T=int(input("Enter the Time: "))
SI=(P*R*T)/100
print("The Simple Interest is:",SI)

# 9. Take two numbers print which is greater
one=int(input("Enter first numer: "))
two=int(input("Enter second number: "))
if one>two:
    print("The number",one,"is greater then",two)
else:
    print("The number",two,"is greater then",one)

# 10. Take a number check if positive negative or zero
A=int(input("enter a number: "))
if A>0:
    print("Positive")
elif A<0:
    print("Negative")
else:
    print("zero")

# 11. Take radius calculate area of circle
rad=float(input("Enter the Radius: "))
Area=3.14*rad**2
print(f"The area of Circle is {Area}")

# 12. Take length width calculate rectangle area
length=float(input("Enter the length: "))
width=float(input("Enter the width: "))
Area=length*width
print(f"The area of rectangle is {Area}")

# 13. Convert celsius to fahrenheit
cel=float(input("Enter temperature in (C): "))
F=(9/5)*cel+32
print("fahrenheit:",F)

# 14. Convert kilometers to miles
km=int(input("Enter km: "))
miles=km*0.621
print(f"{km} km is equal to {miles} miles")

# 15. Calculate percentage of marks in 5 subjects
sub1=int(input("Enter the marks: "))
sub2=int(input("Enter the marks: "))
sub3=int(input("Enter the marks: "))
sub4=int(input("Enter the marks: "))
sub5=int(input("Enter the marks: "))
per=((sub1+sub2+sub3+sub4+sub5)/500)*100
print(f"Total Percentage is {per}")

# 16. Take a number print remainder when divided by 7
num=int(input("enter a number: "))
print(num/7)

# 17. Check if number is divisible by 5
num=int(input("enter a number: "))
if num%5==0:
    print("the number is divisible by 5")
else:
    print("not divisible")

# 18. Take age check if eligible to vote (18+)
age=int(input('enter age: '))
if age>18:
    print("you are eligible to vote.")
else:
    print("you are not eligible to vote.")

#19. Calculate power of a number without ** operator
num=int(input("enter a number: "))
power=num*num
print(f"{power} is the power of {num}.")

# 20. Take two numbers swap them using += and -=
a=int(input("Enter first number: "))
b=int(input("enter second number: "))
a=a+b
b=a-b
a=a-b
print("a =",a)
print("b =",b)

#MEDIUM
# 1. Take 3 numbers check if all are equal

num1=int(input("enter first number: "))
num2=int(input("enter second number: "))
num3=int(input("enter thired number: "))
if num1==num2 and num1==num3:
    print("All are equal")
else:
    print("They are not equal")

# 2. Take 3 numbers check if any two are equal
num1=int(input("enter first number: "))
num2=int(input("enter second number: "))
num3=int(input("enter thired number: "))
if num1==num2 or num1==num3 or num2==num3:
    print("Two numbers are equal")
else:
    print("They are not equal")

# 3. Check if number is between 10 and 50
num=int(input("enter a number: "))
if num>=10 and num<=50:
    print("The number is in between 10 and 50")
else:
    print("its not between 10 and 50")

# 4. Take a year check if leap year
year=int(input("enter the year: "))
if year%4==0:
    print("it is a leap year")
elif year%400==0:
    print("it is a leap year")
elif year%100==0:
    print("it is not a leap year")
else:
    print("it is not a leap year")

# 5. Calculate BMI — weight divided by height squared
weight=float(input("enter your weight:"))
height=float(input("enter your height: "))
BMI=weight/(height**2)
print("Your BMI is",BMI)

# 6. Take a number check divisible by both 3 and 5
num=int(input("enter a number: "))
if num%3==0 and num%5==0:
    print("The number is divisible by both 3 and 5")
else:
    print("its not divisible by both 3 and 5")

# 7. Check if number is divisible by 2 or 3 but not both
num=int(input("enter a number: "))
if num%2==0 and num%3==0:
    print("It is divisible by both 2 and 3")
elif num%3==0:
    print("It is divisible by 3")
elif num%2==0:
    print("The number is divisible by 2")
else:
    print("the number is not divisible by 2 or 3")

# 8. Take price and discount calculate final price
original_price=float(input("Enter the original_price: "))
Discount_percentage=float(input("Enter the discount percentage: "))
Discount=(original_price*Discount_percentage)/100
current_price=original_price-Discount
print("price after discount is",current_price)

# 9. Take salary calculate tax if salary above 50000
salary=float(input("Enter the salary"))
Tax_rate=float(input("enter the tax"))
if salary<=50000:
    print("no tax")
else:
    Tax=(salary*Tax_rate)/100
    Final_salary=salary-Tax
    print("The final salary is",Final_salary)

# 10. Take a number add 10 using += operator
num=int(input("enter a number: "))
num+=10
print(num)

# 11. Take a number multiply by 5 using *= operator
num=int(input("enter a number: "))
num*=5
print(num)

# 12. Check if person is teenager between 13 and 19
age=int(input("enter your age: "))
if age>=13 and age<=19:
    print("you are a teenager")
else:
    print("you are not a teenager")

# 13. Take three subject marks check if passed all above 35

sub1=int(input("enter marks of first subject: "))
sub2=int(input("enter marks of second subject: "))
sub3=int(input("enter marks of third subject: "))
if sub1>=35 and sub2>=35 and sub3>=35:
    print("all pass")
else:
    print("all did not pass")

# 14. Calculate electricity bill — units multiplied by rate
units=float(input("enter the units: "))
rate=float(input("enter the rate: "))
electricity_bill=units*rate
print("the electricity bill is =",electricity_bill)

#15. Check if triangle is valid given 3 sides (sum of any two sides is greater then 3rd side)
s1=float(input("enter side 1: "))
s2=float(input("enter side 2: "))
s3=float(input("enter side 3: "))
if s1+s2>s3 and s1+s3>s2 and s2+s3>s1:
    print("it is a triangle")
else:
    print("its not a triangle")

# 17. Take a number check if it is a perfect square
import math
n=int(input("enter a number: "))
root=math.sqrt(n)
if root ==int(root):
    print("it is a perfect square")
else:
    print("its not a perfect square")

# 18. Calculate compound interest
p=float(input("enter principle: "))
r=float(input("enter the rate: "))
t=float(input("enter time in years: "))
A=p*((1+(r/100))**t)
print("compound interest is:",A)

# 19. Take speed and time calculate distance
speed=float(input("enter the speed: "))
time=float(input("enter the time: "))
dis=speed*time
print("the distance covered is:",dis)

# 20. Take a 3 digit number print sum of its digits
num=int(input("enter three digit number: "))
digit1=num//100
digit2=(num//10)%10
digit3=num%10
sum=digit1+digit2+digit3
print("the sum is",sum)



# 1. What is difference between / and //? 
a=int(input("enter a number: "))
b=int(input("enter a number"))
c=a/b
d=a//b
print(a/b,"=",c,"its a normal division which gives quotient with decimals")
print(a//b,"=",d,"its floor devision which gives quotient rounded down as whole number. it takes out decimals")

# 2. What does % operator do? 
a=int(input("enter a number: "))
b=int(input("enter a number"))
c=a%b
print(a%b,"=",c,"% is a modulo operator which gives remainder")

# 3. Without if else check if number even using %
a=int(input("enter a number: "))
print(a%2==0)

# 4. What happens when you use + between two strings?
a="hi"
b="hi"
c=a+b
print(c,"+ operator concatenates two strings.")#output:hihi

# 5. Check if number is divisible by 2 3 and 5 all three
a=int(input("enter a number: "))
if a%2==0 and a%3==0 and a%5==0:
    print("the number",a,"is divisible by 2,3 and 5")
else:
    print("its not divisible by all three numbers.")

# 6. Take two boolean values print and or not results
a=True
b=False
print(a and b)
print(a or b)
print(not a)
print(not b)

# 7. What is operator precedence? Show with example

#operator precedence means which operator is considered to be solved 
# first and which is to be ssolved last
print((2/3)+5*6)#bracket is solved first, then multiply and then add

# 8. Take a number check if it is power of 2

a=int(input("enter a number: "))
if num>0 and (num-1)==0:
    print("it is the power of 2")
else:
    print("its not the power of 2")

# 9. Swap two numbers without using third variable
a=3
b=4
a=a+b
b=a-b
a=a-b
print("a =",a)
print("b =",b)

# 10. Take a number reverse its digits using operators

a=int(input("enter a number: "))
rev = 0

rev = (rev * 10) + (a % 10)
a = a // 10

rev = (rev * 10) + (a % 10)
a = a // 10

rev = (rev * 10) + (a % 10)
a = a // 10

print("Reversed number is:", rev)

# 11. Check if number is palindrome using operators only

num = int(input("Enter a number: "))

original = num
rev = 0

rev = rev * 10 + num % 10
num = num // 10

rev = rev * 10 + num % 10
num = num // 10

rev = rev * 10 + num % 10
num = num // 10

if original == rev:
    print("Palindrome")
else:
    print("Not Palindrome")

# 12. Take a 4 digit number extract each digit separately
num=int(input("Enter 4 digit number: "))

d1 = num // 1000
d2 = (num // 100) % 10
d3 = (num // 10) % 10
d4 = num % 10

print("First digit:", d1)
print("Second digit:", d2)
print("Third digit:", d3)
print("Fourth digit:", d4)













