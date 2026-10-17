# #1. OPening a file
# file=open("data.txt","r")
# # data.txt → filename
# # "r"      → mode
# #2. Reading a entire file
# file =open("data.txt","r")
# content=file.read()
# print(content)
# file.close()
# #3. Writing to a file
# file=open("data.txt","w")
# file.write("Hello Ishwar")
# file.close()
# #4. Append
# file=("data.txt","a")
# file.write("\nWeelcome to python")
# file.close()
# #5.  better way to read
# with open("data.txt","r") as file:
#     content=file.read()
# print(content)
# #6. reading line by line
# with open("data.txt","r") as file:
#     for line in file:
#         print(line)
# #7. readline() = to read only one line
# with open("data.txt","r") as file:
#     line=file.readline()
#     print(line)
# #8. readlines() =Now lines is a list of strings, one for each line
# with open("data.txt", "r") as file:
#     lines = file.readlines()
# # You might get:
# # ['Ishwar\n', 'Rahul\n', 'Aman\n']
# # Notice something important:
# # \n
# # is still attached to each line.
# #9. Newline \n
# file.write("Ishwar\n")
# file.write("Rahul\n")
# file.write("Aman\n")
# #10. important mental model

#11 .split()
sentence="I love python"
words=sentence.split()
print(words)
data="Ishwar,85"
parts=data.split(",")
print(parts)
name=parts[0]
marks=parts[1]
print(name)
print(marks)