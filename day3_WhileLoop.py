#While Loop
i = 1
while i <= 5:
    print(i)
    i = i + 1
# problem 2 : sum of 1 to n 
n = int(input("Enter the number: "))
i = 1
total = 0
while i <= n:
    total += i
    i = i + 1
    print("SUM: ", total)
# problem 3 : countdown
n=int(input("Enter the timer: "))
i = n
while 0<=i<=n:
    print(i)
    i = i - 1 
# problem 4 : passwoed checker
password = input("Enter the password: ")
correct_password = "TheNoob-09"

while password != correct_password:
    print("Wrong password.Try Again")
    password = input("Enter the password: ")

print("Access granted")
          
