#Exercise 1
for i in range(1,4):
    for j in range(1,4):
        print(i, j)
# #Exercise 2
for i in range (4):
  for j in range (4):
    print("*",end="")
  print()

#using of end""
for i in range(1):
  for j in range(4):
    print("*",end="")
  print()
for i in range (3):
    for j in range(4):
        print("*", end="")
    print()
#problem 3 
for i in range(1,6):
    for j in range(i):
        print("*",end="")
    print()
#problem 4
for i in range(1,6):
    for j in range(i):
     print(j,end="")
    print()
#problem 5
for i in range(1,6):
    for j in range(1,11):
        print(i,"*",j,"=",i*j)
#problem 6
n=int(input("Enter the number: "))
i=1
total=0
while i<=n:
    t=i*i 
    total+=t
    i+=1
print("Sum: ",total)

    