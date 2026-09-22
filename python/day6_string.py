#strings
name = "Ishwar"
x="123"
#1.string indexing
# I s h w a r
# 0 1 2 3 4 5
#-6-5-4-3-2-1 #2.negative indexing
print(name[0])
print(name[-1])
#3.string length
print(len(name))
wish="hi bro"
print(len(wish))#here it will pritn 5 as space is also included
#4.string slicing
print(name[0:3])
#5. Useful string method
#.upper()
print(name.upper())#for uppercase
#.lower()
print(name.lower())#for lowercase
#.strop()
print(name.strip())#remove unnecessay spce from start and end 
#.replace()
text="I like java"
print(text.replace("java","python"))
#string searching  .find()
print(name.find("q"))#if something isnt't found it retuen -1

