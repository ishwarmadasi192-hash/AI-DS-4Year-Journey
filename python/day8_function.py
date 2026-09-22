# 🧩 1. What is a function?
# A function is a reusable block of code that performs a specific task.
# For example:
def greet():
    print("Hello")
# Here:
# def → tells Python we're defining a function
# greet → function's name
# () → where inputs can go
# : → starts the function block
# indented code → what the function does
#2 Run a function
# But notice something important:
# The function hasn't run yet.
# We have only created it.
# # To run it:
greet()
#3. Tiny example
def say_hello():
    print("Hello Ishwar")
say_hello()
say_hello()
say_hello()
#4. Function with inputs
def greet(name):
    print("Hell0",name)
greet("Ishwar")
greet("Rahul")
#5. Another example
def square(number):
    print(number*number)
square(5)
square(10)
# 6. return
def square(number):
    return number*number
result = square(5)
print(result)
result=square(7)
# print vs return

# This is VERY important:

# def square(number):
#     print(number * number)

# → displays the answer.

# def square(number):
#     return number * number

# → sends the answer back so we can store/use it.

# For example:

# answer = square(7)

# Now answer contains:

# 49
# FUNCTION WITH PARAMETER
def greet(name): #here name is paramerer= placeholder inside function
    print("Hello",name)
greet("Ishwar")#Ishwar Rahul Alex are argument= the value whichwe assign to it 
greet("Rahul")
greet("Alex")
# MULTIPLE PARAMETERS
def add(a,b):
    print(a+b)
add(1,2)
# 🔥 P4 — Now we introduce return
# This is an important jump.
# So far we've done:
def add(a, b):
     print(a + b)
# The function prints the answer.
# But imagine we want to do this:
# result = add(10, 20)
# and then use result somewhere else.
# For that, we need return.
# Concept
def add(a, b):
     return a + b
# Then:
result = add(10, 20)
print(result)
# Think of it like:
# add(10, 20)
#       ↓
#     30
#       ↓
#  return 30
#       ↓
# result = 30
# print vs return
# print()	                                      return
# Shows something on screen	                       Sends a value back
# Mainly for displaying	                           Mainly for using the result
# Doesn't give the result to the caller	           Gives the result to the caller
# 5.WHY IS RETURN POWERFUL
def add(a,b):
    return a+b
x=add(10,20)
y=add(5,7)
print(x+y)
# 6. FUNCTION + INPUT()
n=int(input("Enter the number: "))
def square(n):
    return n*n
result=square(n)
print(result)
# 7. FUNCTION + CONDITIONALS
# 8. DEFAULT PARAMETERS
#Sometimes we want a parameter to have a default value.
#Example:
def greet(name="Ishwar"):
    print("Hello", name)
#Now we can do:
greet()
#Output:
#Hello Ishwar
#But we can also provide another argument:
greet("Rahul")
#Output:
#Hello Rahul
#So:
#greet()
#uses default → Ishwar
#greet("Rahul")
#uses given argument → 