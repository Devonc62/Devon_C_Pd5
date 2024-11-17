def main():
    from random import randint

    computer_choice = randint(1,3)

    if computer_choice == 1:
        computer = 'Rock'
    elif computer_choice == 2:
        computer = 'Paper'
    else:
        computer = 'Scissors'

    user_choice = input('Would you like Rock, Paper, or Scissors?\n').capitalize()

    print('You have chosen {user_choice} and the computer chose {computer}')

    if user_choice == computer:
        print('its a tie!')
    elif (user_choice == "Rock" and computer == "Scissors") or \
         (user_choice == "Paper" and computer == "Rock") or \
         (user_choice == "Scissors" and computer == "Paper"):
        print("you win!")
    else:
        print("you lose!")

