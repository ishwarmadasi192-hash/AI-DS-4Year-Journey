#problem 1
import numbers


file=open("student.txt","w")
file.write("Name:Ishwar\n")
file.write("Branch:AI&DS\n")
file.write("College:MIT CSN")
#problem 2
with open("student.txt","r") as file:
    content=file.read()
print(content)
#problem 3
file=open("student.txt","a")
file.write("\nGoal:20+ lpa")
with open("student.txt","r") as file:
    content=file.read()
print(content)
#problem 4
counter=0
with open("5line.txt","r") as file:
    for line in file:
        counter+=1
        print(line)
print(counter)
#problem 5
with open("sentence.txt","r") as file:
    content=file.read()
    part=content.split()
print(content)
print(len(part))
# problem 6
with open("mark.txt","r") as file:
    mark=file.read()
    ind=mark.split()
    num1=int(ind[0])
    num2=int(ind[1])
    num3=int(ind[2])
    num4=int(ind[3])
    num5=int(ind[4])
    num=[num1,num2,num3,num4,num5]
    total=0
    highest=num[0]
    lowest=num[0]
    for number in num:
        total+=number
        average=total/len(num)
        if highest<number:
            highest=number
        if lowest>number:
            lowest=number
print(total)
print(average)
print(highest)
print(lowest)
#problem 7
with open("numbers.txt","r") as file:
    content=file.read()
    part=content.split()
    n1=int(part[0])
    n2=int(part[1])
    n3=int(part[2])
    n4=int(part[3])
    n5=int(part[4])
    n6=int(part[5])
    n7=int(part[6])
    even_counter=0
    odd_counter=0
    num=[n1,n2,n3,n4,n5,n6,n7]
    for number in num:
        if number%2==0:
            even_counter+=1
        else:
            odd_counter+=1
print(even_counter)
print(odd_counter)
#problem 8
def analyze_file(numbers):
    with open("numbers.txt","r") as file:
        content=file.read()
        part=content.split()
        n1=int(part[0])
        n2=int(part[1])
        n3=int(part[2])
        n4=int(part[3])
        n5=int(part[4])
        n6=int(part[5])
        n7=int(part[6])
        num=[n1,n2,n3,n4,n5,n6,n7]
        total=0
        highest=num[0]
        lowest=num[0]
        even_counter=0
        odd_counter=0
        for number in num:
            total+=number
            average=total/len(num)
            if highest<number:
                highest=number
            if lowest>number:
                lowest=number
            if number%2==0:
                even_counter+=1
            else:
                odd_counter+=1

    return total,average,highest,lowest,even_counter,odd_counter
total,average,highest,lowest,even_counter,odd_counter=analyze_file(numbers)
print(total)
print(average)
print(even_counter)
print(odd_counter)
print(highest)
print(lowest)
     ###########FINAL BOSS#############
def analyze_students(filename):
    total=0
    highest=0
    lowest=0
    highet_name=""
    student_counter=0
    above75=0
    with open(filename,"r") as file:
        for line in file:
            line=line.strip()
            parts=line.split(",")
            name=parts[0]
            marks=int(parts[1])
            total+= marks
            student_counter+=1
            if student_counter==1:
                highest=marks
                lowest=marks
                highest_name=name
            else:
                if marks>highest:
                    highest=marks
                    highest_name=name
                if marks<lowest:
                    lowest=marks
            if marks<=75:
                above75+=1
    average=total/student_counter
    return total,average,highest,lowest,highest_name,above75
total,average,highest,lowest,highest_name,above75=analyze_students("students.txt")
print("total marks: ",total)
print("Average: ",average)
print("Highest: ",highest)
print("Lowest: ",lowest)
print("Highest Student: ",highest_name)
print("Student above or at 75: ",above75)