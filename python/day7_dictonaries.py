#Dictonaries
student=["Ishwar",17,"AI&DS"]
#Problem: What does student[1] mean?
# You have to remember:
# 0 → name
# 1 → age
# 2 → branch
#A dictionary solves this by giving every value a key.
#2. creating dictonaries
student={
    "name":"Ishwar",
    "age":17,
    "Branch":"AI&DS"
}
#3. Accessing value
print(student["name"]) # here the name is key word so we donot have to remember all the index value
#4. changing a value = dictonaries are mutable just like lists
student={
    "name":"Ishwar",
    "age":17,
    "Branch":"AI&DS"
}
student["age"] = 18
#5. Adding a new key
student["city"]="Aurangabad"
#student["new_key"]=value
#6. Removing a key
student.pop("age")
#7. Geeting the number of items
print(len(student))
#8. looping through dictonaries
student = {
    "name": "Ishwar",
    "age": 18,
    "branch": "AI&DS"
}
for key in student:
    print(key)
    print(student[key])
    print(key , student[key])
    