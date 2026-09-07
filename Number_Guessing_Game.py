secret_number = 7
n = int(input("Guess the number: "))
while n<secret_number:
    print("Too Low.Try Again")
    n=int(input("Guess the number: "))
while n>secret_number:
    print("Too High.Try Again")
    n=int(input("Guess the number: "))
print("YOU GUESSED IT RIGHT.CONGRATULATIONS.")