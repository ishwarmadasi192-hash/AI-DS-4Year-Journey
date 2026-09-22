#Basics of list
languages = ["Python","C++","Java","JavaScript"]
print(languages)
print("Frist language: ", languages[0])
print("Second language: ", languages[1])
print("Third language: ", languages[2])
print("Fourth language: ", languages[3])
print("Number of language: ", len(languages))

#Task 1 - add something new in a list
skills=["Python","C++","Problem Solving"]
new_skill = input("Enter the new skill to learn: ")
skills.append(new_skill)
print("Updated skilld: ",skills)
  
# Task 2 - loop thorugh a list
colleges = ["PR Pote", "VNIT","COEP","VJTI"]
for college in colleges:
    print(college)

#by chatgpt
#1.list
marks=[85,72,91,64,78]
#2. indexing
#index=0   1  2  3  4
#3. negative indexing
#-ve index=-5 -4-3-2-1
#4.changing list of element
marks = [85,72,91]
marks[1]=82
#5.adding element-- append()
marks = [85,72,91]
marks.append(64)#it inserts thr elemnt st the end of the list
        #one more method is: insert()
marks = [85,72,91]
marks.insert(1,100)
#     insert(index,value)
#7. removing elements
marks = [85,72,91,72]
marks.remove(72)#it removes the first matching element
#pop()  it is similar to append( )the diff is pop( delete the last element)  in default and delete the index value if it is given inside()
marks = [85,72,91,72]
marks.pop(1)
#8. len()  used to tell how many elements are in list
marks = [85,72,91,64,78]
print(len(marks))
# 🧠 The cheat sheet
# Operation	Meaning
# list[0]	---Get first element
# list[-1]	----Get last element
# list[2] = 50	---Change element
# list.append(50)	---Add to end
# list.insert(1, 50)	---Insert at index
# list.remove(50)	---Remove first matching value
# list.pop()	---Remove last element
# list.pop(2)	----Remove element at index 2
# len(list)	----Number of elements

#tiny actioms
marks = [85,72,91,64,78]
print(marks[0])
print(marks[2])
print(marks[-1])
print(len(marks))

#loops for list
numbers=[10,20,30,40]
for number in numbers:
    print(number)
    