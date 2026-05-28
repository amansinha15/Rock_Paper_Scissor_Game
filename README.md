# Rock Paper Scissor Game 🎮

A simple yet engaging **Rock–Paper–Scissors** game built in Python.  
This project demonstrates basic Python concepts such as `conditional statements`, `user input`, and `random module` usage.

---

## 📌 Project Overview

This Python program allows a user to play the classic **Rock–Paper–Scissor** game against the computer.  
The computer randomly selects one of the three options, and the program determines the winner based on the traditional rules.

---

## 🧠 Features

- User vs Computer gameplay  
- Randomized computer moves using Python’s `random` module  
- Clear win/lose/tie messages  
- Beginner-friendly script  
- Easy to modify and extend  

---

## 🖼️ Screenshot

> Add your screenshot inside an `/Screenshot1.png` folder in your repo and use the below format.
(./Screenshot1.png)
---

---

## 🛠️ Tools & Technologies Used

- **Python 3.x**
- **VS Code** (for development)
- **Random Module**

---

## ▶️ How to Run the Project

1. Install Python 3.x  
2. Clone the repository  
3. Open a terminal in the project folder  
4. Run the script:

```bash
python Rock_paper_Scissor_game.py

## code snippeet


import random

item_list = ["Rock", "Paper", "Scissor"]

user_choice = input("Enter your move = Rock, Paper, Scissor: ")
comp_choice = random.choice(item_list)

print(f"user choice = {user_choice}, computer choice = {comp_choice}")

if user_choice == comp_choice:
    print("Both choose same: Match Tie")
elif user_choice == "Rock":
    if comp_choice == "Paper":
        print("Paper covers Rock = Computer win")
    else:
        print("Rock smashes Scissor = You win")



Fork the repo
Create a new branch
Commit your changes
Submit a pull request


