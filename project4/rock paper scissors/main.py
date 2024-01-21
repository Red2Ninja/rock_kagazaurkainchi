# Rock
rock = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

# Paper
paper = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

# Scissors
scissors = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
import random
game_img = [rock,paper,scissors]
print('What do you choose? Type 0 for rock,1 for paper and 2 for scissors:')
user_choice = int(input())

print(game_img[user_choice])
computer_choice = random.randint(0,2)
print(f'Computer choses {computer_choice}')

print(game_img[computer_choice])
if user_choice == computer_choice:
    print('Its a tie!')
if user_choice== 0 and computer_choice==2:
    print('You win!')
elif user_choice== 2 and computer_choice ==0:
    print('Computer wins!')
elif computer_choice>user_choice:
    print('Computer wins!')
elif user_choice> computer_choice:
    print('You win!')
