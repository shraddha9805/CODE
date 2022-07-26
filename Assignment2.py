#1Assing three differnt values to three different variable and the print them

name,roll_no,percentage = "Shraddha",39,86.80
print(name)
print(roll_no)
print(percentage)

#2 Write a program to demonstrate single and multiple assignment of values to a variable

a=10,20,30
print(a)
#3Write a program to swap two varaibles

a,b = 20,10
print(f"a,b")
a,b = 20,10
print(f"a,b")

#4Write a program to demostrate that a single variable can store different type of values at different instance of time
 
#5wite a program to concatenate two string
 
name ='abdul kalam'
print("wings of fire book writer "+name) 

#6WAP to assign different type of one varible at diffrent instance of and input its type each time

#7 Write a program to calculate simple interest.Accept values from user.(si=pnr/100)

p=float(input("enter the principle amount"))
n=float(input("enter the rate amount"))
r=float(input("enter the year amount"))
si=(p*n*r/100)
print(si) 

#8  

#int to float
print(f"\n{'='*9}int to float {'='*9}")
a=20
print(f"{a} \t\t {type(a)}")
a=float(a)
print(f"{a} \t\t {(type(a))}")
print(f"\n{'='*30}")

#int to bool

print(f"\n{'='*9}int to bool {'='*9}")
a=20
print(f"{a} \t\t {type(a)}")
a=bool(a)
print(f"{a} \t\t {type(a)}")
print(f"\n{'='*30}")

#int to complex

print(f"\n{'='*9}int to  complex #{'='*9}")
a=20
print(f"{a} \t\t {type(a)}")
a=complex(a)
print(f"{a} \t\t {type(a)}")
print(f"\n{'='*30}")

#int to str

print(f"\n{'='*9}int to str {'='*9}")
a=20
print(f"{a} \t\t {type(a)}")
a=str(a)
print(f"{a} \t\t {type(a)}")
print(f"\n{'='*30}")

#float to int

print(f"\n{'='*9} float to int {'='*9}")
a=20.0
print(f"{a} \t\t {type(a)}")
a=int(a)
print(f"{a} \t\t {type(a)}")
print(f"\n{'='*30}")

#float to float

print(f"\n{'='*9}float to float {'='*9}")
a=20.0
print(f"{a} \t\t {type(a)}")
a=float(a)
print(f"{a} \t\t {type(a)}")
print(f"\n{'='*30}")

#float to bool

print(f"\n{'='*9}float to bool {'='*9}")
a=20.0
print(f"{a} \t\t {type(a)}")
a=bool(a)
print(f"{a} \t\t {type(a)}")
print(f"\n{'='*30}")

#float to complex

print(f"\n{'='*9}float to complex {'='*9}")
a=20.0
print(f"{a} \t\t {type(a)}")
a=complex(a)
print(f"{a} \t\t {type(a)}")
print(f"\n{'='*30}")

#float to str

print(f"\n{'='*9}float to str {'='*9}")
a=20.0
print(f"{a} \t\t {type(a)}")
a=str(a)
print(f"{a} \t\t {type(a)}")
print(f"\n{'='*30}")

#bool to int

print(f"\n{'='*9}bool to int {'='*9}")
a=False
print(f"{a} \t\t {type(a)}")
a=int(a)
print(f"{a} \t\t {type(a)}")
print(f"\n{'='*30}")

#bool to float

print(f"\n{'='*9}bool to float {'='*9}")
a=True
print(f"{a} \t\t {type(a)}")
a=float(a)
print(f"{a} \t\t {type(a)}")
print(f"\n{'='*30}")

#bool to bool

print(f"\n{'='*9}bool to bool {'='*9}")
a=False
print(f"{a} \t\t {type(a)}")
a=bool(a)
print(f"{a} \t\t {type(a)}")
print(f"\n{'='*30}")

#bool to complex

print(f"\n{'='*9}bool to complex {'='*9}")
a=True
print(f"{a} \t\t {type(a)}")
a=complex(a)
print(f"{a} \t\t {type(a)}")
print(f"\n{'='*30}")

#bool to str

print(f"\n{'='*9}bool to str {'='*9}")
a=False
print(f"{a} \t\t {type(a)}")
a=str(a)
print(f"{a} \t\t {type(a)}")
print(f"\n{'='*30}")

#str to int

print(f"\n{'='*9}str to int {'='*9}")
a='9'
print(f"{a} \t\t {type(a)}")
a=complex(a)
print(f"{a} \t\t {type(a)}")
print(f"\n{'='*30}")


#str to float

print(f"\n{'='*9}str to float {'='*9}")
a='9'
print(f"{a} \t\t {type(a)}")
a=float(a)
print(f"{a} \t\t {type(a)}")
print(f"\n{'='*30}")

#str to bool

print(f"\n{'='*9}str to bool {'='*9}")
a='9'
print(f"{a} \t\t {type(a)}")
a=bool(a)
print(f"{a} \t\t {type(a)}")
print(f"\n{'='*30}")

#str to complex

print(f"\n{'='*9}str to complex {'='*9}")
a='9'
print(f"{a} \t\t {type(a)}")
a=complex(a)
print(f"{a} \t\t {type(a)}")
print(f"\n{'='*30}")

#str to str

print(f"\n{'='*9}str to str {'='*9}")
a='9'
print(f"{a} \t\t {type(a)}")
a=str(a)
print(f"{a} \t\t {type(a)}")
print(f"\n{'='*30}")

#complex to int

#complex to float

#complex to bool

print(f"\n{'='*9}complex to bool{'='*9}")
a=+0j
print(f"{a} \t\t {type(a)}")
a=bool(a)
print(f"{a} \t\t {type(a)}")
print(f"\n{'='*30}")

#complex to complex

print(f"\n{'='*9}complex to complex {'='*9}")
a=+0j
print(f"{a} \t\t {type(a)}")
a=complex(a)
print(f"{a} \t\t {type(a)}")
print(f"\n{'='*30}")

#complex to str

print(f"\n{'='*9}complex to str {'='*9}")
a=+0j
print(f"{a} \t\t {type(a)}")
a=str(a)
print(f"{a} \t\t {type(a)}")
print(f"\n{'='*30}")
