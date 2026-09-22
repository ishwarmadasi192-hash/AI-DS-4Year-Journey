# 1️⃣ What is a Tuple?
# A tuple is a collection of values, similar to a list.
numbers = (10, 20, 30, 40)
# You can access elements:
print(numbers[0])
print(numbers[2])
# Output:
# 10
# 30
# So tuples also use indexing starting from 0.
# 2️⃣ The BIG difference: List vs Tuple
# List
# numbers = [10, 20, 30]
# numbers[0] = 100
# Allowed ✅
# Tuple
# numbers = (10, 20, 30)
# numbers[0] = 100
# Not allowed ❌
# Why?
# Because a tuple is immutable.
# Mutable = can be changed
# Immutable = cannot be changed
# Remember:
# List → mutable
# Tuple → immutable
# 3️⃣ Why do tuples exist?
# Suppose you have a student's basic information:
# student = ("Ishwar", 18, "AI&DS")
# You generally don't want random code to accidentally change that collection.
# That's where tuples are useful.
# 4️⃣ Tuple unpacking
# This connects directly to yesterday's theory.
student = ("Ishwar", 18, "AI&DS")
name, age, branch = student
print(name)
print(age)
print(branch)
# Output:
# Ishwar
# 18
# AI&DS
# Python takes:
# "Ishwar" → name
# 18       → age
# "AI&DS"  → branch
# That's tuple unpacking.
#3. Tuple Indexing
#Exactly like lists.
numbers = (10, 20, 30, 40, 50)
#Positions:
#Value:   10   20   30   40   50
#Index:    0    1    2    3    4
#Therefore:
print(numbers[0])   # 10
print(numbers[2])   # 30
print(numbers[4])   # 50
#Negative indexing also works:
print(numbers[-1])  # 50
print(numbers[-2])  # 40
#You already learned this with strings and lists.
#4. Tuple Length
#Same len() you've already learned:
numbers = (10,20,30,40,50)
print(len(numbers))
#5. Tuple Slicing
#You already learned string/list slicing, so tuples use the same idea.
numbers = (10,20,30,40,50)
print(numbers[1:4])
#Output:
#(20, 30, 40)
#Remember:
#Start included, end excluded.
#So [1:4] means indexes:
#6. Looping Through a Tuple
#Exactly like a list.
numbers = (10,20,30,40,50)
for number in numbers:
    print(number)
#Python takes one element at a time:
# number = 10
# number = 20
# number = 30
# number = 40
# number = 50
#This is the exact concept you were confused about earlier.
#number is NOT a parameter.
#It's simply the loop variable.
# 7. Tuple Methods
# There are two important methods you need right now.
# count()
# Counts how many times a value occurs.
numbers = (10,20,10,30,10)
print(numbers.count(10))
# Output:
# 3
# index()
# Finds the index of the first occurrence.
numbers = (10,20,30,40)
print(numbers.index(30))
# Output:
# 2
# If a value occurs multiple times, index() gives the first occurrence.
#8. in — Membership
#You've seen in with loops, but now let's use it to check membership.
numbers = (10,20,30,40)
#print(20 in numbers)
#Output:
#True
#And:
print(99 in numbers)
#Output:
#False
#You can also use:
if 30 in numbers:
    print("Found")
# Tuple → List
numbers = (10,20,30)
lst = list(numbers)
print(lst)
# Result:
# [10, 20, 30]
# So:
# list()  → converts to list
# tuple() → converts to tuple
# 10. Tuple Unpacking 🔥
# This is especially important because you already encountered it with functions.
# Suppose:
student = ("Ishwar", 18, "AI&DS")
# You can do:
name, age, branch = student
# Python assigns:
# name   → "Ishwar"
# age    → 18
# branch → "AI&DS"
# Then:
print(name)
print(age)
print(branch)
# This is called unpacking.
# 11. Tuple Unpacking for Swapping 🔥
# This is a very useful Python feature.
# Normally, you might do:
# temp = a
# a = b
# b = temp
# But Python lets you do:
# a, b = b, a
# Example:
a = 10
b = 20
a, b = b, a
print(a)
print(b)
# Output:
# 20
# 10
# We'll later understand exactly why Python allows this.
# 12. Nested Tuples
# Now we're ready for the thing I previously threw at you without teaching. 😭
# A tuple can contain another tuple.
students = (
     ("Ishwar", 85),
     ("Rahul", 72),
     ("Aman", 91)
 )
# Think of it as:
# students
#  ├── ("Ishwar", 85)
#  ├── ("Rahul", 72)
#  └── ("Aman", 91)
# Now:
print(students[0])
# gives:
# ("Ishwar", 85)
# And:
print(students[0][0])
# gives:
# Ishwar
# While:
print(students[0][1])
# gives:
# 85
# So:
# students[0][0]
# means:
# First student → first value
# And:
# students[0][1]
# means:
# First student → second value
# 13. Looping Through Nested Tuples
# This is the final concept you need for today's harder problems.
students = (
     ("Ishwar", 85),
     ("Rahul", 72),
     ("Aman", 91)
 )
for student in students:
     print(student)
# Output:
# ("Ishwar", 85)
# ("Rahul", 72)
# ("Aman", 91)
# But we can unpack during the loop:
for name, marks in students:
     print(name, marks)
# Output:
# Ishwar 85
# Rahul 72
# Aman 91
# Here:
# name  → first value
# marks → second value
# for every student.