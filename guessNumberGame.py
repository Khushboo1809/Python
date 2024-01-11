import random

def guess(x):
    random_num =random.randint(1,x)
    guess = 0
    while guess!= random_num:
        guess=int(input(f"Guess a number between 1 and {x} : "))
        if guess< random_num:
            print("sorry, guess again. too low.")
        elif guess > random_num:
            print("guess again, its too high")
    print(f"Yaaay, Congrats. You guessed the right number  {random_num} correctly")        

guess(10)        