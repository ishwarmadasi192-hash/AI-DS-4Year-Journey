secret_number = 7
n = int(input("Guess the number: "))
while n<secret_number:
    print("Too Low.Try Again")
    n=int(input("Guess the number: "))
while n>secret_number:
    print("Too High.Try Again")
    n=int(input("Guess the number: "))
print("YOU GUESSED IT RIGHT.CONGRATULATIONS.")

#by chatgpt
secret_Number=7
n=int(input("Guess the secret number: "))
while n>secret_Number:
    print("Too High")
    n=int(input("Guess the secret number: "))
while n<secret_Number:
    print("Too Low.")
    n=int(input("guess the secret number: "))
print("You Guessed it correctly.")

#using while +if/else
secret_number = 7
n=int(input("Gyess the secret number: "))
while n!=secret_number:
    if n>secret_number:
        print("Too high")
   
    else:
        print("Too Low")
    n=int(input("Guess the number"))
print("You guessed it right")