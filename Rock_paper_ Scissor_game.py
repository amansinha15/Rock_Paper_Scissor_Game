""" 
WORKFLOW OF PROJECT:
1- Input from users (Rock, Paper, Scissor)
2- Computer choice (Computer will choose randomly not conditionally)
3- Result print 

Cases:
A- Rock
Rock - Rock = tie
Rock - Paper = Paper win 
Rock - Scissor = Rock win 

B- Paper
Paper - Paper = tie
Paper - Rock = paper win 
Paper - Scissors = Scissor win

C- Scissor
Scissor - Scissor = tie
Scissor - paper = Scissor win 
Scissor - Rock = Rock win 

"""

import random
item_list = ["Rock", "Paper", "Scissor"]

user_choice = input("Enter your move = Rock, Paper, Scissor: ")
comp_choice = random.choice(item_list)

print(f"user choice = {user_choice}, computer choice = {comp_choice}")

if user_choice == comp_choice:
    print("Both chooses same: Match Tie")

elif user_choice == "Rock":
    if comp_choice == "Paper":
        print("Paper covers Rock = Computer win")
    else:
        print("Rock smashes Scissor = You win")   

elif user_choice == "Paper":
    if comp_choice == "Scissor":
        print("Scissor cuts paper, computer win")
    else:
        print("Paper covers rock, You win")

elif user_choice == "Scissor":
    if comp_choice == "Paper":
        print("Scissor cuts paper, You win")
    else:
        print("Rock smashes the scissor, Computer win")            
