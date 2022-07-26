#1 WAP to demonstrate use of arithmatic oprators(numeric as well as str object)

print(f"\n {'='*10}Arithmatic Operators{'='*10}")

num1=int(input("enter first number :"))
num2=int(input("enter first number :"))

print(f"\{'='*10}Result {'='*10}")
print(f"Addition : {num1+num2}")
print(f"Substrction : {num1-num2}")
print(f"Division : {num1/num2}")
print(f"Modulo : {num1+num2}")
print(f"ClearFloor Division : {num1//num2}")
print(f" {num1} raised to {num2} :{num1**num2}")
#2 WAP to demonstrate use of assignment opration(numeric as well as str object)

print(f"\n {'='*10}Assignment Operators{'='*10}")
a = 5
print(f"value of a:{a}")
a += 5
print(f"after a+= :{a}")
a -= 5
print(f"after a-=: {a}")
a *= 5
print(f"after a*=: {a}")
a **=5
print(f"after a**=: {a}")
a /=5
print(f"after a/= : {a}")
a //=5
print(f" after a//=  :{a}")
a %=5
print(f" after a%=  :{a}")

#3 WAP to demonstrate use of comparison oprator(numeric as well as str object)
print(f"\n{'='*10}Comparison operator{'='*10}")
num1 = int(input("enter first number"))
num2 = int(input("enter second number"))
print(f"\n{'='*10}Result{'='*10}")
print(f"{num1}>{num2}: {num1>num2}")
print(f"{num1}<{num2}: {num1<num2}")
print(f"{num1}>={num2}: {num1>=num2}")
print(f"{num1}<={num2}: {num1<=num2}")
print(f"{num1}=={num2}: {num1==num2}")
print(f"{num1}!={num2}: {num1!=num2}")

#4 WAP to demonstrate use of logical oprators(numeric as well as str object)

print(f"\n{'='*10}logical oprators{'='*10}")
result = num1 >=30 and num1 <=50
result1 = num1 >=30 and num1 <=50
print(f"{num1} >=30 and {num1} <=50: {result}")
print(f"{num1} >=30 or {num1} <=50: {result1}")
print(f" not {num1} >=21 and : {not num1>21}")