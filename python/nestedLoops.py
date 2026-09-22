#Nested loops
for i in range(3):
    for j in range(3):
        print(i,j)
#2.Range
# you have already learned range as range(1,11) meand (start,stop)where stop is not included today to learn:
for i in range(1,11,2):#range(start,stop,step) output = 1,3,5,7,9 here step may be the difference between two consecutive number
    print(i)
# backward
for a in range(10,0,-1):
    print(a)