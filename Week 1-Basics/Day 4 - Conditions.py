# 1. Check if a number is positive or negative
num=3
if num>0:
    print("Positive")
elif num==0:
    print("zero")
else:
    print("negative")

# 2. Check if a number is even or odd
num=4
if num%2==0:
    print(f"{num} is even")
else:
    print(f"{num} is odd")

# 3. Check if a person is eligible to vote (age >= 18)
age=int(input())
if age>=18:
    print("you are eligible to vote")
else:
    print("you are too young to vote")

# 5. Check if a number is greater than 100
num=int(input())
if num>100:
    print(f"{num} is greater than 100")
else:
    print(f"{num} is smaller than 100")

# 6. Take two numbers check which one is greater
a=int(input("enter num 1: "))
b=int(input("enter num 2: "))
if a>b:
    print(f"{a} is greater than {b}")
elif a==b:
    print(f"{a} is equal to {b}")
else:
    print(f"{a} is smaller than {b}")

# 7. Check if a number is divisible by 5
num=int(input())
if num%5==0:
    print(f"{num} is divisible by 5")
else:
    print(f"{num} is not divisible by 5")

# 9. Take marks check if student passed (marks >= 35)
marks=int(input())
if marks>=35:
    print("pass")
else:
    print("not pass")

# 10. Check if a number is between 10 and 50
num=int(input())
if num>=10 and num<50:
    print(f"{num} is between 10 and 50")
else:
    print(f"{num} is not between 10 and 50")

#11. Check if temperature is hot cold or normal
#     hot above 35, cold below 15, normal in between

temp=int(input("enter the temperature "))
if temp>35:
    print("its hot")
elif temp<15:
    print("its cold")
else:
    print("its normal")

# 12. Take age print if child teenager or adult
#     child below 12, teenager 13-19, adult above 19

age=int(input("enter age: "))
if age<13:
    print("you are a child")
elif age>20:
    print("you are a teenager")
else:
    print("you are a adult")

# 13. Check if a year is leap year
year=int(input())
if year%400==0:
    print("it is a leap year")
elif year%100==0:
    print("its not a leap year")
elif year%4==0:
    print("it is a leap year")
else:
    print("not a leap year")

# 14. Check if a number is single digit or double digit
num=int(input())
if num>=0 and num<=9:
    print(f"{num} is single digit")
elif num>=10 and num<=99:
    print("its double digit")
else:
    print("its more than 2 digit")

# 15. Take salary check if above below or equal to 50000
salary=int(input())
if salary<50000:
    print("its below 50k")
elif salary>50000:
    print("salary is above 50k")
else:
    print("salary is equal")

# 16. Check if a character is vowel or consonant
wor=input("enter a character: ")
if wor in "aeiouAEIOU":
    print("its vowel")
else:
    print("its consonent")

# 18. Take a number check if it is 1 2 or 3
#     print one two or three accordingly

num=int(input())
if num==1:
    print("one")
elif num==2:
    print("two")
elif num==3:
    print("three")
else:
    print("its different")

# 1. Take 3 numbers find the largest

num1=int(input())

num2=int(input())

num3=int(input())
if num1>num2 and num1>num3:
    print(f"{num1} is largest")
elif num2>num1 and num2>num3:
    print(f"{num2} is greater")
else:
    print(f"{num3} is largest")

# 2. Take 3 numbers find the smallest

num1=int(input())

num2=int(input())

num3=int(input())
if num1<num2 and num1<num3:
    print(f"{num1} is smallest")
elif num2<num1 and num2<num3:
    print(f"{num2} is smallest")
else:
    print(f"{num3} is smallest")

# 3. Check if triangle is valid given 3 sides(sum of any 2 sides is > than 3rd side)

num1=int(input())

num2=int(input())

num3=int(input())
if (num1+num2)>num3 and (num2+num3)>num1 and (num1+num3)>num2:
    print("it is valid triangle")
else:
    print("its not valid")

# 4. Check if number is divisible by both 2 and 3
num=int(input())
if num%2==0 and num%3==0:
    print("it is divisible by both 2 and 3")

# 5. Check if number is divisible by 2 or 3 but not both
num=int(input())
if num%2==0 or num%3==0:
    print("it is NOT divisible by both 2 and 3")

