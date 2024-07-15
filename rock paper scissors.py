import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print("Welcome!\n")
user_choice = int(input("Choose '0' for rock, '1'for paper or '2' for scissors."))

choice = [rock, paper, scissors]
user = choice[user_choice]

computer_choice = random.randint(0, 2)
computer = choice[computer_choice]

print(f"You chose:{user}")
print(f"computer choose:{computer}")


if  (user == rock and computer == scissors)or\
    (user == paper and computer == rock) or\
    (user == scissors and computer == paper):
    print("You win!")

elif(user == computer):
    print("Its a draw!")
else:
    print("You lose!")



