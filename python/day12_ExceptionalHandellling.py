# Day 12 — Exception Handling
# Today we're learning how Python handles errors without crashing the entire program.
# Simple example
# Without exception handling:
# number = int(input("Enter a number: "))
# print(number)# If the user enters:
# hello
# 💥 Program crashes.
# With try/except:
try:
     number = int(input("Enter a number: "))
     print(number)

except:
     print("Invalid input")
# Now:
# Enter a number: hello
# Invalid input
# The program doesn't crash.