# 6. Take price check if discount applies
#    above 1000 gets 10% discount
#    above 5000 gets 20% discount
#    below 1000 no discount

price=int(input())
if price>1000:
    print("10% dis")
elif price>2000:
    print("20% dis")
elif price<1000:
    print("No discount")

#7. Check if person is eligible for loan
#    age between 21 and 60 and salary above 25000

age=int(input("age: "))
sal=int(input("salary: "))
if age>=21 and age<=60 and sal>25000:
    print("you are eligible for loan")
else:
    print("you are not eligible")
    
# 8. Take month number print how many days in that month
#    ignore leap year for now

month=int(input("enter the month number:"))
match month:
    case 1:
        print("january has 31 days")
    case 2:
        print("feb has 28 days(not leap year)")
    case 3:
        print("march has 31 days")
    case 4:
        print("april has 30 days")
    case 5:
        print("may has 31 days")
    case 6:
        print("june has 30 days")
    case 7:
        print("july has 31 days")
    case 8:
        print("august has 30 days")
    case 9:
        print("september has 31 days")
    case 10:
        print("october has 30 days")
    case 11:
        print("november has 31 days")
    case 12:
        print("december has 30 days")
    case _:
        print("invalid month number")

# 9. Take a number check if it is positive even or positive odd
#    or negative even or negative odd

num=int(input())
if num%2==0:
    if num>0:
        print("its positive even")
    else:
        print("its negative even")  
else:
    if num>0:
        print("its positive odd")
    else:
        print("its negative odd")

# 10. Check if BMI is underweight normal overweight or obese
#     underweight below 18.5
#     normal 18.5 to 24.9
#     overweight 25 to 29.9
#     obese above 30

bmi=float(input())
if bmi<18.5:
    print("underweight")
elif bmi>=18.5 and bmi<=24.9:
    print("normal")
elif bmi>=25 and bmi<=29.9:
    print("overweight")
else:
    print("obese")

# 11. Take electricity units calculate bill
#     first 100 units — 1.50 per unit
#     next 100 units — 2.50 per unit
#     above 200 units — 4.00 per unit

ele_un = int(input("units: "))
bill = 0
if ele_un <= 100:
    bill = ele_un * 1.5
elif ele_un <= 200:
    bill = (100 * 1.5) + ((ele_un - 100) * 2.5)
else:
    bill = (100 * 1.5) + (100 * 2.5) + ((ele_un - 200) * 4.0)
print("bill =", bill)

# 12. Take 3 subject marks check if student passed all
#     failed any or failed all

sub1=int(input("sub1: "))
sub2=int(input("sub2: "))
sub3=int(input("sub3: "))
if sub1>=35 and sub2>=35 and sub3>=35:
    print("student passed all subjects")
elif sub1<35 and sub2<35 and sub3<35:
    print("NOT passed any subjects")
else:
    print("student passed some and failed some")

# 13. Check if number is between 1 and 100 inclusive
num=int(input())
if num>=1 and num<=100:
    print("number is between 1 and 100")    

# 14. Take day number 1 to 7 print day name
#     1 is Monday 7 is Sunday

day=int(input("enter day number (1 to 7)"))
match day:
    case 1:
        print("Monday")
    case 2:
        print("tuesday")
    case 3:
        print("wednesday")
    case 4:
        print("thursday")
    case 5:
        print("friday")
    case 6:
        print("saturday")
    case 7:
        print("sunday")
    case _:
        print("invalid input")

 # 15. Check if character is uppercase lowercase or digit
char=input()
if char.isupper():
    print("uppercase")
elif char.islower():
    print("lowercase")
elif char.isnumeric():
    print("its digit")
else:
    print("special character")

# 17. Check if two numbers are both positive both negative
#     or one positive one negative

num1=int(input())
num2=int(input())
if num1>0 and num2>0:
    print("both are positive")
elif num1<0 and num2<0:
    print("both are negative")
elif num1==0 or num2==0:
    print("zero")
else:
    print("one positive and one negative")
            
# 18. Take speed check if slow normal or overspeeding
#     below 40 slow, 40 to 80 normal, above 80 overspeeding

