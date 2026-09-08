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
