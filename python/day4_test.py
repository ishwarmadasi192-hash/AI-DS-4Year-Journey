# #Q5 
numbers=[5,12,8,17,20,3]

for number in numbers:
    if number>=10:
        print(number)
#Q6
names = ["Ishwar","Aman","Ravi"]
counter = 1
for name in names:
    print(counter,".",name)
    counter = counter + 1

# by chatgpt
#problem 1
numbers = [10,20,30,40,50]
print(numbers[0])
print(numbers[-1])
print(numbers[1])
print(numbers[-2])
#problem 2
fruits=["Apple","Banana","Mango","Orange"]
print(fruits[0])
print(fruits[2])
print(fruits[3])
#problem 3
marks=[10,20,30,40,50]
marks[2]=100
print(marks)
##LEVEL 2
#problem 4 
numbers=[10,20,30]
numbers.append(40)
numbers.append(50)
print(numbers)
#problem 5
numbers=[10,20,40,50]
numbers.insert(2,30)
print(numbers)
#problem 6
number=[10,20,30,40,50]
number.remove(30)
print(number)
#problem 7
numbers=[10,20,30,40,40]
numbers.pop()
print(numbers)
#problem 8
marks=[65,72,81,59,90]
marks[-2]=69
marks.append(95)
marks.remove(72)
print(marks)
print(len(marks))
##Level 3
#problem 9
numbers=[5,10,15,20,25]
for number in numbers:
    print(number)
#problem 10
numbers = [2,4,6,8,10]
total=0
for number in numbers:
    total+=number
    
print("sum: ",total)
#problem 11
numbers=[3,7,2,9,4,8]
counter=0
for number in numbers:
    if number%2==0:
        counter=counter+1
print(counter)

##LEVEL 4
#problem 12
marks=[85,72,91,64,78]
total=0
counter=0
highest=marks[0]
lowest=marks[0]
for mark in marks:
    total+=mark
    
    average=total/len(marks)
    if mark>highest:
     highest=mark
    if lowest>mark:
        lowest=mark
    if mark>=75:
        counter+=1
print("total: ",total)
print("average: ",average)
print("marks above or at 75: ",counter)
print("Highest",highest)
print("lowest",lowest)

