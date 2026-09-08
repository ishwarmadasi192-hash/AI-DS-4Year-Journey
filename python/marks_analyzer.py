marks = [78,84,91,67,88]
total=0
count= 0
for mark in marks:
    print(mark)
    total = total + mark
    average_marks = total/len(marks)
    if mark>=75:
        count += 1  
print(mark)
print("Total marks: ",total)
print("Average marks: ",average_marks)
print("Highest marks: ",max(marks))
print("Lowest marks: ",min(marks))
print("Marks at or above 75: ",count)