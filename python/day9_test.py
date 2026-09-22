#problem 1
numbers=(10,20,30,40,50)
print(numbers[0])
print(numbers[-1])
print(numbers[2])
print(len(numbers))
#problem 2
student=("Ishwar",18,"AI&DS")
name,age,branch=student
print(name)
print(age)
print(branch)
#problem 3
total=0
even_counter=0
odd_counter=0
numbers=(10,20,30,40,50)
for number in numbers:
    print(number)
    total+=number
    if number%2!=0:
        odd_counter+=1
    else:
        even_counter+=1
print("Total: ",total)
print("even: ",even_counter)
print("odd: ",odd_counter)

   ######BOSS######
marks=(85,72,91,64,78)
total=0
even_counter=0
odd_counter=0
highest=marks[0]
lowest=marks[0]
for mark in marks:
    total+=mark
    if mark%2==0:
        even_counter+=1
    else:
        odd_counter+=1
    if highest<mark:
        highest=mark
    if lowest>mark:
        lowest=mark
average=total/len(marks)
print("Total: ",total)
print("Average: ",average)
print("Even number: ",even_counter)
print("Odd number: ",odd_counter)
print("Highest: ",highest)
print("Lowest: ",lowest)

#problem 1
numbers=(10,20,30,40,50)
print(numbers[0])
print(numbers[-1])
print(numbers[1])
print(numbers[-2])
print(len(numbers))
#Problem 2 — Negative Indexing
data = ("Python","C++","Java","SQL","AI")
print(data[-1])
print(data[-2])
print(data[0])
#problem 3
numbers=(10,20,30,40,50,60)
print(numbers[0:3])
print(numbers[-3:])
print(numbers[0:4])
#problem 4
#it shows error because tuples cannot be modified
##LEVEL 2
#problem 5
numbers=(10,20,30,40,50)
total=0
for number in numbers:
    total+=number
average=total/len(numbers)
print("Total: ",total)
print("Average: ",average)
#problem 6
numbers=(11,22,33,44,55,66,77,88)
even_counter=0
odd_counter=0
for number in numbers:
    if number%2==0:
        even_counter+=1
    else:
         odd_counter+=1
print("Even number: ",even_counter)
print("odd_counter: ",odd_counter)
#problem 7
numbers=(5,15,25,35,45,55)
highest=numbers[0]
lowest=numbers[0]
for number in numbers:
    if highest<number:
        highest=number
    if lowest>number:
        lowest=number
print("Highest: ",highest)
print("Lowest: ",lowest)
#problem 8
numbers=(10,20,10,30,10,40,20)
print(numbers.count(10))
print(numbers.count(20))
#problem 9
numbers=(10,20,30,40,50)
print(numbers.index(30))
print(numbers.index(50))
#problem 10
numbers=(10,20,30,40,50)
print(30 in numbers)
print(100 in numbers)
##LEVEL 3
#Problem 11
numbers=[10,20,30,40,50]
q=tuple(numbers)
print(q)
#problem 12
numbers=(10,20,30,40,50)
w=list(numbers)
w.append(60)
print(w)
#Problem 13
student=("Ishwar",18,"AI&DS")
name,age,branch=student
print(name)
print(age)
print(branch)
#problem 14
numbers=(10,20,30)
a,b,c=numbers
sum=a+b+c
print(sum)
product=a*b*c
print(product)
#problem 15
a=10
b=20
a,b=b,a
print(a)
print(b)
#problem 16
# a,b=(10,20,30) this will give us error because there are 2 variable but 3 values 
#a,b,c = (10,20) this will also give erroe as there are 3 variable but only 2 value assigned
# # LEVEL 4 
#problem 17
student=(
    ("Ishwar",85),
    ("Rahul",72),
    ("Aman",91)
)
for name,mark in student:
    print(name,mark)
#problem 18
student=(
    ("Ishwar",85),
    ("Rahul",72),
    ("Aman",91)
)
print(student[0][1])
print(student[2][0])
print(student[1][1])
#problem 19
student=(
    ("Ishwar",85),
    ("Rahul",72),
    ("Aman",91),
    ("Rohit",64)
)
total=0
for name,mark in student:
    total+=mark
average=total/len(student)
print("Average marks: ",average)
#problem 20
student=(
    ("Ishwar",85),
    ("Rahul",72),
    ("Aman",91),
    ("Rohit",64)
)
highest=student[0][1]
highest_name=""
for name,mark in student:
    if highest<mark:
        highest=mark
        highest_name=name   
print("Highest: ",highest)
print("Highest Name: ",highest_name)
##LEVEL 5
# problem 21
marks = (85,71,91,64,78,95,67,88)
total=0
highest=marks[0]
lowest=marks[0]
counter=0
even_counter=0
odd_counter=0
for mark in marks:
    total+=mark
    if highest<mark:
        highest=mark
    if lowest>mark:
        lowest=mark
    if mark>=75:
        counter+=1
    if mark%2==0:
        even_counter+=1
    else:
        odd_counter+=1
average=total/len(marks)
print("Total: ",total)
print("Average: ",average)
print("Highest: ",highest)
print("Lowest: ",lowest)
print("Marks on or above 75: ",counter)
print("Even number: ",even_counter)
print("Odd number: ",odd_counter)
#problem 22
students = (
    ("Ishwar",85),
    ("Rahul",72),
    ("Aman",91),
    ("Rohit",64),
    ("Karan",78)
)
total=0
highest=students[0][1]
lowest=students[0][1]
counter=0
for name,mark in students:
    total+=mark
    if highest<mark:
        highest=mark
    if lowest>mark:
        lowest=mark
    if mark>=75:
        counter+=1
average=total/len(students)
print("Total: ",total)
print("Average: ",average)
print("Highest: ",highest)
print("Lowest: ",lowest)
print("Marks on or above 75: ",counter)
       ##############3day 9 : FInal Boss##############3
students = (
           ("Ishwar",85),
           ("Rahul",72),
           ("Aman",91),
           ("Rohit",64),
           ("Karan",78)
       )
def analyze_students(students):
 
    total=0
    highest=students[0][1]
    lowest=students[0][1]
    highest_name=""
    
    counter=0
    for name,mark in students:
        total+=mark
        average =total/len(students)
        if highest<mark:
            highest=mark
            highest_name=name
        if lowest>mark:
            lowest=mark
        if mark>=75 :
            counter+=1
    return total,average,highest,lowest,counter,highest_name
total,average,highest,lowest,counter,highest_name=analyze_students(students)

print("Total: ",total)
print("Average: ",average)
print("Highest: ",highest)
print("Lowest: ",lowest)
print("Mark on or above 75: ",counter)
print("Highest Name: ",highest_name)
