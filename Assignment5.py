#WAP to determine input number is even or odd 


num=int(input("enter a number:"))
if num%2==0:
    print(f"{num} is even")
else:
    print(f"{num} is odd")

#find out if a given year is leap year or not

year=2004
if year%4==0:
    print("leap year")
else:
    print("not leap year")

#write a program to check if a triangle valid or not.(input-3 angles of triangle)

p=int(input(f"enter first angle"))
q=int(input(f"enter second angle"))
r=int(input(f"enter third angle"))
sum=p+q+r
if sum==180:
    print("triangle is valid")
else: 
    print("triangle is not valid")   


#WAP to determine if the seller has made profit or loss.Display amount of profit/loss.(input:cost price and selling price)
cost_price=float(input(f"enter the costprice"))
selling_price=float(input(f"enter the selling price"))
if selling_price>cost_price:
    print(f"profit {selling_price-cost_price}")
else :
    print(f"loss {cost_price-selling_price}") 

#WAP to determine if the given number is the armsrtong number or not(153 is the Armstrong as 1^3+5^3+3^3
#determibe if the input number is positive or negative
 
num=int(input("enter a number:"))
if num>0:
    print(f"positive number")
else:
    print(f"negative number")    

#WAP to check if a candidate is eligibal for voting or not
 
age=20
if age>=18:
    print("eligibal for voating")
else:
    print("not eligibal for voating")      

#WAP to find largest among 3 numbers
num1=50
num2=40
num3=30
if num1>num2 and num1>num3:
    print(f"largest num is num1")
elif num2>num1 and num2>num3:
    print(f"largest num is num2")
if num3>num1 and num>2:
    print(f"largest num is num3")

#categorize the person depending on the haight
# a.<150        Dwarf
# b.=150        avrage heighted
# c.>=165       tall

height=175
if height<150:
    print("dwarf")
elif height==150:
    print("avrage heighted")
if height>=165:
    print("tall")           

#WAP to accept coordinate of a point and determine in which quadrant it lies

#WAP to check if the alphabet is a vowel or consonant
ch='a'
if (ch=='a'or ch=='e'or ch=='i'or ch=='o'or ch=='u'):
    print("vowel")
else:
    print("consonant")


match=int(input(f"enter the month number"))   
match month:

    case 1:
        print("january  and  31days")
    case 2:
        print("february  and  30days")
    case 3:
        print("march and  31days")
    case 4:
        print("april and  30days") 
    case 5:
        print("may and  31days")
    case 6:
        print("june and  30days") 
    case 7:
        print("july and  31days") 
    case 8:
        print("augest  and  31days") 
    case 9:
        print("september  and  30days") 
    case 10:
        print("october  and  31days") 
    case 11:
        print("november  and  30days") 
    case 12:
        print("desember  and  31days")

# accept marital status and print miss or mrs in front of name

#write a menu driven program for following
# .area of circle(pi*r^2)
# .area of rectangle(l*b) 
# .area of tringle(b*h/2)
# .area of square(a^2)

num = 5 
match num:
    case 1:
        r=4
        pi=3.14
        ans=pi*r
        print(f"area of circle {ans}")
    case 2:8
        l=4
        b=3
        ans=l*b
        print(f"area of rectangle {ans}")
    case 3:
        b=4
        h=3
        ans=b*h/2
        print(f"area of triangle {ans}")
    case 4:
        side=3
        side=3
        ans=side*side
        print(f"area of square {ans}")        