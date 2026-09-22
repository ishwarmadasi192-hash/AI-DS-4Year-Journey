# 🧠 PART 1 — What is a Set?
# A set is a collection of values where:
# Duplicates are automatically removed
# Order is not guaranteed
# You can add/remove elements
# Sets are useful when you care about unique value
# Example:
numbers = {10, 20, 20, 30, 30}
print(numbers)
# You will get something equivalent to:
# {10, 20, 30}
# 🧠 PART 2 — Set vs List vs Tuple
# Feature	   List	  Tuple	   Set
# [] / () / {}	[]	   ()	   {}
# Ordered	    ✅	 ✅	    ❌
# Duplicates	✅	 ✅	    ❌
# Mutable	    ✅	 ❌	    ✅
# Indexing	    ✅	 ✅	    ❌
# Important:
# You cannot do:
numbers = {10,20,30}
# print(numbers[0])
# because sets don't use indexes.
# 🧠 PART 3 — Adding Elements
# .add()
numbers = {10,20,30}
numbers.add(40)
print(numbers)
# Result:
# {10,20,30,40}
# Adding something that already exists doesn't create a duplicate:
numbers.add(20)
# Still:
# {10,20,30,40}
# 🧠 PART 4 — Removing Elements
# .remove()
numbers = {10,20,30}
numbers.remove(20)
# Now:
# {10,30}
# ⚠️ If the element doesn't exist, .remove() produces an error.
# .discard()
numbers.discard(100)
# If 100 doesn't exist, nothing happens.
# 🧠 PART 5 — Membership
# This is one of the most useful things about sets.
numbers = {10,20,30,40}
print(20 in numbers)
print(100 in numbers)
# Output:
# True
# False
# You already learned in with tuples, so this is just applying an old concept to sets.
# 🧠 PART 6 — Set Operations 🔥
# This is the important new part.
# Imagine:
A = {1,2,3,4}
B = {3,4,5,6}
# UNION — everything from both
# A | B
# Result: {1,2,3,4,5,6}
# Think:
# A OR B
# A & B
# INTERSECTION — things common to both
# Result:{3,4}
# Think:A AND B
# DIFFERENCE — in A but NOT B
# A - B
# Result:{1,2}
# And:
# B - A
# gives:{5,6}
# ⚠️ Direction matters.
# 🧠 PART 7 — Symmetric Difference
# This sounds scary but isn't.
# A ^ B
# means:
# Elements that are in A or B, but NOT both.
# For: A = {1,2,3,4}
# B = {3,4,5,6}
# Result:{1,2,5,6}
# The common elements 3,4 disappear.
# 🔥 PART 8 — Why Sets Matter for AI & DS
# This isn't just random Python theory.
# Sets are useful for things like:
# Removing duplicate data
# Finding unique categories
# Comparing datasets
# Finding common values between datasets
# Finding values present in one dataset but missing in another
# Example:
students_python = {"Ishwar","Rahul","Aman","Rohit"}
students_cpp = {"Ishwar","Aman","Karan"}
print(students_python & students_cpp)
# This tells you which students know both Python and C++.
# Output: {"Ishwar","Aman"}
# That's already a tiny piece of data-processing thinking.