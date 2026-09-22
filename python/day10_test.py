#problem 1
numbers={10,20,20,30,30,40,40,40}
print(numbers)
#all the duplicate ge removed automatically and the result get prints but in un ordered form
#problem 2
fruits={"Apple","Banana","Mango"}
fruits.add("Orange")
fruits.add("Grape")
print(fruits)
#problem 3
numbers={10,20,30,40,50}
numbers.remove(30)
numbers.discard(100)
print(numbers)
#problem 4
numbers={10,20,30,40,50}
print(20 in numbers)
print(100 in numbers)
##LEVEL 2
# problem 5
numbers={10,20,30,40,50}
for number in numbers:
    print(number)
#problem 6
numbers={10,15,20,25,30,35,40}
even_counter=0
odd_counter=0
for number in numbers:
    if number%2==0:
        even_counter+=1
    else:
        odd_counter+=1
print("Even number: ",even_counter)
print("Odd number: ",odd_counter)
#problem 7
numbers=[10,20,10,30,20,40,30,50]
q=set(numbers)
print(numbers)
#problem 8
names = ["Ishwar","Rahul","Ishwar","Aman","Rahul","Rohit"]

## LEVEL 3
# problem 9
a={1,2,3,4,5,}
b={4,5,6,7,8}
print(a|b)
print(a & b)
print(a-b)
print(b-a)
print(a^b)
