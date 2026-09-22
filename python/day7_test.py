#problem 1
student = {
    "name": "Ishwar",
    "age": 18,
    "branch": "AI&DS"
}
print(student["name"])
print(student["age"])
print(student["branch"])
#problem 2
person = {
    "name": "Rahul",
    "age": 20,
    "city": "Pune"
}
person["age"]=21
print(person)
#problem 3
person = {
    "name": "Rahul",
    "age": 21
}
person["branch"]="AI&DS"
print(person)
#problem 4
person = {
    "name": "Rahul",
    "age": 21,
    "city": "Pune"
}
person.pop("city")
print(person)
##LEVEL 2
#problem 5
marks = {
    "Maths": 85,
    "Physics": 72,
    "Chemistry": 91
}
for key in marks:
    print(key)
#problem 7
marks = {
    "Maths": 85,
    "Physics": 72,
    "Chemistry": 91
}
for key in marks:
    print(key,marks[key])

    ###LEVEL 3#####
    #problem 7
marks = {
    "Maths": 85,
    "Physics": 72,
    "Chemistry": 91
}
total=0

highest=marks["Maths"]
lowest=marks["Maths"]
for key in marks:
    total+=marks[key]
    average=total/len(marks)
    if highest<marks[key]:
        highest=marks[key]
    if lowest>marks[key]:
        lowest=marks[key]

print("total",total)
print("average",average)
print("Highest",highest)
print("Lowest",lowest)