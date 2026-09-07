# #Basics of list
# languages = ["Python","C++","Java","JavaScript"]
# print(languages)
# print("Frist language: ", languages[0])
# print("Second language: ", languages[1])
# print("Third language: ", languages[2])
# print("Fourth language: ", languages[3])
# print("Number of language: ", len(languages))

# #Task 1 - add something new in a list
# skills=["Python","C++","Problem Solving"]
# new_skill = input("Enter the new skill to learn: ")
# skills.append(new_skill)
# print("Updated skilld: ",skills)
  
# # Task 2 - loop thorugh a list
# colleges = ["PR Pote", "VNIT","COEP","VJTI"]
# for college in colleges:
#     print(college)

# Task 3 - Total and average marks
marks = [78,84,91,67,88]
total = 0
for mark in marks:
    total = total + mark
    average_marks = total/len(marks)
print("Total marks: ",total)
print("Average marks: ",average_marks)