# # Q1 1.for loop as the range is given to us 
# # 2.while loop as it would never come out of the loop till it is true 
# # 3.for loop as range is given 
# # 4.  while loop as it continue the loop till its value is true            
# # Part B 
# # Q2. 1 2 3 4 5 done 
# # Q3. 1.the result would be continuous printing of i = 1 and i will never end 
# # Q3.2 at last inside the loop i =   i+1 should be there 
# # Q4.output will be Wrong password and access granted both as the last statement of the loop is false  
# #Q5 sum of even number from 1 to n
# n = int(input("Enter the number: "))
# total = 0
# i = 0
# while i%2==0 and i<=n:
#     total +=i
#     i = i + 2

# print("Sum: ", total)
# # #Q6 three attempt password
# password = input("Enter the password: ")
# correct_password = "Theidkwtf"
# attempt = 3
# while attempt>0 and password != correct_password:
#     print("Wrong password. Attempt left: ", attempt)
#     password = input("Enter the password: ")
#     attempt = attempt - 1
# while attempt==0 and password!=correct_password:
#     print("Too many wrong attempt. try again after 1hour")
#     password = input("Enter the password: ") 
# while attempt>=0 and password == correct_password:
#     print("ACCESS GRANTED") 
#     break
# #exercise 1 print 1-10
# for i in range(1,11):
#     print(i)
# #by while loop
# i=1
# while i<=10:
#     print(i)
#     i=i+1
# #exercise 2 10 to 1 
# i = 10
# while i>0:
#     print(i)
#     i = i-1
# # exercise 3 print even number
# i=0
# for i in range(1,21):
#        i=i+1
#        if i%2==0:
#               print(i)
            

# #problem 4 sum using while loop
# n= int(input("Enter the number: "))
# i=1
# total=0
# while i in range(1,n+1):
#     total += i
#     i=i+1
# print("sum: ",total)
#  #problem 5 multiplication table
# num=int(input("Enter the number: "))
# i=1
# for i in range(1,11):
#     print(i*num)
# #by while loop
# num=int(input("Enter the number: "))
# i=1
# while i<=10:
#     print(i*num)
#     i=i+1

#exercise 6
n=int(input("Enter the number: "))
i=2
count=0
while  i<=n :
    
    i=i+2
    count = count + 1
print("There are ",count,"even number") 