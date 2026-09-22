#problem 1
def welcome():
    print("Welcome to python")
welcome()
welcome()
welcome()
#problem 2
def greet(name):
    print("Hello",name)
greet("Ishwar")
greet("Rahul")
greet("Alex")
# problem 3
def add(a,d):
    print(a+d)
add(2,20)
add(79,90)
add(698,68)
# problem 4
def multiply(w,e):
    return(w*e)
result=multiply(5,4)
print(result)
result=multiply(10, 7)
print(result) 
result=multiply(6, 8)
print(result)
# problem 5
def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
x=add(20,10)
y=subtract(20,10)
z=multiply(20,10)
print("Addition: ",x)
print("Subtract: ",y)
print("Multiply: ",z)
# problem 6
def square(n):
    return n*n
n=int(input("Enter the number: "))
result=square(n)
print(result)
# problem 7
def check_even_odd(n):
    if n%2==0:
        return "Even"
    else:
        return "odd"
n=int(input("Enter the number: "))
result=check_even_odd(n)
print(result)
# problem 8
def power(n,p=2):
     return n**p
result=power(5)
print(result)
result=power(2,3)
print(result)
result=power(10)
print(result)

###### 9. FUNCTION CHALLENGE########
def student_result(maths,physics,chemistry):
    total = maths + chemistry + physics
    average=total/3
    if maths>=40 and chemistry>=40 and physics>=40:
        result= "Pass"
    else:
        result= "Fail"
    return total,average,result
total,average,result,highest,lowest=student_result(50,60,70)
print("Total: ",total)
print("Average: ",average)  
print("Result: ",result)

############# FINAL BOSS###########
def analyze_number(numbers):
    total=0
    even_counter=0
    odd_counter=0
    highest=numbers[0]
    lowest=numbers[0]
    for number in numbers:
        total+=number
        if number % 2==0:
            even_counter+=1
        else:
         odd_counter+=1
        if highest<number:
            highest=number
        if lowest>number:
            lowest=number   
    average=total/len(numbers)
    return total,average,even_counter,odd_counter,highest,lowest
total,average,even_counter,odd_counter,highest,lowest=analyze_number([10,20,30,40,50])
print("Total: ",total)
print("Average: ",average)
print("Even Counter: ",even_counter)
print("Odd Counter: ",odd_counter)
print("Highest: ",highest)
print("Lowest: ",lowest)