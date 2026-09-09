#first test with perplexity
name = input("Enter your name: ")
age = input("Enter your age: ")
print(f"Hello, {name}!")
print(f"You are {age} years old.")
birth_year = 2026 - int(age)
year_turn_21 = birth_year + 21
print(f" Youe= were born in year {birth_year}.")
print(f"You will turn 21 in the year {year_turn_21}.")

# with chatgpt
#excercise 1
n1=int(input("Enter the n1: "))
n2=int(input("Enter the n2: "))
print(n1+n2)
print(n1-n2)
print(n1/n2)
print(n1%n2)
#Exercise 2 
age = int(input("Enter the age: "))
print("Your age after 5 years wille be: ",age+5)
#exercise 3
l=int(input("Enter the length: "))
b=int(input("Enter the breadth: "))
area = l*b
print(area)
perimeter = 2*(l+b)
print(perimeter)
#exercise 4 
c=float(input("Enter the degree in celcius: "))
f= (c*9/5)+32
print("the degree in fahrenheit is: ",f)
#exercise 5
n1=int(input("Enter the mark of subject1: "))
n2=int(input("Enter the mark of subject2: "))
n3=int(input("Enter the mark of subject3: "))
n4=int(input("Enter the mark of subject4: "))
n5=int(input("Enter the mark of subject5: "))
total = n1+n2+n3+n4+n5
print(total)
average = total/5
print(average)
percentage = (total/500)*100
print(percentage)