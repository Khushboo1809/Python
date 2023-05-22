questions = ("How many elements are in periodic table? ",
             "Which animal lays the largest egg?",
             "What is the most abundant gas in Earth's atmosphere ? ",
             "How many bones are in the human body ?",
             "Whish planet has life in solar system?")

options = (("A 118","B 117 ","C 116","D 119"),
           ("A ant","B whale","C ostrich","D elephant"),
           ("A oxygen","B co2","C nitrogen","D hydrogen"),
           ("A 206","B 211","C 209","D 208"),
           ("A mars","B venus","C Jupiter","D Earth"))

answers  = ("A","C","C","A","D")
gueses = []
score = 0
quest_num = 0

for question in questions:
    print(question)
    for option in options[quest_num]:
        print(option)
 
    guess = input("Enter( A , B , C , D): ").upper()
    gueses.append(guess)
    if guess == answers[quest_num]:
        score += 1
        print("CORRECT")
        print("    ")
    else:
        print("    ")
        print("INCORRECT !")
        print(f"{answers[quest_num]} is the correct answer.")  
        print("    ")  

    quest_num += 1 
   

print("-----------------------") 
print("        RESULT        ")
print("-----------------------")  

print("answers: ", end=" ")
for answer in answers:
    print(answer,end="  ")
print()

print("gueses: ", end=" ")
for guess in gueses:
    print(guess,end="  ")
print()

print("----------------------")
score = int(score / len(questions)*100)
print(f"your score is: {score}%")
print("----------------------")