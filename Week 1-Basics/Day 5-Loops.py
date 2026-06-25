# 1. Print numbers from 1 to 10
for i in range (1,11):
    print(i)

# 2. Print numbers from 10 to 1 (reverse)
for i in range(10,0,-1):
    print(i)

# 3. Print first 10 even numbers
for i in range(2,21,2):
    print(i)

# 4. Print first 10 odd numbers
for i in range(1,21,2):
    print(i)

# 5. Print numbers from 1 to 50 using while loop
i=1
while i<51:
    print(i)
    i+=1

# 6. Print your name 5 times using loop
name=input("enter your name: ")
for i in range(5):
    print(name)
    i+=1

# 7. Print multiplication table of 5
num=int(input("enter a number: "))
for i in range(1,11):
    print(num,"x",i,"=",num*i)
    i+=1

 #9. Print sum of numbers from 1 to 10
sum=0
for i in range(1,11):
    sum+=i
    print(sum)

# 10. Print sum of numbers from 1 to 100
sum=0
for i in range(1,101):
    sum+=i
print(sum)

# 11. Print all numbers from 1 to 20 that are divisible by 3
for i in range(1,21):
    if i%3==0:
        print(i)

# 12. Count how many numbers between 1 and 50 are even
count=0
for i in range(1,51):
    if i%2==0:
        count+=1
print("there are",count,"even numbers between 1 to 50")

# 13. Print squares of numbers from 1 to 10
for i in range(1,11):
    p=i**2
    print(p)

# 14. Print cubes of numbers from 1 to 5
for i in range(1,6):
    c=i**3
    print(c)

# 15. Print numbers from 1 to 10 except number 5 (use continue)
for i in range(1,11):
    if i==5:
        continue
    print(i)

# 16. Print numbers from 1 to 10 but stop at 7 (use break)
for i in range(1,11):
    if i==7:
        break
    print(i)

# 17. Print "Hello" 10 times using for loop
for i in range(10):
    print("hello")

# 18. Print numbers from 100 to 1 in steps of 10
for i in range(100,0,-10):
    print(i)

# 19. Take a number print all numbers from 1 to that number
num=int(input("enter a number: "))
for i in range(1,num+1):
    print(i)

# 20. Print all even numbers between 1 and 30 using while loop
i=1
while i<=30:
    if i%2==0:
        print(i)
    i+=1

# 1. Print sum of all even numbers from 1 to 50
sum=0
for i in range(1,51):
    if i%2==0:
        sum+=i
print(f"result= {sum}")

# 2. Print sum of all odd numbers from 1 to 50
sum=0
for i in range(1,51,2):
    sum+=i
print("result=",sum)

# 3. Find factorial of a number using loop
mul=1
num=int(input("enter a number: "))
for i in range(num,0,-1):
    mul*=i
print("factorial=",mul)

# 4. Print Fibonacci series up to 10 terms
current=0
previous=1
for i in range(10):
    print(current)
    res=current+previous
    current=previous
    previous=res

# 5. Count total digits in a number using loop
num=int(input("enter a number: "))
s=str(num)
print("total number of digits in",num,"is",len(s))

#using loop

num=int(input())
count=0
for i in num:
    count+=1
print(count)

# 6. Print sum of digits of a number
num=input()
sum=0
for i in num:
    sum+=int(i)
print(sum)

# 7. Reverse a number using loop (without string)
num=int(input())
rev=0
while num>0:
    digit=num%10
    rev=rev*10+digit
    num=num//10
print(rev)

# 8. Check if a number is prime using loop
num=int(input())
if num<=0:
    print("not prime")
else:
    for i in range(2,num):
        if num%i==0:
            print("not prime")
            break
    else:
        print("its prime")

# 9. Print all prime numbers between 1 and 50
for i in range(2,51):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i)

# 10. Print all factors of a number using loop
num=int(input())
for i in range(1,num+1):
    if num%i==0:
        print(i)

# 11. Find largest number in a list using loop
l=[3,2,29,15,48]
largest=l[0]
for i in l:
    if i>largest:
        largest=i
print("largest=",largest)

# 12. Find smallest number in a list using loop
l=[3,2,29,15,48]
smallest=l[0]
for i in l:
    if i<smallest:
        smallest=i
print("smallest=",smallest)

# 13. Count vowels in a string using loop
s="abcdefg"
vo="aeiouAEIOU"
count=0
for i in s:
    if i in vo:
        count+=1
print(count)

# 14. Print each character of a string using loop
s="fjqoxlaid"
for i in s:
    print(i)

# 15. Print pattern:
#     *
#     **
#     ***
#     ****

rows=int(input("enter number of rows: "))
for i in range(1,rows+1):
    print('*'*i)

# 16. Print pattern:
#     ****
#     ***
#     **
#     *

rows=int(input("enter number of rows: "))
for i in range(rows,0,-1):
    print("*"*i)

# 17. Take 5 numbers from user using loop and find their sum
sum=0
for i in range(5):
    num=int(input("enter a number: "))
    sum+=num
