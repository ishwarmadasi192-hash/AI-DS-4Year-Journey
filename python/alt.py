n=int(input("ENter the n: "))
total=0
i=1
while i<=n:
    total+=i
    i=(i*1)
print(total)

#2 prime number sum
total=0
for num in range(2,n+1):
    is_prime=True
    for i in range(2,num):
        if num%i==0:
            is_prime=False
            break
    if is_prime:
        total+=num
print("The sum og the prime numbers are: ",total)     