speed=int(input())
if speed<40:
    print("its slow")
elif speed>=40 and speed<=80:
    print("normal speed")
elif speed>80:
    print("overspeed")
else:
    print("invalid input")

# 19. Check if a number is perfect — 
#     sum of divisors equals the number (use only conditions)

num=int(input())
sum=0
for i in range(1,num):
    if num%i==0:
        sum+=i
if sum==num:
    print("its perfect number")
else:
    print("its not a perfect number")

# 1. Take 3 numbers check if they form right angle triangle
side1=int(input())
side2=int(input())
side3=int(input())
if side1*side1+ side2*side2==side3*side3 or side1*side1+side3*side3==side2*side2 or side2*side2+side3*side3==side1*side1:
    print("its right angle triangle")
else:
    print("its not right angle triangle")

# 2. Check if number is positive and divisible by both 3 and 5

num=int(input())
if num>0:
    if num%3==0 and num%5==0:
        print("the number is positive and divisible by both 3 and 5")
    else:
        print("its not divisible by both 3 and 5")
else:
    print("its not positive")

# 3. Take two numbers and operator + - * /
#    perform that operation using conditions

num1=int(input())
num2=int(input())
op=input("enter the operator")
if op=="+":
    print(num1,"+",num2,"=",num1+num2)
elif op=="-":
    print(num1,"-",num2,"=",num1-num2)
elif op=="*":
    print(num1,"*",num2,"=",num1*num2)
elif op=="/":
    if num2==0:
        print("cannot divide by zero")
    else:
         print(num1,"/",num2,"=",num1/num2)
   
else:
    print("invalid input")

# 4. Check if person can drive and vote
#    drive age above 18, vote age above 18

age=int(input())
if age>=18:
    print("you can drive and vote")
else:
    print("you cannot drive or vote")

# 5. Take month and year check days in that month
#    now include leap year logic

month=input()
year=int(input())
match month:
    case "jan":
        print("january has 31 days")
    case "feb":
        if (year%400==0)or(year%4==0 and year%100!=0):
            print("its leap year")
            print("feb has 29 days")
        else:
            print("feb has 28 days")
    case "march":
        print("march has 31 days")
    case "april":
        print("april has 30 days")
    case "may":
        print("may has 31 days")
    case "june":
        print("june has 30 days")
    case "july":
        print("july has 31 days")
    case "august":
        print("august has 31 days")
    case "september":
        print("september has 30 days")
    case "october":
        print("october has 31 days")
    case "november":
        print("november has 30 days")
    case "december":
        print("december has 31 days")
    case _:
        print("invalid input")

# 6. Check if number is between 1 and 10
#    and also check if it is even

num=int(input())
if num%2==0:
    print(num,"is even")
    if num>=1 and num<=10:
        print(num,"is between 1 and 10 and its even")
    else:
        print(num,"is not between 1 and 10 but its even")
else:
    if num>=1 and num<=10:
        print(num,"is between 1 and 10 but its odd")
    else:
        print(num,"is not between 1 and 10 also its odd")

# 7. Take three numbers check if all equal
#    any two equal or all different
num1=int(input())
num2=int(input())
num3=int(input())
if num1==num2==num3:
    print("all are equal")
elif num1!=num2!=num3!=num1:
    print("all are different")
elif num1==num2:
    print(num1,"and",num2,"are equal")
elif num2==num3:
     print(num2,"and",num3,"are equal")
else:
    print(num1,"and",num3,"are equal")

# 8. Check if character entered is
#    uppercase vowel, uppercase consonant
#    lowercase vowel, lowercase consonant
#    or digit

cha=input("enter a character: ")

vol="aeiouAEIOU"
if vol in cha and cha.isupper():
    print("its vowel and is in uppercase")
elif cha not in vol and cha.isupper():
    print(cha,"is consonent and its uppercase")
elif cha in vol and cha.islower():
     print("its vowel and is in lowercase")
elif cha not in vol and cha.islower():
    print(cha,"is consonent and its lowercase")
elif cha.isnumeric():
    print("digit")

# 10. Take a number check if it is
#     divisible by 2 only
#     divisible by 3 only
#     divisible by both
#     divisible by neither

