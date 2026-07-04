# 1. Create variables for your name, age, city and print them
name="supreeth"
age=22
city="Bangalore"
print("my name is",name)
print("i am",age,"years old!")
print("I live in",city)

# 2. Create a variable and change its value 3 times
vari="abc"
vari=34
vari=3.14
print(vari)

# 3. Store your height in meters as float and print it
height=3.5
print(" my height is:",height,"m")

# 4. Create a boolean variable called is_student and print it
is_student=True
print(is_student)

# 5. Print the type of these values: 42, 3.14, "hello", True
integer=42
floating=3.14
string="hello"
boolean=True
print(type(integer))
print(type(floating))
print(type(string))
print(type(boolean))

# 6. Store your first and last name separately and join them
name1="supreeth"
name2="Murthy"
print(name1,""+name2)

# 7. Store price as 99.99 and quantity as 5, calculate total
price=99.99
quantity=5
total=price*quantity
print("Total:",total)

# 8. Take your age and calculate what year you were born
age=int(input("enter your age: "))
current_year=2026
year_born=current_year-age
print("The year you were born is:",year_born)

# 9. Create a variable with value 10, another with 3
#    print their sum, difference, multiply, divide
a=10
b=3
sum=a+b
diff=a-b
mul=a*b
div=a/b
print(a,"+",b,"=",sum)
print(a,"-",b,"=",diff)
print(a,"*",b,"=",mul)
print(a,"/",b,"=",div)

# 10. Store "Hello" in a variable, print it 3 times using *
a="Hello"
print((a+"\n")*3)

# 11. What happens when you add integer and float? Try it
a=5
b=4.3
c=a+b
print(c)
print(type(c))

# 12. Can you store True + True? What answer do you get?
a=True+True
print(a)
print(type(a))

# 13. What is type of 5/2? And type of 5//2? Why different?
a=5/2
print(a,type(a))#float
b=5//2
print(b,type(b))#integer

# 14. Create variable x = 10, now swap it with y = 20
#     without using third variable
x=10
y=20
x,y=y,x # swap in one line
print(x)
print(y)

# 15. What happens when you multiply string by integer?
a="hello"
b=3
print(a*b)