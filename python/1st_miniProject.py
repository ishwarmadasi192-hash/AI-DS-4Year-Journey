# name=input("Enter your name: ")
# m1=int(input("Enter your Maths marks: "))
# m2=int(input("Enter your Physics marks: "))
# m3=int(input("Enter your Chemistry marks: "))
# print(name)
# total = m1+m2+m3
# print("Your total is: ",total)
# average = total/3
# print("aYour average marks are: ",average)
# percentage= total/3
# print("Your Percentage is: ",percentage,"%")

# #by if else 
# name=input("Enter your name: ")
# m1=int(input("Enter your Maths marks: "))
# m2=int(input("Enter your Physics marks: "))
# m3=int(input("Enter your Chemistry marks: "))
# print(name)
# total = m1+m2+m3
# print("Your total is: ",total)
# average = total/3
# print("aYour average marks are: ",average)
# percentage= total/3
# print("Your Percentage is: ",percentage,"%")
# if percentage>45:
#     print("You are passed.")
# else :
#     print("Failed!")
# if m1>40 and m2>40 and m3>40:
#     print("You are passed in all subject ")
# elif m1>40 and m2>40 and m3<40:
#     print("You are failed in 1 subject")
# elif m1>40 and m2<40 and m3>40:
#     print("You are failed in 1 subject")
# elif m1<40 and m2>40 and m3>40:
#     print("You are failed in 1 subject")
# elif m1>40 and m2<40 and m3<40:
#     print("You are failed in 2 subject")
# elif m1<40 and m2>40 and m3<40:
#     print("You are failed in 2 subject")
# elif m1<40 and m2<40 and m3>40:
#     print("You are failed in 2 subject")
# elif m1<40 and m2<40 and m3<40:
#     print("You are failed in 3 subject")

  # by loop in list
n1=int(input("Enter the number: "))
n2=int(input("Enter the number: "))
n3=int(input("Enter the number: "))
n4=int(input("Enter the number: "))
n5=int(input("Enter the number: "))
marks=[n1,n2,n3,n4,n5]
total=0
counter=0
odd_counter=0
highest=marks[0]
lowest=marks[0]
for mark in marks:
    total+=mark
    average=total/len(marks)
    if mark % 2 == 0:
        odd_counter+=1
    else:
        counter+=1
    if highest<mark:
        highest=mark
    if lowest>mark:
        lowest=mark
print("Total: ",total)
print("Average: ",average)
print("Even: ",counter)
print("Odd: ",odd_counter)
print("Highest",highest)
print("Lowest",lowest)
  