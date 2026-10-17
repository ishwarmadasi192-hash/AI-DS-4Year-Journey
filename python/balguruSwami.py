# # #q1. area of circle
# # r=float(input("enter the radius: "))
# # area = 3.14*r*r
# # print("The area of the circle is: ",area)
# # #Q2 roots of quadratic equation
# import math
# a=float(input("Enter a: "))
# b=float(input("Enter b: "))
# c=float(input("Enter c: "))
# D=b**2-4*a*c
# if a==0:
#      print("This is not quadratic equation")
# elif(D>0):
#      root1=(-b+math.sqrt(D))/(2*a)
#      root2=(-b-math.sqrt(D))/(2*a)
#      print("Two distinct real roots: ",root1,root2)
# elif D==0:
#      root=-b/(2*a)
#      print("Real and equal root: ",root)
# else:
#      real=-b/(2*a)
#      imaginary=math.sqrt(-D)/abs(2*a)
#      print("Complex roots: ",real,"+",imaginary,"i")
#      print("Complex roots: ",real,"-",imaginary,"i")
# #Q3. simple intrest
# p=int(input("Enter the principle amount: " ))
# t=float(input("Enter the time peroid: "))
# r=float(input("Enter the rate: "))
# intrest=(p*r*t)/100
# print("The simple intrest is: ",intrest)
# # Q4, compound intrest
# p=float(input("Enter the principle amount: "))
# r=float(input("Enter the rate: "))
# t=float(input("Enter the time peroid: "))
# n=int(input("Enter the number of time intrest is compounded per year: "))
# compound_intrest=p*(1+(r/100)**n)-p
# print("Your compound intrest is : ",compound_intrest)
# # # # Q5 sum of digit of 3 digit number

# or in one liner
# num=int(input("Enter any number: "))
# sum=sum(int(digit) for digit in str(num))
# print("The sum of the digit is: ",sum)

# #Q6. leap year
# year=int(input("Enter the year: "))
# if year%4==0:
#     print("The year is leap year.")
# else:
#     print("The year is not leap year")

# #Q7student grade
# marks=int(input("Enter the marks: "))
# if marks>=90:
#     print("O") 
# elif 80<marks<90:
#     print("E") 
# elif 70<marks<80:
#     print("A") 
# elif 60<marks<70:
#     print("B") 
# elif 50<marks<60:
#     print("C") 
# elif 40<marks<50:
#     print("D") 
# else:
#     print("F") 
# # #Q8 3 point collinear
# x1=int(input("Enter the coordinate x1: "))
# y1=int(input("Enter the coordinate y1: "))
# x2=int(input("Enter the coordinate x2: "))
# y2=int(input("Enter the coordinate y2: "))
# x3=int(input("Enter the coordinate x3: "))
# y3=int(input("Enter the coordinate y3: "))
# area=x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2)
# if area==0:
#     print("The points are collinear")
# else:
#     print("Points are not collinear")
# # #Q9 given age find out correct no. of days ,months,years
# # age=int(input("Enter the age: "))
# # birth_year=2026-age
# # print("Birth year")
# # days = 

# #Q 10 calculate no of digit in a number
# method 1 string conversion 
# n=int(input("Enter the number: "))
# digit=len(str(abs(n)))
# print("The number of digit in the number is: ",digit)
# # method 2 maths
# n=int(input("Enter the number: "))
# if n==0:
#     digit=1
# else:
#     digit=0
#     temp=abs(n)
# while temp>0:
#     temp=temp//10
#     digit+=1
# print("The number of digits in number is: ",digit)
# #Q 11 sum of even number till n
# n=int(input("Enter the number: "))
# total=0
# i=2
# while i<=n:
#     total+=i
#     i=i+2
# print(total)
# # # Q12 sum of n number but the odd digit are in factorial
# # n=int(input("Enter the number: "))
# # total=0
# # i=1
# # fact=0
# # while i<=n:
# #     if i%2!=0:
# #         fact+=1
# #         i+=1
# #         break
# # else:
# #         total+=fact   
     


# # Q13 find the sum of series in the form of 1*2+2*3+3*4.........

# # Q14 find wether the number is armstrong

# #Q15 sum of prime number from 1 to 200
# total=0
# for num in range(2,201):
#     is_prime=True
#     for i in range(2,num):
#         if num%i==0:
#             is_prime=False
#             break
#     if is_prime:
#             total+=num
# print("Sum of all prime number is: ",total)
# # Q16 display the number in words
# from num2words import num2words
# num=int(input("Enter the number: "))
# output=num2words(num)
# print("your text number is: ",output)
# #Q17 find the sum of square of odd numbers 
# n=int(input("Enter the number: "))
# total=0
# i=1
# while i<=n:
#     total+=(i*i)
#     i+=2
# print(total)

