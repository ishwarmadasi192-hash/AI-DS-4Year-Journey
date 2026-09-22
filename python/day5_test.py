#problem 1
numbers={10,20,20,30,30,40}
print(numbers)
#problem 2
numbers={10,20,30}
numbers.add(40)
numbers.add(50)
print(numbers)
#peoblem 3
numbers={10,20,30,40}
numbers.remove(20)
print(numbers)
         ###### MINI BOSS######
student = {
    "name": "Ishwar",
    "Maths": 85,
    "Physics": 72,
    "Chemistry": 91
}
print(student["name"])
total=0
counter=0
highest=student["Maths"]
lowest=student["Maths"]
for key in student:
    if key!="name":
     total += student[key]
     if highest<student[key]:
        highest=student[key]
     if lowest>student[key]:
        lowest=student[key]
     if student[key]>=75:
        counter+=1
average = total/3
print("Total: ",total)
print("average: ",average)
print("highest: ",highest)
print("Lowest: ",lowest)
print("Marks at or above 75: ",counter)