print("sum:",sum)

# 18. Print multiplication table from 1 to 10 (all tables
num=int(input("enter a number: "))
for num in range(1,11):
    print("table of=",num)
    for i in range(1,11):
        print(num,"x",i,"=",num*i)

# 19. Find average of numbers from 1 to 100 using loop
sum=0
for i in range(1,101):
    sum+=i
avg=sum/100
print("average=",avg)

# 20. Count how many times a digit appears in a number
num=input("enter a number: ")
digit=input("enter a digit to find: ")
count=0
for i in num:
    if i == digit:
        count+=1
print(digit,"appears",count,"times")

# 1. Check if a number is Armstrong number using loop
sum=0
num=input("enter a number: ")
for i in num:
    di=int(i)**len(num)
    sum+=di
if sum==int(num):
    print(num,"is a armstrong number")
else:
    print(num,"is not a armstrong number")

# 2. Print all Armstrong numbers between 1 and 1000
for num in range(1,1001):
    total=0
    for i in str(num):
        total+=int(i)**len(str(num))
    if total==num:
        print(num)

# 3. Find GCD of two numbers using loop
num1=int(input("enter a number: "))
num2=int(input("enter a number: "))
for i in range(1,min(num1,num2)+1):
    if num1%i==0 and num2%i==0:
        gcd=i
print("gcd=",gcd)

# 4. Find LCM of two numbers using loop
num1=int(input("enter a number: "))
num2=int(input("enter a number: "))
lcm=max(num1,num2)
while True:
    if lcm%num1==0 and lcm%num2==0:
        print("lcm=",lcm)
        break
    lcm+=1

# 5. Print pyramid pattern:
#       *
#      ***
#     *****

rows=int(input("enter number of rows: "))
for i in range(1,rows+1):
    print(" "*(rows-i)+"*"*(2*i-1))

# 6. Print number pattern:
#     1
#     1 2
#     1 2 3
#     1 2 3 4
rows=int(input("enter number of rows: "))
for i in range(1,rows+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

# 20. Print triangle pattern with numbers:
#     1
#     2 3
#     4 5 6
#     7 8 9 10

rows = int(input("enter rows: "))

num = 1

for i in range(1, rows + 1):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()

# 7. Check if a number is palindrome using loop (without string)
num=int(input("enter a number: "))
original=num
rev=0
while num>0:
    digit=num%10
    rev=rev*10+digit
    num=num//10
if original==rev:
    print("palimdrome")
else:
    print("not palimdrome")

# 8. Print all palindrome numbers between 1 and 1000
for num in range(1,1001):
    original=num
    temp=num
    while temp>0:
        digit=temp%10
        rev=rev*10+digit
        temp=temp//10
        if rev==original:
            print(original)

# 9. Find second largest number in a list using loop
lis=[12,34,11,56,33]
largest=lis[0]
second=lis[0]
for i in lis:
    if i>largest:
        second=largest
        largest=i
    elif i>second and i!=largest:
        second=i
print("second largest:",second)

# 10. Print Fibonacci series until a number user enters
num=int(input("enter a number: "))
a=0
b=1
while a<=num:
    print(a,end=" ")#end prints o/p horizontally(in one line)
    c=a+b
    a=b
    b=c

# 11. Count how many prime numbers between 1 and 100
count=0
for num in range(2,101):
    for i in range(2,num):
        if num%i==0:
            break
        else:
            count+=1
print(count)

# 12. Sum of even and odd numbers separately from 1 to 100
even_sum=0
odd_sum=0
for i in range(1,101):
    if i%2==0:
        even_sum+=i
    else:
        odd_sum+=i
print("even sum:",even_sum)
print("odd_sum:",odd_sum)

# 13. Find sum of squares from 1 to 10
sum=0
sq=1
for i in range(1,11):
    sq=i**2
    sum+=sq
print("sum:",sum)

# 15. Find power of a number using loop (without **)
base=int(input("enter the base: "))
power=int(input("enter the power: "))
sq=1
for i in range(power):
    sq*=base
print(sq)

# 16. Check if number is perfect number using loop
num=int(input("enter a number: "))
sum=0
for i in range(1,num):
    if num%i==0:
        fac=i
        sum+=fac
if sum==num:
    print("its a perfect number")
else:
    print("its not a perfect number")

# 17. Print multiplication table only for even numbers 1-10
for num in range(2,11,2):
    for i in range(1,11):
        print(num,"x",i,"=",num*i)
    

# 18. Reverse a string using loop (without slicing)
s=input("enter a string: ")
rev=""
for ch in s:
    rev=ch+rev
print("reverse=",rev)

             #or
s=input("enter a string: ")
for i in range(len(s)-1,-1,-1):
    print(i)


# 19. Count frequency of each digit in a number
digit=input()
for i in digit:
    count=0
    for j in digit:
        if i==j:
            count+=1
    print(i,"=",count)




        




    













    


    





    
    



    




       
















      
    
      
  


    