num=int(input())
if num%2==0 and num%3!=0:
    print(num,"is divisible only by 2")
elif num%2!=0 and num%3==0:
    print(num,"is divisible only by 3")
elif num%2==0 and num%3==0:
    print(num,"is divisible by both 2 and 3")
else:
    print(num,"is not divisible by 2 or 3")

# 11. Check if year is leap year using single if condition
#     without using elif or else

year=int(input())
if (year%400==0) or (year%4==0 and year%100!=0):
    print("its a leap year")

# 12. Take price quantity and membership status
#     member gets 20% discount
#     non member gets 10% if amount above 1000
#     calculate final price

price=int(input("enter the price: "))
quantity=int(input("enter the quantity: "))
membership=input("are you a member(yes/no): ")
amount=price*quantity
if membership=="yes":
    dis_amount=amount*(20/100)
    total=amount-dis_amount
    print("final price =",total)
else:
    if amount>1000:
         dis_amount=amount*(10/100)
         total=amount-dis_amount
         print("final price =",total)
    else:
        print("final price =",amount)

# 13. Check if three sides form
#     equilateral, isoceles or scalene triangle
s1=int(input())
s2=int(input())
s3=int(input())
if s1+s2>s3 and s1+s3>s2 and s2+s3>s1:
    if s1==s2==s3:
        print("its a equilateral triangle")
    elif s1==s2 or s1==s3 or s2==s3:
        print("its isoceles triangle")
    elif s1!=s2 and s2!=s3 and s1!=s3:
        print("its scalene triangle")
else:
    print("its not a triangle")

# 14. Take two numbers check
#     if both divisible by 5
#     if both divisible by 3
#     if first divisible by 5 and second by 3
#     if first divisible by 3 and second by 5

num1=int(input())
num2=int(input())
if num1%5==0 and num2%5==0:
    print("both are divisible by 5")
elif num1%3==0 and num2%3==0:
    print("both are divisible by 3")
elif num1%5==0 and num2%3==0:
    print(num1,"is divisible by 5 and",num2,"is divisible by 3")
elif num1%3==0 and num2%5==0:
     print(num1,"is divisible by 3 and",num2,"is divisible by 5")
else:
    print("they are not divisible by 5 and 3")

# 15. Rock paper scissors result
#     take player1 and player2 choice
#     print who wins using conditions only

p1=input("choose (rock/paper/scissor): ")
p2=input("choose (rock/paper/scissor): ")
if p1=="rock" and p2=="paper":
    print("p2 wins")
elif p1=="paper" and p2=="rock":
    print("p1 wins")
elif p1=="rock" and p2=="scissor":
    print("p1 wins")
elif p1=="scissor" and p2=="rock":
    print("p2 wins")
elif p1=="scissor" and p2=="paper":
    print("p1 wins")
elif p1=="paper" and p2=="scissor":
    print("p2 wins")
elif p1==p2:
    print("Draw")
else:
    print("invalid input")

# 16. Check if number is armstrong number
#     153 = 1³ + 5³ + 3³ = 153

num=int(input("enter a number: "))
sum=0
for i in str(num):
    am=int(i)**3
    sum+=am
if sum==num:
    print("its a armstrong number")
else:
    print("its not armstrong number")

# 19. Nested condition — take number
#     first check if positive
#     if positive check if even or odd
#     if negative check if greater than -10 or not

num=int(input())
if num>0:
    if num%2==0:
        print("its even")
    else:
        print("its odd")
elif num<0:
    if num>-10:
        print("its greater than -10")
    else:
        print("its not")
else:
    print("number is zero")

# 20. ATM machine logic
#     check if pin is correct (use 1234 as pin)
#     if correct check if balance sufficient
#     if sufficient deduct amount and print balance
#     if not sufficient print insufficient balance
#     if pin wrong print wrong pin

pin=int(input("enter your pin: "))
balance_am=20000
if pin!=1234:
    print("invalid pin")
else:
     draw=int(input(("enter the amount to draw: ")))
     if draw>balance_am:
        print("insufficient balance")
     else:
            balance_am-=draw
            print("balance:",balance_am)



            
            

       






         


   






        

   








    




