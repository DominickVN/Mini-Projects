import random

def game():
    user = input("Please type 'R' for Rock, 'P' for Paper, or 'S' for Scissors: \n").lower()
    computer = random.choice(['Rock','Paper','Scissors'])

    if user == computer:
        return "It's a Tie!"

    if is_win(user,computer):
        return f'The Computer chose {computer}. You Won!'

    return f'The Computer chose {computer}. You lost...'

def is_win(player,opponent):
    #true if player wins
    if (player == 'Rock' and opponent == 'Scissors' ) or (player == 'Scissors' and opponent == 'Paper') or (player == 'Paper' and opponent == \
            'Rock'):
        return True

print(game())