# Q1 1.for loop as the range is given to us 
# 2.while loop as it would never come out of the loop till it is true 
# 3.for loop as range is given 
# 4.  while loop as it continue the loop till its value is true            
# Part B 
# Q2. 1 2 3 4 5 done 
# Q3. 1.the result would be continuous printing of i = 1 and i will never end 
# Q3.2 at last inside the loop i =   i+1 should be there 
# Q4.output will be Wrong password and access granted both as the last statement of the loop is false  
#Q5 sum of even number from 1 to n
n = int(input("Enter the number: "))
total = 0
i = 0
while i%2==0 and i<=n:
    total +=i
    i = i + 2

print("Sum: ", total)
# #Q6 three attempt password
password = input("Enter the password: ")
correct_password = "Theidkwtf"
attempt = 3
while attempt>0 and password != correct_password:
    print("Wrong password. Attempt left: ", attempt)
    password = input("Enter the password: ")
    attempt = attempt - 1
while attempt==0 and password!=correct_password:
    print("Too many wrong attempt. try again after 1hour")
    password = input("Enter the password: ") 
while attempt>=0 and password == correct_password:
    print("ACCESS GRANTED") 
    break