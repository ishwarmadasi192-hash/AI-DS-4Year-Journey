#problem 1 even or odd
num = int(input("ENter the number: "))
if num % 2 == 0 :
    print("EVEN NUMBER")
else:
    print("ODD NUMBER")

#2.Positive,Negative,Zero
num = int(input("Enter the Number: "))
if num>0:
    print("Positive number")
elif num<0:
    print("Negative number")
else:
    print("Zero")
#3Multiplication table
num = int(input("Enter the number: "))
for i in range(1,11):
    print(num,"*",i,"=",num*i)
#4. sum of first n natural number 

n = int(input("Enter n: "))
total = 0
for i in range(1,n+1):
    total += i
    print(total)

# 5. Tough one it is caleed fizzBuzz problem
n = int(input("Enter n:"))

for i in range(1, n + 1):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)