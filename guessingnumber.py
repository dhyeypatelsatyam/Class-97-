import random

number=random.randint(1,9)
chances=0


print("Guess a number b/w 1 to 9")
guess=int(input("Enter your guessed number"))


while chances<5:
    if guess==number:
        print("Congrats you win")

    else :
        print("you lose") 

    chances=chances+1    

