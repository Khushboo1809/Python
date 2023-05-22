#---------------------------------------------
def new_game():

    guesses =[]
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print(" ")
        print(key) 
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter (A, B, C, D):  ").upper()
        guesses.append(guess)   

        correct_guesses += check_answer(questions.get(key),guess)
        question_num += 1

    display_score(correct_guesses,guesses)    
#-------------------------------------------------
def check_answer(answer,guess):
    if answer == guess:
        print("correct")
        return 1
    else:
        print("wrong")
        return 0


#---------------------------------------------
def display_score( correct_guesses,guesses):
    print("result")

    print("Answers: ", end=" ")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses: ", end=" ")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int(correct_guesses/len(questions)*100)
    print("  ")
    print("Your Score is : "+str(score)+"%")
    print("  ")
#---------------------------------------------
def play_again():
     response = input("Do you want to play again? (YES/NO): ").upper()

     if response == "YES":
         return True
     else:
         return False

#---------------------------------------------


questions ={
   "WHO CREATED PYTHON? " :"A",
   "WHAT YEAR WAS PYTHON CREATED? " :"B",
   "PYTHON IS TRIBUTED TO WHICH COMEDY GROUP?  " :"C",
   "SUN RISES IN WHICH DIRECTION? " :"B"
}

options =[
    ["A. Guido Van Rossum","B. Bill Gates","C. Elon Musk","D. None"],
    ["A. 1989","B. 1991","C. 2000","D. 2016"],
    ["A. Lonely Island","B. Smosh","C. Monty Python","D. None"],
    ["A. West","B. East","C. North","D. None"]
]

new_game()

while play_again():
    new_game()

print(" ")
print("OKAY!!")    