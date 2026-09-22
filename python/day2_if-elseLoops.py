#1. if-else statement
age = int(input("Enter your age: "))
if age >= 18:
   print("You are an adult")
else:
   print("You are minor")
   #1.example of 1 
   score  = int(input("Enter your score: "))
   if score >= 90:
       print("Grade: A")
   elif score >= 80:
       print("Grade: B")
   elif score >= 70:
       print("Grade: C")
   elif score >= 60:
       print("Grade: D")
   else:
       print("Grade: F")
#2.for loop in python
for i in range(1,11):
    print(i)



# example of 2
for i in range(1,11):
    print(i)

    n=int(input("ENter n: "))
    total = 0
    for i in range(1,n+1):
       total += i
    print("sum: ", total)

    #by chatgpt
age = int(input("Enter the age: "))
if age>=18:
        print("You are eligible to vote")
else :
        print("You are not eigible to vote.")
#Exercise 1
n = int(input("Enter the number: "))
if n>0:
        print("Positive")
elif n==0:
        print("Zero")

else:
        print("Negative")

#even or odd
n=int(input("Enter the number: "))
if n%2==0:
        print("Your number is even")

else:
        print("Youe number is odd")

#Largest of two number 
n1=int(input("Enter the n1: "))
n2=int(input("Enter the n2: "))
if n1-n2>0:
        print(n1)
else :
        print(n2)
#Grade calculation
n=int(input("Enter your Grade: "))
if n>85:
        print("A+")
elif 70<n>85:
        print("A")
elif 60<n>70:
        print("B")
elif 50<n>60:
        print("C")

        

