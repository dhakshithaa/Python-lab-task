#if else
#even or odd
a=int(input("Enter a:"))
if a%2==0:
    print("even")
else:
    print("odd")
#eligible to vote >=18
a=int(input("enter a:"))
if a>=18:
    print("eligible")
else:
    print ("not eligible")
# pass or fail >=40
a=int(input("Enter a:"))
if a>=40:
    print("pass")
else:
    print("fail")
#positive or negative
a=int(input("Enter a:"))
if a>0:
    print("positive")
else:
    print("negative")
#elif
#grade based mark
a=int(input("Enter a:"))
if a>=90:
    print("well done")
elif a>=85:
    print("good")
elif a>=50:
    print("should improve")
else:
    print("fail")
# calculator operation (+, -, *, /)
# division
a=int(input("Enter a:"))
if a/2==0 or a/5==0:
     print ("done")
else:
     print("not")

#subraction
#2
a=int(input("Enter a:"))
if a-4==0 or a-9==0:
     print ("done")
else:
     print("not")
# addition
#3
a=int(input("Enter a:"))
if a+4==0 or a+9==0:
     print ("done")
else:
     print("not")
#multiplication
#4
a=int(input("Enter a:"))
if a*4==0 or a*9==0:
     print ("done")
else:
     print("not")
# largest among three numbers
a=int(input("Enter a:"))
b=int(input("Enter b:"))
c=int(input("Enter c:"))
if a<=b:
    print("greater")
elif b<=c:
    print("greater")
else:
    print("low")
#Nested if-else
#check the username and password arew correct
u=int(input("enter the username:"))
p=int(input("Enter the password:"))
if u== varaxx02:
     print("enter password")
        if p== 20954:
           print("Login success")
        else:
           print("invalid password")
else:
    print("Invalid username")
#Traffic Signal System
print(" Red → Stop")
print("Yellow → Get Ready")
print("Green → Go")
#If invalid signal → print error
r=int(input("enter red:"))
if r==0:
    print("stop")
    y=int(input("enter yello:"))
    if y==0:
        print("get ready")       
        g=int(input("enter green:"))
        if g==0:
            print("GO")
